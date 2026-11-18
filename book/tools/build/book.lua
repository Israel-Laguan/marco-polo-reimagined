-- book.lua: the Markdown conventions (plans/registry/markdown-conventions.md) -> LaTeX macros
-- defined in book.latex. Mechanical by design: each element has one fixed Markdown shape.
local stringify = pandoc.utils.stringify
local function raw(s) return pandoc.RawBlock('latex', s) end
local function rawi(s) return pandoc.RawInline('latex', s) end

local TAGS = { ['[V]'] = 'V', ['[R]'] = 'R', ['[M]'] = 'M', ['[reception]'] = 'reception' }
-- Note markers -> code points; ~ prints as U+223C so it never reads as a raised tilde.
local MARKS = { ['✓'] = '"2713', ['✗'] = '"2717', ['◇'] = '"25C7', ['?'] = '"003F', ['~'] = '"223C' }

local chap = 0
local main = false -- \mainmatter emitted (before the first # Chapter; front files keep roman pages)
local linked = true -- false inside the how-to box, where [3] is an example, not a citation

local function exists(p)
  local f = io.open(p)
  if f then f:close() return true end
end

-- drop a leading Str (exactly `lead`, or starting with it) and the Space after it
local function strip_lead(inlines, lead)
  local c = inlines:clone()
  local first = c[1]
  if first and first.t == 'Str' and first.text:sub(1, #lead) == lead then
    local rest = first.text:sub(#lead + 1)
    if rest == '' then c:remove(1) else c[1] = pandoc.Str(rest) end
    if c[1] and c[1].t == 'Space' then c:remove(1) end
    return c
  end
end

-- Epigraph: a quotation whose last line is "— credit". "> quote" + "> — credit" with no blank
-- line between is one paragraph, so split it at the line break before the dash.
-- Returns the quotation blocks and the credit inlines, or nil.
local function epigraph(bq)
  local last = bq.content[#bq.content]
  if not last or last.t ~= 'Para' then return nil end
  local il = last.content
  for k = 0, #il - 1 do
    if k == 0 or il[k].t == 'SoftBreak' or il[k].t == 'LineBreak' then
      local credit = strip_lead(pandoc.List({ table.unpack(il, k + 1) }), '—')
      if credit then
        local body = bq.content:clone(); body:remove()
        if k > 1 then body:insert(pandoc.Para({ table.unpack(il, 1, k - 1) })) end
        return body, credit
      end
    end
  end
end

local function is_notes(b) return b.t == 'Header' and stringify(b) == 'Notes' end

-- Real file type and pixel width from the header (the extension is not trusted).
local function sniff(path)
  local f = io.open(path, 'rb'); if not f then return nil end
  local d = f:read(65536); f:close()
  local function be(i) return d:byte(i) * 256 + d:byte(i + 1) end
  if d:sub(1, 4) == '%PDF' then return 'pdf' end
  if d:sub(2, 4) == 'PNG' then return 'png', be(17) * 65536 + be(19) end
  if d:sub(1, 3) == 'GIF' then return 'gif', d:byte(7) + d:byte(8) * 256 end
  if d:sub(1, 2) == '\255\216' then
    local i = 3
    while i + 8 <= #d do -- walk the segments to the frame header (SOFn)
      local m = d:byte(i + 1)
      if m >= 0xC0 and m <= 0xCF and m ~= 0xC4 and m ~= 0xC8 and m ~= 0xCC then return 'jpg', be(i + 7) end
      i = i + 2 + be(i + 2)
    end
    return 'jpg'
  end
  return 'unknown'
end

local PRINT_PX = 1350 -- 4.5 in measure at 300 dpi (illustration-style-guide.md, Technical spec)

-- 1. Figures: ../media/x.jpg -> media/x.jpg (paths are relative to book/); prefer a vector x.pdf.
-- A file LaTeX cannot place (missing, wrong extension, GIF/SVG) becomes a labelled placeholder
-- so the rest of the build still runs; a raster under 300 dpi at full width is a warning.
local function Image(img)
  local src = img.src:gsub('^%.%./', '')
  local pdf = src:gsub('%.%w+$', '.pdf')
  if exists(pdf) then src = pdf end
  local ext = (src:match('%.(%w+)$') or ''):lower():gsub('jpeg', 'jpg')
  local kind, px = sniff(src)
  local problem
  if not kind then problem = 'missing file'
  elseif kind ~= ext then problem = 'is a ' .. kind .. ', not a .' .. ext
  elseif kind ~= 'pdf' and kind ~= 'png' and kind ~= 'jpg' then problem = kind .. ': export a PDF or PNG'
  elseif px and px < PRINT_PX then
    io.stderr:write(('book.lua: %s is %d px wide (%d dpi at full width; print needs %d px)\n')
      :format(src, px, math.floor(px / 4.5), PRINT_PX))
  end
  if problem then
    io.stderr:write('book.lua: placeholder for ' .. src .. ' (' .. problem .. ')\n')
    return rawi('\\figplaceholder{' .. src:gsub('_', '\\_') .. '}{' .. problem .. '}')
  end
  img.src = src
  return img
end

-- 2. Tables: pipe tables with short dashes have no widths, and would overflow a 4.5 in measure.
-- Give each column a share of the line proportional to its longest cell (capped, with a floor).
-- a verdict column takes the Note markers, set as in the Notes
local table_marks = { Str = function(s) if MARKS[s.text] then return rawi('\\mk{' .. MARKS[s.text] .. '}') end end }

local function Table(t)
  for _, spec in ipairs(t.colspecs) do
    if type(spec[2]) == 'number' then return t:walk(table_marks) end -- the author set widths; keep them
  end
  local len = {}
  local function scan(rows)
    for _, r in ipairs(rows) do
      for c, cell in ipairs(r.cells) do
        len[c] = math.max(len[c] or 4, math.min(utf8.len(stringify(cell.contents)) or 4, 60))
      end
    end
  end
  scan(t.head.rows)
  for _, b in ipairs(t.bodies) do scan(b.body) end
  local tot = 0
  for _, l in ipairs(len) do tot = tot + l end
  for c, spec in ipairs(t.colspecs) do
    t.colspecs[c] = { spec[1], math.max((len[c] or 4) / tot, 0.1) }
  end
  return t:walk(table_marks)
end

-- Body citations: [n] -> \notemark (superscript, linked to the Note in the same chapter).
-- Applied to every block step 3 emits; a Note's own leading [n] is already a \noteitem by then.
-- The space before the mark is dropped.
local function Inlines(ils)
  local out = pandoc.List()
  for _, el in ipairs(ils) do
    local pre, n, post
    if el.t == 'Str' then pre, n, post = el.text:match('^(.-)%[(%d+)%](.*)$') end
    if n then
      if pre ~= '' then out:insert(pandoc.Str(pre))
      elseif #out > 0 and out[#out].t == 'Space' then out:remove() end
      out:insert(rawi(linked and ('\\notemark{%d}{%s}'):format(chap, n) or '\\textsuperscript{' .. n .. '}'))
      if post ~= '' then out:insert(pandoc.Str(post)) end
    elseif not linked and el.t == 'Str' and MARKS[el.text] then
      out:insert(rawi('\\mk{' .. MARKS[el.text] .. '}')) -- the box explains the markers: same glyphs as the Notes
    else
      out:insert(el)
    end
  end
  return out
end

-- 3. Block structure: chapter heads, tag line, epigraph, asides, box, scene breaks, Notes.
local function Pandoc(doc)
  local out, blocks = pandoc.List(), doc.blocks
  local put = function(x) out:insert(x:walk({ Inlines = Inlines })) end
  local in_notes, first_rule = false, false
  local function close_notes()
    if in_notes then put(raw('\\end{chapternotes}')); in_notes = false end
  end
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    if b.t == 'Header' and b.level == 1 then
      -- "# Chapter II-2" + "## Title" -> \bookchapter{II-2}{Title}; front/back/test heads print no label
      close_notes(); chap = chap + 1; first_rule = true
      local label = stringify(b.content):match('^Chapter%s+(.+)$') or ''
      if label ~= '' and not main then put(raw('\\mainmatter')); main = true end
      local title = b.content
      local nxt = blocks[i + 1]
      if nxt and nxt.t == 'Header' and nxt.level == 2 and not is_notes(nxt) then title = nxt.content; i = i + 1 end
      local il = pandoc.List({ rawi('\\bookchapter{' .. label .. '}{') })
      il:extend(title); il:insert(rawi('}'))
      put(pandoc.Plain(il))
    elseif is_notes(b) then
      close_notes(); in_notes = true
      put(raw('\\notesheading\n\\begin{chapternotes}'))
    elseif in_notes and b.t == 'Para' and b.content[1] and b.content[1].t == 'Str'
        and b.content[1].text:match('^%[%d+%]$') then
      local n = b.content[1].text:match('%d+')
      local c = strip_lead(b.content, b.content[1].text)
      for k, el in ipairs(c) do
        if el.t == 'Str' and MARKS[el.text] then c[k] = rawi('\\mk{' .. MARKS[el.text] .. '}') end
      end
      c:insert(1, rawi(('\\noteitem{%d}{%s}'):format(chap, n)))
      put(pandoc.Para(c))
    elseif b.t == 'HorizontalRule' then
      -- the rule under the title block and the rule before Notes are structural; any other is a scene break
      local nxt = blocks[i + 1]
      if first_rule or (nxt and is_notes(nxt)) then first_rule = false
      else put(raw('\\scenebreak')) end
    elseif b.t == 'Para' and #b.content == 1 and b.content[1].t == 'Strong' and TAGS[stringify(b)] then
      put(raw('\\chaptertag{' .. TAGS[stringify(b)] .. '}'))
    elseif b.t == 'BlockQuote' and epigraph(b) then
      local body, credit = epigraph(b)
      put(raw('\\begin{epigraphq}')); for _, x in ipairs(body) do put(x) end
      local il = pandoc.List({ rawi('\\epicredit{') }); il:extend(credit); il:insert(rawi('}'))
      put(pandoc.Plain(il)); put(raw('\\end{epigraphq}'))
    elseif b.t == 'Para' and not in_notes and strip_lead(b.content, '—') then
      put(raw('\\begin{aside}')); put(pandoc.Para(strip_lead(b.content, '—')))
      put(raw('\\end{aside}'))
    elseif b.t == 'Div' and b.classes:includes('howto') then
      put(raw('\\begin{howto}')); linked = false
      for _, x in ipairs(b.content) do put(x) end
      linked = true; put(raw('\\end{howto}'))
    else
      put(b)
    end
    i = i + 1
  end
  close_notes()
  doc.blocks = out
  return doc
end

return { { Image = Image, Table = Table }, { Pandoc = Pandoc } }

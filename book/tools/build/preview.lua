-- preview.lua: HTML / EPUB citations like the print build (BLD.T9). Runs citeproc itself:
-- use it instead of --citeproc, with --bibliography and --csl as usual.
-- Pandoc's biblatex reader drops `shorthand`, so no CSL can print "YC": cites of the sigla are
-- written here as "YC 1.61" / "YC Add. on 2.23" inside the same parentheses as any other key in
-- the group, the keys go to nocite (Works cited still lists them), and the Abbreviations page
-- (abbreviations.md, the same prose as book.latex) goes first. Their Works cited entries lead
-- with the siglum, "YC (Polo, Marco). 1903. …", as biblatex prints them.
local SIGLA = { yc = 'YC', ycadd = 'YC Add.' }
local stringify = pandoc.utils.stringify
local used = {}

local function siglum(c)
  local pre, loc = stringify(c.prefix), stringify(c.suffix):gsub('^,?%s*', '')
  return (pre ~= '' and pre .. ' ' or '') .. SIGLA[c.id] .. (loc ~= '' and ' ' .. loc or '')
end

local function Cite(el)
  local pieces, real = {}, {} -- pieces: siglum strings and Citations, in source order
  for _, c in ipairs(el.citations) do
    if SIGLA[c.id] then used[c.id] = true; table.insert(pieces, siglum(c))
    else table.insert(pieces, c); table.insert(real, c) end
  end
  if #real == #el.citations then return nil end
  if #real == 0 then
    local t = {}
    for _, p in ipairs(pieces) do t[#t + 1] = p end
    return pandoc.Inlines('(' .. table.concat(t, '; ') .. ')')
  end
  -- mixed group: a siglum joins the prefix of the next real citation, or the suffix of the last
  local before = {}
  for _, p in ipairs(pieces) do
    if type(p) == 'string' then table.insert(before, p)
    elseif #before > 0 then
      p.prefix = pandoc.Inlines(table.concat(before, '; ') .. ';') .. (#p.prefix > 0 and pandoc.Inlines(' ') .. p.prefix or {})
      before = {}
    end
  end
  if #before > 0 then
    local last = real[#real]
    last.suffix = last.suffix .. pandoc.Inlines('; ' .. table.concat(before, '; '))
  end
  el.citations = real
  return el
end

-- "Polo, Marco. 1903." -> "YC (Polo, Marco). 1903."
local function lead(div)
  local id = div.identifier:match('^ref%-(.+)$')
  local para = SIGLA[id] and div.content[1]
  if not (para and para.content) then return nil end
  for k, el in ipairs(para.content) do
    if el.t == 'Str' and el.text:match('%.$') then
      para.content[k] = pandoc.Str(el.text:sub(1, -2) .. ').')
      para.content:insert(1, pandoc.Str(SIGLA[id] .. ' ('))
      return div
    end
  end
end

local function Pandoc(doc)
  -- As in print, show the glossary title as the sole heading for B2.
  for i = #doc.blocks - 1, 1, -1 do
    local label, title = doc.blocks[i], doc.blocks[i + 1]
    if label.t == 'Header' and label.level == 1 and stringify(label):match('^Back Matter [IVX]+%-2$')
        and title.t == 'Header' and title.level == 2 and title.identifier == 'names-and-pronunciation' then
      title.level = 1
      doc.blocks:remove(i)
    end
  end

  local keys = {}
  for id in pairs(used) do table.insert(keys, id) end
  if #keys == 0 then return pandoc.utils.citeproc(doc) end
  table.sort(keys)
  local nocite = doc.meta.nocite and pandoc.Inlines(doc.meta.nocite) or pandoc.Inlines({})
  for _, id in ipairs(keys) do
    nocite:insert(pandoc.Cite({}, { pandoc.Citation(id, 'NormalCitation') }))
  end
  doc.meta.nocite = nocite
  local dir = PANDOC_SCRIPT_FILE:match('(.*)/') or '.'
  local f = assert(io.open(dir .. '/abbreviations.md'))
  local abbr = pandoc.read(f:read('a'), 'markdown').blocks
  f:close()
  abbr:extend(doc.blocks)
  doc.blocks = abbr
  return pandoc.utils.citeproc(doc):walk({ Div = lead })
end

local function Span(span)
  -- The manuscript's comparative quotation source is for tools/comparanda.py.
  -- A literal src attribute on an HTML span is invalid in the EPUB output.
  if span.attributes.src then
    span.attributes.src = nil
    return span
  end
end

return { { Cite = Cite, Span = Span }, { Pandoc = Pandoc } }

-- Markdown links name the target chapter so they work when chapters are read
-- separately. In an assembled volume, jump to the heading or figure itself.
function Pandoc(doc)
  local anchors = {}
  doc:walk({
    Header = function(header)
      if header.identifier:match('^map%-of%-') then
        anchors[header.identifier] = true
      end
    end,
    Figure = function(figure)
      if figure.identifier ~= '' then anchors[figure.identifier] = true end
    end
  })
  return doc:walk({
    Link = function(link)
      local id = link.target:match('^[%w%-]+%.md#([%w%-]+)$')
      if anchors[id] then
        link.target = '#' .. id
        return link
      end
    end
  })
end

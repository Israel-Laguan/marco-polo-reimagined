-- Markdown links name the target chapter so they work when chapters are read
-- separately. In an assembled volume, jump directly to a map heading.
function Pandoc(doc)
  local anchors = {}
  doc:walk({
    Header = function(header)
      if header.identifier:match('^map%-of%-') then
        anchors[header.identifier] = true
      end
    end
  })
  return doc:walk({
    Link = function(link)
      local id = link.target:match('^[%w%-]+%.md#(map%-of%-[%w%-]+)$')
      if anchors[id] then
        link.target = '#' .. id
        return link
      end
    end
  })
end

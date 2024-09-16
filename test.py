tags_to_remove = ['nav', 'script', 'footer', 'header', 'style', 'img', 'svg', 'noscript', 'form', 'input', 'button', 'select', 'textarea', 'label', 'iframe', 'video', 'audio', 'object', 'embed', 'canvas', 'map', 'area', 'base', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'br', 'hr', 'col', 'colgroup', 'caption', 'table', 'thead', 'tfoot', 'tbody', 'tr', 'th', 'td', 'dl', 'dt', 'dd', 'ol', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'b', 'i', 'u', 's', 'strong', 'em', 'mark', 'small', 'del', 'ins', 'sub', 'sup', 'code', 'pre', 'blockquote', 'q', 'cite', 'abbr', 'dfn', 'kbd', 'var', 'samp', 'data', 'time', 'span', 'div', 'section', 'article', 'aside', 'main', 'figure', 'figcaption', 'details', 'summary', 'dialog', 'caption', 'fieldset', 'legend', 'label', 'optgroup', 'option', 'textarea', 'button', 'output', 'progress', 'meter', 'details', 'summary', 'menu', 'menuitem', 'dialog', 'legend', 'fieldset', 'caption', 'colgroup', 'col', 'optgroup', 'option', 'textarea', 'button', 'output', 'progress', 'meter', 'menu', 'menuitem', 'dialog', 'legend', 'fieldset', 'caption', 'colgroup', 'col', 'optgroup', 'option', 'textarea', 'button', 'output', 'progress', 'meter', 'menu', 'menuitem', 'dialog', 'legend', 'fieldset', 'caption', 'colgroup', 'col', 'optgroup', 'option', 'textarea', 'button', 'output', 'progress', 'meter', 'menu', 'menuitem', 'dialog', 'legend', 'fieldset', 'caption', 'colgroup', 'col', 'optgroup', 'option', 'textarea', 'button', 'output', 'progress', 'meter', 'menu', 'menuitem', 'dialog', 'legend']

tags_to_remove = [
    'nav', 'script', 'footer', 'header', 'style', 'img', 'svg', 'noscript', 
    'form', 'input', 'button', 'select', 'textarea', 'label', 'iframe', 
    'video', 'audio', 'object', 'embed', 'canvas', 'map', 'area', 'base', 
    'link', 'meta', 'param', 'source', 'track', 'wbr','s','del','option'
]

tags_to_unwrap = [
    'span', 'div', 'section', 'article', 'aside', 'main', 'figure', 'figcaption',
    'details', 'summary', 'dialog', 'fieldset', 'legend', 'optgroup', 
    'output', 'progress', 'meter','hr', 'b', 'i', 'u',  'strong', 'em','mark', 'small','ins','dfn', 'kbd','data','a'
]

tags_to_keep = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',  
      'sub', 'sup', 'code', 'pre', 'blockquote', 
    'q', 'cite', 'abbr',  'var', 'samp',  'time', 'ol', 
    'ul', 'li', 'table', 'thead', 'tfoot', 'tbody', 'tr', 'th', 'td'
]
print(len(tags_to_remove)+len(tags_to_unwrap)+len(tags_to_keep))
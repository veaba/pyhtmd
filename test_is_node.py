# 第一步，解析img 最小标签
# 解析 button标签
# 解析span 标签
# 解析b标签

import re 
from test_html import html_content
html_re=re.compile(r"""
  <[a-zA-Z][^\t\n\r\f />\x00]*       # tag name
  (?:[\s/]*                          # optional whitespace before attribute name
    (?:(?<=['"\s/])[^\s/>][^\s/=>]*  # attribute name
      (?:\s*=+\s*                    # value indicator
        (?:'[^']*'                   # LITA-enclosed value
          |"[^"]*"                   # LIT-enclosed value
          |(?!['"])[^>\s]*           # bare value
         )
       )?(?:\s|/(?!>))*
     )*
   )?
  \s*
  """)

html_nodes=html_re.match(html_content)

# print(html_nodes.strip())

print(html_content.strip().replace('\n','').replace('\t',''))
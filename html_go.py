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


# aa= html_re.match(html_co/ntent)
bb= re.findall(r'<div(.*?)>',html_content)

content= html_content
# 移除div里面的属性
for item in bb:
    print(item)
    # html_content= re.sub(r''+item+'','',html_content)

# 移除注释

comment_count= content.count('<!--')

for item in range(comment_count):
    content=re.sub(r'<!--(.*?)-->','',content,count=1)


# 移除span
span_count= content.count('<span')
for item in range(span_count):
    content=re.sub(r'<span(.*?)>|</span>','',content,count=1)

# 移除button
button_count= content.count('button')
for item in range(button_count):
    content=re.sub(r'<button(.*?)>|</button>','',content,count=1)

# 移除自定义标签

custom = re.findall(r'</(.*?)>',content)

print(custom)
print(111,content)
import re

from test_html import html_content

html_re = re.compile(r"""
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
bb = re.findall(r'<div(.*?)>', html_content)

content = html_content
# 移除div里面的属性
for item in bb:
    print(item)
    # html_content= re.sub(r''+item+'','',html_content)

# 移除注释

comment_count = content.count('<!--')

for item in range(comment_count):
    content = re.sub(r'<!--(.*?)-->', '', content, count=1)

# 移除span
span_count = content.count('<span')
for item in range(span_count):
    content = re.sub(r'<span(.*?)>|</span>', '', content, count=1)

# 移除button
button_count = content.count('button')
for item in range(button_count):
    content = re.sub(r'<button(.*?)>|</button>', '', content, count=1)

# 移除自定义标签

all_tag_list = re.findall(r'</(.*?)>', content)

HTML_NODE = [
    'a',
    'li',
    'div',
    'ul',
    'ol',
    'em',
    'b',
    'code',
    'p',
    'span',
    'button',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'article',
    'section',
    'table',
    'tbody',
    'th',
    'td',
    'tr',
    'pre'
]
custom_list = [tag for tag in all_tag_list if tag not in HTML_NODE]
print(custom_list)

# 移除自定义标签
for custom in custom_list:
    reg_str = '<' + custom + '(.*?)>|</' + custom + '>'
    content = re.sub(r'' + reg_str + '', '', content)

print("结果：\n", content)

# 新的全部标签
all_tag_list = re.findall(r'</(.*?)>', content)

print(all_tag_list)

# todo 需要跳开img 和 a标签

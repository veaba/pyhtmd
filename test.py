from pyhtmd.core import Pyhtmd

# from pyhtmd.utils import remove_attrs, get_tag_name

from test_html import html_content


item = html_content

mk = Pyhtmd(item).markdown()
print('============结果Start：===============')
print(mk)
# with open('ul.txt', "w", errors="ignore", encoding='utf-8') as f:
#             f.write(mk)
print('============结果End：===============')

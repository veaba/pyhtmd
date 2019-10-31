# TODO 1、校验是合法的HTML字符串
# TODO 2、将html string 分割为数组才能使用本文件
# todo：逐行将HTML转为markdown字符串输出
# html to markdown

import re
from utils import is_li, is_head,is_img, is_pre, get_tag_text, is_has_child,remove_attrs
from html_parser import parser_li, parser_head, parser_pre, parser_p,parser_img


class HTMK:
    def __init__(self, html=""):
        self.html = html
        # 错误处理
        if not isinstance(self.html, str):
            raise RuntimeError('The params is no str type')

    # 移除无关标签,净化标签
    # 比如：span
    # <span>xx</span>  => xxx
    @staticmethod
    def __clean_up_tag(self, block=""):
        return re.sub(r'(<span>)(.*?)(<\/span>)', '\\2', block.strip())

    # todo 解析出来markdown
    def markdown(self):
        if is_li(self.html):
            print('is_li')
            text = parser_li(self.html)
        elif is_head(self.html):
            print('__is_head')
            clear_head_block=remove_attrs(self.html)
            text = parser_head(clear_head_block)
        elif is_pre(self.html):
            print('__is_pre')
            text = parser_pre(self.html)
        elif is_img(self.html):
            print('__is_img')
            text = parser_img(self.html)
        else:
            print('__parser_p')
            # 此时就应该清空span标签
            clear_block = self.__clean_up_tag(self, block=self.html)
            text = parser_p(clear_block)

        return text
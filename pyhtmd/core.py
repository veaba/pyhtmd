# TODO 1、校验是合法的HTML字符串
# TODO 2、将html string 分割为数组才能使用本文件
# todo：逐行将HTML转为markdown字符串输出
# html to markdown

import re
from .utils import is_li, is_head, is_img, is_pre, is_quote, remove_attrs, init_html
from .html_parser import parser_li, parser_head, parser_pre, parser_p, parser_img, parser_quote


class Pyhtmd:
    def __init__(self, html="", language="", img=True):
        # print('原始标签：', html)
        # todo 需要检测是合法的HTML标签
        self.html = init_html(html)
        self.language = language
        self.img = img
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
            return parser_li(self.html)
        # 导致递归移除，但看起来没有什么啊
        elif is_head(self.html):
            print('is_head')
            return parser_head(remove_attrs(self.html))
        elif is_pre(self.html):
            print('is_pre')
            return parser_pre(element=self.html, language=self.language)
        elif is_img(self.html):
            print('is_img')
            if self.img:
                return parser_img(self.html)
            return self.html
        elif is_quote(self.html):
            print('引用部分：', self.html)
            clear_block = self.__clean_up_tag(self, block=self.html)
            return parser_quote(clear_block)
        else:
            print('other tag')
            # 此时就应该清空span标签
            other_block = self.__clean_up_tag(self, block=self.html)
            return parser_p(other_block)

    def get(self):
        return self.html

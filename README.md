# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具，实验demo

请勿使用于生成环境，这个只是一次尝试demo项目

## 注意：

- 无法解析多层级HTML
- 只能是单Node
- 这项目目前只针对 [tensorflow-docs](https://github.com/veaba/tensorflow-docs) 项目
- 存在个别自定义标签无法识别，基本可以适用平常场景
- python官方html_parser https://docs.python.org/zh-cn/3.7/library/html.parser.html
- html.parser 源码 https://github.com/python/cpython/blob/3.7/Lib/html/parser.py

## parser
- [x] single html node element
- [x] infinite html list node element
- [x] img
- [x] head html node element

## bug
当前的list 标签算法无法解析这种结构：
因为算法中，假定是依次序性ul组成结束的标签
```html
<!--假定的是-->
<ul><li><ul><li></ul><ul><li></li></ul></li></ul>
<!--bug-->
<ul>
    <li>甲甲甲甲甲</li>
    <li>乙乙乙乙乙</li>
    <li>
        <ul>
            <li>aaaaaaa</li>
            <li>bbbbbbb</li>
            <li>ccccccc</li>
        </ul>
    </li>
    <li>丙丙丙丙丙</li>
    <li>丁丁丁丁丁</li>
    <li>
        <ul>
            <li>33333</li>
            <li>44444</li>
            <li>55555</li>
        </ul>
    </li>
</ul>
```

## install 

> pip install pyhtmd


## usage

```python
from pyhtmd import Pyhtmd
html="<code> Hello, world ! by Pyhtmd. </code>"
md= Pyhtmd(html)
content=md.markdown()
print(content) # `Hello, world ! by Pyhtmd.`
```

## API
Pyhtmd(html,
 language="",
 img=True
)

- language：类型 string （js、python、java等）
- img:{Boolean}，默认True，可以不需要img渲染
```python
from pyhtmd import Pyhtmd
html="<pre><code>import time\n print(time.time()) </code><pre>"
md= Pyhtmd(html,language="python")
content=md.markdown()
print(content) # `Hello, world ! by Pyhtmd.`
```

## todo 开发中 
- 核心的问题是，粘在一起的代码如何拆分？

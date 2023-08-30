# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具，实验demo

请勿使用于生产环境，这个只是一次尝试demo项目


## install 

> pip install pyhtmd

## usage

```python
from pyhtmd import Pyhtmd
html="<code> Hello, world ! by Pyhtmd. </code>"
md=Pyhtmd(html)
content=md.markdown()
print(content) # `Hello, world ! by Pyhtmd.`
```

## API
Pyhtmd(html,
 language="",
 img=True
)

- language：类型 string （js、python、java等）
- img:{Boolean}，默认 `True`，可以不需要 `img`渲染
```python
from pyhtmd import Pyhtmd
html="<pre><code>import time\n print(time.time()) </code><pre>"
md=Pyhtmd(html,language="python")
content=md.markdown()
print(content) # `Hello, world ! by Pyhtmd.`
```


## 注意：

- 无法解析多层级HTML
- 只能是单Node
- 这项目目前只针对 [tensorflow-docs](https://github.com/veaba/tensorflow-docs) 项目
- 存在个别自定义标签无法识别，基本可以适用平常场景
- python官方html_parser https://docs.python.org/zh-cn/3.7/library/html.parser.html
- html.parser 源码 https://github.com/python/cpython/blob/3.7/Lib/html/parser.py
- 不支持美化后的HTML内容，需要内容紧凑

## parser
- [x] single html node element
- [x] infinite html list node element，无限级ul/ol 标签解析
- [x] img tag
- [x] head html node element
- [x] 内置支持svg 图标转img图片，不用担心svg格式的数学符号不会被解析


## todo 
- 核心的问题是，粘在一起的代码如何拆分？
- 本质还是要分割的，但具体怎么分割呢？
- table

## fix
- 已解决list算法问题：
    - 当前的list 标签算法无法解析这种结构：
    - 因为算法中，假定是依次序性ul组成结束的标签
    - 核心算法一：算出开始标签的level
    - 核心算法二：根据左边的开始标签索引值算出其所对应的右边索引值序列，我自己给他起了一个炫酷拽炸天的名字：标记逆序奇偶互斥算法
    - 上面两个算法我自己算出来的，第一个花了两天，第二个花了1-2周


# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具，实验demo

请勿使用于生成环境，这个只是一次尝试demo项目

## 注意：

- 无法解析多层级HTML
- 只能是单Node
- 这项目目前只针对 [tensorflow-docs](https://github.com/veaba/tensorflow-docs) 项目
- 存在个别自定义标签无法识别，基本可以适用平常场景


## parser
- [x] single html node element
- [x] infinite html list node element
- [x] img
- [x] head html node element


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

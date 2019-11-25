# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具，实验demo

请勿使用于生成环境，这个只是一次尝试demo项目

## 注意：

- 无法解析多层级HTML
- 只能是单Node


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
- 递归太多被打断了
- 特殊字符，数学符号！：'<p><a href="https://tensorflow.google.cn/api_docs/python/tf/math/exp"><code translate="no" dir="ltr">exp(...)</code></a>: Computes exponential of x element-wise.  <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax_SVG" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>y</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math>" role="presentation" style="font-size: 100%; display: inline-block; position: relative;"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="6.51ex" height="2.494ex" viewBox="0 -766.3 2802.9 1074" role="img" focusable="false" style="vertical-align: -0.715ex;" aria-hidden="true"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#MJMATHI-79" x="0" y="0"></use><use xlink:href="#MJMAIN-3D" x="775" y="0"></use><g transform="translate(1831,0)"><use xlink:href="#MJMATHI-65" x="0" y="0"></use><use transform="scale(0.707)" xlink:href="#MJMATHI-78" x="659" y="513"></use></g></g></svg><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></span></span><script type="math/tex" id="MathJax-Element-1">y = e^x</script>.</p>' 无法识别这个特殊
- 尚未处理ol标签

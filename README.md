# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具

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


## todo 开发中 
- 递归太多被打断了
- 


### demo1
```html
Given a tensor <code translate="no" dir="ltr">t</code>, this operation returns a tensor of the same type andshape as <code translate="no" dir="ltr">t</code> with its values clipped to <code translate="no" dir="ltr">clip_value_min</code> and <code translate="no" dir="ltr">clip_value_max</code>.Any values less than  <code translate="no" dir="ltr">clip_value_min</code> are set to <code translate="no" dir="ltr">clip_value_min</code>. Any valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are  set to <code translate="no" dir="ltr">clip_value_max</code>. 

```
---------------------------------------
Given a tensor `t`, this operation returns a tensor of the same type andshape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.Any values less than `clip_value_min` are set to `clip_value_min`. Any valuesgreater than `clip_value_max` are set to `clip_value_max`. 

### demo2
```html
<strong>Note:</strong><span> <code translate="no" dir="ltr">clip_value_min</code> needs to be smaller or equal to <code translate="no" dir="ltr">clip_value_max</code> forcorrect results.</span>
```
---------------------------------------
**Note:** `clip_value_min` needs to be smaller or equal to `clip_value_max` forcorrect results.


### demo3

```html
<h4 id="for_example" is-upgraded="">For example:</h4>
```
---------------------------------------
#### For example:


### demo4：todo ，换行的字符不是特别好

```html
k = '<pre class="prettyprint lang-python" translate="no" dir="ltr" is-upgraded=""><code translate="no" dir="ltr">A = tf.constant([[1, 20, 13], [3, 21, 13]])B = tf.clip_by_value(A, clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]C = tf.clip_by_value(A, clip_value_min=0., clip_value_max=3.) # throws `TypeError`as input and clip_values are of different dtype</code></pre>'

```
---------------------------------------
``` 
A = tf.constant([[1, 20, 13], [3, 21, 13]])B = tf.clip_by_value(A, clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]C = tf.clip_by_value(A, clip_value_min=0., clip_value_max=3.) # throws `TypeError`as input and clip_values are of different dtype
```

### demo5:

```html
<li><b><code translate="no" dir="ltr">t</code></b>: A <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.</li><li><b><code translate="no" dir="ltr">clip_value_min</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The minimum value to clip by.</li><li><b><code translate="no" dir="ltr">clip_value_max</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The maximum value to clip by.</li><li><b><code translate="no" dir="ltr">name</code></b>: A name for the operation (optional).</li>

```
---------------------------------------
- **`t`: A `Tensor` or `IndexedSlices`.**
- **`clip_value_min`: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shapeas `t`. The minimum value to clip by.**
- **`clip_value_max`: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shapeas `t`. The maximum value to clip by.**
- **`name`: A name for the operation (optional).**

### demo6:

```html
<h4 id="raises" is-upgraded="">
    Raises:
    <button role="button" class="devsite-heading-link button-flat material-icons" title="Copy link to this section">
    </button>
</h4> 
```
---------------------------------------
#### Raises:



### demo7:

```html
<li>
	<b> <code translate="no" dir="ltr">ValueError</code> </b> : If the clip tensors would trigger array broadcastingthat would make the returned tensor larger than the input.
</li>

<li>
	<b><code translate="no" dir="ltr">TypeError</code></b>: If dtype of the input is <code translate="no" dir="ltr">int32</code> and dtype of the <code translate="no" dir="ltr">clip_value_min or</code> clip_value_max <code translate="no" dir="ltr">is</code> float32
</li> 
```
---------------------------------------
- **`ValueError`**: If the clip tensors would trigger array broadcastingthat would make the returned tensor larger than the input.
- **`TypeError`**: If dtype of the input is  `int32`  and dtype ofthe  `clip_value_min or` clip_value_max `is` float32


### demo8:


```html
<a href="/api_docs/python/tf/clip_by_value"><code>tf.compat.v2.clip_by_value</code></a>
```

---------------------------------------

- [ `tf.compat.v2.clip_by_value` ](/api_docs/python/tf/clip_by_value)


### demo9:

```html
<img src="https://www.baidu.com/img/bd_logo1.png">
<img src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo">
```

---------------------------------------

 ![](https://www.baidu.com/img/bd_logo1.png)
  ![百度logo](https://www.baidu.com/img/bd_logo1.png)


  ## 吐槽

 这正则会引发： maximum recursion depth exceeded in comparison
 什么毛病，其他就没有！！！！
 问题：由于一个正则替换引发的无限递归
  ```python
  def remove_attrs(block):
    content=block
    # remove_h1 = re.sub(r'<h1(.*?)">', '<h1>', content)
    # remove_h2 = re.sub(r'<h2(.*?)">', '<h2>', remove_h1)
    # remove_h3 = re.sub(r'<h3(.*?)">', '<h3>', remove_h2)
    # remove_h4 = re.sub(r'<h4(.*?)">', '<h4>', remove_h3)
    # remove_h5 = re.sub(r'<h5(.*?)">', '<h5>', remove_h4)
    # remove_h6 = re.sub(r'<h6(.*?)">', '<h6>', remove_h5)
    # remove_code = re.sub(r'<code(.*?)">', '<code>', remove_h6)
    # remove_span = re.sub(r'<span(.*?)">', '<span>', remove_code)
    remove_b = re.sub(r'<b(.*?)">', '<b>', content)
    # remove_button = re.sub(r'<button(.*?)">', '<button>', content) # 这个就没报错，很奇怪
    # remove_div = re.sub(r'<div(.*?)">', '<div>', content)
    # remove_a = re.sub(r'<a(.*?)">', '<a>', remove_div)
    return remove_b

# todo table
import re
from pyhtmd.core import Pyhtmd
array=[
'<h3 id="aliases" is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons" title="Copy link to this section"></button></h3>'
]
for item in array:
    mk=Pyhtmd(item).markdown()
    print('===========================')
    print(mk)
    print('===========================')

  ```
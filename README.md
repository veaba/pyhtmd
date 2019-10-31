# 一款Python版本的HTML转markdown解析器，不使用任何第三方工具

## todo 开发中 


### demo1
```html
Given a tensor <code translate="no" dir="ltr">t</code>, this operation returns a tensor of the same type andshape as <code translate="no" dir="ltr">t</code> with its values clipped to <code translate="no" dir="ltr">clip_value_min</code> and <code translate="no" dir="ltr">clip_value_max</code>.Any values less than  <code translate="no" dir="ltr">clip_value_min</code> are set to <code translate="no" dir="ltr">clip_value_min</code>. Any valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are  set to <code translate="no" dir="ltr">clip_value_max</code>. 

```
Given a tensor `t`, this operation returns a tensor of the same type andshape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.Any values less than `clip_value_min` are set to `clip_value_min`. Any valuesgreater than `clip_value_max` are set to `clip_value_max`. 

### demo2
```html
<strong>Note:</strong><span> <code translate="no" dir="ltr">clip_value_min</code> needs to be smaller or equal to <code translate="no" dir="ltr">clip_value_max</code> forcorrect results.</span>
```

**Note:** `clip_value_min` needs to be smaller or equal to `clip_value_max` forcorrect results.


### demo3

```html
<h4 id="for_example" is-upgraded="">For example:</h4>
```

#### For example:


### demo4：todo ，换行的字符不是特别好

```html
k = '<pre class="prettyprint lang-python" translate="no" dir="ltr" is-upgraded=""><code translate="no" dir="ltr">A = tf.constant([[1, 20, 13], [3, 21, 13]])B = tf.clip_by_value(A, clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]C = tf.clip_by_value(A, clip_value_min=0., clip_value_max=3.) # throws `TypeError`as input and clip_values are of different dtype</code></pre>'

```

``` 
A = tf.constant([[1, 20, 13], [3, 21, 13]])B = tf.clip_by_value(A, clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]C = tf.clip_by_value(A, clip_value_min=0., clip_value_max=3.) # throws `TypeError`as input and clip_values are of different dtype
```

### demo5:

```html
<li><b><code translate="no" dir="ltr">t</code></b>: A <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.</li><li><b><code translate="no" dir="ltr">clip_value_min</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The minimum value to clip by.</li><li><b><code translate="no" dir="ltr">clip_value_max</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The maximum value to clip by.</li><li><b><code translate="no" dir="ltr">name</code></b>: A name for the operation (optional).</li>

```

- **`t`: A `Tensor` or `IndexedSlices`.**
- **`clip_value_min`: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shapeas `t`. The minimum value to clip by.**
- **`clip_value_max`: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shapeas `t`. The maximum value to clip by.**
- **`name`: A name for the operation (optional).**
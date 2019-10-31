# todo table
import re
from src.core import Pyhtmd
import time

table = '<table class="tfo-notebook-buttons tfo-api" align="left"><tbody><tr><td>  <a target="_blank" ' \
        'href="/versions/r1.15/api_docs/python/tf/clip_by_value">  <img ' \
        'src="https://tensorflow.google.cn/images/tf_logo_32px.png">  TensorFlow 1 version</a></td><td>  <a ' \
        'target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/clip_ops.py#L36' \
        '-L93">    <img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">    View source on GitHub  ' \
        '</a></td></tr></tbody></table> '
b = 'Clips tensor values to a specified min and max.'
c = '<h3 id="aliases" is-upgraded="">Aliases:</h3>'
d = '<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" ' \
    'dir="ltr">tf.compat.v1.clip_by_value</code></a></li><li><a href="/api_docs/python/tf/clip_by_value"><code ' \
    'translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a></li> '
e = '<pre class="prettyprint lang-python" translate="no" dir="ltr" is-upgraded=""><code translate="no" ' \
    'dir="ltr">tf.clip_by_value(    t,    clip_value_min,    clip_value_max,    name=None)</code></pre> '
f = '<h3 id="used_in_the_tutorials" is-upgraded="">Used in the tutorials:</h3>'
g = '<li><a href="https://tensorflow.google.cn/tutorials/generative/deepdream">DeepDream</a></li><li><a ' \
    'href="https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm">Adversarial example using ' \
    'FGSM</a></li><li><a href="https://tensorflow.google.cn/tutorials/generative/style_transfer">Neural style ' \
    'transfer</a></li> '
h = 'Given a tensor <code translate="no" dir="ltr">t</code>, this operation returns a tensor of the same type ' \
    'andshape as <code translate="no" dir="ltr">t</code> with its values clipped to <code translate="no" ' \
    'dir="ltr">clip_value_min</code> and <code translate="no" dir="ltr">clip_value_max</code>.Any values less than ' \
    '<code translate="no" dir="ltr">clip_value_min</code> are set to <code translate="no" ' \
    'dir="ltr">clip_value_min</code>. Any valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are ' \
    'set to <code translate="no" dir="ltr">clip_value_max</code>. '
i = '<strong>Note:</strong><span> <code translate="no" dir="ltr">clip_value_min</code> needs to be smaller or equal ' \
    'to <code translate="no" dir="ltr">clip_value_max</code> forcorrect results.</span> '
j = '<h4 id="for_example" is-upgraded="">For example:</h4>'
k = '<pre><code translate="no" dir="ltr">A = tf.constant([[1, 20, 13], [3, 21, 13]])B = tf.clip_by_value(A, ' \
    'clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]C = tf.clip_by_value(A, clip_value_min=0., ' \
    'clip_value_max=3.) # throws `TypeError`as input and clip_values are of different dtype</code></pre> '
l = '<h4 id="args" is-upgraded="">Args:</h4>'
m = '<li><b><code translate="no" dir="ltr">t</code></b>: A <code translate="no" dir="ltr">Tensor</code> or <code ' \
    'translate="no" dir="ltr">IndexedSlices</code>.</li><li><b><code translate="no" ' \
    'dir="ltr">clip_value_min</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code ' \
    'translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The ' \
    'minimum value to clip by.</li><li><b><code translate="no" dir="ltr">clip_value_max</code></b>: A 0-D (scalar) ' \
    '<code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same ' \
    'shapeas <code translate="no" dir="ltr">t</code>. The maximum value to clip by.</li><li><b><code translate="no" ' \
    'dir="ltr">name</code></b>: A name for the operation (optional).</li> '
n = '<h4 id="returns" is-upgraded="">Returns:</h4>'
o = 'A clipped <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.'
p = '<h4 id="raises" is-upgraded="">Raises:<button role="button" class="devsite-heading-link button-flat ' \
    'material-icons" title="Copy link to this section"></button></h4> '
q = '<li><b><code translate="no" dir="ltr">ValueError</code></b>: If the clip tensors would trigger array ' \
    'broadcastingthat would make the returned tensor larger than the input.</li><li><b><code translate="no" ' \
    'dir="ltr">TypeError</code></b>: If dtype of the input is <code translate="no" dir="ltr">int32</code> and dtype ' \
    'ofthe <code translate="no" dir="ltr">clip_value_min or</code>clip_value_max<code translate="no" ' \
    'dir="ltr">is</code>float32</li> '

a1 = '<a href="https://baidu.com">baidu.com </a>'
a2 = '<a>baidu.com </a>'
a3 = '<a href="https://baidu.com">baidu.com</a>'
h1 = '<h1>I am H1 tag </h1>'
h2 = '<h2>I am H1 tag </h2>'
h3 = '<h3>I am H1 tag </h3>'
h4 = '<h4>I am H1 tag </h4>'
h5 = '<h5>I am H1 tag </h5>'
h6 = '<h6>I am H1 tag </h6>'
code = '<code>Python</code>'

img = '<img src="https://www.baidu.com/img/bd_logo1.png">'
img1 = '<img src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo">'

# todo table

start = time.time()
x = Pyhtmd(i).markdown()
print("结果：\n", x)
end = time.time()
print('耗时====：', end - start)
# todo table
from pyhtmd.core import Pyhtmd
# from pyhtmd.core import Pyhtmd

array=[
# '<a href="https://baidu.com">baidu.com </a>',
# '<a>baidu.com </a>',
# '<a href="https://baidu.com">baidu.com</a>',
# '<h1>I am H1 tag </h1>',
# '<h2>I am H2 tag </h2>',
# '<h3>I am H3 tag </h3>',
# '<h4>I am H4 tag </h4>',
# '<h5>I am H5 tag </h5>',
# '<h6>I am H6 tag </h6>',
# '<code>Python</code>',
# '<img src="https://www.baidu.com/img/bd_logo1.png">',
# '<img src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo">',
# '<pre><code>coooood</code></pre>',
'left center <b>haha</b>',
'<b>left</b> center right',
# 'left<b>center</b>right',
# 'left <b>center</b> right',
# '<table class="tfo-notebook-buttons tfo-api" align="left"><tbody><tr><td>  <a target="_blank" ' \
#         'href="/versions/r1.15/api_docs/python/tf/clip_by_value">  <img ' \
#         'src="https://tensorflow.google.cn/images/tf_logo_32px.png">  TensorFlow 1 version</a></td><td>  <a ' \
#         'target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/clip_ops.py#L36' \
#         '-L93">    <img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">    View source on GitHub  ' \
#         '</a></td></tr></tbody></table> ',
# 'Clips tensor values to a specified min and max.',
# '<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no"',
# '<li>Hello world</li>',
# '<pre class="prettyprint lang-python" translate="no" dir="ltr" is-upgraded=""><code translate="no" ' \
#     'dir="ltr">tf.clip_by_value(    t,    clip_value_min,    clip_value_max,    name=None)</code></pre> ',
# '<li><a href="https://tensorflow.google.cn/tutorials/generative/deepdream">DeepDream</a></li><li><a ' \
#     'href="https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm">Adversarial example using ' \
#     'FGSM</a></li><li><a href="https://tensorflow.google.cn/tutorials/generative/style_transfer">Neural style ' \
#     'transfer</a></li> ',
# '<strong>Note:</strong><span> <code translate="no" dir="ltr">clip_value_min</code> needs to be smaller or equal ' \
#     'to <code translate="no" dir="ltr">clip_value_max</code> forcorrect results.</span> ',
# 'A clipped <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.',

# '<li>liiiiiiiii</li>'
]


for item in array:
    mk=Pyhtmd(item).markdown()
    print('===========================')
    print(mk)
    print('===========================')
   
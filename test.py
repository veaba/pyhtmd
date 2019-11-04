# todo table
from pyhtmd.core import Pyhtmd
from pyhtmd.utils import remove_attrs,get_tag_name
from pyhtmd.html_parser import Pip

# from pyhtmd.core import Pyhtmd

array = [
    # '<a href="https://baidu.com">baidu.com </a>',
    # '<a>baidu.com </a>',
    # '<a href="https://baidu.com">baidu.com</a>',
    # '<p><a href="https://tensorflow.google.cn/api_docs/python/tf/audio"><code translate="no" dir="ltr">audio</code></a> module: Public API for tf.audio namespace.</p>',
    # '<h1>I am H1 tag </h1>',
    # '<h2>I am H2 tag </h2>',
    # '<h2>Modules</h2>',
    '<h2 id="class_devicespec" is-upgraded="">Class <code translate="no" dir="ltr">DeviceSpec</code></h2>',
    # '<h2><a href="x22">222</a>aaaaa</h2>'
    # '<h2 id="modules" is-upgraded="">Modules<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button><a href="#top_of_page" class="devsite-back-to-top-link material-icons" data-title="返回页首"></a></h2>',
    # '<h3>I am H3 tag </h3>',
    # '<h4>I am H4 tag </h4>',
    # '<h5>I am H5 tag </h5>',
    # '<h6>I am H6 tag </h6>',
    # '<code>Python</code>',
    # '<img src="https://www.baidu.com/img/bd_logo1.png">',
    # '<img src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo">',
    # '<pre><code>coooood</code></pre>',
    # 'left center <b>haha</b>',
    # '<b>left</b> center right',
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

    # '<h3 id="aliases" is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons" title="Copy link to this section"></button></h3>'
    # '<li>liiiiiiiii</li>',
    # #首尾换行符
    # '\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v1.clip_by_value</code></a></li>\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a></li>\n',
    # '<table class="tfo-notebook-buttons tfo-api" align="left">\n\n<tbody><tr><td><a target="_blank" href="/versions/r1.15/api_docs/python/tf/clip_by_value"><img src="https://tensorflow.google.cn/images/tf_logo_32px.png">TensorFlow 1 version</a></td><td><a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/clip_ops.py#L36-L93"><img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">View source on GitHub</a></td></tr></tbody></table>',
    # 'Clips tensor values to a specified min and max.',
    # '<h3 id="aliases" is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons" title="Copy link to this section"></button></h3>',
    # '<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v1.clip_by_value</code></a></li>\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a></li>',
    # '<h4 id="returns" is-upgraded="">Returns:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4>===21===A clipped <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.===21===<h4 id="raises" is-upgraded="">Raises:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4>===21===<li><b><code translate="no" dir="ltr">ValueError</code></b>: If the clip tensors would trigger array broadcastingthat would make the returned tensor larger than the input.</li><li><b><code translate="no" dir="ltr">TypeError</code></b>: If dtype of the input is <code translate="no" dir="ltr">int32</code> and dtype ofthe <code translate="no" dir="ltr">clip_value_min\' or</code>clip_value_max<code translate="no" dir="ltr">is</code>float32</li>',
    # '<pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">A </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">constant</span><span class="pun">([[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span class="pun">],</span><span class="pln"> </span><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">21</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span class="pun">]])</span><span class="pln"><br>B </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span class="lit">3</span><span class="pun">)</span><span class="pln"> </span><span class="com"># [[1, 3, 3],[3, 3, 3]]</span><span class="pln"><br>C </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0.</span><span class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span class="lit">3.</span><span class="pun">)</span><span class="pln"> </span><span class="com"># throws `TypeError`</span><span class="pln"><br></span><span class="kwd">as</span><span class="pln"> input </span><span class="kwd">and</span><span class="pln"> clip_values are of different dtype<br></span></code></pre><div class="devsite-code-buttons-container"><button class="gc-analytics-event material-iconsdevsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div>',
    # '<li><b><code translate="no" dir="ltr">t</code></b>: A <code translate="no" dir="ltr">Tensor</code> or <code translate="no" dir="ltr">IndexedSlices</code>.</li><li><b><code translate="no" dir="ltr">clip_value_min</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The minimum value to clip by.</li><li><b><code translate="no" dir="ltr">clip_value_max</code></b>: A 0-D (scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code translate="no" dir="ltr">t</code>. The maximum value to clip by.</li><li><b><code translate="no" dir="ltr">name</code></b>: A name for the operation (optional).</li>',
    # '<li><b><code translate="no" dir="ltr">ValueError</code></b>: If the clip tensors would trigger array broadcastingthat would make the returned tensor larger than the input.</li><li><b><code translate="no" dir="ltr">TypeError</code></b>: If dtype of the input is <code translate="no" dir="ltr">int32</code> and dtype ofthe <code translate="no" dir="ltr">clip_value_min or</code>clip_value_max<code translate="no" dir="ltr">is</code>float32</li>',
    # '<pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">A </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">constant</span><span class="pun">([[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span class="pun">],</span><span class="pln"> </span><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">21</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span class="pun">]])</span><span class="pln"><br>B </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span class="lit">3</span><span class="pun">)</span><span class="pln"> </span><span class="com"># [[1, 3, 3],[3, 3, 3]]</span><span class="pln"><br>C </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0.</span><span class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span class="lit">3.</span><span class="pun">)</span><span class="pln"> </span><span class="com"># throws `TypeError`</span><span class="pln"><br></span><span class="kwd">as</span><span class="pln"> input </span><span class="kwd">and</span><span class="pln"> clip_values are of different dtype<br></span></code></pre><div class="devsite-code-buttons-container"><button class="gc-analytics-event material-iconsdevsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" title="Copy"></button></div>',
    # '<pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; t</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_min</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_max</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"><br></span><span class="pun">)</span><span class="pln"><br></span></code></pre>',
    # '<pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; t</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_min</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_max</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"><br></span><span class="pun">)</span><span class="pln"><br></span></code></pre>',
    # '<h2 id="modules" isupgraded="">Modules<button role="button" class="devsite-heading-link button-flat ',
    # 'material-icons" title="Copy link to this section"></button><a href="#top_of_page" class="devsite-back-to-top-link ',
    # 'material-icons" title="返回页首"></a></h2> '
]

for item in array:
    # mk = Pip(item).factory()
    mk = Pyhtmd(item).markdown()
    
    print('===========================')
    print(mk)
    # x =get_tag_name(item)
    # print(x)
    print('===========================')

# x ='\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v1.clip_by_value</code></a></li>\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a></li>\n'

# o = x.replace('\n','')
# print(o)

# mk=Pyhtmd(o).markdown()
# print(mk)


# array=[
#     '<h3 id="aliases" is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons" title="Copy link to this section"></button></h3>'
# ]

# for item in array:
#     ret = re.sub(r'<b(.*?)">', '<b>', item)
#     print(ret)

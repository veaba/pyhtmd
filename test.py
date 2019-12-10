# todo table
from pyhtmd.core import Pyhtmd
from pyhtmd.utils import remove_attrs, get_tag_name
from pyhtmd.html_parser import Pip

# from pyhtmd.core import Pyhtmd

array = [
    # '<a href="https://baidu.com">baidu.com </a>', '<a>baidu.com </a>', '<a href="https://baidu.com">baidu.com</a>',
    # '<p><a href="https://tensorflow.google.cn/api_docs/python/tf/audio"><code translate="no"
    # dir="ltr">audio</code></a> module: Public API for tf.audio namespace.</p>', '<h1>I am H1 tag </h1>',
    # '<h2>I am H2 tag </h2>', '<h2>Modules</h2>', '<h2 id="class_devicespec" is-upgraded="">Class <code
    # translate="no" dir="ltr">DeviceSpec</code></h2>', '<h2><a href="x22">222</a>aaaaa</h2>' '<h2 id="modules"
    # is-upgraded="">Modules<button role="button" class="devsite-heading-link button-flat material-icons"
    # data-title="Copy link to this section"></button><a href="#top_of_page" class="devsite-back-to-top-link
    # material-icons" data-title="返回页首"></a></h2>', '<h3>I am H3 tag </h3>', '<h4>I am H4 tag </h4>', '<h5>I am H5
    # tag </h5>', '<h6>I am H6 tag </h6>', '<code>Python</code>',
    # '<img src="https://www.baidu.com/img/bd_logo1.png">', '<img src="https://www.baidu.com/img/bd_logo1.png"
    # alt="百度logo">', '<pre><code>coooood</code></pre>', 'left center <b>haha</b>', '<b>left</b> center right',
    # 'left<b>center</b>right', 'left <b>center</b> right', '<table class="tfo-notebook-buttons tfo-api"
    # align="left"><tbody><tr><td>  <a target="_blank" ' \ 'href="/versions/r1.15/api_docs/python/tf/clip_by_value">
    # <img ' \ 'src="https://tensorflow.google.cn/images/tf_logo_32px.png">  TensorFlow 1 version</a></td><td>  <a '
    # \ 'target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/clip_ops.py
    # #L36' \ '-L93">    <img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">    View source on
    # GitHub  ' \ '</a></td></tr></tbody></table> ', 'Clips tensor values to a specified min and max.',
    # '<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no"', '<li>Hello world</li>',
    # '<pre class="prettyprint lang-python" translate="no" dir="ltr" is-upgraded=""><code translate="no" ' \
    # 'dir="ltr">tf.clip_by_value(    t,    clip_value_min,    clip_value_max,    name=None)</code></pre> ',
    # '<li><a href="https://tensorflow.google.cn/tutorials/generative/deepdream">DeepDream</a></li><li><a ' \
    # 'href="https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm">Adversarial example using ' \
    # 'FGSM</a></li><li><a href="https://tensorflow.google.cn/tutorials/generative/style_transfer">Neural style ' \
    # 'transfer</a></li> ', '<strong>Note:</strong><span> <code translate="no" dir="ltr">clip_value_min</code> needs
    # to be smaller or equal ' \ 'to <code translate="no" dir="ltr">clip_value_max</code> forcorrect results.</span>
    # ', 'A clipped <code translate="no" dir="ltr">Tensor</code> or <code translate="no"
    # dir="ltr">IndexedSlices</code>.', '<h3 id="aliases" is-upgraded="">Aliases:<button role="button"
    # class="devsite-heading-link button-flat material-icons" title="Copy link to this section"></button></h3>'
    # '<li>liiiiiiiii</li>', #首尾换行符 '\n<li><a href="/api_docs/python/tf/clip_by_value"><code translate="no"
    # dir="ltr">tf.compat.v1.clip_by_value</code></a></li>\n<li><a href="/api_docs/python/tf/clip_by_value"><code
    # translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a></li>\n', '<table class="tfo-notebook-buttons
    # tfo-api" align="left">\n\n<tbody><tr><td><a target="_blank"
    # href="/versions/r1.15/api_docs/python/tf/clip_by_value"><img
    # src="https://tensorflow.google.cn/images/tf_logo_32px.png">TensorFlow 1 version</a></td><td><a target="_blank"
    # href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/clip_ops.py#L36-L93"><img
    # src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">View source on
    # GitHub</a></td></tr></tbody></table>', 'Clips tensor values to a specified min and max.', '<h3 id="aliases"
    # is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons"
    # title="Copy link to this section"></button></h3>', '<li><a href="/api_docs/python/tf/clip_by_value"><code
    # translate="no" dir="ltr">tf.compat.v1.clip_by_value</code></a></li>\n<li><a
    # href="/api_docs/python/tf/clip_by_value"><code translate="no"
    # dir="ltr">tf.compat.v2.clip_by_value</code></a></li>', '<h4 id="returns" is-upgraded="">Returns:<button
    # role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this
    # section"></button></h4>===21===A clipped <code translate="no" dir="ltr">Tensor</code> or <code translate="no"
    # dir="ltr">IndexedSlices</code>.===21===<h4 id="raises" is-upgraded="">Raises:<button role="button"
    # class="devsite-heading-link button-flat material-icons" data-title="Copy link to this
    # section"></button></h4>===21===<li><b><code translate="no" dir="ltr">ValueError</code></b>: If the clip tensors
    # would trigger array broadcastingthat would make the returned tensor larger than the input.</li><li><b><code
    # translate="no" dir="ltr">TypeError</code></b>: If dtype of the input is <code translate="no"
    # dir="ltr">int32</code> and dtype ofthe <code translate="no" dir="ltr">clip_value_min\'
    # or</code>clip_value_max<code translate="no" dir="ltr">is</code>float32</li>', '<pre class="lang-python"
    # translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">A </span><span
    # class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span
    # class="pln">constant</span><span class="pun">([[</span><span class="lit">1</span><span class="pun">,
    # </span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln">
    # </span><span class="lit">13</span><span class="pun">],</span><span class="pln"> </span><span class="pun">[
    # </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span
    # class="lit">21</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span
    # class="pun">]])</span><span class="pln"><br>B </span><span class="pun">=</span><span class="pln">
    # tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span
    # class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span
    # class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln">
    # clip_value_max</span><span class="pun">=</span><span class="lit">3</span><span class="pun">)</span><span
    # class="pln"> </span><span class="com"># [[1, 3, 3],[3, 3, 3]]</span><span class="pln"><br>C </span><span
    # class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span
    # class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,
    # </span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0.</span><span
    # class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span
    # class="lit">3.</span><span class="pun">)</span><span class="pln"> </span><span class="com"># throws
    # `TypeError`</span><span class="pln"><br></span><span class="kwd">as</span><span class="pln"> input </span><span
    # class="kwd">and</span><span class="pln"> clip_values are of different dtype<br></span></code></pre><div
    # class="devsite-code-buttons-container"><button class="gc-analytics-event material-iconsdevsite-icon-code-dark
    # devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle"
    # track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button
    # class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide
    # Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle"
    # data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy"
    # data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode"
    # track-name="clickToCopy" data-title="Copy"></button></div>', '<li><b><code translate="no"
    # dir="ltr">t</code></b>: A <code translate="no" dir="ltr">Tensor</code> or <code translate="no"
    # dir="ltr">IndexedSlices</code>.</li><li><b><code translate="no" dir="ltr">clip_value_min</code></b>: A 0-D (
    # scalar) <code translate="no" dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with
    # the same shapeas <code translate="no" dir="ltr">t</code>. The minimum value to clip by.</li><li><b><code
    # translate="no" dir="ltr">clip_value_max</code></b>: A 0-D (scalar) <code translate="no"
    # dir="ltr">Tensor</code>, or a <code translate="no" dir="ltr">Tensor</code> with the same shapeas <code
    # translate="no" dir="ltr">t</code>. The maximum value to clip by.</li><li><b><code translate="no"
    # dir="ltr">name</code></b>: A name for the operation (optional).</li>', '<li><b><code translate="no"
    # dir="ltr">ValueError</code></b>: If the clip tensors would trigger array broadcastingthat would make the
    # returned tensor larger than the input.</li><li><b><code translate="no" dir="ltr">TypeError</code></b>: If dtype
    # of the input is <code translate="no" dir="ltr">int32</code> and dtype ofthe <code translate="no"
    # dir="ltr">clip_value_min or</code>clip_value_max<code translate="no" dir="ltr">is</code>float32</li>',
    # '<pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">A
    # </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span
    # class="pln">constant</span><span class="pun">([[</span><span class="lit">1</span><span class="pun">,
    # </span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln">
    # </span><span class="lit">13</span><span class="pun">],</span><span class="pln"> </span><span class="pun">[
    # </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span
    # class="lit">21</span><span class="pun">,</span><span class="pln"> </span><span class="lit">13</span><span
    # class="pun">]])</span><span class="pln"><br>B </span><span class="pun">=</span><span class="pln">
    # tf</span><span class="pun">.</span><span class="pln">clip_by_value</span><span class="pun">(</span><span
    # class="pln">A</span><span class="pun">,</span><span class="pln"> clip_value_min</span><span
    # class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln">
    # clip_value_max</span><span class="pun">=</span><span class="lit">3</span><span class="pun">)</span><span
    # class="pln"> </span><span class="com"># [[1, 3, 3],[3, 3, 3]]</span><span class="pln"><br>C </span><span
    # class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span
    # class="pln">clip_by_value</span><span class="pun">(</span><span class="pln">A</span><span class="pun">,
    # </span><span class="pln"> clip_value_min</span><span class="pun">=</span><span class="lit">0.</span><span
    # class="pun">,</span><span class="pln"> clip_value_max</span><span class="pun">=</span><span
    # class="lit">3.</span><span class="pun">)</span><span class="pln"> </span><span class="com"># throws
    # `TypeError`</span><span class="pln"><br></span><span class="kwd">as</span><span class="pln"> input </span><span
    # class="kwd">and</span><span class="pln"> clip_values are of different dtype<br></span></code></pre><div
    # class="devsite-code-buttons-container"><button class="gc-analytics-event material-iconsdevsite-icon-code-dark
    # devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle"
    # track-type="exampleCode" track-name="darkCodeToggle" title="Dark code theme"></button><button
    # class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide
    # Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle"
    # title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy"
    # data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode"
    # track-name="clickToCopy" title="Copy"></button></div>', '<pre class="lang-python" translate="no" dir="ltr"
    # is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span
    # class="pln">clip_by_value</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; t</span><span
    # class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_min</span><span class="pun">,</span><span
    # class="pln"><br>&nbsp; &nbsp; clip_value_max</span><span class="pun">,</span><span class="pln"><br>&nbsp;
    # &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"><br></span><span
    # class="pun">)</span><span class="pln"><br></span></code></pre>', '<pre class="lang-python" translate="no"
    # dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span
    # class="pln">clip_by_value</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; t</span><span
    # class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; clip_value_min</span><span class="pun">,</span><span
    # class="pln"><br>&nbsp; &nbsp; clip_value_max</span><span class="pun">,</span><span class="pln"><br>&nbsp;
    # &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"><br></span><span
    # class="pun">)</span><span class="pln"><br></span></code></pre>', '<h2 id="modules" isupgraded="">Modules<button
    # role="button" class="devsite-heading-link button-flat ', 'material-icons" title="Copy link to this
    # section"></button><a href="#top_of_page" class="devsite-back-to-top-link ', 'material-icons"
    # title="返回页首"></a></h2> ' '<a href="https://tensorflow.google.cn/api_docs/python/tf/math/exp"><code
    # translate="no" dir="ltr">exp(' '...)</code></a>: Computes exponential of x element-wise.  <span
    # class="MathJax_Preview" style="color: ' 'inherit;"></span><span class="MathJax_SVG"
    # id="MathJax-Element-1-Frame" tabindex="0" data-mathml="<math '
    # 'xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>y</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup
    # ></math' '>" role="presentation" style="font-size: 100%; display: inline-block; position: relative;"><img '
    # 'src="Overview.md_0.png"><span class="MJX_Assistive_MathML" role="presentation"><math '
    # 'xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></span'
    # '></span><script type="math/tex" id="MathJax-Element-1">y = e^x</script>. ', '<li><p>whahaww <a
    # href="xxx"><code>cococoococo</code></a></p></li>', '<li><p><code translate="no"
    # dir="ltr">EXPERIMENTAL_ACCUMULATE_N</code>: Gradient terms are summed using the ' '"AccumulateN" op (see <code
    # translate="no" dir="ltr">tf.accumulate_n</code>), which accumulates theoverall sum ' 'in a single buffer that
    # is shared across threads. This method of summing gradients can result in a lower memory ' 'footprint and lower
    # latency at the expense of higher CPU/GPU utilization.For gradients of types that ' '"AccumulateN" does not
    # support, this summation method falls back on the behavior of <code translate="no" '
    # 'dir="ltr">EXPERIMENTAL_TREE</code></p></li> ', '<devsite-code><pre class="" translate="no" dir="ltr"
    # is-upgraded=""><code dir="ltr"><span class="com"># my_spec ' 'and my_updated_spec are unrelated.</span><span
    # class="pln"><br>my_spec </span><span class="pun">=</span><span ' 'class="pln"> tf</span><span
    # class="pun">.</span><span class="typ">DeviceSpec</span><span ' 'class="pun">.</span><span
    # class="pln">from_string</span><span class="pun">(</span><span ' 'class="str">"/CPU:0"</span><span
    # class="pun">)</span><span class="pln"><br>my_updated_spec </span><span ' 'class="pun">=</span><span
    # class="pln"> tf</span><span class="pun">.</span><span ' 'class="typ">DeviceSpec</span><span
    # class="pun">.</span><span class="pln">from_string</span><span class="pun">(' '</span><span
    # class="str">"/GPU:0"</span><span class="pun">)</span><span class="pln"><br></span><span '
    # 'class="kwd">with</span><span class="pln"> tf</span><span class="pun">.</span><span '
    # 'class="pln">device</span><span class="pun">(</span><span class="pln">my_updated_spec</span><span '
    # 'class="pun">):</span><span class="pln"><br>&nbsp; </span><span class="pun">...</span><span '
    # 'class="pln"><br></span></code></pre><div class="devsite-code-buttons-container"><button '
    # 'class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide
    # ' 'Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" '
    # 'data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light
    # ' 'devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" '
    # 'track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button '
    # 'class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" '
    # 'data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" '
    # 'data-title="Copy"></button></div></devsite-code> ', '<li>11111 <ul><li>2222</li>3333<li>444</li></ul></li>',
    # '<li>11111<ul><li>222</li><ul><li>4444</li></ul></ul></li>',
    # '<li>aaaaa</li><li>bbbbb</li><li>ccccc</li><li>ddddd</li><li>eeeee</li> \
    # <li>ffff</li><li>gggg</li><li>hhhhh</li><li>jjjjj</li>v', '<ol><li>1111</li>2222<li></li></ol>',
    # '<devsite-heading><h3 id="aliases" is-upgraded="">Aliases:</h3></devsite-heading>',
    # 'dsad <p> dddddd</p>',
    # 'a',
    # '<a>',
    # '<a></a>',
    '""""'
    ''
    ''
    '"""'
]


item = """
<p><em>NOTE</em>: <code translate="no" dir="ltr">Substr</code> supports broadcasting up to two dimensions. More about
broadcasting
<a href="http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html">here</a></p>
"""

mk = Pyhtmd(item).markdown()
print('============结果Start：===============')
print(mk)
# x =get_tag_name(item)
# print(x)
print('============结果End：===============')


# todo table
from pyhtmd.core import Pyhtmd
# from pyhtmd.utils import remove_attrs, get_tag_name

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
    # '<p><em>NOTE</em>: <code translate="no" dir="ltr">Substr</code> supports broadcasting up to two dimensions. More about broadcasting<a href="http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html">here</a></p>',
    ''
    ''
    '"""'
]


item = """
<ul>
<li><p><b><code translate="no" dir="ltr">model_fn</code></b>: Model function. Follows the signature:</p>

<ul>
<li><p>Args:</p></li>
<li><p><code translate="no" dir="ltr">features</code>: This is the first item returned from the <code translate="no" dir="ltr">input_fn</code>
   passed to <code translate="no" dir="ltr">train</code>, <code translate="no" dir="ltr">evaluate</code>, and <code translate="no" dir="ltr">predict</code>. This should be a
   single <a href="https://tensorflow.google.cn/api_docs/python/tf/Tensor"><code translate="no" dir="ltr">tf.Tensor</code></a> or <code translate="no" dir="ltr">dict</code> of same.</p></li>
<li><p><code translate="no" dir="ltr">labels</code>: This is the second item returned from the <code translate="no" dir="ltr">input_fn</code>
   passed to <code translate="no" dir="ltr">train</code>, <code translate="no" dir="ltr">evaluate</code>, and <code translate="no" dir="ltr">predict</code>. This should be a
   single <a href="https://tensorflow.google.cn/api_docs/python/tf/Tensor"><code translate="no" dir="ltr">tf.Tensor</code></a> or <code translate="no" dir="ltr">dict</code> of same (for multi-head models).
   If mode is <a href="https://tensorflow.google.cn/api_docs/python/tf/estimator/ModeKeys#PREDICT"><code translate="no" dir="ltr">tf.estimator.ModeKeys.PREDICT</code></a>, <code translate="no" dir="ltr">labels=None</code> will
   be passed. If the <code translate="no" dir="ltr">model_fn</code>'s signature does not accept
   <code translate="no" dir="ltr">mode</code>, the <code translate="no" dir="ltr">model_fn</code> must still be able to handle
   <code translate="no" dir="ltr">labels=None</code>.</p></li>
<li><p><code translate="no" dir="ltr">mode</code>: Optional. Specifies if this is training, evaluation or
   prediction. See <a href="https://tensorflow.google.cn/api_docs/python/tf/estimator/ModeKeys"><code translate="no" dir="ltr">tf.estimator.ModeKeys</code></a>.</p></li>
<li><p><code translate="no" dir="ltr">params</code>: Optional <code translate="no" dir="ltr">dict</code> of hyperparameters.  Will receive what
   is passed to Estimator in <code translate="no" dir="ltr">params</code> parameter. This allows
   to configure Estimators from hyper parameter tuning.</p></li>
<li><p><code translate="no" dir="ltr">config</code>: Optional <a href="/api_docs/python/tf/estimator/RunConfig"><code translate="no" dir="ltr">estimator.RunConfig</code></a> object. Will receive what
   is passed to Estimator as its <code translate="no" dir="ltr">config</code> parameter, or a default
   value. Allows setting up things in your <code translate="no" dir="ltr">model_fn</code> based on
   configuration such as <code translate="no" dir="ltr">num_ps_replicas</code>, or <code translate="no" dir="ltr">model_dir</code>.</p></li>
<li><p>Returns:
<a href="https://tensorflow.google.cn/api_docs/python/tf/estimator/EstimatorSpec"><code translate="no" dir="ltr">tf.estimator.EstimatorSpec</code></a></p></li>
</ul></li>
<li><p><b><code translate="no" dir="ltr">model_dir</code></b>: Directory to save model parameters, graph and etc. This can
also be used to load checkpoints from the directory into an estimator to
continue training a previously saved model. If <code translate="no" dir="ltr">PathLike</code> object, the
path will be resolved. If <code translate="no" dir="ltr">None</code>, the model_dir in <code translate="no" dir="ltr">config</code> will be used
if set. If both are set, they must be same. If both are <code translate="no" dir="ltr">None</code>, a
temporary directory will be used.</p></li>
<li><p><b><code translate="no" dir="ltr">config</code></b>: <a href="/api_docs/python/tf/estimator/RunConfig"><code translate="no" dir="ltr">estimator.RunConfig</code></a> configuration object.</p></li>
<li><p><b><code translate="no" dir="ltr">params</code></b>: <code translate="no" dir="ltr">dict</code> of hyper parameters that will be passed into <code translate="no" dir="ltr">model_fn</code>.
    Keys are names of parameters, values are basic python types.</p></li>
<li><p><b><code translate="no" dir="ltr">warm_start_from</code></b>: Optional string filepath to a checkpoint or SavedModel to
             warm-start from, or a <a href="https://tensorflow.google.cn/api_docs/python/tf/estimator/WarmStartSettings"><code translate="no" dir="ltr">tf.estimator.WarmStartSettings</code></a>
             object to fully configure warm-starting.</p>
<devsite-code><pre class="" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="typ">If</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> only TRAINABLE variables are warm</span><span class="pun">-</span><span class="pln">started</span><span class="pun">.</span><span class="pln"><br><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="typ">If</span><span class="pln"> the </span><span class="kwd">string</span><span class="pln"> filepath </span><span class="kwd">is</span><span class="pln"> provided instead of a<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">a href</span><span class="pun">=</span><span class="str">"../../../../tf/estimator/WarmStartSettings"</span><span class="pun">&gt;&lt;</span><span class="pln">code</span><span class="pun">&gt;</span><span class="pln">tf</span><span class="pun">.</span><span class="pln">estimator</span><span class="pun">.</span><span class="typ">WarmStartSettings</span><span class="pun">&lt;</span><span class="str">/code&gt;&lt;/</span><span class="pln">a</span><span class="pun">&gt;,</span><span class="pln"> </span><span class="kwd">then</span><span class="pln"> all variables are<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;warm</span><span class="pun">-</span><span class="pln">started</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">and</span><span class="pln"> it </span><span class="kwd">is</span><span class="pln"> assumed that vocabularies<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">and</span><span class="pln"> </span><span class="pun">&lt;</span><span class="pln">a href</span><span class="pun">=</span><span class="str">"../../../../tf/Tensor"</span><span class="pun">&gt;&lt;</span><span class="pln">code</span><span class="pun">&gt;</span><span class="pln">tf</span><span class="pun">.</span><span class="typ">Tensor</span><span class="pun">&lt;</span><span class="str">/code&gt;&lt;/</span><span class="pln">a</span><span class="pun">&gt;</span><span class="pln"> names are unchanged</span><span class="pun">.</span><span class="pln"><br></span></code></pre><div class="devsite-code-buttons-container"><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" title="Copy"></button></div></devsite-code></li>
</ul>
"""

mk = Pyhtmd(item).markdown()
print('============结果Start：===============')
print(mk)
print('============结果End：===============')


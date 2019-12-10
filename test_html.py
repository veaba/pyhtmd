html_content="""
<article class="devsite-article-inner"><div>  <ul class="devsite-breadcrumb-list"><li class="devsite-breadcrumb-item "><a href="/" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="1">TensorFlow</a></li><li class="devsite-breadcrumb-item "><div></div><a href="/api" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="2">API</a></li><li class="devsite-breadcrumb-item "><div></div>  <a href="/api_docs" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3">TensorFlow Core r2.0</a></li><li class="devsite-breadcrumb-item "><div></div><a href="/api_docs/python/tf" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="4">Python</a></li>  </ul>   <devsite-page-rating position="header" selected-rating="0" hover-rating-star="0"> <div><div><div></div><div></div><div></div><div></div><div></div></div><div><span class="devsite-rating-stats"></span></div></div></devsite-page-rating>  </div>  <devsite-heading text="tf.compat.v1.substr" for="tf.compat.v1.substr" level="h1"><h1 class="devsite-page-title" is-upgraded="" id="tf.compat.v1.substr">tf.compat.v1.substr</h1></devsite-heading><devsite-toc class="devsite-nav devsite-toc-embedded" devsite-toc-embedded="" hidden=""></devsite-toc><div><div><meta itemprop="name" content="tf.compat.v1.substr"><meta itemprop="path" content="Stable"></div><div><table class="tfo-notebook-buttons tfo-api" align="left"><tbody><tr><td>  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/string_ops.py#L389-L392"><img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">View source on GitHub  </a></td></tr></tbody></table></div><p>Return substrings from <code translate="no" dir="ltr">Tensor</code> of strings.</p><devsite-code><pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span class="pln">compat</span><span class="pun">.</span><span class="pln">v1</span><span class="pun">.</span><span class="pln">substr</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; input</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; pos</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; len</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; unit</span><span class="pun">=</span><span class="str">'BYTE'</span><span class="pln"><br></span><span class="pun">)</span><span class="pln"><br></span></code></pre><div><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><p>For each string in the input <code translate="no" dir="ltr">Tensor</code>, creates a substring starting at index<code translate="no" dir="ltr">pos</code> with a total length of <code translate="no" dir="ltr">len</code>.</p><p>If <code translate="no" dir="ltr">len</code> defines a substring that would extend beyond the length of the inputstring, then as many characters as possible are used.</p><p>A negative <code translate="no" dir="ltr">pos</code> indicates distance within the string backwards from the end.</p><p>If <code translate="no" dir="ltr">pos</code> specifies an index which is out of range for any of the input strings,then an <code translate="no" dir="ltr">InvalidArgumentError</code> is thrown.</p><p><code translate="no" dir="ltr">pos</code> and <code translate="no" dir="ltr">len</code> must have the same shape, otherwise a <code translate="no" dir="ltr">ValueError</code> is thrown onOp creation.</p><p><em>NOTE</em>: <code translate="no" dir="ltr">Substr</code> supports broadcasting up to two dimensions. More aboutbroadcasting<a href="http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html">here</a></p><hr><p>Examples</p><p>Using scalar <code translate="no" dir="ltr">pos</code> and <code translate="no" dir="ltr">len</code>:</p><devsite-code><pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">input </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="pln">b</span><span class="str">'Hello'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'World'</span><span class="pun">]</span><span class="pln"><br>position </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pln"><br>length </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pln"><br><br>output </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="pln">b</span><span class="str">'ell'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'orl'</span><span class="pun">]</span><span class="pln"><br></span></code></pre><div><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><p>Using <code translate="no" dir="ltr">pos</code> and <code translate="no" dir="ltr">len</code> with same shape as <code translate="no" dir="ltr">input</code>:</p><devsite-code><pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">input </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="pln">b</span><span class="str">'ten'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'eleven'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'twelve'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">[</span><span class="pln">b</span><span class="str">'thirteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'fourteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'fifteen'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">[</span><span class="pln">b</span><span class="str">'sixteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'seventeen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'eighteen'</span><span class="pun">]]</span><span class="pln"><br>position </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]]</span><span class="pln"><br>length </span><span class="pun">=</span><span class="pln"> &nbsp; </span><span class="pun">[[</span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">4</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="lit">4</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">]]</span><span class="pln"><br><br>output </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="pln">b</span><span class="str">'en'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'eve'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'lve'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="pln">b</span><span class="str">'hirt'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'urt'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'te'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="pln">b</span><span class="str">'ixtee'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'vente'</span><span class="pun">,</span><span class="pln">b</span><span class="str">'hteen'</span><span class="pun">]]</span><span class="pln"><br></span></code></pre><div><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><p>Broadcasting <code translate="no" dir="ltr">pos</code> and <code translate="no" dir="ltr">len</code> onto <code translate="no" dir="ltr">input</code>:</p><devsite-code><pre class="" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">input </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="pln">b</span><span class="str">'ten'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'eleven'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'twelve'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">[</span><span class="pln">b</span><span class="str">'thirteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'fourteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'fifteen'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">[</span><span class="pln">b</span><span class="str">'sixteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'seventeen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'eighteen'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">[</span><span class="pln">b</span><span class="str">'nineteen'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'twenty'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'twentyone'</span><span class="pun">]]</span><span class="pln"><br>position </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span><span class="pln"><br>length </span><span class="pun">=</span><span class="pln"> &nbsp; </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span><span class="pln"><br><br>output </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="pln">b</span><span class="str">'e'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'ev'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'lve'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="pln">b</span><span class="str">'h'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'ur'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'tee'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="pln">b</span><span class="str">'i'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'ve'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'hte'</span><span class="pun">],</span><span class="pln"><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">[</span><span class="pln">b</span><span class="str">'i'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'en'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'nty'</span><span class="pun">]]</span><span class="pln"><br></span></code></pre><div><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><p>Broadcasting <code translate="no" dir="ltr">input</code> onto <code translate="no" dir="ltr">pos</code> and <code translate="no" dir="ltr">len</code>:</p><devsite-code><pre class="" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">input </span><span class="pun">=</span><span class="pln"> b</span><span class="str">'thirteen'</span><span class="pln"><br>position </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><spanclass="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">]</span><span class="pln"><br>length </span><span class="pun">=</span><span class="pln"> &nbsp; </span><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]</span><span class="pln"><br><br>output </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="pln">b</span><span class="str">'hir'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'ee'</span><span class="pun">,</span><span class="pln"> b</span><span class="str">'n'</span><span class="pun">]</span><span class="pln"><br></span></code></pre><div><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle"
track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><devsite-heading text="Args:" for="args" level="h4" link=""><h4 id="args" is-upgraded="">Args:</h4></devsite-heading><ul><li><b><code translate="no" dir="ltr">input</code></b>: A <code translate="no" dir="ltr">Tensor</code> of type <code translate="no" dir="ltr">string</code>. Tensor of strings</li><li><b><code translate="no" dir="ltr">pos</code></b>: A <code translate="no" dir="ltr">Tensor</code>. Must be one of the following types: <code translate="no" dir="ltr">int32</code>, <code translate="no" dir="ltr">int64</code>.Scalar defining the position of first character in each substring</li><li><b><code translate="no" dir="ltr">len</code></b>: A <code translate="no" dir="ltr">Tensor</code>. Must have the same type as <code translate="no" dir="ltr">pos</code>.Scalar defining the number of characters to include in each substring</li><li><b><code translate="no" dir="ltr">unit</code></b>: An optional <code translate="no" dir="ltr">string</code> from: <code translate="no" dir="ltr">"BYTE", "UTF8_CHAR"</code>. Defaults to <code translate="no" dir="ltr">"BYTE"</code>.The unit that is used to create the substring.  One of: <code translate="no" dir="ltr">"BYTE"</code> (fordefining position and length by bytes) or <code translate="no" dir="ltr">"UTF8_CHAR"</code> (for the UTF-8encoded Unicodecode points).  The default is <code translate="no" dir="ltr">"BYTE"</code>. Results are undefined if<code translate="no" dir="ltr">unit=UTF8_CHAR</code> and the <code translate="no" dir="ltr">input</code> strings do not contain structurally validUTF-8.</li><li><b><code translate="no" dir="ltr">name</code></b>: A name for the operation (optional).</li></ul><devsite-heading text="Returns:" for="returns" level="h4" link=""><h4 id="returns" is-upgraded="">Returns:</h4></devsite-heading><p>A <code translate="no" dir="ltr">Tensor</code> of type <code translate="no" dir="ltr">string</code>.</p>  </div>   <devsite-page-rating position="footer" selected-rating="0" hover-rating-star="0"> <div><div>Was this page helpful?</div><div><div></div><div></div><div></div><div></div><div></div></div><div><span class="devsite-rating-stats"></span></div></div></devsite-page-rating>  </article>
"""

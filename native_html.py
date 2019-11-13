from html.parser import HTMLParser


class HTML(HTMLParser):
    def handle_starttag(self,tag,attrs):
        pass
        # print('start:',tag,attrs)
    def handle_endtag(self,tag):
        pass
        # print('end:',tag)
    def handle_data(self,data):
        pass
        # print('data:',data)

content="""

              
<style>/* override theme */
table img {
  max-width: 100%;
}

/* override var element to differentiate color from comment */
var, var code, var span, .prettyprint var span {
  color: #039be5;
}

/* .devsite-terminal virtualenv prompt */
.tfo-terminal-venv::before {
  content: "(venv) $ " !important;
}

/* .devsite-terminal root prompt */
.tfo-terminal-root::before {
  content: "# " !important;
}

/* .devsite-terminal Windows prompt */
.tfo-terminal-windows::before {
  content: "C:\\> " !important;
}

/* .devsite-terminal Windows prompt w/ virtualenv */
.tfo-terminal-windows-venv::before {
  content: "(venv) C:\\> " !important;
}

devsite-code .tfo-notebook-code-cell-output {
  max-height: 300px;
  overflow: auto;
  background: rgba(255, 247, 237, 1);  /* orange bg to distinguish from input code cells */
}

devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button {
  background: rgba(255, 247, 237, .7);  /* orange bg to distinguish from input code cells */
}

devsite-code[dark-code] .tfo-notebook-code-cell-output {
  background: rgba(64, 78, 103, 1);  /* medium slate */
}

devsite-code[dark-code] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button {
  background: rgba(64, 78, 103, .7);  /* medium slate */
}

/* override default table styles for notebook buttons */
.devsite-table-wrapper .tfo-notebook-buttons {
  display: inline-block;
  margin-left: 3px;
  width: auto;
}

.tfo-notebook-buttons td {
  padding-left: 0;
  padding-right: 20px;
}

.tfo-notebook-buttons a,
.tfo-notebook-buttons :link,
.tfo-notebook-buttons :visited {
  border-radius: 8px;
  box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15);
  color: #202124;
  padding: 12px 24px;
  transition: box-shadow 0.2s;
}

.tfo-notebook-buttons a:hover,
.tfo-notebook-buttons a:focus {
  box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15);
}

.tfo-notebook-buttons tr {
  background: 0;
  border: 0;
}

/* on rendered notebook page,
   remove link to webpage since we're already here */
.tfo-notebook-buttons:not(.tfo-api) td:first-child {
  display: none;
}

.tfo-notebook-buttons td > a {
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.tfo-notebook-buttons td > a > img {
  margin-right: 8px;
}

/* landing pages */

.tfo-landing-row-item-inset-white {
  background-color: #fff;
  padding: 32px;
}

.tfo-landing-row-item-inset-white ol,
.tfo-landing-row-item-inset-white ul {
  padding-left: 20px;
}

/* colab callout button */
.colab-callout-row devsite-code {
  border-radius: 8px 8px 0 0;
  box-shadow: none;
}

.colab-callout-footer {
  background: #e3e4e7;
  border-radius: 0 0 8px 8px;
  color: #37474f;
  padding: 20px;
}

.colab-callout-row devsite-code[dark-code] + .colab-callout-footer {
  background: #3f4f66;
}


.colab-callout-footer > .button {
  margin-top: 4px;
  color: #ff5c00;
}

.colab-callout-footer > a > span {
  padding-top: 10px;
  vertical-align: middle;
  color: #37474f;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 14px;
}

.colab-callout-row devsite-code[dark-code] + .colab-callout-footer > a > span {
  color: #fff;
}

a.colab-button {
  background: rgba(255, 255, 255, .75);
  border: solid 1px rgba(0, 0, 0, .08);
  border-bottom-color: rgba(0, 0, 0, .15);
  border-radius: 4px;
  color: #aaa;
  display: inline-block;
  font-size: 11px !important;
  font-weight: 300;
  line-height: 16px;
  padding: 4px 8px;
  text-decoration: none;
  text-transform: uppercase;
}

a.colab-button:hover {
  background: white;
  border-color: rgba(0, 0, 0, .2);
  color: #666;
}

a.colab-button span {
  background: url(/images/colab_logo_button.svg) no-repeat 1px 1px / 20px;
  border-radius: 4px;
  display: inline-block;
  padding-left: 24px;
  text-decoration: none;
}

@media screen and (max-width: 600px) {
  .tfo-notebook-buttons td {
    display: block;
  }
}

/* guide and tutorials landing page cards and sections */

.tfo-landing-page-card {
  padding: 16px;
  box-shadow: 0 0 36px rgba(0,0,0,0.1);
  border-radius: 10px;
}

/* Page section headings */
.tfo-landing-page-heading h2, h2.tfo-landing-page-heading {
  font-family: "Google Sans", sans-serif;
  color: #425066;
  font-size: 30px;
  font-weight: 700;
  line-height: 40px;
}

/* Item title headings */
.tfo-landing-page-heading h3, h3.tfo-landing-page-heading,
.tfo-landing-page-card h3, h3.tfo-landing-page-card {
  font-family: "Google Sans", sans-serif;
  color: #425066;
  font-size: 20px;
  font-weight: 500;
  line-height: 26px;
}

/* List of tutorials notebooks for subsites */
.tfo-landing-page-resources-ul {
  padding-left: 15px
}

.tfo-landing-page-resources-ul > li {
  margin: 6px 0;
}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

<div itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.argsort">
<meta itemprop="path" content="Stable">
</div>



<!-- Insert buttons -->

<div class="devsite-table-wrapper"><table class="tfo-notebook-buttons tfo-api" align="left">

<tbody><tr><td>
  <a target="_blank" href="/versions/r1.15/api_docs/python/tf/argsort">
  <img src="https://tensorflow.google.cn/images/tf_logo_32px.png">
  TensorFlow 1 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.0/tensorflow/python/ops/sort_ops.py#L69-L109">
    <img src="https://tensorflow.google.cn/images/GitHub-Mark-32px.png">
    View source on GitHub
  </a>
</td></tr></tbody></table></div>

<!-- Start diff -->

<p>Returns the indices of a tensor that give its sorted order along an axis.</p>

<devsite-heading text="Aliases:" for="aliases" level="h3" link="" toc=""><h3 id="aliases" is-upgraded="">Aliases:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h3></devsite-heading>

<ul>
<li><a href="/api_docs/python/tf/argsort"><code translate="no" dir="ltr">tf.compat.v1.argsort</code></a></li>
<li><a href="/api_docs/python/tf/argsort"><code translate="no" dir="ltr">tf.compat.v2.argsort</code></a></li>
</ul>
<devsite-code><pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="pln">tf</span><span class="pun">.</span><span class="pln">argsort</span><span class="pun">(</span><span class="pln"><br>&nbsp; &nbsp; values</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; axis</span><span class="pun">=-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; direction</span><span class="pun">=</span><span class="str">'ASCENDING'</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; stable</span><span class="pun">=</span><span class="kwd">False</span><span class="pun">,</span><span class="pln"><br>&nbsp; &nbsp; name</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"><br></span><span class="pun">)</span><span class="pln"><br></span></code></pre><div class="devsite-code-buttons-container"><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code>
<!-- Placeholder for "Used in" -->

<p>For a 1D tensor, <code translate="no" dir="ltr">tf.gather(values, tf.argsort(values))</code> is equivalent to
<a href="https://tensorflow.google.cn/api_docs/python/tf/sort"><code translate="no" dir="ltr">tf.sort(values)</code></a>. For higher dimensions, the output has the same shape as
<code translate="no" dir="ltr">values</code>, but along the given axis, values represent the index of the sorted
element in that slice of the tensor at the given position.</p>

<devsite-heading text="Usage:" for="usage" level="h4" link=""><h4 id="usage" is-upgraded="">Usage:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4></devsite-heading>
<devsite-code><pre class="lang-python" translate="no" dir="ltr" is-upgraded=""><code dir="ltr"><span class="kwd">import</span><span class="pln"> tensorflow </span><span class="kwd">as</span><span class="pln"> tf<br>a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">26.9</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2.8</span><span class="pun">,</span><span class="pln"> </span><span class="lit">166.32</span><span class="pun">,</span><span class="pln"> </span><span class="lit">62.3</span><span class="pun">]</span><span class="pln"><br>b </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">argsort</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln">axis</span><span class="pun">=-</span><span class="lit">1</span><span class="pun">,</span><span class="pln">direction</span><span class="pun">=</span><span class="str">'ASCENDING'</span><span class="pun">,</span><span class="pln">stable</span><span class="pun">=</span><span class="kwd">False</span><span class="pun">,</span><span class="pln">name</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">)</span><span class="pln"><br>c </span><span class="pun">=</span><span class="pln"> tf</span><span class="pun">.</span><span class="pln">keras</span><span class="pun">.</span><span class="pln">backend</span><span class="pun">.</span><span class="kwd">eval</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"><br></span><span class="com"># Here, c = [0 3 1 2 5 4]</span><span class="pln"><br></span></code></pre><div class="devsite-code-buttons-container"><button class="gc-analytics-event material-icons devsite-icon-code-dark devsite-toggle-dark" data-category="Site-Wide Custom Events" data-label="Dark Code Toggle" track-type="exampleCode" track-name="darkCodeToggle" data-title="Dark code theme"></button><button class="gc-analytics-event material-icons devsite-icon-code-light devsite-toggle-light" data-category="Site-Wide Custom Events" data-label="Light Code Toggle" track-type="exampleCode" track-name="lightCodeToggle" data-title="Light code theme"></button><button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code>
<devsite-heading text="Args:" for="args" level="h4" link=""><h4 id="args" is-upgraded="">Args:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4></devsite-heading>

<ul>
<li><b><code translate="no" dir="ltr">values</code></b>: 1-D or higher numeric <code translate="no" dir="ltr">Tensor</code>.</li>
<li><b><code translate="no" dir="ltr">axis</code></b>: The axis along which to sort. The default is -1, which sorts the last
axis.</li>
<li><b><code translate="no" dir="ltr">direction</code></b>: The direction in which to sort the values (<code translate="no" dir="ltr">'ASCENDING'</code> or
<code translate="no" dir="ltr">'DESCENDING'</code>).</li>
<li><b><code translate="no" dir="ltr">stable</code></b>: If True, equal elements in the original tensor will not be
re-ordered in the returned order. Unstable sort is not yet implemented,
but will eventually be the default for performance reasons. If you require
a stable order, pass <code translate="no" dir="ltr">stable=True</code> for forwards compatibility.</li>
<li><b><code translate="no" dir="ltr">name</code></b>: Optional name for the operation.</li>
</ul>

<devsite-heading text="Returns:" for="returns" level="h4" link=""><h4 id="returns" is-upgraded="">Returns:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4></devsite-heading>

<p>An int32 <code translate="no" dir="ltr">Tensor</code> with the same shape as <code translate="no" dir="ltr">values</code>. The indices that would
    sort each slice of the given <code translate="no" dir="ltr">values</code> along the given <code translate="no" dir="ltr">axis</code>.</p>

<devsite-heading text="Raises:" for="raises" level="h4" link=""><h4 id="raises" is-upgraded="">Raises:<button role="button" class="devsite-heading-link button-flat material-icons" data-title="Copy link to this section"></button></h4></devsite-heading>

<ul><li><b><code translate="no" dir="ltr">ValueError</code></b>: If axis is not a constant scalar, or the direction is invalid.</li></ul>'
"""
h=HTML()
h.feed(content)

print(dir(h))
# 第一步，解析img 最小标签
# 解析 button标签
# 解析span 标签
# 解析b标签

import re 

a="""
<button class="gc-analytics-event material-icons devsite-icon-copy" data-category="Site-Wide Custom Events" data-label="Click To Copy" track-type="exampleCode" track-name="clickToCopy" data-title="Copy"></button></div></devsite-code><devsite-heading text="Args:" for="args" level="h4" link=""><h4 id="args" is-upgraded="">Args:</h4></devsite-heading><ul><li><b><code translate="no" dir="ltr">input</code></b>: A <code translate="no" dir="ltr">Tensor</code> of type <code translate="no" dir="ltr">string</code>. Tensor of strings</li><li><b><code translate="no" dir="ltr">pos</code></b>: A <code translate="no" dir="ltr">Tensor</code>. Must be one of the following types: <code translate="no" dir="l
tr">int32</code>, <code translate="no" dir="ltr">int64</code>.Scalar defining the position of first character in each substring</li><li><b><code translate="no" dir="ltr">len</code></b>: A <code translate="no" dir="ltr">Tensor</code>. Must have the same type as <code translate="no" dir="ltr">pos</code>.Scalar defining the number of characters to include in each substring</li><li><b><code translate="no" dir="ltr">unit</code></b>: An optional <code translate="no" dir="ltr">string</code> from: <code translate="no" dir="ltr">"BYTE", "UTF8_CHAR"</code>. Defaults to <code translate="no" dir="ltr">"BYTE"</code>.The unit that is used to create the substring.  One of: <code translate="no" dir="ltr">"BYTE"</code> (fordefining position and length by bytes) or <code translate="no" dir="ltr">"UTF8_CHAR"</code> (for the UTF-8encoded Unicodecode points).  The default is <code translate="no" dir="ltr">"BYTE"</code>. Results are undefined if<code translate="no" dir="ltr">unit=UTF8_CHAR</code> and the <code translate="no" dir="ltr">input</code> strings do not contain structurally validUTF-8.</li><li><b><code translate="no" dir="ltr">name</code></b>: A name for the operation (optional).</li></ul><devsite-heading text="Returns:" for="returns" level="h4" link=""><h4 id="returns" is-upgraded="">Returns:</h4></devsite-heading><p>A <code translate="no" dir="ltr">Tensor</code>
"""


# j_count= a.count('<button')

# for item in range(j_count):
#   a=re.sub(r'<button(.*?)>|</button>','',a)

# print(a)

b=re.match(r'code',a)
# b=re.search(r'</(.*?)>',a)

print(b)
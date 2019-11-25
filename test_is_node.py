import re

nodes = [
    'aaa',
    'b dad',
    'img',
    '<img src="http://xx"',
    '<img src="http://xx">',
    '<div>sdsad</div>',
    '<div-s>sdsad</div-s>',
    '<br>',
    '<br />',
    '<>',
    '<1>'
]

HTML_TAGS = [
    '<a',
    '<b',
    '<button',
    '<div',
    '<h1',
    '<h2',
    '<h3',
    '<h4',
    '<h5',
    '<h6',
    '<img',
    '<pre',
    '<span',
]

for node in nodes:
    if re.match(r'^(<img)|(<br)+(.*?)>$',node):
        print('===> ', node)
    else:
        print('---> ', node)

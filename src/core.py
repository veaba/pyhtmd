
# TODO 1、校验是合法的HTML字符串
# TODO 2、将html string 分割为数组才能使用本文件
# todo：逐行将HTML转为markdown字符串输出
# html to markdown

import re


class HTMK:
	def __init__(self, html=""):
		self.html = html
		# 错误处理
		if not isinstance(self.html, str):
			raise RuntimeError('The params is no str type')

	# 判断是否li开头的标签
	@staticmethod
	def __is_li(self):
		if re.match(r'^.*<li>', self.html):
			return True
		else:
			return False
	# 判断是否是code标签
	@staticmethod
	def __is_code(self):
		if re.match(r'^.*<code>', self.html):
			return True
		else:
			return False
	# 判断h1-h6
	@staticmethod
	def __is_head(self):
		if re.match(r'^.*\<([h1|h2|h3|h4|h5|h6])', self.html):
			return True
		else:
			return False
	# 判断是pre code 代码的标签
	@staticmethod
	def __is_pre(self):
		if re.match(r'^.*\<pre', self.html):
			return True
		else:
			return False
	# 判断是content，不存在外边框了
	@staticmethod
	def __is_content(self):
		if self.__get_tag_text(self) == self.html:
			return True
		else:
			return False

	# 判断如果不是被包围的标签
	@staticmethod
	def __is_no_wrap(self):
		if re.match(r'^.*<(.*?)>.*$',self.html):
			return False
		else:
			return True
	# todo 判断所包围的标签还含有子标签,
	# 存在 True，不存在False
	@staticmethod
	def __is_has_child(self,html=""):
		first_remove= self.__remove_parent_wrap(self,html=html)
		second_remove= self.__remove_parent_wrap(self,html=first_remove)
		if first_remove==second_remove:
			return False
		else:
			return True
	 # ***************************动作部分************************ #
	# 获取href地址url
	def __get_href(self,element=""):
		the_href_element= re.search(r'(href=")(.+?)(")',element)
		the_href= re.sub(r'(href=")(.+?)(")','\\2',the_href_element.group()) # 获得a标签的地址
		return the_href
	
	# 移除无关标签,净化标签
	# 比如：span
	# <span>xx</span>  => xxx
	@staticmethod
	def __clean_up_tag(self,element):
		return re.sub(r'(<span>)(.*?)(<\/span>)','\\2',element.strip())
	# 剥离外边父级标签,等同于获取内容  
	@staticmethod 
	def __remove_parent_wrap(self,html=""):
		left= re.sub(r'^<(.*?)(>)','',html)
		return re.sub(r'<\/*\/([^\/]+[^\.])$','',left)

	# 移除父级标签直接获取内容
	# <h1>xxx</h1> => xxx
	@staticmethod
	def __get_tag_text(self,html=""):
		text=''
		if not self.__is_has_child(self):
			print('进入：__get_tag_text，不存在子元素')
			text= self.__remove_parent_wrap(self,html=html)
		else:
			print('进入：__get_tag_text，存在子元素')
			return self.__get_tag_text(self,html=self.__remove_parent_wrap(self,html=html))
		return text
   
	# 获取是标签名
	@staticmethod
	def __get_tag_name(self):
		return re.sub(r'<(.*?) .*$','\\1',self.html)

	# 判断是哪种标签，todo，此时先判断code
	@staticmethod
	def __check_what_element(self,element=""):
		clear_attrs_element=re.sub(r' (.*?)>','>',element)
		tag_name=re.sub(r'<(.*?)>.*$','\\1',clear_attrs_element)
		# tag_name=re.sub(r'<(.*?) .*$','\\1',element)
		if tag_name=='code':
			print('what：code')
			return self.__parser_code(self,element=element)
		elif tag_name=='a':
			print('what：a')
			return self.__parser_a(self,element=element)
		# todo ...
		elif tag_name=='strong':
			print('what：strong')
			return self.__parser_strong(self,element=element)
		elif tag_name=='b':
			return self.__parser_b(self,element=element)
		print('标签名字:',tag_name)
		return element

	# ***************************解析部分************************ #
	# 将获取被包围的node节点解析成为数组
	# Given a tensor <code translate="no" dir="ltr">t<\/code>, this operation returns a tensor of the same type  andshape as <code translate="no" dir="ltr">t<\/code> with its values clipped to <code translate="no"
    # dir="ltr">clip_value_min<\/code> and <code translate="no" dir="ltr">clip_value_max</code>.Any values less than
    # <code translate="no" dir="ltr">clip_value_min</code> are set to <code translate="no" 
    # dir="ltr">clip_value_min</code>. Any valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are
    # set to <code translate="no" dir="ltr">clip_value_max</code>. 
	# ===> re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', h)
	"""
	<code translate="no" dir="ltr">t</code>
	<code translate="no" dir="ltr">t</code>
	<code translate="no" dir="ltr">clip_value_min</code>
	<code translate="no" dir="ltr">clip_value_max</code>
	<code translate="no" dir="ltr">clip_value_min</code>
	<code translate="no" dir="ltr">clip_value_min</code>
	<code translate="no" dir="ltr">clip_value_max</code>
	<code translate="no" dir="ltr">clip_value_max</code>
	"""
	@staticmethod
	def __parser_p(self,html=""):
		new_html=html 
		html_blocks= re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', html)
		for item in html_blocks:
			block_string=item.group() or ""
			print('block_string:',block_string)
			new_html=new_html.replace(block_string,self.__check_what_element(self,element=block_string))
			print('what_element:',self.__check_what_element(self,element=block_string))
			print('new_html:',new_html)
		return new_html

	# h1-h6 todo 可能还有其他子标签
	@staticmethod
	def __parser_head(self):
		text=''
		tag_name=self.__get_tag_name(self)
		if self.__is_has_child(self):
			text ='ERRPR TODO ::含有child'
		else:
			if tag_name=='h1':
				text='# '+ self.__get_tag_text(self,html=self.html) +'\n'
			elif tag_name=='h2':
				text='## '+ self.__get_tag_text(self,html=self.html) +'\n'
			elif tag_name=='h3':
				text='### '+ self.__get_tag_text(self,html=self.html) +'\n'
			elif tag_name=='h4':
				text='#### '+ self.__get_tag_text(self,html=self.html) +'\n'
			elif tag_name=='h5':
				text='##### '+ self.__get_tag_text(self,html=self.html) +'\n'
			elif tag_name=='h6':
				text='###### '+ self.__get_tag_text(self,html=self.html) +'\n'
		return text

	# 解析 pre code的标签
	@staticmethod
	def __parser_pre(self,html=""):
		content = self.__get_tag_text(self,html=html).replace('    ','\n')
		content_remove_code= self.__get_tag_text(self,html=content)
		return '```\n'+content_remove_code+'\n```'

	# 解析 li 标签
	# todo 可能还有其他子标签
	@staticmethod
	def __parser_li(self,html):
		temp_array=re.finditer(r'\<li\>(.*?)\<\/li\>',html)
		text=''
		for ele in temp_array:
			# 判断不存在包围子元素
			if not self.__is_has_child(self,html=ele.group()):
				text=self.__get_tag_text(self,html=html)
			# 如果存在子元素
			else:
				remove_li_tag=self.__remove_parent_wrap(self,html=ele.group())
				text+='- '+self.__check_what_element(self,element=remove_li_tag)+'\n'
		return text

	# 将code 解析为``,
	# <code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code>
	# => tf.compat.v2.clip_by_value
	@staticmethod
	def __parser_code(self,element=""):
		left=re.sub(r'<code(.*?)>','`',element.strip())
		return re.sub(r'</code>','`',left)

	# 将a标签 <a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a> 
	# 转为 [xx](xxx)
	@staticmethod
	def __parser_a(self,element=""):
		# todo 先检查a 标签里面包含其他东西
		the_href=self.__get_href(element=element)
		left =re.sub(r'<a(.*?)>','',element)
		a_content=re.sub(r'</a>','',left)
		return '['+self.__check_what_element(self,element=a_content)+']('+the_href+')'
	
	# 解析strong
	@staticmethod
	def __parser_strong(self,element=""):
		print('解析：__parser_strong')
		left =re.sub(r'<strong(.*?)>','',element)
		strong_content=re.sub(r'</strong>','',left)
		return '**'+self.__check_what_element(self,element=strong_content)+'**'
	
	# 解析 b
	@staticmethod
	def __parser_b(self,element=""):
		print('解析：__parser_a')
		left =re.sub(r'<b(.*?)>','',element)
		b_content=re.sub(r'</b>','',left)
		return '**'+self.__check_what_element(self,element=b_content)+'**'
	# todo 解析出来markdown
	def markdown(self):
		text=self.html
		if self.__is_li(self):
			print('__is_li')
			text= self.__parser_li(self,html=self.html)
		elif self.__is_head(self):
			print('__is_head')
			text=self.__parser_head(self)
		elif self.__is_pre(self):
			print('__is_pre')
			text=self.__parser_pre(self,html=self.html)
		else:
			print('__parser_p')
			# 此时就应该清空span标签
			text=self.__parser_p(self,html=self.__clean_up_tag(self,self.html))
		
		return text

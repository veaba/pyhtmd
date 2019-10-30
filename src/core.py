
# TODO 1、校验是合法的HTML字符串
# TODO 2、将html string 分割为数组才能使用本文件
import re
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
			text= self.__remove_parent_wrap(self,html=html)
		else:
			return self.__get_tag_text(self,html=self.__remove_parent_wrap(self,html=html))
		return text
   
	# 获取是标签名
	@staticmethod
	def __get_tag_name(self):
		return re.sub(r'<(.*?) .*$','\\1',self.html)

	# 判断是哪种标签，todo，此时先判断code
	@staticmethod
	def __check_what_element(self,element=""):
		tag_name=re.sub(r'<(.*?) .*$','\\1',element)
		if tag_name=='code':
			return self.__parser_code(self,element=element)
		elif tag_name=='a':
			return self.__parser_a(self,element=element)
		# todo ...
		return element

	# ***************************解析部分************************ #
	
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
	# todo 解析出来markdown
	def markdown(self):
		text=self.html
		if self.__is_li(self):
			text= self.__parser_li(self,html=self.html)
		if self.__is_head(self):
			text=self.__parser_head(self)
			pass
		if self.__is_pre(self):
			text=self.__parser_pre(self,html=self.html)
		
		return text

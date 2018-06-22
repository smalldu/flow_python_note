# encoding=utf-8
from collections import abc
from collections import defaultdict
from collections import UserDict
import sys 
import re
# 字典和集合  


my_dict = {}
print(isinstance(my_dict,abc.Mapping)) # True

# 标准库中所有的映射类型都是通过dict来实现的
# 如果一个对象是可散列的，那么在这个对象的生命周期中，他的散列值是不变的。且这个对象需要实现__hash__()方法,还需要有__qe__() 方法

tt = (1,2,(30,40))
print(hash(tt)) 

tf = (1,2,frozenset([30,40]))
print(hash(tf))

a = dict(one=1,two=2,three=3)
print(a) # {'two': 2, 'one': 1, 'three': 3}
b = {'two': 2, 'one': 1, 'three': 3}
c = dict(zip(['one','two','three'],[1,2,3]))
print(c)  # {'two': 2, 'three': 3, 'one': 1}
d = dict([('one',1),('two',2),('three',3)])
print(d)
e = dict({'two': 2, 'one': 1, 'three': 3})

print(a == b == c == d == e) # True

f = {k.upper(): v for k,v in a.items()} 
# {'THREE': 3, 'ONE': 1, 'TWO': 2}
print(f)
f.clear()
print(f)



WORD_RE = re.compile(r'\w+')

index = {}

index.setdefault('U',[]).append(1)
print(index)

# 处理找不到key时给默认值  defaultdict




class StrKeyDict(UserDict):
	def __missing__(self,key):
		if isinstance(key,str):
			raise KeyError(key)
		return self[str(key)]
	def __contains__(self,key):
		return str(key) in self.data
	def __setitem__(self,key,item):
		self.data[str[key]] = item






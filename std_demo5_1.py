# encoding=utf-8

from functools import reduce
from operator import add
import random
 
# 阶乘
def factorial(n):
	'''returns n!'''
	return 1 if n < 2 else n * factorial(n-1)

print(factorial(42)) 
print(factorial.__doc__)  # returns n!
print(type(factorial)) # <class 'function'>

fact = factorial

print(fact(5)) 


print(reduce(add,range(100))) 
print(sum(range(100)))

# 如果想判断对象能否调用 可以使用callable()



class BingoCage:
	def __init__(self,items):
		self._items = list(items)
		random.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		return self.pick()



bingo = BingoCage(range(3))
print(bingo.pick())


# print(dir(factorial))bingo()

class C: pass

obj = C()
def func():
	pass

print(sorted(set(dir(func))-set(dir(obj))))

def clip(text,max_len=80):
	end = None
	if len(text) > max_len:
		space_before = text.rfind(' ',0,max_len)
		if space_before >= 0:
			end = space_before
		else: 
			space_after = text.rfind(' ',max_len)
			if space_after > 0:
				end = space_after
	if end is None:
		end = len(text)
	return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames) # ('text', 'max_len', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount) # 2

from inspect import signature


sig = signature(clip)
print(sig)
for name,param in sig.parameters.items():
	print(param.kind , ":" , name , "=" , param.default)



def deco(func):
	print("This is a deco method")
	return func


@deco
def be_deco():
	print("This is a Be decoed method")


be_deco()



















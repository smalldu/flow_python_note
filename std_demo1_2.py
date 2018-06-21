# encoding=utf-8

from math import hypot


# 向量 特殊方法的实现: __repr__ , __abs__ , __add__ , __mul__ 


class Vector:

	def __init__(self,x = 0 ,y = 0):
		self.x = x 
		self.y = y

	def __repr__(self):
		return 'Vector({},{})'.format(self.x,self.y)
	
	# abs()方法
	def __abs__(self):
		return hypot(self.x,self.y)

	def __bool__(self):
		return bool(abs(self))

	# + 运算符 
	def __add__(self,other):
		x = self.x + other.x 
		y = self.y + other.y
		return Vector(x,y)

	# * 运算符
	def __mul__(self,scalar):
		return Vector(self.x * scalar , self.y * scalar)


vec = Vector(9,8)
print(vec)

vec2 = Vector(8,8)
print(vec + vec2)

print(vec * 3)
print(bool(vec))






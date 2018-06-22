# encoding=utf-8

import array
import numpy 
from collections import deque

# numbers = array.array('h',[-2,-1,0,1,2])
# memv = memoryview(numbers)
# print(len(memv))
# print(memv)
# memv_oct = memv.cast('B')
# memv_oct.tolist()
# print(memv_oct)
# memv_oct[5] = 4
# print(numbers)

a = numpy.arange(12)
print(a)
print(type(a)) # <class 'numpy.ndarray'> 
print(a.shape) # (12,)
a.shape = 3,4  # 转换为3行4列
print(a) 

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[2]) # [ 8  9 10 11]
print(a[2,1]) # 9
print(a[:,1]) # 第二列数据 [1 5 9]
print(a.transpose()) # 行和列交换 得到新的数组
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

dq = deque(range(10),maxlen=10)

print(dq)

dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11,12,13])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)







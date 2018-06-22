# encoding=utf-8

from collections import namedtuple
import bisect 
import sys
import array

# 切片操作

l = [10,20,30,40,50,60]
print(l[:2])

print(l[2:])

# 对对象进行切片

# 在1 和 4 之间以2为间隔取值 间隔可以为负数 表示反向取值
print(l[1:4:2]) 

# 给切片赋值 

l = list(range(10))
print(l)
l[2:5] = [20,30]
print(l)

l = [1,2,3]*5
print(l) #  [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(5*'abcd') # abcdabcdabcdabcdabcd



board = [ ['_'] * 3 for i in range(3) ]
print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[1][2] = ['X']

# += 背后的方法是 __iadd__ 

l.sort()
print(l)


# 用 bisect 来管理已排序的序列  bisect 和 insort 都是利用二分查找进行查询和插入元素

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,19,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'


def demo(bisect_fn):
	for needle in reversed(HAYSTACK):
		position = bisect_fn(HAYSTACK,needle)
		offset = position * '  |'
		print(ROW_FMT.format(needle,position,offset))





if __name__ == '__main__':
	if sys.argv[-1] == 'left':
		bisect_fn = bisect.bisect_left
	else :
		bisect_fn = bisect.bisect
	print('DEMO:',bisect_fn.__name__)
	print('haystack ->',' '.join('%2d' % n for n in HAYSTACK))
	demo(bisect_fn)



















































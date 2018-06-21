# encoding=utf-8

from collections import namedtuple
import array

# 序列构成的数组 


symbols = '$%^'

# codes = []
# for symbol in symbols:
# 	codes.append(ord(symbol))

# print(codes)

# 列表推导的方式 原则： 只用列表推导来创建新的列表， 并尽量保持简洁
codes = [ ord(symbol) for symbol in symbols ]
print(codes)


beyoud_ascii = [ ord(s) for s in symbols if ord(s) > 36 ]
print(beyoud_ascii)

# 两个结果一样的 但是上面的可读性高很多
beyoud_ascii = list( filter( lambda c: c > 36 , map(ord , symbols) ))
print(beyoud_ascii)


colors = ['black','white']
sizes = ['S','M','L']

# 两个列表的笛卡尔积  2*3  个元素
tshirts = [ (color,size) for color in colors for size in sizes]

print(tshirts)


tp = tuple(ord(s) for s in symbols)
print(tp)


arr = array.array('I' , ( ord(s) for s in symbols ))
print(arr)

# tuple 元祖

lax_coordinates = (33.9425 , 118.408056)
city,area,pop,chg,year = ('上海','长宁' , 1002 , 223 , 2018)

print("%f/%f" % lax_coordinates)


a,b,*rest = range(5)

print(rest)


# 具名元祖  collections.namedtuple 是一个工厂函数 。 


City = namedtuple('City','name contry population coordinates')
tokyo = City('Tokyo','JP' , 36.9 , (35.689,137.3432))
print(tokyo)

# 具名专有属性

print(City._fields) # ('name', 'contry', 'population', 'coordinates') 
LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','In',31,LatLong(28.3,77.2))
delhi = City._make(delhi_data)

print(delhi._asdict())
















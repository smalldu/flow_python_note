# encoding=utf-8

import collections 
from random import choice

# 构建一个简单的类来表示纸牌 namedtuple 用来构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
	ranks = [ str(n) for n in range(2,11)] + list('JQKA') 
	suits = 'spades diamonds clubs hearts︎'.split()
	
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits 
									   for rank in self.ranks ]
	def __len__(self):
		return len(self._cards)

	def __getitem__(self,position):
		return self._cards[position]


# beer_card = Card('7','diamonds')
# print(beer_card)

# 实现了 __len__ 方法就可以使用len()
# 实现了 __getitem__ 方法就可以使用 items[position] 

deck = FrenchDeck()
print(len(deck))
print(deck[-1])

# for i in range(20):
# 	print(choice(deck))

# 抽出索引为12的那一张 然后每隔13张拿出一张
print(deck[12::13])

# 可迭代
# for card in deck:
# 	print(card)

# 反向迭代
# for card in reversed(deck):
# 	print(card)


res = Card(rank='7', suit='♠') in deck
print(res) # True



# 排序规则
suit_values = dict(spades = 3,hearts︎ = 2,diamonds = 1,clubs = 0)

def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck,key = spades_high):
	print(card)





















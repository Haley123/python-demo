"""
列表生成式 List Comprehensions
即列表生成列表
"""

a = list(range(1, 20))
print(a)

b = [i*i for i in range(1, 20)]
print(b)

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str) ==True]
print(L2)

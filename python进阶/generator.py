'''
在Python中，这种一边循环一边计算的机制，称为生成器：generator
是列表生成式的补充版
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
简单地讲，yield 的作用就是把一个函数变成一个 generator.
带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
备注：yield只能和函数一起用，否则会报错
'''

b = (i*i for i in range(1, 2))
print(b)   # 直接打印是会报错的,没有更多的元素时，抛出StopIteration的错误。
for i in b:
    print(i)




'''
map()函数接收两个参数，一个是函数，一个是Iterable（迭代），map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回


'''
def f(x):
    return x*x
if __name__ == '__main__':
    r = map(f, [1, 2, 3, 45, 6, 7])
    print(list(r))
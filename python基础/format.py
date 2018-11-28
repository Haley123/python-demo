#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# format ：格式化
# 格式化的目的：即str输入多个变量
# 格式化有两种方式，一个通过 % 运算符 ，一个通过format()方法

# 第一种
# 利用占位符 ，整数 %d, 浮点数%f，字符段%s
print('我是%d岁的%s, 我今天有%s块零花钱'%(21, 'pasca', 1.5 ))

# 第二种
# 利用format()方法
print('我是{0}岁的{1}, 我今天有{2}块零花钱'.format(21, 'pasca', 1.5))


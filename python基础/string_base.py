#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python 的内置字符串方法大全（收藏专用）
概览
字符串大小写转换
str.capitalize()  # 将首字母转换成大写，需要注意的是如果首字没有大写形式，则返回原字符串。
str.lower()       # 将字符串转换成小写，其仅对 ASCII 编码的字母有效。
str.casefold()    # 将字符串转换成小写，Unicode 编码中凡是有对应的小写形式的，都会转换。
str.swapcase()    # 对字符串字母的大小写进行反转。
str.title()       # 将字符串中每个“单词”首字母大写。其判断“单词”的依据则是基于空格和标点
str.upper()       # 将字符串所有字母变为大写，会自动忽略不可转成大写的字符

字符串格式输出
str.center(width[, fillchar])              # 将字符串按照给定的宽度居中显示，可以给定特定的字符填充多余的长度，如果指定的长度小于字符串长度，则返回原字符串。
str.ljust(width[, fillchar]); str.rjust(width[, fillchar])   # 返回指定长度的字符串，字符串内容居左（右）如果长度小于字符串长度，则返回原始字符串，默认填充为 ASCII 空格，可指定填充的字符串。
str.zfill(width)                   # 用 '0' 填充字符串，并返回指定宽度的字符串。
str.expandtabs(tabsize=8)          # 用指定的空格替代横向制表符，使得相邻字符串之间的间距保持在指定的空格数以内。
str.format(^args, ^^kwargs)        # 格式化，已讲过
str.format_map(mapping)            # 类似 str.format(*args, **kwargs) ，不同的是 mapping 是一个字典对象

字符串搜索定位与替换
str.count(sub[, start[, end]])      # 计算字符串的个数，start，开始位置。end结束位置
str.find(sub[, start[, end]]); str.rfind(sub[, start[, end]])   # 搜索字符串
str.index(sub[, start[, end]]); str.rindex(sub[, start[, end]]) # 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
str.replace(old, new[, count])      # 替换
str.lstrip([chars]); str.rstrip([chars]); str.strip([chars])  # 用于截掉字符串左边的空格或指定字符
static str.maketrans(x[, y[, z]]); str.translate(table)       # maktrans 是一个静态方法，用于生成一个对照表，以供 translate 使用。

字符串的联合与分割
str.join(iterable)    # 用指定的字符串，连接元素为字符串的可迭代对象。
str.partition(sep); str.rpartition(sep)    # 根据指定的分隔符将字符串进行分割，如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
str.split(sep=None, maxsplit=-1); str.rsplit(sep=None, maxsplit=-1) # 过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
str.splitlines([keepends])  # 照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表

字符串条件判断
str.endswith(suffix[, start[, end]]); str.startswith(prefix[, start[, end]])
str.isalnum()
str.isalpha()
str.isdecimal(); str.isdigit(); str.isnumeric()
str.isidentifier()
str.islower()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()

字符串编码
str.encode(encoding="utf-8", errors="strict")


字符串切割大全
+ 字符串连接操作
* 字符串复制操作
[] 字符串索引操作，通过索引访问指定位置的字符，索引从0开始
[::] 字符串取片操作
完整格式：[开始索引:结束索引:间隔值]
[:结束索引]  从开头截取到结束索引之前
[开始索引:]  从开始索引截取到字符串的最后
[开始索引：结束索引]  从开始索引截取到结束索引之前
[:]  截取所有字符串
[开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前按照指定的间隔截取字符
r'字符串'   元字符串，所有字符串中的转义字符不会转义，当作普通字符


'''

# 一、字符串大小写转换


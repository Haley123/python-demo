#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Character Encoding 字符串编码
# 美国人有ASCII编码，中国有GB2311编码
# Unicode编码= ASCII + GB2311
# 区别：ASCII编码是1个字节，而Unicode编码通常是2个字节

# Unicode编码  再编码 得到——》UTF-8编码 —————— 英文：1个字节   汉字：3个字节

# python2 = 需要标注Unicode
# python3 = 自带Unicode

# 在python中， 字符串= str->unicode->bytes->decode->str

a = 'abc'
b = b'abc'
c = b.decode('utf-8')
print('我是a，纯正的unicode编码：', a)
print('我是b,bytes编码：', b)
print('我是c，解码后的unicode编码',c )



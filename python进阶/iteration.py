# -*- coding: utf-8 -*-

'''

 iteration ：迭代
迭代是什么？
其实就是将列表&元组&字典遍历的方式叫做遍历
不过这里字典有点特殊，默认迭代的是key值，如果需要迭代value，则是dict.values()
下面一一讲解。

'''

# 1、遍历列表
# 寻找最大值，最小值
a = [1, 2, 3, 14, 6, 17, 9]
min = max = a[0]
for i in a:
    if i > max:
        max = i
    if i < min:
        min = 1
print('最大值：', max)
print('最小值', min)


# 2、遍历字典

a = {
    'name': 'hzb',
    'info':{
        'height': '180',
        'location': '上海'
    }
}
for dict in a:
    print(dict)

for dict in a.values():
    print(dict)


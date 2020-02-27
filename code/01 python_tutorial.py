# -*- coding: utf-8 -*-

#===字符串,string===
print("===1 字符串,string===")
stock_name = '贵州茅台'
print (stock_name, type(stock_name))
stock_code = "600519.XSHG"
print (stock_code, type(stock_code))
# 占位符
stock = "the code is : %s" %(stock_code)
print(stock)
print ("***"*10)

# 数字
print("===2 数字===")
stock_num = 4000 # 整数，有4000只股票在交易
print (stock_num, type(stock_num)) # type()函数的作用是输出变量的类型
stock_price = 198.88  # 浮点数，股票价格是198.88
print(stock_price, type(stock_price))
stock_value = 1.234E10  # 可以使用科学技术发来表示很大的数字，例如股票市值
print(stock_value, type(stock_value))
complex_value=123-111j
print (complex_value.real) # output 实数部分 123.0
print (complex_value.imag)# output虚数部分 -111.0

print ("***"*10)

# 容器
print("===3 容器===")
# list是具有顺序的一组对象，其中的元素不需要是同类型
sample_list = [1, '2', 3, 4.0, 5, 6, 'seven', [8], '九']  # list举例
print ("***"*10)

# =====list常见操作：索引，选取list中的某个元素
print ("输出排在第1个位置的元素：",sample_list[0])  # 输出排在第1个位置的元素。位置的计数是从0开始的。
print ("输出排在第2个位置的元素：",sample_list[1]) # 输出排在第2个位置的元素。位置的计数是从0开始的。
print ("输出最后一个元素的另外一种方式：",sample_list[-1])  # 输出最后一个元素的另外一种方式。
# print (sample_list[-10])  # 超出长度会报错 IndexError: list index out of range
sample_list[3] = 100  # 可以根据索引，直接修改list中对应位置的元素
print ("根据索引，直接修改list中对应位置的元素：",sample_list)
print ("***"*10)

# =====list常见操作：切片，选取list中的一连串元素
sample_list = [1, '2', 3, 4.0, 5, 6, 'seven', [8], '九']  # list举例
print ("从第a个位置开始，一直到第b个位置之前的那些元素:",sample_list[3:8])  # list[a:b]，从第a个位置开始，一直到第b个位置之前的那些元素
print ("从头开始，一直到第b个位置之前的那些元素:",sample_list[:4])  # list[:b]，从头开始，一直到第b个位置之前的那些元素
print("从第a个位置开始，一直到最后一个元素:",sample_list[3:]) # list[a:]，从第a个位置开始，一直到最后一个元素
print ("每c个元素，选取其中的一个:",sample_list[1:7:3])  # list[a:b:c]，每c个元素，选取其中的一个
print ("***"*10)

# =====list常见操作：两个list相加
sample_list1 = [1, '2', 3, 4.0, 5]
sample_list2 = [6, 'seven', [8], '九']
print ("两个list相加:",sample_list1 + sample_list2)  # 两个list相加
print ("***"*10)

# =====list常见操作：判断一个元素是否在list当中
sample_list = [1, '2', 3, 4.0, 5]
print ("判断1元素，是否在list中出现:",1 in sample_list)  # 判断1元素，是否在list中出现
print ("***"*10)


# =====list常见操作：len，max，min
sample_list = [1, 2, 3, 4, 5]
print ("list的长度:",len(sample_list))  # list中元素的个数，或者说是list的长度
print ("这个list中最大的元素:",max(sample_list))  # 这个list中最大的元素，
print ("最小的元素:",min(sample_list)) # 最小的元素
print ("***"*10)


# =====list常见操作：删除其中的一个元素
sample_list = [1, 2, 3, 4, 5]
print(sample_list)
del sample_list[0]  # 删除位置0的那个元素
print ("删除位置0的那个元素:",sample_list)

print ("***"*10)

# =====list常见操作：如何查找一个元素的在list中的位置
sample_list = [3, 5, 1, 2, 4]  # 如何才能知道5这个元素，在list中的位置是什么？
print(sample_list)
print ("5这个元素，在list中的位置是什么:",sample_list.index(5))
print ("***"*10)


# =====list常见操作：append,在后方增加一个元素
sample_list = [1, '2', 3, 4.0, 5]
print (sample_list)
sample_list.append(['seven', [8], '九'])
print ("append,在后方增加一个元素:",sample_list)

print ("***"*10)

# =====list常见操作：两个list合并
sample_list = [1, '2', 3, 4.0, 5]
sample_list.extend([6, 'seven', [8], '九'])
print ("两个list合并:",sample_list)

print ("***"*10)

# =====list常见操作：逆序、排序、
sample_list = [3, 5, 1, 2, 4]
print (sample_list)
sample_list.reverse()
print ("逆序:",sample_list)
sample_list = [3, 5, 1, 2, 4]
sample_list.sort()
print ("排序：",sample_list)


# =====元组
tup = (1, 2, 3, 4, 5)  #创建元组
print(tup)
#查询元组,下标索引从0开始
print("查询出元组第一个元素为：", tup[0])

# 元组合并
tup1 = (111, 2222);
tup2 = ('ab', 'cd')
tup3 = tup1 + tup2
print (tup3)


#=====集合
s1 = set(['A','B','C','D'])
print("集合:",s1)

#增加元素:update
s1.update(['E'])
print("增加元素:update:",s1)

#删除元素:discard
s1.discard('E')
print("删除元素:discard:",s1)

#查询元素
ss = 'B' in s1
print("'B' in s1",ss)


# =====字典dict介绍
# 使用{}大括号就可以新建一个dict。
sample_dict = {}  # 这是一个空dict
print(sample_dict, type(sample_dict))

# 具有一系列成对的对象。一个叫做key，一个叫做value。其中的元素(包括key和value)不需要是同类型
sample_dict = {'600519.XSHG': '贵州茅台',
            '000002.XSHE': '万科A',
            '300001:': '特锐德'}  # 其中'600519.XSHG'、就是key，贵州茅台就是相对应的value。
print (sample_dict)

# 字典是无顺序，key不可重复
# print("dict_var[0]:", sample_dict[0])  # 因为没有顺序，所以dict_var[0]并不能取出第0个位置的元素，此处会报错。


# =====dict常见操作：根据key的值，取相应的value的值
print( "获取'600519.XSHG'这个key对应的value:", sample_dict['600519.XSHG']) # 获取'600519.XSHG'这个key对应的value
print (sample_dict.get('000002.XSHE'))  # 效果同上


# =====dict常见操作：增加、修改一对key：value
sample_dict['000001.XSHG'] = '上证指数'
print(sample_dict)
sample_dict['000001.XSHG'] = '上证综合指数'
print ("进行修改之后：", sample_dict['000001.XSHG'])

# =====dict常见操作：判断一个key是不是在dict里面
print ("判断一个key是不是在dict里面:",'600519.XSHG' in sample_dict)

# =====dict常见操作：输出一个dict中所有的key和value
print ("输出所有的key:", sample_dict.keys())  # 输出所有的key
print ("输出所有的value:", sample_dict.values())  # 输出所有的value


# 条件语句
a = 100
if a >= 50:
    print("Yes")
else:
    print ("No")

x = "中国"
if x == "上海":
    print ("大")
elif x == "中国":
    print ("特别大")
else:
    print("无")
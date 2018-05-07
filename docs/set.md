## Python中集合（set）类型的详细解释及操作



一、集合（set）类型的含义：

Set是一个无序不重复元素集，与列表和元组不同，集合是无序的，无法通过数字进行索引。

注意：下面所举例子在python3.6,IDE为pycharm2016.1中通过。

创建集合：用set（）函数，或直接赋值。

例子：

x=set('Nike MM')

y=set(['w','a','m','a'])

print(x)

print(y)

输出：

{'M', 'N', 'e', 'k', ' ', 'i'}

{'w', 'm', 'a'}

可以看到，在输出中，是用一对｛｝号包住，里面重复的元素被去除。

再看一个例子：

s={'11','22','33'}

print(s)

print(type(s))

s={}

{'33', '11', '22'}

<class 'set'>

<class 'dict'>

在定义不，不能用s={}，这关创建的实际上是一个字典类型。

二、有关集合的操作：

1．增加操作

a=set('python')

a.add('why')

print(a)

b=set('python')

b.update('why')

print(b)

{'n', 'p', 'y', 'h', 'o', 't', 'why'}

{'n', 'p', 'y', 'h', 'o', 'w', 't'}

可能看到：add是单个元素的添加，并没有把元素再分拆为单个字符。Update是批量的增加，增加的元素如果是一个字符串（实际上，在Python中字符串也是一个系列），是作为一个系列增加的。在输出结果中，两个函数都是无序的，并且无重复，也非添加到尾部。

2．删除操作（remove,discard,pop）

例子1：

a=set('abcdefghijk')

a.remove('a')

a.remove('w')

输出 ：

Traceback (most recent call last):

{'h', 'k', 'e', 'd', 'g', 'c', 'f', 'i', 'b', 'j'}

File "D:/python/temp3.py", line 4, in <module>

KeyError: 'w'

例子2：

a.discard('a')

a.discard('w')

{'f', 'h', 'd', 'e', 'b', 'k', 'i', 'j', 'c', 'g'}

例子3：

b=a.pop()

print(b,type(b))

{'k', 'd', 'h', 'c', 'b', 'j', 'g', 'i', 'e', 'f'}

a <class 'str'>

从以上例子可以看到，remove方法删除指定无素，如果要删除的元素的不在集合中，则报错；discard方法删除指定元素，如果要删除物元素不在集合中，则不报错，pop方法删除任意元素，并可将这个元素赋值给一个变量，但集合并没有把这个元素移除。

3.清空（clear）

例子:

a.clear()

set()

4.交集&，并集|，差集-，对称差集^，子集（被包含）<=，父集(包含)>=

a=set(['a','b','c','d','e','f'])

b=set(('d','e','f','g','h','i'))

d=set('def')

print('交集：',a.intersection(b))

print('交集：',a & b)

print('并集：',a.union(b))

print('并集：',a | b)

print('差集:',a.difference(b))

print('差集:',a-b)

\#对称差集:

\#把两个集合中相同的元素去掉，然后

\#两个集合中剩下的元素组成一个新的集合

print('对称差集:',a.symmetric_difference(b) )

print('对称差集:',a ^ b )

print('子集：',a.issubset(d) )

print('子集：',a<=d )

print('父集：',a.issuperset(d) )

print('父集：',a>=d )

交集： {'f', 'e', 'd'}

并集： {'c', 'e', 'd', 'b', 'f', 'a', 'g', 'i', 'h'}

差集: {'a', 'c', 'b'}

对称差集: {'a', 'c', 'g', 'b', 'i', 'h'}

子集： False

父集： True

5．集合的其它一些操作

\#如果a和d没有交集，返回True，有则返回False

print(a.isdisjoint(d) ) 输出：False

print(a<d) 输出：False

print(a>d) 输出：True

print（a!=b） 输出：True

print(a.copy()) 输出：{'f', 'e', 'b', 'a', 'd', 'c'} #复制一个集合

print('a' in a) 输出：True #测试元素是否在集合中

print('a' not in a) 输出：False #测试元素是否不在集合中

print(len(a)) 输出：6 #返回集合的长度

6．集合计算：

（1）

\#从a中减去a和b的交集，即从a集合中删除和b集合中相同的元素

a.difference_update(b) 即等于：a=a-b 或a-=b

print(a) 输出：{'a', 'b', 'c'}

（2）

\#修改a集合，仅仅保持a与b的交集，如果没有交集，则a变为空集合set()

a.intersection_update(b) 即等于：a=a&b 或a&=b

print(a )

输出：{'e', 'd', 'f'}

(3)

\#a集合中增加‘在b集合中除去a和b交集剩下的元素’

a.symmetric_difference_update(b) 即等于：a=a^b 或 a^=b

print(a) 输出：{'i', 'g', 'a', 'c', 'b', 'h'}
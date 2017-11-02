#!/usr/bin/env python3

import math
import random

'''
数学函数
函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)
如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根。
'''

print(max(1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3))

'''
随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
Python包含以下常用随机数函数：
函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''

print(random.random())

'''
三角函数
Python包括以下三角函数：
函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。	
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''

print(math.tan(60))

'''
数学常量
常量	描述
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
'''

"""
Python转义字符
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
转义字符	描述
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出
Python字符串运算符
下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
操作符	描述	实例
+	字符串连接	a + b 输出结果： HelloPython
*	重复输出字符串	a*2 输出结果：HelloHello
[]	通过索引获取字符串中字符	a[1] 输出结果 e
[ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell
in	成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
%	格式字符串	请看下一节内容。
"""

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print('\n')
print(r'\n')
print(R'\n')

"""
Python字符串格式化
Python 支持格式化字符串的输出 。
尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
"""
print("我叫 %s 今年 %d 岁!" % ('小明', 10))

'''
Python 的字符串内建函数
Python 的字符串常用内建函数如下：
序号	方法及描述
1	
capitalize()
将字符串的第一个字符转换为大写
2	
center(width, fillchar)

返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3	
count(str, beg= 0,end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
4	
bytes.decode(encoding="utf-8", errors="strict")

Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5	
encode(encoding='UTF-8',errors='strict')

以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6	
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
7	
expandtabs(tabsize=8)

把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8	
find(str, beg=0 end=len(string))

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9	
index(str, beg=0, end=len(string))

跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10	
isalnum()

如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11	
isalpha()

如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12	
isdigit()

如果字符串只包含数字则返回 True 否则返回 False..
13	
islower()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
14	
isnumeric()

如果字符串中只包含数字字符，则返回 True，否则返回 False
15	
isspace()

如果字符串中只包含空白，则返回 True，否则返回 False.
16	
istitle()

如果字符串是标题化的(见 title())则返回 True，否则返回 False
17	
isupper()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
18	
join(seq)

以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
19	
len(string)

返回字符串长度
20	
ljust(width[, fillchar])

返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
21	
lower()

转换字符串中所有大写字符为小写.
22	
lstrip()

截掉字符串左边的空格或指定字符。
23	
maketrans()

创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24	
max(str)

返回字符串 str 中最大的字母。
25	
min(str)

返回字符串 str 中最小的字母。
26	
replace(old, new [, max])

把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27	
rfind(str, beg=0,end=len(string))

类似于 find()函数，不过是从右边开始查找.
28	
rindex( str, beg=0, end=len(string))

类似于 index()，不过是从右边开始.
29	
rjust(width,[, fillchar])

返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30	
rstrip()

删除字符串字符串末尾的空格.
31	
split(str="", num=string.count(str))

num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
32	
splitlines([keepends])

按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33	
startswith(str, beg=0,end=len(string))

检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
34	
strip([chars])

在字符串上执行 lstrip()和 rstrip()
35	
swapcase()

将字符串中大写转换为小写，小写转换为大写
36	
title()

返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37	
translate(table, deletechars="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38	
upper()

转换字符串中的小写字母为大写
39	
zfill (width)

返回长度为 width 的字符串，原字符串右对齐，前面填充0
40	
isdecimal()

检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''

a = "hello word! hi python."
print(a.title())

print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        # age = int(input("请输入您家狗的年龄:"))
        age = 1
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2) * 5
            print("相当于人类：", human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
# input("点击 enter 键退出")

count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

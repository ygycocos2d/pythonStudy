#-*-coding:utf-8-*-
#乱码解决方案
import sys
type = sys.getfilesystemencoding()


#time使用
import time
a = [1,2,3]
for i in a:
    print i
    time.sleep(1)#暂停一秒
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


#素数判断
print '素数判断-------------------------------'.decode('UTF-8').encode(type)
import math
def sushu(num):
    max = int(math.sqrt(num))
    for i in range(2,max+1):
        if num % i == 0:
            return False
    return True

for i in range(101,200):
    if sushu(i):
        print i

#水仙花数
print '水仙花数----------------------------------------'.decode('UTF-8').encode(type)
for i in range(100,1000):
    a = i/100
    b = i/10%10
    c = i%10
    if (a**3 + b**3 + c**3) == i:
        print i

#正整数分解质因子
print '正整数分解质因子------------'.decode('UTF-8').encode(type)
def zhiyinzi(num):
    l = []
    for i in range(2,num+1):
        while num > i:
            if num%i ==0:
                l.append(i)
                num = num/i
            else:
                break
    l.append(num)
    return l
print zhiyinzi(100)

#三元表达式,python2.7不支持
print '三元表达式python2.7不支持------------'.decode('UTF-8').encode(type)
#def score(num):
#   return (num>=90)?'A':((num>=80)?'B':((num>=60)?'C':'D'))
#print score(75)


#datetime使用
print 'datetime使用-------------------'.decode('UTF-8').encode(type)
import datetime
print datetime.date.today().strftime('%Y-%m-%d')

#---
print '输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数----'.decode('UTF-8').encode(type)
import string
s = 'dfghjkl910524214   #$%^&*('
letters = 0
space = 0
digit = 0
other = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print 'letters=%d,space=%d,digit=%d,other=%d'%(letters,space,digit,other)

#求s=a+aa+aaa+aaaa+aa...a的值
print '求s=a+aa+aaa+aaaa+aa...a的值-------'.decode('UTF-8').encode(type)
num = int(raw_input('待计算的整数'))
n = int(raw_input('计算次数'))
sum = 0
temp = 0
for i in range(0,n):
    temp = temp*10 + num
    sum += temp
print '累加值为sum=%d'%sum


#个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
print '一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数'.decode('UTF-8').encode(type)
for num in range(1,1001):
    k=[]
    s = num
    for i in range(1,s):
        if num % i == 0:
            s -= i
            k.append(i)
    if s == 0:
        print num
        print k

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
print '一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'.decode('UTF-8').encode(type)
total = 0
h = 100
for i in range(0,10):
    total += h
    h = h/2
print 'total=%f,h=%f'%(total,h)

#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
print '--------------------'
x2=1
for day in range(9,0,-1):
    x1 = (x2+1) * 2
    x2 = x1
print x1


#打印出如下图案（菱形）:
print '打印出如下图案（菱形）:'
from sys import stdout
for i in range(4):
    for j in range(4-i):
        stdout.write(' ')
    for j in range(2*i+1):
        stdout.write('*')
    print
for i in range(3,0,-1):
    for j in range(5-i):
        stdout.write(' ')
    for j in range(2*i-1):
        stdout.write('*')
    print


#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
print '有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'
a = 1.0
b = 2.0
s = 0.0
for i in range(20):
    s += b / a
    #t = a
    #a = b
    #b = t + b
    a,b = b,a+b
print s


#求1+2!+3!+...+20!的和。
print '求1+2!+3!+...+20!的和。------------------------'
s = 0
t = 1
for i in range(1,21):
    t *= i
    s += t
print '1+2!+3!+...+20!=%d'%s

#s = 0
#l = range(1,21)
#def op(x):
#    r = 1
#    for i in range(1,x + 1):
#        r *= i
#    return r
#s = sum(map(op,l))
#print '1! + 2! + 3! + ... + 20! = %d' % s

#利用递归方法求5!。
print '利用递归方法求5!。------'
def func(num):
    if (num == 0) or (num == 1):
        return 1
    return num*func(num-1)

print func(5)


#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
print '利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来'
def nixu(s,l):
    if l==0:
        return
    print s[l-1]
    nixu(s,l-1)
s = raw_input('输入的字符串')
l = len(s)
nixu(s,l)

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
print '给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字'
num = int(raw_input('请输入一个整数'))
s = str(num)
l = len(s)
print '该整数是%d位数'%l
for i in range(l):
    print s[i]

#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
print '一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同'
def huiwen(num):
    s = str(num)
    l = len(s)
    j = l-1
    for i in range(l/2):
        if s[i] != s[j]:
            return False
        j -=1
    return True
num = int(raw_input('输入一个整数'))
if huiwen(num):
    print '%d是回文数'%num
else:
    print '%d不是回文数'%num



#按逗号分隔列表
print '按逗号分隔列表'
l = [1,2,3,4]
s = ','.join(str(n) for n in l)
print s



#if __name__ == '__main__',__name__表示py文件模块的名字，
#在模块中使用时值为'__main__'，在外边import使用时值为文件名
if __name__ == '__main__':
    print huiwen(12321)


#文本置色，跟终端有关
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC


#
def exchange(a,b):
    a,b = b,a
    return (a,b)
x = 10
y = 20
print 'x = %d,y = %d' % (x,y)
x,y = exchange(x,y)
print 'x = %d,y = %d' % (x,y)


#lambda表达式--速写表达式
a = lambda x,y:x+y
print a(1,2)

#随机数
import random
print int(random.uniform(1,10))

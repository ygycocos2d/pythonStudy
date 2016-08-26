#-*- coding:UTF-8 -*-

def fabs(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    l = [1,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    return l

print fabs(10)



def fabs2(n):
    a,b = 0,1
    for i in range(0,n):
        yield b
        a,b = b,a+b

for i in fabs2(10):
    print i

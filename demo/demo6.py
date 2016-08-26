a = [1,2,3]
b = a[0:2]

c = a[:]
print b
print c


for i in range(1,10):
    for j in range(1,10):
        result = i*j
        print '%d * %d = %-3d' %(i,j,result)
    print

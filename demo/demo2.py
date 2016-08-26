# -*- coding: UTF-8 -*-

money = int(raw_input('净利润：'))

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for i in range(0,6):
    if money > arr[i]:
        r += (money-arr[i])*rat[i]
        money = arr[i]
print '提成为:',r

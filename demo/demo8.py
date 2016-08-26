#-*-coding:utf-8-*-

from Tkinter import *
canvas = Canvas(width=800,height=600,bg='#00ffff')
canvas.pack(expand=YES,fill=BOTH)
k = 1
j = 1
for i in range(0,26):
    canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
    k += j
    j +=0.3
mainloop()



# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from Tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()


# -*- coding: UTF-8 -*-

import math
class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []

def LineToDemo():
    from Tkinter import *
    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()
if __name__ == '__main__':
    LineToDemo()

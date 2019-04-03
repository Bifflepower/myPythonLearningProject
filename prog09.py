from tkinter import *
fen1=Tk()
can1=Canvas(fen1,bg='dark grey', height=500, width=500)
can1.pack(side=LEFT)
bou1=Button(fen1, text='quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)

x=0
y=0
r=20
def drawcircle(x,y,r):
    x=0
    y=0
    r=20
    while(x<500 and y<500):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = x + r
        can1.create_oval(x0,y0,x1,y1)
        x=x+10
        y=y+10
        r=r+20

drawcircle(x,y,r)

fen1.mainloop()

fen1.destroy()

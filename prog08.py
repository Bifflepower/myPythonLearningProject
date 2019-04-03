from tkinter import *
fen1=Tk()
can1=Canvas(fen1,bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1=Button(fen1, text='quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
y=0
x=0
def drawline(x):
    y=0
    while(y<200):
        can1.create_line(x,0,100,y)
        y=y+10

drawline(0)
drawline(200)

fen1.mainloop()

fen1.destroy()

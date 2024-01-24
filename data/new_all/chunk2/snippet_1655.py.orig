#Source: https://stackoverflow.com/questions/66630453/how-can-i-add-a-score-tracker-to-my-pong-game-using-tkinter-and-why-am-i-getting
from tkinter import *
from random import *
myHeight=400
myWidth=800
mySpeed=10
scoreplayer1=0
scoreplayer2=0

def initialiseBall(dx,dy,radius,color):
    b=[myWidth/2,myHeight/2,dx,dy,radius]
    b.append(myCanvas.create_oval(myWidth/2-radius,myHeight/2-radius,\
                                  myWidth/2+radius,myHeight/2+radius,\
                                  width=2,fill=color))
    return b

def initialisePaddle(x,y,width, height, radius,color):
    r=[x,y,0,0,width,height]
    r.append(myCanvas.create_rectangle(x-width/2,y-height/2,\
                                      x+width/2,y+height/2,\
                                      width=2,fill=color))
    return r

def updateBall():
    # new position calculation
    global scoreplayer1, scoreplayer2 
    newX=balle[0]+balle[2]
    newY=balle[1]+balle[3]
    hit1=paddle1[0]+paddle1[4]
    hit2=paddle2[1]+paddle2[5]
    
    if newY<0 or newY>=myHeight:
        newY=balle[1]
        balle[3]*=-1         
    # intersection with paddles

    bbox1 = myCanvas.bbox(paddle1[6])
    bbox2 = myCanvas.bbox(paddle2[6])
        
    if newX <= bbox1[2] and (newY>bbox1[1] and newY<bbox1[3]):
        newX=balle[0]
        balle[2]*=-1  
        scoreplayer1+=1    
    if newX >= bbox2[0] and (newY>bbox2[1] and newY<bbox2[3]):
        newX=balle[0]
        balle[2]*=-1
        scoreplayer2+=1      
    # update of coordinates
    balle[0]=newX
    balle[1]=newY
    # update of graphic element 
    myCanvas.coords(balle[5],\
                    balle[0]-balle[4],balle[1]-balle[4],\
                    balle[0]+balle[4],balle[1]+balle[4])    
def updatePaddle(r):
    newY=r[1]+r[3]
    if newY-r[5]/2<0 or newY+r[5]/2>=myHeight:
        newY=r[1]
        r[3]=0
    r[1]=newY
    myCanvas.coords(r[6],\
                    r[0]-r[4]/2,r[1]-r[5]/2,\
                    r[0]+r[4]/2,r[1]+r[5]/2)       
def animation():
    global score
    updateBall()
    updatePaddle(paddle1)
    updatePaddle(paddle2)
    myCanvas.after(mySpeed,animation)    

def movePaddles(event):
    if event.keysym == 'a':
        paddle1[3]=-5
    if event.keysym == 'q':
        paddle1[3]=5
    if event.keysym == 'Up':
        paddle2[3]=-5
    if event.keysym == 'Down':
        paddle2[3]=5
def stopPaddles(event):
    if event.keysym == 'q' or event.keysym == 'a':
        paddle1[3]=0
    if event.keysym == 'Up' or event.keysym == 'Down':
        paddle2[3]=0
mainWindow=Tk()
mainWindow.title('Pong')
mainWindow.geometry(str(myWidth)+'x'+str(myHeight))
myCanvas=Canvas(mainWindow,bg='dark grey',height=myHeight,width=myWidth)
myCanvas.pack(side=TOP)
balle=initialiseBall(5,5,20,'red')
paddle1=initialisePaddle(60,myHeight/2,40,100,'green')
paddle2=initialisePaddle(myWidth-60,myHeight/2,40,100,'blue')
mainWindow.bind("<Key>",movePaddles)
mainWindow.bind("<KeyRelease>",stopPaddles)
animation()
mainWindow.mainloop()
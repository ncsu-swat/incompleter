# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66630453/how-can-i-add-a-score-tracker-to-my-pong-game-using-tkinter-and-why-am-i-getting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(431190)

except ImportError:
    pass
try:
    from random import *
    _l_(431192)

except ImportError:
    pass
myHeight=400
_l_(431193)
myWidth=800
_l_(431194)
mySpeed=10
_l_(431195)
scoreplayer1=0
_l_(431196)
scoreplayer2=0
_l_(431197)

def initialiseBall(dx,dy,radius,color):
    _l_(431222)

    b=[_n_(431198, "myWidth", lambda: myWidth)/2,_n_(431199, "myHeight", lambda: myHeight)/2,_n_(431200, "dx", lambda: dx),_n_(431201, "dy", lambda: dy),_n_(431202, "radius", lambda: radius)]
    _l_(431203)
    _c_(431218, _a_(431205, _n_(431204, "b", lambda: b), "append"), _c_(431217, _a_(431207, _n_(431206, "myCanvas", lambda: myCanvas), "create_oval"), _n_(431208, "myWidth", lambda: myWidth)/2-_n_(431209, "radius", lambda: radius),_n_(431210, "myHeight", lambda: myHeight)/2-_n_(431211, "radius", lambda: radius),\
                                  _n_(431212, "myWidth", lambda: myWidth)/2+_n_(431213, "radius", lambda: radius),_n_(431214, "myHeight", lambda: myHeight)/2+_n_(431215, "radius", lambda: radius),\
                                  width=2,fill=_n_(431216, "color", lambda: color)))
    _l_(431219)
    aux = _n_(431220, "b", lambda: b)
    _l_(431221)
    return aux

def initialisePaddle(x,y,width, height, radius,color):
    _l_(431246)

    r=[_n_(431223, "x", lambda: x),_n_(431224, "y", lambda: y),0,0,_n_(431225, "width", lambda: width),_n_(431226, "height", lambda: height)]
    _l_(431227)
    _c_(431242, _a_(431229, _n_(431228, "r", lambda: r), "append"), _c_(431241, _a_(431231, _n_(431230, "myCanvas", lambda: myCanvas), "create_rectangle"), _n_(431232, "x", lambda: x)-_n_(431233, "width", lambda: width)/2,_n_(431234, "y", lambda: y)-_n_(431235, "height", lambda: height)/2,\
                                      _n_(431236, "x", lambda: x)+_n_(431237, "width", lambda: width)/2,_n_(431238, "y", lambda: y)+_n_(431239, "height", lambda: height)/2,\
                                      width=2,fill=_n_(431240, "color", lambda: color)))
    _l_(431243)
    aux = _n_(431244, "r", lambda: r)
    _l_(431245)
    return aux

def updateBall():
    _l_(431321)

    # new position calculation
    global scoreplayer1, scoreplayer2 
    _l_(431247) 
    newX=_n_(431248, "balle", lambda: balle)[0]+_n_(431249, "balle", lambda: balle)[2]
    _l_(431250)
    newY=_n_(431251, "balle", lambda: balle)[1]+_n_(431252, "balle", lambda: balle)[3]
    _l_(431253)
    hit1=_n_(431254, "paddle1", lambda: paddle1)[0]+_n_(431255, "paddle1", lambda: paddle1)[4]
    _l_(431256)
    hit2=_n_(431257, "paddle2", lambda: paddle2)[1]+_n_(431258, "paddle2", lambda: paddle2)[5]
    _l_(431259)
    
    if _n_(431260, "newY", lambda: newY)<0 or _n_(431261, "newY", lambda: newY)>=_n_(431262, "myHeight", lambda: myHeight):
        _l_(431267)

        newY=_n_(431263, "balle", lambda: balle)[1]
        _l_(431264)
        _n_(431265, "balle", lambda: balle)[3]*=-1         
        _l_(431266)         
    # intersection with paddles

    bbox1 = _c_(431271, _a_(431269, _n_(431268, "myCanvas", lambda: myCanvas), "bbox"), _n_(431270, "paddle1", lambda: paddle1)[6])
    _l_(431272)
    bbox2 = _c_(431276, _a_(431274, _n_(431273, "myCanvas", lambda: myCanvas), "bbox"), _n_(431275, "paddle2", lambda: paddle2)[6])
    _l_(431277)
        
    if _n_(431278, "newX", lambda: newX) <= _n_(431279, "bbox1", lambda: bbox1)[2] and (_n_(431280, "newY", lambda: newY)>_n_(431281, "bbox1", lambda: bbox1)[1] and _n_(431282, "newY", lambda: newY)<_n_(431283, "bbox1", lambda: bbox1)[3]):
        _l_(431289)

        newX=_n_(431284, "balle", lambda: balle)[0]
        _l_(431285)
        _n_(431286, "balle", lambda: balle)[2]*=-1  
        _l_(431287)  
        scoreplayer1+=1    
        _l_(431288)    
    if _n_(431290, "newX", lambda: newX) >= _n_(431291, "bbox2", lambda: bbox2)[0] and (_n_(431292, "newY", lambda: newY)>_n_(431293, "bbox2", lambda: bbox2)[1] and _n_(431294, "newY", lambda: newY)<_n_(431295, "bbox2", lambda: bbox2)[3]):
        _l_(431301)

        newX=_n_(431296, "balle", lambda: balle)[0]
        _l_(431297)
        _n_(431298, "balle", lambda: balle)[2]*=-1
        _l_(431299)
        scoreplayer2+=1      
        _l_(431300)      
    # update of coordinates
    _n_(431302, "balle", lambda: balle)[0]=_n_(431303, "newX", lambda: newX)
    _l_(431304)
    _n_(431305, "balle", lambda: balle)[1]=_n_(431306, "newY", lambda: newY)
    _l_(431307)
    # update of graphic element 
    _c_(431319, _a_(431309, _n_(431308, "myCanvas", lambda: myCanvas), "coords"), _n_(431310, "balle", lambda: balle)[5],\
                    _n_(431311, "balle", lambda: balle)[0]-_n_(431312, "balle", lambda: balle)[4],_n_(431313, "balle", lambda: balle)[1]-_n_(431314, "balle", lambda: balle)[4],\
                    _n_(431315, "balle", lambda: balle)[0]+_n_(431316, "balle", lambda: balle)[4],_n_(431317, "balle", lambda: balle)[1]+_n_(431318, "balle", lambda: balle)[4])    
    _l_(431320)    
def updatePaddle(r):
    _l_(431351)

    newY=_n_(431322, "r", lambda: r)[1]+_n_(431323, "r", lambda: r)[3]
    _l_(431324)
    if _n_(431325, "newY", lambda: newY)-_n_(431326, "r", lambda: r)[5]/2<0 or _n_(431327, "newY", lambda: newY)+_n_(431328, "r", lambda: r)[5]/2>=_n_(431329, "myHeight", lambda: myHeight):
        _l_(431334)

        newY=_n_(431330, "r", lambda: r)[1]
        _l_(431331)
        _n_(431332, "r", lambda: r)[3]=0
        _l_(431333)
    _n_(431335, "r", lambda: r)[1]=_n_(431336, "newY", lambda: newY)
    _l_(431337)
    _c_(431349, _a_(431339, _n_(431338, "myCanvas", lambda: myCanvas), "coords"), _n_(431340, "r", lambda: r)[6],\
                    _n_(431341, "r", lambda: r)[0]-_n_(431342, "r", lambda: r)[4]/2,_n_(431343, "r", lambda: r)[1]-_n_(431344, "r", lambda: r)[5]/2,\
                    _n_(431345, "r", lambda: r)[0]+_n_(431346, "r", lambda: r)[4]/2,_n_(431347, "r", lambda: r)[1]+_n_(431348, "r", lambda: r)[5]/2)       
    _l_(431350)       
def animation():
    _l_(431370)

    global score
    _l_(431352)
    _c_(431354, _n_(431353, "updateBall", lambda: updateBall))
    _l_(431355)
    _c_(431358, _n_(431356, "updatePaddle", lambda: updatePaddle), _n_(431357, "paddle1", lambda: paddle1))
    _l_(431359)
    _c_(431362, _n_(431360, "updatePaddle", lambda: updatePaddle), _n_(431361, "paddle2", lambda: paddle2))
    _l_(431363)
    _c_(431368, _a_(431365, _n_(431364, "myCanvas", lambda: myCanvas), "after"), _n_(431366, "mySpeed", lambda: mySpeed),_n_(431367, "animation", lambda: animation))    
    _l_(431369)    

def movePaddles(event):
    _l_(431391)

    if _a_(431372, _n_(431371, "event", lambda: event), "keysym") == 'a':
        _l_(431375)

        _n_(431373, "paddle1", lambda: paddle1)[3]=-5
        _l_(431374)
    if _a_(431377, _n_(431376, "event", lambda: event), "keysym") == 'q':
        _l_(431380)

        _n_(431378, "paddle1", lambda: paddle1)[3]=5
        _l_(431379)
    if _a_(431382, _n_(431381, "event", lambda: event), "keysym") == 'Up':
        _l_(431385)

        _n_(431383, "paddle2", lambda: paddle2)[3]=-5
        _l_(431384)
    if _a_(431387, _n_(431386, "event", lambda: event), "keysym") == 'Down':
        _l_(431390)

        _n_(431388, "paddle2", lambda: paddle2)[3]=5
        _l_(431389)
def stopPaddles(event):
    _l_(431406)

    if _a_(431393, _n_(431392, "event", lambda: event), "keysym") == 'q' or _a_(431395, _n_(431394, "event", lambda: event), "keysym") == 'a':
        _l_(431398)

        _n_(431396, "paddle1", lambda: paddle1)[3]=0
        _l_(431397)
    if _a_(431400, _n_(431399, "event", lambda: event), "keysym") == 'Up' or _a_(431402, _n_(431401, "event", lambda: event), "keysym") == 'Down':
        _l_(431405)

        _n_(431403, "paddle2", lambda: paddle2)[3]=0
        _l_(431404)
mainWindow=_c_(431408, _n_(431407, "Tk", lambda: Tk))
_l_(431409)
_c_(431412, _a_(431411, _n_(431410, "mainWindow", lambda: mainWindow), "title"), 'Pong')
_l_(431413)
_c_(431422, _a_(431415, _n_(431414, "mainWindow", lambda: mainWindow), "geometry"), _c_(431418, _n_(431416, "str", lambda: str), _n_(431417, "myWidth", lambda: myWidth))+'x'+_c_(431421, _n_(431419, "str", lambda: str), _n_(431420, "myHeight", lambda: myHeight)))
_l_(431423)
myCanvas=_c_(431428, _n_(431424, "Canvas", lambda: Canvas), _n_(431425, "mainWindow", lambda: mainWindow),bg='dark grey',height=_n_(431426, "myHeight", lambda: myHeight),width=_n_(431427, "myWidth", lambda: myWidth))
_l_(431429)
_c_(431433, _a_(431431, _n_(431430, "myCanvas", lambda: myCanvas), "pack"), side=_n_(431432, "TOP", lambda: TOP))
_l_(431434)
balle=_c_(431436, _n_(431435, "initialiseBall", lambda: initialiseBall), 5,5,20,'red')
_l_(431437)
paddle1=_c_(431440, _n_(431438, "initialisePaddle", lambda: initialisePaddle), 60,_n_(431439, "myHeight", lambda: myHeight)/2,40,100,'green')
_l_(431441)
paddle2=_c_(431445, _n_(431442, "initialisePaddle", lambda: initialisePaddle), _n_(431443, "myWidth", lambda: myWidth)-60,_n_(431444, "myHeight", lambda: myHeight)/2,40,100,'blue')
_l_(431446)
_c_(431450, _a_(431448, _n_(431447, "mainWindow", lambda: mainWindow), "bind"), "<Key>",_n_(431449, "movePaddles", lambda: movePaddles))
_l_(431451)
_c_(431455, _a_(431453, _n_(431452, "mainWindow", lambda: mainWindow), "bind"), "<KeyRelease>",_n_(431454, "stopPaddles", lambda: stopPaddles))
_l_(431456)
_c_(431458, _n_(431457, "animation", lambda: animation))
_l_(431459)
_c_(431462, _a_(431461, _n_(431460, "mainWindow", lambda: mainWindow), "mainloop"))
_l_(431463)
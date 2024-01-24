# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48071947/why-is-my-enclosed-area-function-giving-typeerror-unsupported-operand-types
#First helping function: FIND POINTS OF INTERSECTION
#---------------------------------------------------------------------
#This function takes four int or float values representing two lines 
#and returns the x value of the point of intersection of the two lines. 
#If the lines are parallel, or identical, the function should return 
#None. 
#---------------------------------------------------------------------

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def f(m1,b1,m2,b2):
    _l_(680553)


    if _n_(680544, "m1", lambda: m1) == _n_(680545, "m2", lambda: m2):
        _l_(680552)

        aux = None
        _l_(680546)
        return aux

    else:
        aux = (_n_(680547, "b2", lambda: b2) - _n_(680548, "b1", lambda: b1))/(_n_(680549, "m1", lambda: m1) - _n_(680550, "m2", lambda: m2))   
        _l_(680551)   
        return aux   



#Second helping function: FIND LENGTH (DISTANCE BETWEEN POINTS)
#--------------------------------------------------------------------
#This function takes four int or float values representing two points 
#and returns the distance between those points.
#--------------------------------------------------------------------

def dist(x1,y1,x2,y2):
    _l_(680560)

    aux = "" 
    _l_(680554) 

    return aux 

    D = ((_n_(680555, "x1", lambda: x1)-_n_(680556, "x2", lambda: x2))**2 + (_n_(680557, "y1", lambda: y1)-_n_(680558, "y2", lambda: y2))**2)
    _l_(680559)


#3RD Helping function:  FIND AREA ENCLOSED BY 3 LINES 
#-----------------------------------------------------------------
#This function takes three int or float values representing side 
#lengths of a triangle, and returns the area of that triangle using 
#Heron's formula
#-----------------------------------------------------------------    
def heron(D1,D2,D3):
    _l_(680575)


    p = (_n_(680561, "D1", lambda: D1) + _n_(680562, "D2", lambda: D2) + _n_(680563, "D3", lambda: D3))*0.5    
    _l_(680564)    
    # where p is half the perimeter 
    area = (_n_(680565, "p", lambda: p)*(_n_(680566, "p", lambda: p)-_n_(680567, "D1", lambda: D1))*(_n_(680568, "p", lambda: p)-_n_(680569, "D2", lambda: D2))*(_n_(680570, "p", lambda: p)-_n_(680571, "D3", lambda: D3)))**0.5
    _l_(680572)
    aux = _n_(680573, "area", lambda: area) 
    _l_(680574) 

    return aux 



#Finally, the last function:
#-------------------------------------------------------------------
#This function makes use of the helping functions above and connects 
#everything together 
#-------------------------------------------------------------------

def func(m1,b1,m2,b2,m3,b3):
    _l_(680636)


#Using 1st helping function:
#---------------------------
    x1  = _c_(680581, _n_(680576, "f", lambda: f), _n_(680577, "m1", lambda: m1), _n_(680578, "b1", lambda: b1), _n_(680579, "m2", lambda: m2), _n_(680580, "b2", lambda: b2))
    _l_(680582)
    x2  = _c_(680588, _n_(680583, "f", lambda: f), _n_(680584, "m1", lambda: m1), _n_(680585, "b1", lambda: b1), _n_(680586, "m3", lambda: m3), _n_(680587, "b3", lambda: b3))
    _l_(680589)
    x3  = _c_(680595, _n_(680590, "f", lambda: f), _n_(680591, "m2", lambda: m2), _n_(680592, "b2", lambda: b2), _n_(680593, "m3", lambda: m3), _n_(680594, "b3", lambda: b3))
    _l_(680596)

    #---

    y1 = _n_(680597, "m1", lambda: m1)*_n_(680598, "x1", lambda: x1) + _n_(680599, "b1", lambda: b1)
    _l_(680600)
    y2 = _n_(680601, "m2", lambda: m2)*_n_(680602, "x2", lambda: x2) + _n_(680603, "b2", lambda: b2)
    _l_(680604)
    y3 = _n_(680605, "m3", lambda: m3)*_n_(680606, "x3", lambda: x3) + _n_(680607, "b3", lambda: b3)
    _l_(680608)


 #Using 2nd helping function:
 #---------------------------

    D1 = _c_(680614, _n_(680609, "dist", lambda: dist), _n_(680610, "x1", lambda: x1),_n_(680611, "y1", lambda: y1),_n_(680612, "x2", lambda: x2),_n_(680613, "y2", lambda: y2))
    _l_(680615)
    D2 = _c_(680621, _n_(680616, "dist", lambda: dist), _n_(680617, "x1", lambda: x1),_n_(680618, "y1", lambda: y1),_n_(680619, "x3", lambda: x3),_n_(680620, "y3", lambda: y3))
    _l_(680622)
    D3 = _c_(680628, _n_(680623, "dist", lambda: dist), _n_(680624, "x2", lambda: x2),_n_(680625, "y2", lambda: y2),_n_(680626, "x3", lambda: x3),_n_(680627, "y3", lambda: y3))
    _l_(680629)
    aux = _c_(680634, _n_(680630, "heron", lambda: heron), _n_(680631, "D1", lambda: D1),_n_(680632, "D2", lambda: D2),_n_(680633, "D3", lambda: D3))
    _l_(680635)


#Using 3rd helping function:
#---------------------------
    return aux


_c_(680640, _n_(680637, "print", lambda: print), _c_(680639, _n_(680638, "func", lambda: func), 0,20,-2,50,0.5,-10))
_l_(680641)
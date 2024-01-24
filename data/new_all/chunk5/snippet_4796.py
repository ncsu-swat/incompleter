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
    _l_(671055)


    if _n_(671046, "m1", lambda: m1) == _n_(671047, "m2", lambda: m2):
        _l_(671054)

        aux = None
        _l_(671048)
        return aux

    else:
        aux = (_n_(671049, "b2", lambda: b2) - _n_(671050, "b1", lambda: b1))/(_n_(671051, "m1", lambda: m1) - _n_(671052, "m2", lambda: m2))   
        _l_(671053)   
        return aux   



#Second helping function: FIND LENGTH (DISTANCE BETWEEN POINTS)
#--------------------------------------------------------------------
#This function takes four int or float values representing two points 
#and returns the distance between those points.
#--------------------------------------------------------------------

def dist(x1,y1,x2,y2):
    _l_(671062)

    aux = "" 
    _l_(671056) 

    return aux 

    D = ((_n_(671057, "x1", lambda: x1)-_n_(671058, "x2", lambda: x2))**2 + (_n_(671059, "y1", lambda: y1)-_n_(671060, "y2", lambda: y2))**2)
    _l_(671061)


#3RD Helping function:  FIND AREA ENCLOSED BY 3 LINES 
#-----------------------------------------------------------------
#This function takes three int or float values representing side 
#lengths of a triangle, and returns the area of that triangle using 
#Heron's formula
#-----------------------------------------------------------------    
def heron(D1,D2,D3):
    _l_(671077)


    p = (_n_(671063, "D1", lambda: D1) + _n_(671064, "D2", lambda: D2) + _n_(671065, "D3", lambda: D3))*0.5    
    _l_(671066)    
    # where p is half the perimeter 
    area = (_n_(671067, "p", lambda: p)*(_n_(671068, "p", lambda: p)-_n_(671069, "D1", lambda: D1))*(_n_(671070, "p", lambda: p)-_n_(671071, "D2", lambda: D2))*(_n_(671072, "p", lambda: p)-_n_(671073, "D3", lambda: D3)))**0.5
    _l_(671074)
    aux = _n_(671075, "area", lambda: area) 
    _l_(671076) 

    return aux 



#Finally, the last function:
#-------------------------------------------------------------------
#This function makes use of the helping functions above and connects 
#everything together 
#-------------------------------------------------------------------

def func(m1,b1,m2,b2,m3,b3):
    _l_(671138)


#Using 1st helping function:
#---------------------------
    x1  = _c_(671083, _n_(671078, "f", lambda: f), _n_(671079, "m1", lambda: m1), _n_(671080, "b1", lambda: b1), _n_(671081, "m2", lambda: m2), _n_(671082, "b2", lambda: b2))
    _l_(671084)
    x2  = _c_(671090, _n_(671085, "f", lambda: f), _n_(671086, "m1", lambda: m1), _n_(671087, "b1", lambda: b1), _n_(671088, "m3", lambda: m3), _n_(671089, "b3", lambda: b3))
    _l_(671091)
    x3  = _c_(671097, _n_(671092, "f", lambda: f), _n_(671093, "m2", lambda: m2), _n_(671094, "b2", lambda: b2), _n_(671095, "m3", lambda: m3), _n_(671096, "b3", lambda: b3))
    _l_(671098)

    #---

    y1 = _n_(671099, "m1", lambda: m1)*_n_(671100, "x1", lambda: x1) + _n_(671101, "b1", lambda: b1)
    _l_(671102)
    y2 = _n_(671103, "m2", lambda: m2)*_n_(671104, "x2", lambda: x2) + _n_(671105, "b2", lambda: b2)
    _l_(671106)
    y3 = _n_(671107, "m3", lambda: m3)*_n_(671108, "x3", lambda: x3) + _n_(671109, "b3", lambda: b3)
    _l_(671110)


 #Using 2nd helping function:
 #---------------------------

    D1 = _c_(671116, _n_(671111, "dist", lambda: dist), _n_(671112, "x1", lambda: x1),_n_(671113, "y1", lambda: y1),_n_(671114, "x2", lambda: x2),_n_(671115, "y2", lambda: y2))
    _l_(671117)
    D2 = _c_(671123, _n_(671118, "dist", lambda: dist), _n_(671119, "x1", lambda: x1),_n_(671120, "y1", lambda: y1),_n_(671121, "x3", lambda: x3),_n_(671122, "y3", lambda: y3))
    _l_(671124)
    D3 = _c_(671130, _n_(671125, "dist", lambda: dist), _n_(671126, "x2", lambda: x2),_n_(671127, "y2", lambda: y2),_n_(671128, "x3", lambda: x3),_n_(671129, "y3", lambda: y3))
    _l_(671131)
    aux = _c_(671136, _n_(671132, "heron", lambda: heron), _n_(671133, "D1", lambda: D1),_n_(671134, "D2", lambda: D2),_n_(671135, "D3", lambda: D3))
    _l_(671137)


#Using 3rd helping function:
#---------------------------
    return aux


_c_(671142, _n_(671139, "print", lambda: print), _c_(671141, _n_(671140, "func", lambda: func), 0,20,-2,50,0.5,-10))
_l_(671143)
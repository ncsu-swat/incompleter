# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70399617/attribute-error-list-object-has-no-attribute-checkclick
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from os import access
   _l_(457363)

except ImportError:
   pass
try:
   import pygame,sys
   _l_(457365)

except ImportError:
   pass
try:
   from random import randrange
   _l_(457367)

except ImportError:
   pass
try:
   import numpy
   _l_(457369)

except ImportError:
   pass
#Constants
Columns =5
_l_(457370)
Rows = 5
_l_(457371)
X,Y = 320,0
_l_(457372)

class Button:
   _l_(457449)

   def __init__(self,x,y,image,scale):
      _l_(457403)

      _n_(457373, "self", lambda: self).x = _n_(457374, "x", lambda: x)
      _l_(457375)
      _n_(457376, "self", lambda: self).y=_n_(457377, "y", lambda: y)
      _l_(457378)
      _n_(457379, "self", lambda: self).image = _c_(457386, _a_(457382, _a_(457381, _n_(457380, "pygame", lambda: pygame), "transform"), "scale"), _n_(457383, "image", lambda: image),(_n_(457384, "scale", lambda: scale),_n_(457385, "scale", lambda: scale)))
      _l_(457387)
      _n_(457388, "self", lambda: self).scale = _n_(457389, "scale", lambda: scale)
      _l_(457390)
      _n_(457391, "self", lambda: self).rect = _c_(457397, _a_(457394, _a_(457393, _n_(457392, "self", lambda: self), "image"), "get_rect"), topleft=(_n_(457395, "x", lambda: x),_n_(457396, "y", lambda: y)))
      _l_(457398)
      _n_(457399, "self", lambda: self).clicked = False 
      _l_(457400) 
      _n_(457401, "self", lambda: self).Action = False
      _l_(457402)

   
   def Draw(self):
      _l_(457414)

      _c_(457412, _a_(457405, _n_(457404, "Win", lambda: Win), "blit"), _a_(457407, _n_(457406, "self", lambda: self), "image"),(_a_(457409, _n_(457408, "self", lambda: self), "x"),_a_(457411, _n_(457410, "self", lambda: self), "y")))
      _l_(457413)
   
   def CheckClick(self):
      _l_(457448)

      isClicked = False
      _l_(457415)
      mousepos= _c_(457419, _a_(457418, _a_(457417, _n_(457416, "pygame", lambda: pygame), "mouse"), "get_pos"))
      _l_(457420)
      if _c_(457425, _a_(457423, _a_(457422, _n_(457421, "self", lambda: self), "rect"), "collidepoint"), _n_(457424, "mousepos", lambda: mousepos)):
         _l_(457444)

         if _c_(457429, _a_(457428, _a_(457427, _n_(457426, "pygame", lambda: pygame), "mouse"), "get_pressed"))[0] ==1 and _a_(457431, _n_(457430, "self", lambda: self), "clicked") == False:
            _l_(457436)

            _n_(457432, "self", lambda: self).clicked = True
            _l_(457433)
            _n_(457434, "self", lambda: self).Action = True
            _l_(457435)
         if _c_(457440, _a_(457439, _a_(457438, _n_(457437, "pygame", lambda: pygame), "mouse"), "get_pressed"))[0] ==0:
            _l_(457443)

            _n_(457441, "self", lambda: self).clicked = False
            _l_(457442)
      aux = _a_(457446, _n_(457445, "self", lambda: self), "Action")
      _l_(457447)
      return aux



#Win
WinWidth, WinHeight = 1280,800
_l_(457450)
Win = _c_(457456, _a_(457453, _a_(457452, _n_(457451, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(457454, "WinWidth", lambda: WinWidth),_n_(457455, "WinHeight", lambda: WinHeight)))
_l_(457457)

#IMAGES
test_img = _c_(457461, _a_(457460, _a_(457459, _n_(457458, "pygame", lambda: pygame), "image"), "load"), "test.png")
_l_(457462)
red_img = _c_(457466, _a_(457465, _a_(457464, _n_(457463, "pygame", lambda: pygame), "image"), "load"), "Red.png")
_l_(457467)
green_img = _c_(457471, _a_(457470, _a_(457469, _n_(457468, "pygame", lambda: pygame), "image"), "load"), "green.png")
_l_(457472)
blue_img = _c_(457476, _a_(457475, _a_(457474, _n_(457473, "pygame", lambda: pygame), "image"), "load"), "blue.png")
_l_(457477)

#Board
Board = [[ _c_(457479, _n_(457478, "randrange", lambda: randrange), 0,3) for column in _c_(457482, _n_(457480, "range", lambda: range), _n_(457481, "Columns", lambda: Columns))] for row in _c_(457485, _n_(457483, "range", lambda: range), _n_(457484, "Rows", lambda: Rows)) ]
_l_(457486)

BoardObjs = []
_l_(457487)

BoardXYs = [[None for column in _c_(457490, _n_(457488, "range", lambda: range), _n_(457489, "Columns", lambda: Columns))]for row in _c_(457493, _n_(457491, "range", lambda: range), _n_(457492, "Rows", lambda: Rows))]
_l_(457494)

#Fill BoardXYS
for k in _c_(457499, _n_(457495, "range", lambda: range), _c_(457498, _n_(457496, "len", lambda: len), _n_(457497, "Board", lambda: Board))):
   _l_(457515)

   for j in _c_(457504, _n_(457500, "range", lambda: range), _c_(457503, _n_(457501, "len", lambda: len), _n_(457502, "Board", lambda: Board)[1])):
      _l_(457512)

      _n_(457505, "BoardXYs", lambda: BoardXYs)[_n_(457506, "k", lambda: k)][_n_(457507, "j", lambda: j)] = [_n_(457508, "X", lambda: X),_n_(457509, "Y", lambda: Y)]
      _l_(457510)
      X += 160
      _l_(457511)
   X = 320
   _l_(457513)
   Y += 160
   _l_(457514)

for r in _c_(457520, _n_(457516, "range", lambda: range), _c_(457519, _n_(457517, "len", lambda: len), _n_(457518, "Board", lambda: Board))):
   _l_(457578)

   for t in _c_(457525, _n_(457521, "range", lambda: range), _c_(457524, _n_(457522, "len", lambda: len), _n_(457523, "Board", lambda: Board)[1])):
      _l_(457577)

      if _n_(457526, "Board", lambda: Board)[_n_(457527, "r", lambda: r)][_n_(457528, "t", lambda: t)] == 0:
         _l_(457542)

         _c_(457540, _a_(457530, _n_(457529, "BoardObjs", lambda: BoardObjs), "append"), _c_(457539, _n_(457531, "Button", lambda: Button), _n_(457532, "BoardXYs", lambda: BoardXYs)[_n_(457533, "r", lambda: r)][_n_(457534, "t", lambda: t)][0],_n_(457535, "BoardXYs", lambda: BoardXYs)[_n_(457536, "r", lambda: r)][_n_(457537, "t", lambda: t)][1],_n_(457538, "red_img", lambda: red_img),100))
         _l_(457541)
      if _n_(457543, "Board", lambda: Board)[_n_(457544, "r", lambda: r)][_n_(457545, "t", lambda: t)] == 1:
         _l_(457559)

         _c_(457557, _a_(457547, _n_(457546, "BoardObjs", lambda: BoardObjs), "append"), _c_(457556, _n_(457548, "Button", lambda: Button), _n_(457549, "BoardXYs", lambda: BoardXYs)[_n_(457550, "r", lambda: r)][_n_(457551, "t", lambda: t)][0],_n_(457552, "BoardXYs", lambda: BoardXYs)[_n_(457553, "r", lambda: r)][_n_(457554, "t", lambda: t)][1],_n_(457555, "green_img", lambda: green_img),100))
         _l_(457558)
      if _n_(457560, "Board", lambda: Board)[_n_(457561, "r", lambda: r)][_n_(457562, "t", lambda: t)] == 2:
         _l_(457576)

         _c_(457574, _a_(457564, _n_(457563, "BoardObjs", lambda: BoardObjs), "append"), _c_(457573, _n_(457565, "Button", lambda: Button), _n_(457566, "BoardXYs", lambda: BoardXYs)[_n_(457567, "r", lambda: r)][_n_(457568, "t", lambda: t)][0],_n_(457569, "BoardXYs", lambda: BoardXYs)[_n_(457570, "r", lambda: r)][_n_(457571, "t", lambda: t)][1],_n_(457572, "blue_img", lambda: blue_img),100))
         _l_(457575)



BoardObjs = [[_n_(457579, "BoardObjs", lambda: BoardObjs)[0],_n_(457580, "BoardObjs", lambda: BoardObjs)[1],_n_(457581, "BoardObjs", lambda: BoardObjs)[2],_n_(457582, "BoardObjs", lambda: BoardObjs)[3],_n_(457583, "BoardObjs", lambda: BoardObjs)[4]],
           [_n_(457584, "BoardObjs", lambda: BoardObjs)[5],_n_(457585, "BoardObjs", lambda: BoardObjs)[6],_n_(457586, "BoardObjs", lambda: BoardObjs)[7],_n_(457587, "BoardObjs", lambda: BoardObjs)[8],_n_(457588, "BoardObjs", lambda: BoardObjs)[9]],
           [_n_(457589, "BoardObjs", lambda: BoardObjs)[10],_n_(457590, "BoardObjs", lambda: BoardObjs)[11],_n_(457591, "BoardObjs", lambda: BoardObjs)[12],_n_(457592, "BoardObjs", lambda: BoardObjs)[13],_n_(457593, "BoardObjs", lambda: BoardObjs)[14]],
           [_n_(457594, "BoardObjs", lambda: BoardObjs)[15],_n_(457595, "BoardObjs", lambda: BoardObjs)[16],_n_(457596, "BoardObjs", lambda: BoardObjs)[17],_n_(457597, "BoardObjs", lambda: BoardObjs)[18],_n_(457598, "BoardObjs", lambda: BoardObjs)[19]],
           [_n_(457599, "BoardObjs", lambda: BoardObjs)[20],_n_(457600, "BoardObjs", lambda: BoardObjs)[21],_n_(457601, "BoardObjs", lambda: BoardObjs)[22],_n_(457602, "BoardObjs", lambda: BoardObjs)[23],_n_(457603, "BoardObjs", lambda: BoardObjs)[24]]]
_l_(457604)

_c_(457609, _n_(457605, "print", lambda: print), _c_(457608, _n_(457606, "len", lambda: len), _n_(457607, "Board", lambda: Board)))
_l_(457610)
_c_(457615, _n_(457611, "print", lambda: print), _c_(457614, _n_(457612, "len", lambda: len), _n_(457613, "BoardObjs", lambda: BoardObjs)))
_l_(457616)


#Images
img_0 = _c_(457619, _a_(457618, _n_(457617, "pygame", lambda: pygame), "Rect"), 0,0,64,64)
_l_(457620)

TouchingReds = 0
_l_(457621)
def CheckMatches(Board):
   _l_(457718)

   VerticalMatch = False
   _l_(457622)
   HorizontalMatch = False
   _l_(457623)
   for m in _c_(457628, _n_(457624, "range", lambda: range), _c_(457627, _n_(457625, "len", lambda: len), _n_(457626, "Board", lambda: Board))):
      _l_(457717)

      for n in _c_(457633, _n_(457629, "range", lambda: range), _c_(457632, _n_(457630, "len", lambda: len), _n_(457631, "Board", lambda: Board)[1])-2):
         _l_(457669)

         if _n_(457634, "Board", lambda: Board)[_n_(457635, "m", lambda: m)][_n_(457636, "n", lambda: n)]==_n_(457637, "Board", lambda: Board)[_n_(457638, "m", lambda: m)][_n_(457639, "n", lambda: n)+1]==_n_(457640, "Board", lambda: Board)[_n_(457641, "m", lambda: m)][_n_(457642, "n", lambda: n)+2]:
            _l_(457668)

            HorizontalMatch = True
            _l_(457643)
            _n_(457644, "Board", lambda: Board)[_n_(457645, "m", lambda: m)][_n_(457646, "n", lambda: n)] = None
            _l_(457647)
            _n_(457648, "Board", lambda: Board)[_n_(457649, "m", lambda: m)][_n_(457650, "n", lambda: n)+1] = None
            _l_(457651)
            _n_(457652, "Board", lambda: Board)[_n_(457653, "m", lambda: m)][_n_(457654, "n", lambda: n)+2] = None
            _l_(457655)
            _n_(457656, "BoardObjs", lambda: BoardObjs)[_n_(457657, "m", lambda: m)][_n_(457658, "n", lambda: n)] = None
            _l_(457659)
            _n_(457660, "BoardObjs", lambda: BoardObjs)[_n_(457661, "m", lambda: m)][_n_(457662, "n", lambda: n)+1] = None
            _l_(457663)
            _n_(457664, "BoardObjs", lambda: BoardObjs)[_n_(457665, "m", lambda: m)][_n_(457666, "n", lambda: n)+2] = None
            _l_(457667)
      for o in _c_(457674, _n_(457670, "range", lambda: range), _c_(457673, _n_(457671, "len", lambda: len), _n_(457672, "Board", lambda: Board)[1])-2):
         _l_(457716)

         for u in _c_(457679, _n_(457675, "range", lambda: range), _c_(457678, _n_(457676, "len", lambda: len), _n_(457677, "Board", lambda: Board))):
            _l_(457715)

            if _n_(457680, "Board", lambda: Board)[_n_(457681, "o", lambda: o)][_n_(457682, "u", lambda: u)]==_n_(457683, "Board", lambda: Board)[_n_(457684, "o", lambda: o)+1][_n_(457685, "u", lambda: u)]==_n_(457686, "Board", lambda: Board)[_n_(457687, "o", lambda: o)+2][_n_(457688, "u", lambda: u)]:
               _l_(457714)

               VerticalMatch = True
               _l_(457689)
               _n_(457690, "Board", lambda: Board)[_n_(457691, "o", lambda: o)][_n_(457692, "u", lambda: u)] = None
               _l_(457693)
               _n_(457694, "Board", lambda: Board)[_n_(457695, "o", lambda: o)+1][_n_(457696, "u", lambda: u)] = None
               _l_(457697)
               _n_(457698, "Board", lambda: Board)[_n_(457699, "o", lambda: o)+2][_n_(457700, "u", lambda: u)] = None
               _l_(457701)
               _n_(457702, "BoardObjs", lambda: BoardObjs)[_n_(457703, "o", lambda: o)][_n_(457704, "u", lambda: u)] = None
               _l_(457705)
               _n_(457706, "BoardObjs", lambda: BoardObjs)[_n_(457707, "o", lambda: o)+1][_n_(457708, "u", lambda: u)] = None
               _l_(457709)
               _n_(457710, "BoardObjs", lambda: BoardObjs)[_n_(457711, "o", lambda: o)+2][_n_(457712, "u", lambda: u)] = None
               _l_(457713)

def Draw(Board,BoardXYs):
   _l_(457751)

   DoAppend = True
   _l_(457719)
   _c_(457722, _a_(457721, _n_(457720, "Win", lambda: Win), "fill"), (255,255,255))
   _l_(457723)
   for y in _c_(457728, _n_(457724, "range", lambda: range), _c_(457727, _n_(457725, "len", lambda: len), _n_(457726, "BoardObjs", lambda: BoardObjs))):
      _l_(457745)

      for u in _c_(457733, _n_(457729, "range", lambda: range), _c_(457732, _n_(457730, "len", lambda: len), _n_(457731, "BoardObjs", lambda: BoardObjs)[1])):
         _l_(457744)

         if _n_(457734, "BoardObjs", lambda: BoardObjs)[_n_(457735, "y", lambda: y)][_n_(457736, "u", lambda: u)] != None:
            _l_(457743)

            _c_(457741, _a_(457740, _n_(457737, "BoardObjs", lambda: BoardObjs)[_n_(457738, "y", lambda: y)][_n_(457739, "u", lambda: u)], "Draw"))
            _l_(457742)
   _c_(457749, _a_(457748, _a_(457747, _n_(457746, "pygame", lambda: pygame), "display"), "update"))
   _l_(457750)

def Swap():
   _l_(457811)

   FirstClick = False
   _l_(457752)
   for i in _c_(457757, _n_(457753, "range", lambda: range), _c_(457756, _n_(457754, "len", lambda: len), _n_(457755, "BoardObjs", lambda: BoardObjs))):
      _l_(457810)

      for t in _c_(457762, _n_(457758, "range", lambda: range), _c_(457761, _n_(457759, "len", lambda: len), _n_(457760, "BoardObjs", lambda: BoardObjs)[1])):
         _l_(457809)

         if _n_(457763, "BoardObjs", lambda: BoardObjs)[_n_(457764, "i", lambda: i)][_n_(457765, "t", lambda: t)] != None:
            _l_(457791)

            if _a_(457769, _n_(457766, "BoardObjs", lambda: BoardObjs)[_n_(457767, "i", lambda: i)][_n_(457768, "t", lambda: t)], "CheckClick") and _n_(457770, "FirstClick", lambda: FirstClick) == True:
               _l_(457784)

               _n_(457771, "BoardObjs", lambda: BoardObjs)[_n_(457772, "num", lambda: num)][_n_(457773, "num2", lambda: num2)]=_n_(457774, "BoardObjs", lambda: BoardObjs)[_n_(457775, "i", lambda: i)][_n_(457776, "t", lambda: t)]
               _l_(457777)
               _n_(457778, "BoardObjs", lambda: BoardObjs)[_n_(457779, "i", lambda: i)][_n_(457780, "t", lambda: t)]=_n_(457781, "Buffer", lambda: Buffer)
               _l_(457782)
               FirstClick = False
               _l_(457783)
            _c_(457789, _n_(457785, "print", lambda: print), _n_(457786, "BoardObjs", lambda: BoardObjs)[_n_(457787, "i", lambda: i)][_n_(457788, "t", lambda: t)])
            _l_(457790)
         if _n_(457792, "BoardObjs", lambda: BoardObjs)[_n_(457793, "i", lambda: i)][_n_(457794, "t", lambda: t)] !=None:
            _l_(457808)

            if _a_(457798, _n_(457795, "BoardObjs", lambda: BoardObjs)[_n_(457796, "i", lambda: i)][_n_(457797, "t", lambda: t)], "CheckClick"):
               _l_(457807)

               Buffer  = _n_(457799, "BoardObjs", lambda: BoardObjs)[_n_(457800, "i", lambda: i)]
               _l_(457801)
               num =_n_(457802, "i", lambda: i)
               _l_(457803)
               num2 = _n_(457804, "t", lambda: t)
               _l_(457805)
               FirstClick = True
               _l_(457806)
#ZEROS - RED
#ONES - GREEN
#TWOS - BLUE

clock = _c_(457815, _a_(457814, _a_(457813, _n_(457812, "pygame", lambda: pygame), "time"), "Clock"))
_l_(457816)
def GameLoop():
   _l_(457855)

   run = True
   _l_(457817)
   while _n_(457818, "run", lambda: run):
      _l_(457846)

      _c_(457821, _a_(457820, _n_(457819, "clock", lambda: clock), "tick"), 60)
      _l_(457822)
      for event in _c_(457826, _a_(457825, _a_(457824, _n_(457823, "pygame", lambda: pygame), "event"), "get")):
         _l_(457833)

         if _a_(457828, _n_(457827, "event", lambda: event), "type") == _a_(457830, _n_(457829, "pygame", lambda: pygame), "QUIT"):
            _l_(457832)

            run = False
            _l_(457831)
      _c_(457836, _n_(457834, "CheckMatches", lambda: CheckMatches), _n_(457835, "Board", lambda: Board))
      _l_(457837)
      _c_(457841, _n_(457838, "Draw", lambda: Draw), _n_(457839, "Board", lambda: Board),_n_(457840, "BoardXYs", lambda: BoardXYs))
      _l_(457842)
      _c_(457844, _n_(457843, "Swap", lambda: Swap))
      _l_(457845)
   _c_(457849, _a_(457848, _n_(457847, "pygame", lambda: pygame), "quit"))
   _l_(457850)
   _c_(457853, _a_(457852, _n_(457851, "sys", lambda: sys), "exit"))
   _l_(457854)

if _n_(457856, "__name__", lambda: __name__) == "__main__":
   _l_(457860)

   _c_(457858, _n_(457857, "GameLoop", lambda: GameLoop))
   _l_(457859)
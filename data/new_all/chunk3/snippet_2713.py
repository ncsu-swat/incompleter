# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65445879/implementing-vkeyboard-in-tkinter-window-causing-error-attributeerror-int-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(560254)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk, ImageSequence
    _l_(560256)

except ImportError:
    pass
try:
    import pygame
    _l_(560258)

except ImportError:
    pass
try:
    import cv2
    _l_(560260)

except ImportError:
    pass
try:
    import numpy as np
    _l_(560262)

except ImportError:
    pass
try:
    import os
    _l_(560264)

except ImportError:
    pass


class tkinterApp(_n_(560265, "Tk", lambda: Tk)):
    _l_(560336)

      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):
        _l_(560309)

          
        # __init__ function for class Tk 
        _c_(560271, _a_(560267, _n_(560266, "Tk", lambda: Tk), "__init__"), _n_(560268, "self", lambda: self), *_n_(560269, "args", lambda: args), **_n_(560270, "kwargs", lambda: kwargs)) 
        _l_(560272) 
          
        # creating a container 
        container = _c_(560275, _n_(560273, "Frame", lambda: Frame), _n_(560274, "self", lambda: self))   
        _l_(560276)   
        _c_(560279, _a_(560278, _n_(560277, "container", lambda: container), "pack"), side = "top", fill = "both", expand = True)  
        _l_(560280)  
   
        # initializing frames to an empty array 
        _n_(560281, "self", lambda: self).frames = {}
        _l_(560282)
        
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (_n_(560283, "Page1", lambda: Page1),_n_(560284, "Page2", lambda: Page2)):
            _l_(560299)

   
            frame = _c_(560288, _n_(560285, "F", lambda: F), _n_(560286, "container", lambda: container), _n_(560287, "self", lambda: self)) 
            _l_(560289) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            _a_(560291, _n_(560290, "self", lambda: self), "frames")[_n_(560292, "F", lambda: F)] = _n_(560293, "frame", lambda: frame)  
            _l_(560294)  
   
            _c_(560297, _a_(560296, _n_(560295, "frame", lambda: frame), "grid"), row = 0, column = 0, sticky ="nsew")
            _l_(560298)
        _c_(560302, _a_(560301, _n_(560300, "self", lambda: self), "update"))
        _l_(560303)
        _c_(560307, _a_(560305, _n_(560304, "self", lambda: self), "show_frame"), _n_(560306, "Page1", lambda: Page1))
        _l_(560308)
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont):
        _l_(560335)

        if _n_(560310, "cont", lambda: cont) not in _a_(560312, _n_(560311, "self", lambda: self), "frames"):
            _l_(560322)

            _a_(560314, _n_(560313, "self", lambda: self), "frames")[_n_(560315, "cont", lambda: cont)] = _c_(560320, _n_(560316, "cont", lambda: cont), _a_(560318, _n_(560317, "self", lambda: self), "container"), _n_(560319, "self", lambda: self))
            _l_(560321)
        frame = _a_(560324, _n_(560323, "self", lambda: self), "frames")[_n_(560325, "cont", lambda: cont)]
        _l_(560326)
        _c_(560329, _a_(560328, _n_(560327, "frame", lambda: frame), "tkraise"))
        _l_(560330)
        _c_(560333, _a_(560332, _n_(560331, "frame", lambda: frame), "event_generate"), "<<ShowFrame>>")
        _l_(560334)

   

class Page1(_n_(560337, "Frame", lambda: Frame)):
    _l_(560929)

      
    def __init__(self, parent, controller):
        _l_(560358)

          
        _c_(560342, _a_(560339, _n_(560338, "Frame", lambda: Frame), "__init__"), _n_(560340, "self", lambda: self), _n_(560341, "parent", lambda: parent))
        _l_(560343)
        _n_(560344, "self", lambda: self).controller = _n_(560345, "controller", lambda: controller)
        _l_(560346)
        _c_(560350, _a_(560349, _a_(560348, _n_(560347, "pygame", lambda: pygame), "mixer"), "init"))
        _l_(560351)
        _c_(560356, _a_(560353, _n_(560352, "self", lambda: self), "bind"), "<<ShowFrame>>", _a_(560355, _n_(560354, "self", lambda: self), "myPage1"))
        _l_(560357)

    def myPage1(self,controller):
        _l_(560928)

        _c_(560362, _a_(560361, _n_(560359, "super", lambda: super)(_n_(560360, "Page1", lambda: Page1)), "__init__"))
        _l_(560363)

        canvas = _c_(560366, _n_(560364, "Canvas", lambda: Canvas), _n_(560365, "self", lambda: self),width=2300, height=900, bd=0, highlightthickness=0, relief='ridge')
        _l_(560367)
        _c_(560370, _a_(560369, _n_(560368, "canvas", lambda: canvas), "pack"))
        _l_(560371)

        canvas1 = _c_(560374, _n_(560372, "Canvas", lambda: Canvas), _n_(560373, "canvas", lambda: canvas), width=2000, height=500, bd=0, highlightthickness=0, relief='ridge')
        _l_(560375)
        _c_(560379, _a_(560377, _n_(560376, "canvas", lambda: canvas), "create_window"), 730,600,window=_n_(560378, "canvas1", lambda: canvas1))
        _l_(560380)

        _n_(560381, "self", lambda: self).background = _c_(560383, _n_(560382, "PhotoImage", lambda: PhotoImage), file="Images/background.png")
        _l_(560384)
        _c_(560389, _a_(560386, _n_(560385, "canvas", lambda: canvas), "create_image"), 525,425,image=_a_(560388, _n_(560387, "self", lambda: self), "background"), tags="B")
        _l_(560390)

        _n_(560391, "self", lambda: self).canvas_textbox = _c_(560395, _a_(560393, _n_(560392, "canvas", lambda: canvas), "create_text"), 290, 250, text='SOME TEXT', anchor=_n_(560394, "NW", lambda: NW),fill="cyan", font=('Orbitron',72))
        _l_(560396)

        def highlight(item):
            _l_(560419)

            # mark focused item.  note that this code recreates the
            # rectangle for each update, but that's fast enough for
            # this case.
            bbox = _c_(560400, _a_(560398, _n_(560397, "canvas", lambda: canvas), "bbox"), _n_(560399, "item", lambda: item))
            _l_(560401)
            _c_(560404, _a_(560403, _n_(560402, "canvas", lambda: canvas), "delete"), "highlight")
            _l_(560405)
            if _n_(560406, "bbox", lambda: bbox):
                _l_(560418)

                i = _c_(560410, _a_(560408, _n_(560407, "canvas", lambda: canvas), "create_rectangle"), _n_(560409, "bbox", lambda: bbox), fill="",
                    tag="highlight"
                    )
                _l_(560411)
                _c_(560416, _a_(560413, _n_(560412, "canvas", lambda: canvas), "lower"), _n_(560414, "i", lambda: i), _n_(560415, "item", lambda: item))
                _l_(560417)

        def has_focus():
            _l_(560424)

            aux = _c_(560422, _a_(560421, _n_(560420, "canvas", lambda: canvas), "focus"))
            _l_(560423)
            return aux

        def has_selection():
            _l_(560432)

            aux = _c_(560430, _a_(560427, _a_(560426, _n_(560425, "canvas", lambda: canvas), "tk"), "call"), _a_(560429, _n_(560428, "canvas", lambda: canvas), "_w"), 'select', 'item')
            _l_(560431)
            # hack to work around bug in Tkinter 1.101 (Python 1.5.1)
            return aux

        def set_focus(event):
            _l_(560466)

            _c_(560434, _n_(560433, "print", lambda: print), "set_focus")
            _l_(560435)
            if _c_(560439, _a_(560437, _n_(560436, "canvas", lambda: canvas), "type"), _n_(560438, "CURRENT", lambda: CURRENT)) != "text":
                _l_(560441)

                aux = ""
                _l_(560440)
                return aux

            _c_(560444, _n_(560442, "highlight", lambda: highlight), _n_(560443, "CURRENT", lambda: CURRENT))
            _l_(560445)

            # move focus to item
            _c_(560448, _a_(560447, _n_(560446, "canvas", lambda: canvas), "focus_set")) # move focus to canvas
            _l_(560449) # move focus to canvas
            _c_(560453, _a_(560451, _n_(560450, "canvas", lambda: canvas), "focus"), _n_(560452, "CURRENT", lambda: CURRENT)) # set focus to text item
            _l_(560454) # set focus to text item
            _c_(560458, _a_(560456, _n_(560455, "canvas", lambda: canvas), "select_from"), _n_(560457, "CURRENT", lambda: CURRENT), 0)
            _l_(560459)
            _c_(560464, _a_(560461, _n_(560460, "canvas", lambda: canvas), "select_to"), _n_(560462, "CURRENT", lambda: CURRENT), _n_(560463, "END", lambda: END))
            _l_(560465)


        def handle_key(event):
            _l_(560605)

            _c_(560468, _n_(560467, "print", lambda: print), "handle_key")
            _l_(560469)
            # widget-wide key dispatcher
            item = _c_(560471, _n_(560470, "has_focus", lambda: has_focus))
            _l_(560472)
            if not _n_(560473, "item", lambda: item):
                _l_(560488)

                aux = ""
                _l_(560474)
                return aux
            elif _a_(560476, _n_(560475, "event", lambda: event), "keysym") == 'Return':
                _l_(560487)

                _c_(560479, _a_(560478, _n_(560477, "canvas", lambda: canvas), "delete"), "highlight")
                _l_(560480)
                _c_(560485, _n_(560481, "print", lambda: print), _c_(560484, _a_(560483, _n_(560482, "canvas", lambda: canvas), "focus"), ""))
                _l_(560486)

            insert = _c_(560493, _a_(560490, _n_(560489, "canvas", lambda: canvas), "index"), _n_(560491, "item", lambda: item), _n_(560492, "INSERT", lambda: INSERT))
            _l_(560494)

            if _a_(560496, _n_(560495, "event", lambda: event), "char") >= " ":
                _l_(560604)

                # printable character
                if _c_(560498, _n_(560497, "has_selection", lambda: has_selection)):
                    _l_(560510)

                    _c_(560504, _a_(560500, _n_(560499, "canvas", lambda: canvas), "dchars"), _n_(560501, "item", lambda: item), _n_(560502, "SEL_FIRST", lambda: SEL_FIRST), _n_(560503, "SEL_LAST", lambda: SEL_LAST))
                    _l_(560505)
                    _c_(560508, _a_(560507, _n_(560506, "canvas", lambda: canvas), "select_clear"))
                    _l_(560509)
                _c_(560516, _a_(560512, _n_(560511, "canvas", lambda: canvas), "insert"), _n_(560513, "item", lambda: item), "insert", _a_(560515, _n_(560514, "event", lambda: event), "char"))
                _l_(560517)
                _c_(560520, _n_(560518, "highlight", lambda: highlight), _n_(560519, "item", lambda: item))
                _l_(560521)

            elif _a_(560523, _n_(560522, "event", lambda: event), "keysym") == "BackSpace":
                _l_(560603)

                if _c_(560525, _n_(560524, "has_selection", lambda: has_selection)):
                    _l_(560546)

                    _c_(560531, _a_(560527, _n_(560526, "canvas", lambda: canvas), "dchars"), _n_(560528, "item", lambda: item), _n_(560529, "SEL_FIRST", lambda: SEL_FIRST), _n_(560530, "SEL_LAST", lambda: SEL_LAST))
                    _l_(560532)
                    _c_(560535, _a_(560534, _n_(560533, "canvas", lambda: canvas), "select_clear"))
                    _l_(560536)
                else:
                    if _n_(560537, "insert", lambda: insert) > 0:
                        _l_(560545)

                        _c_(560543, _a_(560539, _n_(560538, "canvas", lambda: canvas), "dchars"), _n_(560540, "item", lambda: item), _n_(560541, "insert", lambda: insert)-1, _n_(560542, "insert", lambda: insert))
                        _l_(560544)
                _c_(560549, _n_(560547, "highlight", lambda: highlight), _n_(560548, "item", lambda: item))
                _l_(560550)

            # navigation
            elif _a_(560552, _n_(560551, "event", lambda: event), "keysym") == "Home":
                _l_(560602)

                _c_(560556, _a_(560554, _n_(560553, "canvas", lambda: canvas), "icursor"), _n_(560555, "item", lambda: item), 0)
                _l_(560557)
                _c_(560560, _a_(560559, _n_(560558, "canvas", lambda: canvas), "select_clear"))
                _l_(560561)
            elif _a_(560563, _n_(560562, "event", lambda: event), "keysym") == "End":
                _l_(560601)

                _c_(560568, _a_(560565, _n_(560564, "canvas", lambda: canvas), "icursor"), _n_(560566, "item", lambda: item), _n_(560567, "END", lambda: END))
                _l_(560569)
                _c_(560572, _a_(560571, _n_(560570, "canvas", lambda: canvas), "select_clear"))
                _l_(560573)
            elif _a_(560575, _n_(560574, "event", lambda: event), "keysym") == "Right":
                _l_(560600)

                _c_(560580, _a_(560577, _n_(560576, "canvas", lambda: canvas), "icursor"), _n_(560578, "item", lambda: item), _n_(560579, "insert", lambda: insert)+1)
                _l_(560581)
                _c_(560584, _a_(560583, _n_(560582, "canvas", lambda: canvas), "select_clear"))
                _l_(560585)
            elif _a_(560587, _n_(560586, "event", lambda: event), "keysym") == "Left":
                _l_(560599)

                _c_(560592, _a_(560589, _n_(560588, "canvas", lambda: canvas), "icursor"), _n_(560590, "item", lambda: item), _n_(560591, "insert", lambda: insert)-1)
                _l_(560593)
                _c_(560596, _a_(560595, _n_(560594, "canvas", lambda: canvas), "select_clear"))
                _l_(560597)

            else:
                pass # print event.keysym
                _l_(560598) # print event.keysym


        # standard bindings
        _c_(560609, _a_(560607, _n_(560606, "canvas", lambda: canvas), "bind"), "<Double-Button-1>", _n_(560608, "set_focus", lambda: set_focus))
        _l_(560610)
        _c_(560614, _a_(560612, _n_(560611, "canvas", lambda: canvas), "bind"), "<Key>", _n_(560613, "handle_key", lambda: handle_key))
        _l_(560615)

        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT',
            ' Space ',
        ]
        _l_(560616)
        curBut = [-1,-1]
        _l_(560617)
        buttonL = [[]]
        _l_(560618)
        #entry = Text(Keyboard_App, width=97, height=8)
        #entry.grid(row=0, columnspan=15)

        varRow = 1
        _l_(560619)
        varColumn = 0
        _l_(560620)

        def leftKey(event):
            _l_(560659)

            if _n_(560621, "curBut", lambda: curBut) == [-1,-1]:
                _l_(560658)

                _n_(560622, "curBut", lambda: curBut)[:] = [0,0]
                _l_(560623)
                _c_(560626, _a_(560625, _n_(560624, "buttonL", lambda: buttonL)[0][0], "configure"), highlightbackground='red')
                _l_(560627)
            elif _n_(560628, "curBut", lambda: curBut)[0] == 4:
                _l_(560657)

                _c_(560633, _a_(560632, _n_(560629, "buttonL", lambda: buttonL)[_n_(560630, "curBut", lambda: curBut)[0]][_n_(560631, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560634)
                _n_(560635, "curBut", lambda: curBut)[:] = [0,10]
                _l_(560636)
                _c_(560639, _a_(560638, _n_(560637, "buttonL", lambda: buttonL)[0][10], "configure"), highlightbackground='red')
                _l_(560640)
            else:
                _c_(560645, _a_(560644, _n_(560641, "buttonL", lambda: buttonL)[_n_(560642, "curBut", lambda: curBut)[0]][_n_(560643, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560646)
                _n_(560647, "curBut", lambda: curBut)[:] = [_n_(560648, "curBut", lambda: curBut)[0], (_n_(560649, "curBut", lambda: curBut)[1]-1)%11]
                _l_(560650)
                _c_(560655, _a_(560654, _n_(560651, "buttonL", lambda: buttonL)[_n_(560652, "curBut", lambda: curBut)[0]][_n_(560653, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560656)

        def rightKey(event):
            _l_(560698)

            if _n_(560660, "curBut", lambda: curBut) == [-1,-1]:
                _l_(560697)

                _n_(560661, "curBut", lambda: curBut)[:] = [0,0]
                _l_(560662)
                _c_(560665, _a_(560664, _n_(560663, "buttonL", lambda: buttonL)[0][0], "configure"), highlightbackground='red')
                _l_(560666)
            elif _n_(560667, "curBut", lambda: curBut)[0] == 4:
                _l_(560696)

                _c_(560672, _a_(560671, _n_(560668, "buttonL", lambda: buttonL)[_n_(560669, "curBut", lambda: curBut)[0]][_n_(560670, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560673)
                _n_(560674, "curBut", lambda: curBut)[:] = [0,0]
                _l_(560675)
                _c_(560678, _a_(560677, _n_(560676, "buttonL", lambda: buttonL)[0][0], "configure"), highlightbackground='red')
                _l_(560679)
            else:
                _c_(560684, _a_(560683, _n_(560680, "buttonL", lambda: buttonL)[_n_(560681, "curBut", lambda: curBut)[0]][_n_(560682, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560685)
                _n_(560686, "curBut", lambda: curBut)[:] = [_n_(560687, "curBut", lambda: curBut)[0], (_n_(560688, "curBut", lambda: curBut)[1]+1)%11]
                _l_(560689)
                _c_(560694, _a_(560693, _n_(560690, "buttonL", lambda: buttonL)[_n_(560691, "curBut", lambda: curBut)[0]][_n_(560692, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560695)

        def upKey(event):
            _l_(560740)

            if _n_(560699, "curBut", lambda: curBut) == [-1,-1]:
                _l_(560739)

                _n_(560700, "curBut", lambda: curBut)[:] = [0,0]
                _l_(560701)
                _c_(560704, _a_(560703, _n_(560702, "buttonL", lambda: buttonL)[0][0], "configure"), highlightbackground='red')
                _l_(560705)
            elif _n_(560706, "curBut", lambda: curBut)[0] == 0:
                _l_(560738)

                _c_(560711, _a_(560710, _n_(560707, "buttonL", lambda: buttonL)[_n_(560708, "curBut", lambda: curBut)[0]][_n_(560709, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560712)
                _n_(560713, "curBut", lambda: curBut)[:] = [(_n_(560714, "curBut", lambda: curBut)[0]-1)%5, 0]
                _l_(560715)
                _c_(560720, _a_(560719, _n_(560716, "buttonL", lambda: buttonL)[_n_(560717, "curBut", lambda: curBut)[0]][_n_(560718, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560721)
            else:
                _c_(560726, _a_(560725, _n_(560722, "buttonL", lambda: buttonL)[_n_(560723, "curBut", lambda: curBut)[0]][_n_(560724, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560727)
                _n_(560728, "curBut", lambda: curBut)[:] = [(_n_(560729, "curBut", lambda: curBut)[0]-1)%5, _n_(560730, "curBut", lambda: curBut)[1]]
                _l_(560731)
                _c_(560736, _a_(560735, _n_(560732, "buttonL", lambda: buttonL)[_n_(560733, "curBut", lambda: curBut)[0]][_n_(560734, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560737)

        def downKey(event):
            _l_(560782)

            if _n_(560741, "curBut", lambda: curBut) == [-1,-1]:
                _l_(560781)

                _n_(560742, "curBut", lambda: curBut)[:] = [0,0]
                _l_(560743)
                _c_(560746, _a_(560745, _n_(560744, "buttonL", lambda: buttonL)[0][0], "configure"), highlightbackground='red')
                _l_(560747)
            elif _n_(560748, "curBut", lambda: curBut)[0] == 3:
                _l_(560780)

                _c_(560753, _a_(560752, _n_(560749, "buttonL", lambda: buttonL)[_n_(560750, "curBut", lambda: curBut)[0]][_n_(560751, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560754)
                _n_(560755, "curBut", lambda: curBut)[:] = [(_n_(560756, "curBut", lambda: curBut)[0]+1)%5, 0]
                _l_(560757)
                _c_(560762, _a_(560761, _n_(560758, "buttonL", lambda: buttonL)[_n_(560759, "curBut", lambda: curBut)[0]][_n_(560760, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560763)
            else:
                _c_(560768, _a_(560767, _n_(560764, "buttonL", lambda: buttonL)[_n_(560765, "curBut", lambda: curBut)[0]][_n_(560766, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560769)
                _n_(560770, "curBut", lambda: curBut)[:] = [(_n_(560771, "curBut", lambda: curBut)[0]+1)%5, _n_(560772, "curBut", lambda: curBut)[1]]
                _l_(560773)
                _c_(560778, _a_(560777, _n_(560774, "buttonL", lambda: buttonL)[_n_(560775, "curBut", lambda: curBut)[0]][_n_(560776, "curBut", lambda: curBut)[1]%11], "configure"), highlightbackground='red')
                _l_(560779)

        def select(value, x, y):
            _l_(560844)

            if _n_(560783, "curBut", lambda: curBut) != [-1,-1]:
                _l_(560790)

                _c_(560788, _a_(560787, _n_(560784, "buttonL", lambda: buttonL)[_n_(560785, "curBut", lambda: curBut)[0]][_n_(560786, "curBut", lambda: curBut)[1]], "configure"), highlightbackground='#d9d9d9')
                _l_(560789)
            _n_(560791, "curBut", lambda: curBut)[:] = [_n_(560792, "x", lambda: x),_n_(560793, "y", lambda: y)]
            _l_(560794)
            _c_(560799, _a_(560798, _n_(560795, "buttonL", lambda: buttonL)[_n_(560796, "x", lambda: x)][_n_(560797, "y", lambda: y)], "configure"), highlightbackground='red')
            _l_(560800)
            if _n_(560801, "value", lambda: value) == "<-":
                _l_(560843)

                input = _c_(560805, _a_(560804, _a_(560803, _n_(560802, "self", lambda: self), "canvas_textbox"), "get"), "1.0", 'end-2c')
                _l_(560806)
                _c_(560811, _a_(560809, _a_(560808, _n_(560807, "self", lambda: self), "canvas_textbox"), "delete"), "1.0", _n_(560810, "END", lambda: END))
                _l_(560812)
                _c_(560818, _a_(560815, _a_(560814, _n_(560813, "self", lambda: self), "canvas_textbox"), "insert"), "1.0", _n_(560816, "input", lambda: input), _n_(560817, "END", lambda: END))
                _l_(560819)

            elif _n_(560820, "value", lambda: value) == " Space ":
                _l_(560842)

                _c_(560825, _a_(560823, _a_(560822, _n_(560821, "self", lambda: self), "canvas_textbox"), "insert"), _n_(560824, "END", lambda: END), ' ')
                _l_(560826)

            elif _n_(560827, "value", lambda: value) == "Tab":
                _l_(560841)

                _c_(560832, _a_(560830, _a_(560829, _n_(560828, "self", lambda: self), "canvas_textbox"), "insert"), _n_(560831, "END", lambda: END), '   ')
                _l_(560833)

            else:
                _c_(560839, _a_(560836, _a_(560835, _n_(560834, "self", lambda: self), "canvas_textbox"), "insert"), _n_(560837, "END", lambda: END), _n_(560838, "value", lambda: value))
                _l_(560840)

        for button in _n_(560845, "buttons", lambda: buttons):
            _l_(560907)

            if _n_(560846, "button", lambda: button) != " Space ":
                _l_(560872)

                but = _c_(560858, _n_(560847, "Button", lambda: Button), _n_(560848, "canvas1", lambda: canvas1), text=_n_(560849, "button", lambda: button), width=5, bg="#000000", fg="#ffffff", highlightthickness=4, 
                               activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                               pady=4, bd=4, command=lambda x=_n_(560850, "button", lambda: button), i=_n_(560851, "varRow", lambda: varRow)-1, j=_n_(560852, "varColumn", lambda: varColumn): _c_(560857, _n_(560853, "select", lambda: select), _n_(560854, "x", lambda: x), _n_(560855, "i", lambda: i), _n_(560856, "j", lambda: j)))
                _l_(560859)
                _c_(560864, _a_(560862, _n_(560860, "buttonL", lambda: buttonL)[_n_(560861, "varRow", lambda: varRow)-1], "append"), _n_(560863, "but", lambda: but))
                _l_(560865)
                _c_(560870, _a_(560867, _n_(560866, "but", lambda: but), "grid"), row=_n_(560868, "varRow", lambda: varRow), column=_n_(560869, "varColumn", lambda: varColumn))
                _l_(560871)

            if _n_(560873, "button", lambda: button) == " Space ":
                _l_(560897)

                but = _c_(560885, _n_(560874, "Button", lambda: Button), _n_(560875, "canvas1", lambda: canvas1), text=_n_(560876, "button", lambda: button), width=60, bg="#000000", fg="#ffffff", highlightthickness=4, 
                               activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=4,
                               pady=4, bd=4, command=lambda x=_n_(560877, "button", lambda: button), i=_n_(560878, "varRow", lambda: varRow)-1, j=_n_(560879, "varColumn", lambda: varColumn): _c_(560884, _n_(560880, "select", lambda: select), _n_(560881, "x", lambda: x), _n_(560882, "i", lambda: i), _n_(560883, "j", lambda: j)))
                _l_(560886)
                _c_(560891, _a_(560889, _n_(560887, "buttonL", lambda: buttonL)[_n_(560888, "varRow", lambda: varRow)-1], "append"), _n_(560890, "but", lambda: but))
                _l_(560892)
                _c_(560895, _a_(560894, _n_(560893, "but", lambda: but), "grid"), row=6, columnspan=16)
                _l_(560896)

            varColumn += 1
            _l_(560898)
            if _n_(560899, "varColumn", lambda: varColumn) > 10:
                _l_(560906)

                varColumn = 0
                _l_(560900)
                varRow += 1
                _l_(560901)
                _c_(560904, _a_(560903, _n_(560902, "buttonL", lambda: buttonL), "append"), [])
                _l_(560905)

        _c_(560911, _a_(560909, _n_(560908, "canvas1", lambda: canvas1), "bind"), '<Left>', _n_(560910, "leftKey", lambda: leftKey))
        _l_(560912)
        _c_(560916, _a_(560914, _n_(560913, "canvas1", lambda: canvas1), "bind"), '<Right>', _n_(560915, "rightKey", lambda: rightKey))
        _l_(560917)
        _c_(560921, _a_(560919, _n_(560918, "canvas1", lambda: canvas1), "bind"), '<Up>', _n_(560920, "upKey", lambda: upKey))
        _l_(560922)
        _c_(560926, _a_(560924, _n_(560923, "canvas1", lambda: canvas1), "bind"), '<Down>', _n_(560925, "downKey", lambda: downKey))
        _l_(560927)

class Page2(_n_(560930, "Frame", lambda: Frame)):
    _l_(560975)

    def __init__(self, parent, controller):
        _l_(560946)

        _c_(560935, _a_(560932, _n_(560931, "Frame", lambda: Frame), "__init__"), _n_(560933, "self", lambda: self), _n_(560934, "parent", lambda: parent))
        _l_(560936)
        _n_(560937, "self", lambda: self).controller = _n_(560938, "controller", lambda: controller)
        _l_(560939)
        _c_(560944, _a_(560941, _n_(560940, "self", lambda: self), "bind"), "<<ShowFrame>>", _a_(560943, _n_(560942, "self", lambda: self), "myPage2"))
        _l_(560945)


    def myPage2(self,controller):
        _l_(560974)

        _c_(560950, _a_(560949, _n_(560947, "super", lambda: super)(_n_(560948, "Page2", lambda: Page2)), "__init__"))
        _l_(560951)

        canvas = _c_(560954, _n_(560952, "Canvas", lambda: Canvas), _n_(560953, "self", lambda: self),width=2300, height=900, bd=0, highlightthickness=0, relief='ridge')
        _l_(560955)
        _c_(560958, _a_(560957, _n_(560956, "canvas", lambda: canvas), "pack"))
        _l_(560959)

        _n_(560960, "self", lambda: self).background = _c_(560962, _n_(560961, "PhotoImage", lambda: PhotoImage), file="Images/background.png")
        _l_(560963)
        _c_(560968, _a_(560965, _n_(560964, "canvas", lambda: canvas), "create_image"), 525,425,image=_a_(560967, _n_(560966, "self", lambda: self), "background"), tags="B")
        _l_(560969)

        _c_(560972, _a_(560971, _n_(560970, "canvas", lambda: canvas), "create_text"), 140,376, fill="cyan",text="Second Frame")
        _l_(560973)

app = _c_(560977, _n_(560976, "tkinterApp", lambda: tkinterApp))
_l_(560978)
_c_(560981, _a_(560980, _n_(560979, "app", lambda: app), "title"), "Test")
_l_(560982)
_c_(560985, _a_(560984, _n_(560983, "app", lambda: app), "mainloop")) 
_l_(560986) 
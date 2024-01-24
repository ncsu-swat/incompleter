# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42201924/getting-an-attributeerror-when-attempting-to-assign-intvar-to-a-variable
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
Created on Sun Jan 22 14:47:36 2017

@author: Jose Chong
"""
try:
    import json
    _l_(626252)

except ImportError:
    pass
try:
    _l_(626258)

    import tkinter as tk
    _l_(626253)
except _n_(626254, "ImportError", lambda: ImportError):
    _l_(626257)

    try:
        import Tkinter as tk
        _l_(626256)

    except ImportError:
        pass
try:
    import os
    _l_(626260)

except ImportError:
    pass
try:
    import pymsgbox
    _l_(626262)

except ImportError:
    pass

filepath = _c_(626266, _a_(626265, _a_(626264, _n_(626263, "os", lambda: os), "path"), "expanduser"), r'~\Documents\joseDzirehChongToDoList\toDoListSaveFile.json')
_l_(626267)

checkboxList = []
_l_(626268)

def checkSaveFile():
    _l_(626354)


    def checkExistenceOfSaveFile():
        _l_(626302)

        if not _c_(626276, _a_(626271, _a_(626270, _n_(626269, "os", lambda: os), "path"), "isdir"), _c_(626275, _a_(626274, _a_(626273, _n_(626272, "os", lambda: os), "path"), "expanduser"), r'~\Documents\joseDzirehChongToDoList')):
            _l_(626285)

            _c_(626283, _a_(626278, _n_(626277, "os", lambda: os), "makedirs"), _c_(626282, _a_(626281, _a_(626280, _n_(626279, "os", lambda: os), "path"), "expanduser"), r'~\Documents\joseDzirehChongToDoList'), 777)
            _l_(626284)

        if not _c_(626290, _a_(626288, _a_(626287, _n_(626286, "os", lambda: os), "path"), "isfile"), _n_(626289, "filepath", lambda: filepath)):
            _l_(626301)

            _c_(626293, _n_(626291, "open", lambda: open), _n_(626292, "filepath", lambda: filepath), 'w')
            _l_(626294)
            _c_(626299, _a_(626298, _c_(626297, _n_(626295, "open", lambda: open), _n_(626296, "filepath", lambda: filepath)), "close"))
            _l_(626300)

    def checkIfSaveFileIsEmpty():
        _l_(626329)

        global checkboxList
        _l_(626303)
        if _c_(626308, _a_(626306, _a_(626305, _n_(626304, "os", lambda: os), "path"), "getsize"), _n_(626307, "filepath", lambda: filepath)) == 0:
            _l_(626319)

            with _c_(626311, _n_(626309, "open", lambda: open), _n_(626310, "filepath", lambda: filepath), 'w') as outfile:
                _l_(626318)

                _c_(626316, _a_(626313, _n_(626312, "json", lambda: json), "dump"), _n_(626314, "checkboxList", lambda: checkboxList), _n_(626315, "outfile", lambda: outfile))
                _l_(626317)


        with _c_(626322, _n_(626320, "open", lambda: open), _n_(626321, "filepath", lambda: filepath)) as infile:
            _l_(626328)

            checkboxList = _c_(626326, _a_(626324, _n_(626323, "json", lambda: json), "load"), _n_(626325, "infile", lambda: infile))
            _l_(626327)
    _c_(626331, _n_(626330, "checkExistenceOfSaveFile", lambda: checkExistenceOfSaveFile))
    _l_(626332)
    _c_(626334, _n_(626333, "checkIfSaveFileIsEmpty", lambda: checkIfSaveFileIsEmpty))
    _l_(626335)
    try:
        _l_(626353)

        _c_(626338, _n_(626336, "open", lambda: open), _n_(626337, "filepath", lambda: filepath), 'w')
        _l_(626339)
        _c_(626344, _a_(626343, _c_(626342, _n_(626340, "open", lambda: open), _n_(626341, "filepath", lambda: filepath)), "close"))
        _l_(626345)
    except (_n_(626346, "IOError", lambda: IOError), _n_(626347, "ValueError", lambda: ValueError)):
        _l_(626352)


        _c_(626350, _a_(626349, _n_(626348, "pymsgbox", lambda: pymsgbox), "alert"), """You're not supposed to see this message ever. If you do, that means your save file is either missing or corrupted, and my methods of stopping that have failed. Please email me at 'josedzirehchong@gmail.com' with a copy of your save file so I can tell what went wrong.

Click the button below to exit, the red button in the corner doesn't work.""", 'Broken Save File')
        _l_(626351)

_c_(626356, _n_(626355, "checkSaveFile", lambda: checkSaveFile))
_l_(626357)

var = _c_(626360, _a_(626359, _n_(626358, "tk", lambda: tk), "IntVar"))
_l_(626361)

def loadToJSON():
    _l_(626372)

    with _c_(626364, _n_(626362, "open", lambda: open), _n_(626363, "filepath", lambda: filepath), 'w') as outfile:
        _l_(626371)

        _c_(626369, _a_(626366, _n_(626365, "json", lambda: json), "dump"), _n_(626367, "checkboxList", lambda: checkboxList), _n_(626368, "outfile", lambda: outfile))
        _l_(626370)

class CheckboxRow(_a_(626374, _n_(626373, "tk", lambda: tk), "Frame")):
    _l_(626454)

    def __init__(self, master, text):
        _l_(626428)

        _n_(626375, "self", lambda: self).text = _n_(626376, "text", lambda: text)
        _l_(626377)
        _c_(626383, _a_(626380, _a_(626379, _n_(626378, "tk", lambda: tk), "Frame"), "__init__"), _n_(626381, "self", lambda: self), _n_(626382, "master", lambda: master))
        _l_(626384)
        checkbox = _c_(626390, _a_(626386, _n_(626385, "tk", lambda: tk), "Checkbutton"), _n_(626387, "self", lambda: self), text=_n_(626388, "text", lambda: text), variable=_n_(626389, "var", lambda: var))
        _l_(626391)
        _c_(626396, _a_(626393, _n_(626392, "checkbox", lambda: checkbox), "pack"), side=_a_(626395, _n_(626394, "tk", lambda: tk), "LEFT"))
        _l_(626397)

        deleteItem = _c_(626403, _a_(626399, _n_(626398, "tk", lambda: tk), "Button"), _n_(626400, "self", lambda: self), text="x", bg="red", fg="white",
                                activebackground="white", activeforeground="red",
                                command=_a_(626402, _n_(626401, "self", lambda: self), "destroyCheckbox"))
        _l_(626404)
        _c_(626409, _a_(626406, _n_(626405, "deleteItem", lambda: deleteItem), "pack"), side=_a_(626408, _n_(626407, "tk", lambda: tk), "RIGHT"))
        _l_(626410)
        newItem = [_a_(626412, _n_(626411, "self", lambda: self), "text"), _c_(626415, _a_(626414, _n_(626413, "var", lambda: var), "get"))]
        _l_(626416)
        _c_(626423, _a_(626421, _a_(626420, _a_(626419, _a_(626418, _n_(626417, "self", lambda: self), "master"), "master"), "checkboxList"), "append"), _n_(626422, "newItem", lambda: newItem))
        _l_(626424)
        _c_(626426, _n_(626425, "loadToJSON", lambda: loadToJSON))
        _l_(626427)

    def destroyCheckbox(self, text):
        _l_(626453)

        _n_(626429, "self", lambda: self).text = _n_(626430, "text", lambda: text)
        _l_(626431)
        newItem = [_a_(626433, _n_(626432, "self", lambda: self), "text"), _c_(626436, _a_(626435, _n_(626434, "var", lambda: var), "get"))]
        _l_(626437)
        _c_(626444, _a_(626442, _a_(626441, _a_(626440, _a_(626439, _n_(626438, "self", lambda: self), "master"), "master"), "checkboxList"), "remove"), _n_(626443, "newItem", lambda: newItem))
        _l_(626445)
        _c_(626448, _a_(626447, _n_(626446, "self", lambda: self), "destroy"))
        _l_(626449)
        _c_(626451, _n_(626450, "loadToJSON", lambda: loadToJSON))
        _l_(626452)


class CheckboxArea(_a_(626456, _n_(626455, "tk", lambda: tk), "Frame")):
    _l_(626469)

    def add(self, name):
        _l_(626468)

        row = _c_(626460, _n_(626457, "CheckboxRow", lambda: CheckboxRow), _n_(626458, "self", lambda: self), _n_(626459, "name", lambda: name))
        _l_(626461)
        _c_(626466, _a_(626463, _n_(626462, "row", lambda: row), "pack"), fill=_a_(626465, _n_(626464, "tk", lambda: tk), "X"))
        _l_(626467)

class InputStuff(_a_(626471, _n_(626470, "tk", lambda: tk), "Frame")):
    _l_(626553)

    def __init__(self, master=None, **kwargs):
        _l_(626535)

        _c_(626478, _a_(626474, _a_(626473, _n_(626472, "tk", lambda: tk), "Frame"), "__init__"), _n_(626475, "self", lambda: self), _n_(626476, "master", lambda: master), **_n_(626477, "kwargs", lambda: kwargs))
        _l_(626479)

        prompt = _c_(626483, _a_(626481, _n_(626480, "tk", lambda: tk), "Label"), _n_(626482, "self", lambda: self), text="What do you want your checkbox to be for?")
        _l_(626484)
        _c_(626487, _a_(626486, _n_(626485, "prompt", lambda: prompt), "pack"))
        _l_(626488)

        bottomInput = _c_(626492, _a_(626490, _n_(626489, "tk", lambda: tk), "Frame"), _n_(626491, "self", lambda: self))
        _l_(626493)
        _n_(626494, "self", lambda: self).entry = _c_(626498, _a_(626496, _n_(626495, "tk", lambda: tk), "Entry"), _n_(626497, "bottomInput", lambda: bottomInput), bd=3)
        _l_(626499)
        _c_(626505, _a_(626502, _a_(626501, _n_(626500, "self", lambda: self), "entry"), "pack"), side=_a_(626504, _n_(626503, "tk", lambda: tk), "LEFT"))
        _l_(626506)
        buttonConfirm = _c_(626512, _a_(626508, _n_(626507, "tk", lambda: tk), "Button"), _n_(626509, "bottomInput", lambda: bottomInput), text="Confirm", command=_a_(626511, _n_(626510, "self", lambda: self), "drawCheckbox"))
        _l_(626513)
        _c_(626518, _a_(626515, _n_(626514, "buttonConfirm", lambda: buttonConfirm), "pack"), side=_a_(626517, _n_(626516, "tk", lambda: tk), "LEFT"))
        _l_(626519)
        _c_(626522, _a_(626521, _n_(626520, "bottomInput", lambda: bottomInput), "pack"))
        _l_(626523)

        buttonDone = _c_(626529, _a_(626525, _n_(626524, "tk", lambda: tk), "Button"), _n_(626526, "self", lambda: self), text = "Close Input", command=_a_(626528, _n_(626527, "master", lambda: master), "hideInputStuff"))
        _l_(626530)
        _c_(626533, _a_(626532, _n_(626531, "buttonDone", lambda: buttonDone), "pack"))
        _l_(626534)

    def drawCheckbox(self, event=None):
        _l_(626552)

        _c_(626543, _a_(626538, _a_(626537, _n_(626536, "self", lambda: self), "master"), "add"), _c_(626542, _a_(626541, _a_(626540, _n_(626539, "self", lambda: self), "entry"), "get")))
        _l_(626544)
        _c_(626550, _a_(626547, _a_(626546, _n_(626545, "self", lambda: self), "entry"), "delete"), 0, _a_(626549, _n_(626548, "tk", lambda: tk), "END"))
        _l_(626551)

class MainWindow(_a_(626555, _n_(626554, "tk", lambda: tk), "Frame")):
    _l_(626701)

    def __init__(self, master=None, **kwargs):
        _l_(626599)

        _c_(626562, _a_(626558, _a_(626557, _n_(626556, "tk", lambda: tk), "Frame"), "__init__"), _n_(626559, "self", lambda: self), _n_(626560, "master", lambda: master), **_n_(626561, "kwargs", lambda: kwargs))
        _l_(626563)

        _n_(626564, "self", lambda: self).checkboxList = []
        _l_(626565)

        _n_(626566, "self", lambda: self).checkboxArea = _c_(626569, _n_(626567, "CheckboxArea", lambda: CheckboxArea), _n_(626568, "self", lambda: self))
        _l_(626570)
        _c_(626576, _a_(626573, _a_(626572, _n_(626571, "self", lambda: self), "checkboxArea"), "pack"), fill=_a_(626575, _n_(626574, "tk", lambda: tk), "X"))
        _l_(626577)

        _n_(626578, "self", lambda: self).inputStuff = _c_(626581, _n_(626579, "InputStuff", lambda: InputStuff), _n_(626580, "self", lambda: self))
        _l_(626582)
        _n_(626583, "self", lambda: self).addButton = _c_(626589, _a_(626585, _n_(626584, "tk", lambda: tk), "Button"), _n_(626586, "self", lambda: self), text="Add Item", command=_a_(626588, _n_(626587, "self", lambda: self), "showInputStuff"))
        _l_(626590)

        _c_(626593, _a_(626592, _n_(626591, "self", lambda: self), "hideInputStuff")) # start with "add" button active
        _l_(626594) # start with "add" button active

        _c_(626597, _a_(626596, _n_(626595, "self", lambda: self), "load"))
        _l_(626598)

    def load(self):
        _l_(626646)

        for savedCheckbox in _n_(626600, "checkboxList", lambda: checkboxList):
            _l_(626645)

            checkboxRow = _c_(626604, _a_(626602, _n_(626601, "tk", lambda: tk), "Frame"), _n_(626603, "checkboxArea", lambda: checkboxArea))
            _l_(626605)
            _c_(626610, _a_(626607, _n_(626606, "checkboxRow", lambda: checkboxRow), "pack"), fill=_a_(626609, _n_(626608, "tk", lambda: tk), "X"))
            _l_(626611)
            checkbox1 = _c_(626617, _a_(626613, _n_(626612, "tk", lambda: tk), "Checkbutton"), _n_(626614, "checkboxRow", lambda: checkboxRow), text=_n_(626615, "savedCheckbox", lambda: savedCheckbox)[0], variable=_n_(626616, "var", lambda: var))
            _l_(626618)
            _c_(626623, _a_(626620, _n_(626619, "checkbox1", lambda: checkbox1), "pack"), side=_a_(626622, _n_(626621, "tk", lambda: tk), "LEFT"))
            _l_(626624)
            deleteItem = _c_(626634, _a_(626626, _n_(626625, "tk", lambda: tk), "Button"), _n_(626627, "checkboxRow", lambda: checkboxRow), text="x", bg="red", fg="white",
                                activebackground="white", activeforeground="red",
                                command=lambda c=_n_(626628, "savedCheckbox", lambda: savedCheckbox), r=_n_(626629, "checkboxRow", lambda: checkboxRow): _c_(626633, _n_(626630, "destroyCheckbox", lambda: destroyCheckbox), _n_(626631, "c", lambda: c), _n_(626632, "r", lambda: r)))
            _l_(626635)
            _c_(626640, _a_(626637, _n_(626636, "deleteItem", lambda: deleteItem), "pack"), side=_a_(626639, _n_(626638, "tk", lambda: tk), "RIGHT"))
            _l_(626641)

            _c_(626643, _n_(626642, "loadToJSON", lambda: loadToJSON))
            _l_(626644)

    def add(self, name):
        _l_(626659)

        _c_(626651, _a_(626649, _a_(626648, _n_(626647, "self", lambda: self), "checkbox_area"), "add"), _n_(626650, "name", lambda: name))
        _l_(626652)
        _c_(626657, _a_(626655, _a_(626654, _n_(626653, "self", lambda: self), "checkboxList"), "append"), _n_(626656, "name", lambda: name))
        _l_(626658)

    def showInputStuff(self):
        _l_(626684)

        _c_(626663, _a_(626662, _a_(626661, _n_(626660, "self", lambda: self), "addButton"), "pack_forget"))
        _l_(626664)
        _c_(626668, _a_(626667, _a_(626666, _n_(626665, "self", lambda: self), "input_stuff"), "pack"))
        _l_(626669)
        _c_(626674, _a_(626673, _a_(626672, _a_(626671, _n_(626670, "self", lambda: self), "input_stuff"), "entry"), "focus"))
        _l_(626675)
        _c_(626682, _a_(626678, _a_(626677, _n_(626676, "self", lambda: self), "master"), "bind"), '<Return>', _a_(626681, _a_(626680, _n_(626679, "self", lambda: self), "input_stuff"), "drawCheckbox"))
        _l_(626683)

    def hideInputStuff(self):
        _l_(626700)

        _c_(626688, _a_(626687, _a_(626686, _n_(626685, "self", lambda: self), "inputStuff"), "pack_forget"))
        _l_(626689)
        _c_(626693, _a_(626692, _a_(626691, _n_(626690, "self", lambda: self), "addButton"), "pack"))
        _l_(626694)
        _c_(626698, _a_(626697, _a_(626696, _n_(626695, "self", lambda: self), "master"), "unbind"), '<Return>')
        _l_(626699)

def main():
    _l_(626728)

    master = _c_(626704, _a_(626703, _n_(626702, "tk", lambda: tk), "Tk"))
    _l_(626705)
    _c_(626708, _a_(626707, _n_(626706, "master", lambda: master), "title"), "To-Do List (with saving!)")
    _l_(626709)
    _c_(626712, _a_(626711, _n_(626710, "master", lambda: master), "geometry"), "300x300")
    _l_(626713)
    win = _c_(626716, _n_(626714, "MainWindow", lambda: MainWindow), _n_(626715, "master", lambda: master))
    _l_(626717)
    _c_(626722, _a_(626719, _n_(626718, "win", lambda: win), "pack"), fill=_a_(626721, _n_(626720, "tk", lambda: tk), "X"))
    _l_(626723)
    _c_(626726, _a_(626725, _n_(626724, "master", lambda: master), "mainloop"))
    _l_(626727)

if _n_(626729, "__name__", lambda: __name__) == "__main__":
    _l_(626733)

    _c_(626731, _n_(626730, "main", lambda: main))
    _l_(626732)
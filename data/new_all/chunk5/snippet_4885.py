# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42714591/typeerror-unsupported-operand-types-for-int-and-str-when-making-grid
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(669198)

except ImportError:
    pass
try:
    import math
    _l_(669200)

except ImportError:
    pass
try:
    import random
    _l_(669202)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(669204)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(669206)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(669208)

except ImportError:
    pass



GridSizeSetByUser = '8x8'
_l_(669209)
choicesRows = ['8', '10', '12', '14']
_l_(669210)
v = _n_(669211, "choicesRows", lambda: choicesRows)[0]
_l_(669212)
choicesColumns = ['8', '10', '12', '14']
_l_(669213)
v2 = _n_(669214, "choicesColumns", lambda: choicesColumns)[0]
_l_(669215)

GridRows = 9
_l_(669216)
GridColumns = 9
_l_(669217)


def getRows():
    _l_(669227)

    global GridRows
    _l_(669218)
    GridRows = _c_(669221, _a_(669220, _n_(669219, "GridRowSpinbox", lambda: GridRowSpinbox), "get"))
    _l_(669222)
    _c_(669225, _n_(669223, "print", lambda: print), _n_(669224, "GridRows", lambda: GridRows))
    _l_(669226)

def getColumns():
    _l_(669237)

    global GridColumns
    _l_(669228)
    GridColumns = _c_(669231, _a_(669230, _n_(669229, "GridColumnSpinbox", lambda: GridColumnSpinbox), "get"))
    _l_(669232)
    _c_(669235, _n_(669233, "print", lambda: print), _n_(669234, "GridColumns", lambda: GridColumns))
    _l_(669236)

def Treasure_Hunt_Window():
    _l_(669259)

    THunt = _c_(669240, _a_(669239, _n_(669238, "tk", lambda: tk), "Tk"))
    _l_(669241)
    _c_(669244, _a_(669243, _n_(669242, "THunt", lambda: THunt), "title"), "Treasure Hunt")
    _l_(669245)
    THuntInstructions = "Find the treasure hidden deep in the sand!Use ye arrow keys to move around,\n\n then press Space to search that spot! Keep searching until ye find it!"
    _l_(669246)
    board = _c_(669249, _n_(669247, "GameBoard", lambda: GameBoard), _n_(669248, "THunt", lambda: THunt))
    _l_(669250)
    _c_(669253, _a_(669252, _n_(669251, "board", lambda: board), "pack"), side="top", fill="both", expand="true", padx=4, pady=4)
    _l_(669254)
    _c_(669257, _a_(669256, _n_(669255, "THunt", lambda: THunt), "mainloop"))
    _l_(669258)

def Settings_Window():
    _l_(669367)

    Settings = _c_(669262, _a_(669261, _n_(669260, "tk", lambda: tk), "Tk"))
    _l_(669263)
    _c_(669266, _a_(669265, _n_(669264, "Settings", lambda: Settings), "title"), "Settings")
    _l_(669267)
    SettingsWelcome = _c_(669271, _a_(669269, _n_(669268, "tk", lambda: tk), "Label"), _n_(669270, "Settings", lambda: Settings), text='Settings Menu', width=50, fg="magenta")
    _l_(669272)
    SettingsGridSize = _c_(669276, _a_(669274, _n_(669273, "tk", lambda: tk), "Label"), _n_(669275, "Settings", lambda: Settings), text='Grid Size:', width =50, fg="magenta")
    _l_(669277)
    global mystring
    _l_(669278)
    mystring = _c_(669280, _n_(669279, "StringVar", lambda: StringVar))
    _l_(669281)
    global mystring2
    _l_(669282)
    mystring2 = _c_(669284, _n_(669283, "StringVar", lambda: StringVar))
    _l_(669285)
    global GridRowSpinbox
    _l_(669286)
    GridRowSpinbox = _c_(669291, _n_(669287, "Spinbox", lambda: Spinbox), _n_(669288, "Settings", lambda: Settings), values=_n_(669289, "choicesRows", lambda: choicesRows), textvariable=_n_(669290, "mystring", lambda: mystring), width=50, state="readonly", fg="magenta")
    _l_(669292)
    SaveRowSize = _c_(669297, _a_(669294, _n_(669293, "tk", lambda: tk), "Button"), _n_(669295, "Settings", lambda: Settings), text='Save row size for grid', width=50, fg="magenta", command = _n_(669296, "getRows", lambda: getRows))
    _l_(669298)
    global GridColumnSpinbox
    _l_(669299)
    GridColumnSpinbox = _c_(669304, _n_(669300, "Spinbox", lambda: Spinbox), _n_(669301, "Settings", lambda: Settings), values=_n_(669302, "choicesColumns", lambda: choicesColumns), textvariable=_n_(669303, "mystring2", lambda: mystring2), state="readonly", width=50, fg="magenta")
    _l_(669305)
    SaveColumnSize = _c_(669310, _a_(669307, _n_(669306, "tk", lambda: tk), "Button"), _n_(669308, "Settings", lambda: Settings), text='Save column size for grid', width=50, fg="magenta", command = _n_(669309, "getColumns", lambda: getColumns))
    _l_(669311)
    SettingsBandits = _c_(669315, _a_(669313, _n_(669312, "tk", lambda: tk), "Label"), _n_(669314, "Settings", lambda: Settings), text='Amount of Bandits:', width =50, fg="magenta")
    _l_(669316)
    BanditAmount = _c_(669320, _a_(669318, _n_(669317, "tk", lambda: tk), "Entry"), _n_(669319, "Settings", lambda: Settings), width = 50, fg="magenta")
    _l_(669321)
    SettingsBandits = _c_(669325, _a_(669323, _n_(669322, "tk", lambda: tk), "Label"), _n_(669324, "Settings", lambda: Settings), text='Amount of Treasure Chests (up to 64)', width =50, fg="magenta")
    _l_(669326)
    _c_(669330, _a_(669328, _n_(669327, "SettingsWelcome", lambda: SettingsWelcome), "pack"), fill=_n_(669329, "X", lambda: X))
    _l_(669331)
    _c_(669335, _a_(669333, _n_(669332, "SettingsGridSize", lambda: SettingsGridSize), "pack"), fill=_n_(669334, "X", lambda: X))
    _l_(669336)
    _c_(669340, _a_(669338, _n_(669337, "GridRowSpinbox", lambda: GridRowSpinbox), "pack"), fill=_n_(669339, "X", lambda: X))
    _l_(669341)
    _c_(669345, _a_(669343, _n_(669342, "SaveRowSize", lambda: SaveRowSize), "pack"), fill=_n_(669344, "X", lambda: X))
    _l_(669346)
    _c_(669350, _a_(669348, _n_(669347, "GridColumnSpinbox", lambda: GridColumnSpinbox), "pack"), fill=_n_(669349, "X", lambda: X))
    _l_(669351)
    _c_(669355, _a_(669353, _n_(669352, "SaveColumnSize", lambda: SaveColumnSize), "pack"), fill=_n_(669354, "X", lambda: X))
    _l_(669356)
    _c_(669360, _a_(669358, _n_(669357, "SettingsBandits", lambda: SettingsBandits), "pack"), fill=_n_(669359, "X", lambda: X))
    _l_(669361)
    _c_(669365, _a_(669363, _n_(669362, "BanditAmount", lambda: BanditAmount), "pack"), fill=_n_(669364, "X", lambda: X))
    _l_(669366)



def main():
    _l_(669424)

    root = _c_(669370, _a_(669369, _n_(669368, "tk", lambda: tk), "Tk"))
    _l_(669371)
    _c_(669374, _a_(669373, _n_(669372, "root", lambda: root), "title"), "Menu")
    _l_(669375)
    WelcomeButton = _c_(669379, _a_(669377, _n_(669376, "tk", lambda: tk), "Label"), _n_(669378, "root", lambda: root), text='Welcome to the menu!', width=50, height=2, fg="magenta")
    _l_(669380)
    _c_(669384, _a_(669382, _n_(669381, "WelcomeButton", lambda: WelcomeButton), "pack"), fill=_n_(669383, "X", lambda: X))
    _l_(669385)
    StartButton = _c_(669390, _a_(669387, _n_(669386, "tk", lambda: tk), "Button"), _n_(669388, "root", lambda: root), text='Start treasure hunting!', width=50, fg="magenta", command = _n_(669389, "Treasure_Hunt_Window", lambda: Treasure_Hunt_Window))
    _l_(669391)
    _c_(669395, _a_(669393, _n_(669392, "StartButton", lambda: StartButton), "pack"), fill=_n_(669394, "X", lambda: X))
    _l_(669396)
    SettingsButton = _c_(669401, _a_(669398, _n_(669397, "tk", lambda: tk), "Button"), _n_(669399, "root", lambda: root), text='''Change the settings of the treasure hunting game.
This includes the grid size.''', width=50, fg="magenta", command = _n_(669400, "Settings_Window", lambda: Settings_Window))
    _l_(669402)
    _c_(669406, _a_(669404, _n_(669403, "SettingsButton", lambda: SettingsButton), "pack"), fill=_n_(669405, "X", lambda: X))
    _l_(669407)
    QuitButton = _c_(669413, _a_(669409, _n_(669408, "tk", lambda: tk), "Button"), _n_(669410, "root", lambda: root), text='Exit the program', width=50, fg="magenta", command = _a_(669412, _n_(669411, "root", lambda: root), "destroy"))# display message in a child window.
    _l_(669414)# display message in a child window.
    _c_(669418, _a_(669416, _n_(669415, "QuitButton", lambda: QuitButton), "pack"), fill=_n_(669417, "X", lambda: X))
    _l_(669419)
    _c_(669422, _a_(669421, _n_(669420, "root", lambda: root), "mainloop"))
    _l_(669423)

def teststuff():
    _l_(669433)

    _c_(669427, _n_(669425, "print", lambda: print), _n_(669426, "GridRows", lambda: GridRows))
    _l_(669428)
    _c_(669431, _n_(669429, "print", lambda: print), _n_(669430, "GridColumns", lambda: GridColumns))
    _l_(669432)

class GameBoard(_a_(669435, _n_(669434, "tk", lambda: tk), "Frame")):
    _l_(669594)

    def __init__(self, parent, size=48, color1="white", color2="black"):
        _l_(669487)

        '''size is the size of a square, in pixels'''
        _l_(669436)

        _n_(669437, "self", lambda: self).rows = _n_(669438, "GridRows", lambda: GridRows)
        _l_(669439)
        _n_(669440, "self", lambda: self).columns = _n_(669441, "GridColumns", lambda: GridColumns)
        _l_(669442)
        _n_(669443, "self", lambda: self).size = _n_(669444, "size", lambda: size)
        _l_(669445)
        _n_(669446, "self", lambda: self).color1 = _n_(669447, "color1", lambda: color1)
        _l_(669448)
        _n_(669449, "self", lambda: self).color2 = _n_(669450, "color2", lambda: color2)
        _l_(669451)
        _n_(669452, "self", lambda: self).pieces = {}
        _l_(669453)

        canvas_width = _n_(669454, "GridColumns", lambda: GridColumns) * _n_(669455, "size", lambda: size)
        _l_(669456)
        canvas_height = _n_(669457, "GridRows", lambda: GridRows) * _n_(669458, "size", lambda: size)
        _l_(669459)

        _c_(669465, _a_(669462, _a_(669461, _n_(669460, "tk", lambda: tk), "Frame"), "__init__"), _n_(669463, "self", lambda: self), _n_(669464, "parent", lambda: parent))
        _l_(669466)
        _n_(669467, "self", lambda: self).canvas = _c_(669473, _a_(669469, _n_(669468, "tk", lambda: tk), "Canvas"), _n_(669470, "self", lambda: self), borderwidth=0, highlightthickness=0,
                                width=_n_(669471, "canvas_width", lambda: canvas_width), height=_n_(669472, "canvas_height", lambda: canvas_height), background="green")
        _l_(669474)
        _c_(669478, _a_(669477, _a_(669476, _n_(669475, "self", lambda: self), "canvas"), "pack"), side="top", fill="both", expand=True, padx=2, pady=2)
        _l_(669479)

        _c_(669485, _a_(669482, _a_(669481, _n_(669480, "self", lambda: self), "canvas"), "bind"), "<Configure>", _a_(669484, _n_(669483, "self", lambda: self), "refresh"))
        _l_(669486)


    def refresh(self, event):
        _l_(669593)

        '''Redraw the board, possibly in response to window being resized'''
        _l_(669488)
        xsize = _c_(669494, _n_(669489, "int", lambda: int), (_a_(669491, _n_(669490, "event", lambda: event), "width")-1) / _a_(669493, _n_(669492, "self", lambda: self), "columns"))
        _l_(669495)
        ysize = _c_(669501, _n_(669496, "int", lambda: int), (_a_(669498, _n_(669497, "event", lambda: event), "height")-1) / _a_(669500, _n_(669499, "self", lambda: self), "rows"))
        _l_(669502)
        _n_(669503, "self", lambda: self).size = _c_(669507, _n_(669504, "min", lambda: min), _n_(669505, "xsize", lambda: xsize), _n_(669506, "ysize", lambda: ysize))
        _l_(669508)
        _c_(669512, _a_(669511, _a_(669510, _n_(669509, "self", lambda: self), "canvas"), "delete"), "square")
        _l_(669513)
        color = _a_(669515, _n_(669514, "self", lambda: self), "color2")
        _l_(669516)
        for row in _c_(669520, _n_(669517, "range", lambda: range), _a_(669519, _n_(669518, "self", lambda: self), "rows")):
            _l_(669568)

            color = _a_(669522, _n_(669521, "self", lambda: self), "color1") if _n_(669523, "color", lambda: color) == _a_(669525, _n_(669524, "self", lambda: self), "color2") else _a_(669527, _n_(669526, "self", lambda: self), "color2")
            _l_(669528)
            for col in _c_(669532, _n_(669529, "range", lambda: range), _a_(669531, _n_(669530, "self", lambda: self), "columns")):
                _l_(669567)

                x1 = (_n_(669533, "col", lambda: col) * _a_(669535, _n_(669534, "self", lambda: self), "size"))
                _l_(669536)
                y1 = (_n_(669537, "row", lambda: row) * _a_(669539, _n_(669538, "self", lambda: self), "size"))
                _l_(669540)
                x2 = _n_(669541, "x1", lambda: x1) + _a_(669543, _n_(669542, "self", lambda: self), "size")
                _l_(669544)
                y2 = _n_(669545, "y1", lambda: y1) + _a_(669547, _n_(669546, "self", lambda: self), "size")
                _l_(669548)
                _c_(669557, _a_(669551, _a_(669550, _n_(669549, "self", lambda: self), "canvas"), "create_rectangle"), _n_(669552, "x1", lambda: x1), _n_(669553, "y1", lambda: y1), _n_(669554, "x2", lambda: x2), _n_(669555, "y2", lambda: y2), outline="black", fill=_n_(669556, "color", lambda: color), tags="square")
                _l_(669558)
                color = _a_(669560, _n_(669559, "self", lambda: self), "color1") if _n_(669561, "color", lambda: color) == _a_(669563, _n_(669562, "self", lambda: self), "color2") else _a_(669565, _n_(669564, "self", lambda: self), "color2")
                _l_(669566)
        for name in _a_(669570, _n_(669569, "self", lambda: self), "pieces"):
            _l_(669582)

            _c_(669580, _a_(669572, _n_(669571, "self", lambda: self), "placepiece"), _n_(669573, "name", lambda: name), _a_(669575, _n_(669574, "self", lambda: self), "pieces")[_n_(669576, "name", lambda: name)][0], _a_(669578, _n_(669577, "self", lambda: self), "pieces")[_n_(669579, "name", lambda: name)][1])
            _l_(669581)
        _c_(669586, _a_(669585, _a_(669584, _n_(669583, "self", lambda: self), "canvas"), "tag_raise"), "piece") 
        _l_(669587) 
        _c_(669591, _a_(669590, _a_(669589, _n_(669588, "self", lambda: self), "canvas"), "tag_lower"), "square")
        _l_(669592)

_c_(669596, _n_(669595, "main", lambda: main))
_l_(669597)
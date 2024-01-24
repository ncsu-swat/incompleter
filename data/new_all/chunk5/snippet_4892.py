# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42714591/typeerror-unsupported-operand-types-for-int-and-str-when-making-grid
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(686917)

except ImportError:
    pass
try:
    import math
    _l_(686919)

except ImportError:
    pass
try:
    import random
    _l_(686921)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(686923)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(686925)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(686927)

except ImportError:
    pass



GridSizeSetByUser = '8x8'
_l_(686928)
choicesRows = ['8', '10', '12', '14']
_l_(686929)
v = _n_(686930, "choicesRows", lambda: choicesRows)[0]
_l_(686931)
choicesColumns = ['8', '10', '12', '14']
_l_(686932)
v2 = _n_(686933, "choicesColumns", lambda: choicesColumns)[0]
_l_(686934)

GridRows = 9
_l_(686935)
GridColumns = 9
_l_(686936)


def getRows():
    _l_(686946)

    global GridRows
    _l_(686937)
    GridRows = _c_(686940, _a_(686939, _n_(686938, "GridRowSpinbox", lambda: GridRowSpinbox), "get"))
    _l_(686941)
    _c_(686944, _n_(686942, "print", lambda: print), _n_(686943, "GridRows", lambda: GridRows))
    _l_(686945)

def getColumns():
    _l_(686956)

    global GridColumns
    _l_(686947)
    GridColumns = _c_(686950, _a_(686949, _n_(686948, "GridColumnSpinbox", lambda: GridColumnSpinbox), "get"))
    _l_(686951)
    _c_(686954, _n_(686952, "print", lambda: print), _n_(686953, "GridColumns", lambda: GridColumns))
    _l_(686955)

def Treasure_Hunt_Window():
    _l_(686978)

    THunt = _c_(686959, _a_(686958, _n_(686957, "tk", lambda: tk), "Tk"))
    _l_(686960)
    _c_(686963, _a_(686962, _n_(686961, "THunt", lambda: THunt), "title"), "Treasure Hunt")
    _l_(686964)
    THuntInstructions = "Find the treasure hidden deep in the sand!Use ye arrow keys to move around,\n\n then press Space to search that spot! Keep searching until ye find it!"
    _l_(686965)
    board = _c_(686968, _n_(686966, "GameBoard", lambda: GameBoard), _n_(686967, "THunt", lambda: THunt))
    _l_(686969)
    _c_(686972, _a_(686971, _n_(686970, "board", lambda: board), "pack"), side="top", fill="both", expand="true", padx=4, pady=4)
    _l_(686973)
    _c_(686976, _a_(686975, _n_(686974, "THunt", lambda: THunt), "mainloop"))
    _l_(686977)

def Settings_Window():
    _l_(687086)

    Settings = _c_(686981, _a_(686980, _n_(686979, "tk", lambda: tk), "Tk"))
    _l_(686982)
    _c_(686985, _a_(686984, _n_(686983, "Settings", lambda: Settings), "title"), "Settings")
    _l_(686986)
    SettingsWelcome = _c_(686990, _a_(686988, _n_(686987, "tk", lambda: tk), "Label"), _n_(686989, "Settings", lambda: Settings), text='Settings Menu', width=50, fg="magenta")
    _l_(686991)
    SettingsGridSize = _c_(686995, _a_(686993, _n_(686992, "tk", lambda: tk), "Label"), _n_(686994, "Settings", lambda: Settings), text='Grid Size:', width =50, fg="magenta")
    _l_(686996)
    global mystring
    _l_(686997)
    mystring = _c_(686999, _n_(686998, "StringVar", lambda: StringVar))
    _l_(687000)
    global mystring2
    _l_(687001)
    mystring2 = _c_(687003, _n_(687002, "StringVar", lambda: StringVar))
    _l_(687004)
    global GridRowSpinbox
    _l_(687005)
    GridRowSpinbox = _c_(687010, _n_(687006, "Spinbox", lambda: Spinbox), _n_(687007, "Settings", lambda: Settings), values=_n_(687008, "choicesRows", lambda: choicesRows), textvariable=_n_(687009, "mystring", lambda: mystring), width=50, state="readonly", fg="magenta")
    _l_(687011)
    SaveRowSize = _c_(687016, _a_(687013, _n_(687012, "tk", lambda: tk), "Button"), _n_(687014, "Settings", lambda: Settings), text='Save row size for grid', width=50, fg="magenta", command = _n_(687015, "getRows", lambda: getRows))
    _l_(687017)
    global GridColumnSpinbox
    _l_(687018)
    GridColumnSpinbox = _c_(687023, _n_(687019, "Spinbox", lambda: Spinbox), _n_(687020, "Settings", lambda: Settings), values=_n_(687021, "choicesColumns", lambda: choicesColumns), textvariable=_n_(687022, "mystring2", lambda: mystring2), state="readonly", width=50, fg="magenta")
    _l_(687024)
    SaveColumnSize = _c_(687029, _a_(687026, _n_(687025, "tk", lambda: tk), "Button"), _n_(687027, "Settings", lambda: Settings), text='Save column size for grid', width=50, fg="magenta", command = _n_(687028, "getColumns", lambda: getColumns))
    _l_(687030)
    SettingsBandits = _c_(687034, _a_(687032, _n_(687031, "tk", lambda: tk), "Label"), _n_(687033, "Settings", lambda: Settings), text='Amount of Bandits:', width =50, fg="magenta")
    _l_(687035)
    BanditAmount = _c_(687039, _a_(687037, _n_(687036, "tk", lambda: tk), "Entry"), _n_(687038, "Settings", lambda: Settings), width = 50, fg="magenta")
    _l_(687040)
    SettingsBandits = _c_(687044, _a_(687042, _n_(687041, "tk", lambda: tk), "Label"), _n_(687043, "Settings", lambda: Settings), text='Amount of Treasure Chests (up to 64)', width =50, fg="magenta")
    _l_(687045)
    _c_(687049, _a_(687047, _n_(687046, "SettingsWelcome", lambda: SettingsWelcome), "pack"), fill=_n_(687048, "X", lambda: X))
    _l_(687050)
    _c_(687054, _a_(687052, _n_(687051, "SettingsGridSize", lambda: SettingsGridSize), "pack"), fill=_n_(687053, "X", lambda: X))
    _l_(687055)
    _c_(687059, _a_(687057, _n_(687056, "GridRowSpinbox", lambda: GridRowSpinbox), "pack"), fill=_n_(687058, "X", lambda: X))
    _l_(687060)
    _c_(687064, _a_(687062, _n_(687061, "SaveRowSize", lambda: SaveRowSize), "pack"), fill=_n_(687063, "X", lambda: X))
    _l_(687065)
    _c_(687069, _a_(687067, _n_(687066, "GridColumnSpinbox", lambda: GridColumnSpinbox), "pack"), fill=_n_(687068, "X", lambda: X))
    _l_(687070)
    _c_(687074, _a_(687072, _n_(687071, "SaveColumnSize", lambda: SaveColumnSize), "pack"), fill=_n_(687073, "X", lambda: X))
    _l_(687075)
    _c_(687079, _a_(687077, _n_(687076, "SettingsBandits", lambda: SettingsBandits), "pack"), fill=_n_(687078, "X", lambda: X))
    _l_(687080)
    _c_(687084, _a_(687082, _n_(687081, "BanditAmount", lambda: BanditAmount), "pack"), fill=_n_(687083, "X", lambda: X))
    _l_(687085)



def main():
    _l_(687143)

    root = _c_(687089, _a_(687088, _n_(687087, "tk", lambda: tk), "Tk"))
    _l_(687090)
    _c_(687093, _a_(687092, _n_(687091, "root", lambda: root), "title"), "Menu")
    _l_(687094)
    WelcomeButton = _c_(687098, _a_(687096, _n_(687095, "tk", lambda: tk), "Label"), _n_(687097, "root", lambda: root), text='Welcome to the menu!', width=50, height=2, fg="magenta")
    _l_(687099)
    _c_(687103, _a_(687101, _n_(687100, "WelcomeButton", lambda: WelcomeButton), "pack"), fill=_n_(687102, "X", lambda: X))
    _l_(687104)
    StartButton = _c_(687109, _a_(687106, _n_(687105, "tk", lambda: tk), "Button"), _n_(687107, "root", lambda: root), text='Start treasure hunting!', width=50, fg="magenta", command = _n_(687108, "Treasure_Hunt_Window", lambda: Treasure_Hunt_Window))
    _l_(687110)
    _c_(687114, _a_(687112, _n_(687111, "StartButton", lambda: StartButton), "pack"), fill=_n_(687113, "X", lambda: X))
    _l_(687115)
    SettingsButton = _c_(687120, _a_(687117, _n_(687116, "tk", lambda: tk), "Button"), _n_(687118, "root", lambda: root), text='''Change the settings of the treasure hunting game.
This includes the grid size.''', width=50, fg="magenta", command = _n_(687119, "Settings_Window", lambda: Settings_Window))
    _l_(687121)
    _c_(687125, _a_(687123, _n_(687122, "SettingsButton", lambda: SettingsButton), "pack"), fill=_n_(687124, "X", lambda: X))
    _l_(687126)
    QuitButton = _c_(687132, _a_(687128, _n_(687127, "tk", lambda: tk), "Button"), _n_(687129, "root", lambda: root), text='Exit the program', width=50, fg="magenta", command = _a_(687131, _n_(687130, "root", lambda: root), "destroy"))# display message in a child window.
    _l_(687133)# display message in a child window.
    _c_(687137, _a_(687135, _n_(687134, "QuitButton", lambda: QuitButton), "pack"), fill=_n_(687136, "X", lambda: X))
    _l_(687138)
    _c_(687141, _a_(687140, _n_(687139, "root", lambda: root), "mainloop"))
    _l_(687142)

def teststuff():
    _l_(687152)

    _c_(687146, _n_(687144, "print", lambda: print), _n_(687145, "GridRows", lambda: GridRows))
    _l_(687147)
    _c_(687150, _n_(687148, "print", lambda: print), _n_(687149, "GridColumns", lambda: GridColumns))
    _l_(687151)

class GameBoard(_a_(687154, _n_(687153, "tk", lambda: tk), "Frame")):
    _l_(687313)

    def __init__(self, parent, size=48, color1="white", color2="black"):
        _l_(687206)

        '''size is the size of a square, in pixels'''
        _l_(687155)

        _n_(687156, "self", lambda: self).rows = _n_(687157, "GridRows", lambda: GridRows)
        _l_(687158)
        _n_(687159, "self", lambda: self).columns = _n_(687160, "GridColumns", lambda: GridColumns)
        _l_(687161)
        _n_(687162, "self", lambda: self).size = _n_(687163, "size", lambda: size)
        _l_(687164)
        _n_(687165, "self", lambda: self).color1 = _n_(687166, "color1", lambda: color1)
        _l_(687167)
        _n_(687168, "self", lambda: self).color2 = _n_(687169, "color2", lambda: color2)
        _l_(687170)
        _n_(687171, "self", lambda: self).pieces = {}
        _l_(687172)

        canvas_width = _n_(687173, "GridColumns", lambda: GridColumns) * _n_(687174, "size", lambda: size)
        _l_(687175)
        canvas_height = _n_(687176, "GridRows", lambda: GridRows) * _n_(687177, "size", lambda: size)
        _l_(687178)

        _c_(687184, _a_(687181, _a_(687180, _n_(687179, "tk", lambda: tk), "Frame"), "__init__"), _n_(687182, "self", lambda: self), _n_(687183, "parent", lambda: parent))
        _l_(687185)
        _n_(687186, "self", lambda: self).canvas = _c_(687192, _a_(687188, _n_(687187, "tk", lambda: tk), "Canvas"), _n_(687189, "self", lambda: self), borderwidth=0, highlightthickness=0,
                                width=_n_(687190, "canvas_width", lambda: canvas_width), height=_n_(687191, "canvas_height", lambda: canvas_height), background="green")
        _l_(687193)
        _c_(687197, _a_(687196, _a_(687195, _n_(687194, "self", lambda: self), "canvas"), "pack"), side="top", fill="both", expand=True, padx=2, pady=2)
        _l_(687198)

        _c_(687204, _a_(687201, _a_(687200, _n_(687199, "self", lambda: self), "canvas"), "bind"), "<Configure>", _a_(687203, _n_(687202, "self", lambda: self), "refresh"))
        _l_(687205)


    def refresh(self, event):
        _l_(687312)

        '''Redraw the board, possibly in response to window being resized'''
        _l_(687207)
        xsize = _c_(687213, _n_(687208, "int", lambda: int), (_a_(687210, _n_(687209, "event", lambda: event), "width")-1) / _a_(687212, _n_(687211, "self", lambda: self), "columns"))
        _l_(687214)
        ysize = _c_(687220, _n_(687215, "int", lambda: int), (_a_(687217, _n_(687216, "event", lambda: event), "height")-1) / _a_(687219, _n_(687218, "self", lambda: self), "rows"))
        _l_(687221)
        _n_(687222, "self", lambda: self).size = _c_(687226, _n_(687223, "min", lambda: min), _n_(687224, "xsize", lambda: xsize), _n_(687225, "ysize", lambda: ysize))
        _l_(687227)
        _c_(687231, _a_(687230, _a_(687229, _n_(687228, "self", lambda: self), "canvas"), "delete"), "square")
        _l_(687232)
        color = _a_(687234, _n_(687233, "self", lambda: self), "color2")
        _l_(687235)
        for row in _c_(687239, _n_(687236, "range", lambda: range), _a_(687238, _n_(687237, "self", lambda: self), "rows")):
            _l_(687287)

            color = _a_(687241, _n_(687240, "self", lambda: self), "color1") if _n_(687242, "color", lambda: color) == _a_(687244, _n_(687243, "self", lambda: self), "color2") else _a_(687246, _n_(687245, "self", lambda: self), "color2")
            _l_(687247)
            for col in _c_(687251, _n_(687248, "range", lambda: range), _a_(687250, _n_(687249, "self", lambda: self), "columns")):
                _l_(687286)

                x1 = (_n_(687252, "col", lambda: col) * _a_(687254, _n_(687253, "self", lambda: self), "size"))
                _l_(687255)
                y1 = (_n_(687256, "row", lambda: row) * _a_(687258, _n_(687257, "self", lambda: self), "size"))
                _l_(687259)
                x2 = _n_(687260, "x1", lambda: x1) + _a_(687262, _n_(687261, "self", lambda: self), "size")
                _l_(687263)
                y2 = _n_(687264, "y1", lambda: y1) + _a_(687266, _n_(687265, "self", lambda: self), "size")
                _l_(687267)
                _c_(687276, _a_(687270, _a_(687269, _n_(687268, "self", lambda: self), "canvas"), "create_rectangle"), _n_(687271, "x1", lambda: x1), _n_(687272, "y1", lambda: y1), _n_(687273, "x2", lambda: x2), _n_(687274, "y2", lambda: y2), outline="black", fill=_n_(687275, "color", lambda: color), tags="square")
                _l_(687277)
                color = _a_(687279, _n_(687278, "self", lambda: self), "color1") if _n_(687280, "color", lambda: color) == _a_(687282, _n_(687281, "self", lambda: self), "color2") else _a_(687284, _n_(687283, "self", lambda: self), "color2")
                _l_(687285)
        for name in _a_(687289, _n_(687288, "self", lambda: self), "pieces"):
            _l_(687301)

            _c_(687299, _a_(687291, _n_(687290, "self", lambda: self), "placepiece"), _n_(687292, "name", lambda: name), _a_(687294, _n_(687293, "self", lambda: self), "pieces")[_n_(687295, "name", lambda: name)][0], _a_(687297, _n_(687296, "self", lambda: self), "pieces")[_n_(687298, "name", lambda: name)][1])
            _l_(687300)
        _c_(687305, _a_(687304, _a_(687303, _n_(687302, "self", lambda: self), "canvas"), "tag_raise"), "piece") 
        _l_(687306) 
        _c_(687310, _a_(687309, _a_(687308, _n_(687307, "self", lambda: self), "canvas"), "tag_lower"), "square")
        _l_(687311)

_c_(687315, _n_(687314, "main", lambda: main))
_l_(687316)
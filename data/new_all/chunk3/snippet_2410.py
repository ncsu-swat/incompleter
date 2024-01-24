# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45383859/typeerror-an-integer-is-required-got-type-str-in-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(566291)

except ImportError:
    pass
try:
    from os import open
    _l_(566293)

except ImportError:
    pass

def addData():
    _l_(566311)

    dataInsert = _c_(566296, _a_(566295, _n_(566294, "dataEntry", lambda: dataEntry), "get"))
    _l_(566297)
    _c_(566304, _a_(566299, _n_(566298, "itemList", lambda: itemList), "insert"), _n_(566300, "END", lambda: END), _c_(566303, _a_(566302, _n_(566301, "dataInsert", lambda: dataInsert), "upper")))
    _l_(566305)
    _c_(566309, _a_(566307, _n_(566306, "dataEntry", lambda: dataEntry), "delete"), 0, _n_(566308, "END", lambda: END))
    _l_(566310)

def deleteData():
    _l_(566321)

    dataSelect = _c_(566314, _a_(566313, _n_(566312, "itemList", lambda: itemList), "curselection"))
    _l_(566315)
    _c_(566319, _a_(566317, _n_(566316, "itemList", lambda: itemList), "delete"), _n_(566318, "dataSelect", lambda: dataSelect))
    _l_(566320)

def clearData():
    _l_(566327)

    _c_(566325, _a_(566323, _n_(566322, "itemList", lambda: itemList), "delete"), 0, _n_(566324, "END", lambda: END))
    _l_(566326)

def printData():
    _l_(566349)

    dataDirectory = _c_(566330, _a_(566329, _n_(566328, "filedialog", lambda: filedialog), "askdirectory"))
    _l_(566331)
    f = _c_(566334, _n_(566332, "open", lambda: open), 'items.txt', _n_(566333, "dataDirectory", lambda: dataDirectory), 'ab+')
    _l_(566335)
    _c_(566343, _a_(566337, _n_(566336, "f", lambda: f), "write"), _c_(566342, _n_(566338, "bytes", lambda: bytes), '', _c_(566341, _a_(566340, _n_(566339, "itemList", lambda: itemList), "get")), 'UTF-8'))
    _l_(566344)
    _c_(566347, _a_(566346, _n_(566345, "f", lambda: f), "close"))
    _l_(566348)

def rootExit():
    _l_(566354)

    _c_(566352, _a_(566351, _n_(566350, "root", lambda: root), "destroy"))
    _l_(566353)

root = _c_(566356, _n_(566355, "Tk", lambda: Tk))
_l_(566357)
_c_(566360, _a_(566359, _n_(566358, "root", lambda: root), "config"), bg='gray79')
_l_(566361)
_c_(566364, _a_(566363, _n_(566362, "root", lambda: root), "title"), 'Inventory Recording Systems')
_l_(566365)
_c_(566368, _a_(566367, _n_(566366, "root", lambda: root), "geometry"), '1300x800')
_l_(566369)
_c_(566372, _a_(566371, _n_(566370, "root", lambda: root), "resizable"), width=False, height=False)
_l_(566373)

mainLabel = _c_(566375, _n_(566374, "Label", lambda: Label), text='Inventory Recording Systems',
                  font=('comic sans ms', 20, 'bold'),
                  bg='gray79',
                  fg='black')
_l_(566376)

_c_(566379, _a_(566378, _n_(566377, "mainLabel", lambda: mainLabel), "place"), x=360, y=10)
_l_(566380)

f1 = _c_(566383, _n_(566381, "Frame", lambda: Frame), _n_(566382, "root", lambda: root),
           bg='black',
           width=300,
           height=40)
_l_(566384)

_c_(566387, _a_(566386, _n_(566385, "f1", lambda: f1), "place"), x=40, y=22)
_l_(566388)

f2 = _c_(566391, _n_(566389, "Frame", lambda: Frame), _n_(566390, "root", lambda: root),
           bg='black',
           width=300,
           height=40)
_l_(566392)

_c_(566395, _a_(566394, _n_(566393, "f2", lambda: f2), "place"), x=950, y=22)
_l_(566396)

dataLabel = _c_(566399, _n_(566397, "Label", lambda: Label), _n_(566398, "root", lambda: root),
                  text='Enter Data:',
                  font=('comic sans ms', 20, 'bold'),
                  bg='gray79')
_l_(566400)

_c_(566403, _a_(566402, _n_(566401, "dataLabel", lambda: dataLabel), "place"), x=10, y=130)
_l_(566404)

dataEntry = _c_(566407, _n_(566405, "Entry", lambda: Entry), _n_(566406, "root", lambda: root),
                  font=('arial', 16, 'bold'))
_l_(566408)

_c_(566411, _a_(566410, _n_(566409, "dataEntry", lambda: dataEntry), "place"), x=250, y=142)
_l_(566412)

itemList = _c_(566415, _n_(566413, "Listbox", lambda: Listbox), _n_(566414, "root", lambda: root),
                    font=('arial', 15, 'bold'),
                    width=47,
                    height=16)
_l_(566416)

_c_(566419, _a_(566418, _n_(566417, "itemList", lambda: itemList), "place"), x=10, y=200)
_l_(566420)

addButton = _c_(566425, _n_(566421, "Button", lambda: Button), _n_(566422, "root", lambda: root),
                   text='Add Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=_n_(566423, "GROOVE", lambda: GROOVE),
                   width=15,
                   height=1,
                   bd=5,
                   command=_n_(566424, "addData", lambda: addData))
_l_(566426)

_c_(566429, _a_(566428, _n_(566427, "addButton", lambda: addButton), "place"), x=865, y=215)
_l_(566430)

deleteButton = _c_(566435, _n_(566431, "Button", lambda: Button), _n_(566432, "root", lambda: root),
                   text='Delete Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=_n_(566433, "GROOVE", lambda: GROOVE),
                   width=15,
                   height=1,
                   bd=5,
                   command=_n_(566434, "deleteData", lambda: deleteData))
_l_(566436)

_c_(566439, _a_(566438, _n_(566437, "deleteButton", lambda: deleteButton), "place"), x=865, y=345)
_l_(566440)

clearButton = _c_(566445, _n_(566441, "Button", lambda: Button), _n_(566442, "root", lambda: root),
                   text='Clear Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=_n_(566443, "GROOVE", lambda: GROOVE),
                   width=15,
                   height=1,
                   bd=5,
                   command=_n_(566444, "clearData", lambda: clearData))
_l_(566446)

_c_(566449, _a_(566448, _n_(566447, "clearButton", lambda: clearButton), "place"), x=865, y=470)
_l_(566450)

printButton = _c_(566455, _n_(566451, "Button", lambda: Button), _n_(566452, "root", lambda: root),
                   text='Print Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=_n_(566453, "GROOVE", lambda: GROOVE),
                   width=15,
                   height=1,
                   bd=5,
                   command=_n_(566454, "printData", lambda: printData))
_l_(566456)

_c_(566459, _a_(566458, _n_(566457, "printButton", lambda: printButton), "place"), x=865, y=595)
_l_(566460)

exitButton = _c_(566465, _n_(566461, "Button", lambda: Button), _n_(566462, "root", lambda: root),
                   text='Exit',
                   font=('arial', 10, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=_n_(566463, "GROOVE", lambda: GROOVE),
                   width=6,
                   height=1,
                   bd=5,
                   command=_n_(566464, "rootExit", lambda: rootExit))
_l_(566466)

_c_(566469, _a_(566468, _n_(566467, "exitButton", lambda: exitButton), "place"), x=1212, y=752)
_l_(566470)

_c_(566473, _a_(566472, _n_(566471, "root", lambda: root), "mainloop"))
_l_(566474)
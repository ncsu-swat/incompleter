# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73675698/typeerror-not-supported-between-instances-of-int-and-entry
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(584250)

except ImportError:
    pass
try:
    from cgitb import grey
    _l_(584252)

except ImportError:
    pass
try:
    from decimal import DefaultContext
    _l_(584254)

except ImportError:
    pass
try:
    from operator import le
    _l_(584256)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(584258)

except ImportError:
    pass
try:
    from turtle import color, width
    _l_(584260)

except ImportError:
    pass


window = _c_(584262, _n_(584261, "Tk", lambda: Tk))
_l_(584263)
_c_(584266, _a_(584265, _n_(584264, "window", lambda: window), "title"), "IDK")
_l_(584267)
_c_(584270, _a_(584269, _n_(584268, "window", lambda: window), "configure"), bg='grey')
_l_(584271)
_c_(584274, _a_(584273, _n_(584272, "window", lambda: window), "geometry"), "500x500")
_l_(584275)
_c_(584278, _a_(584277, _n_(584276, "window", lambda: window), "geometry"))
_l_(584279)


label_title=_c_(584282, _n_(584280, "Label", lambda: Label), _n_(584281, "window", lambda: window), width=6, text="Lenght:", font=(30), bg='#0000FF')
_l_(584283)
_c_(584286, _a_(584285, _n_(584284, "label_title", lambda: label_title), "place"), x=0,y=120) 
_l_(584287) 
len_Entry= _c_(584290, _n_(584288, "Entry", lambda: Entry), _n_(584289, "window", lambda: window), bd =5)
_l_(584291)
_c_(584294, _a_(584293, _n_(584292, "len_Entry", lambda: len_Entry), "place"), x=120,y=120)
_l_(584295)

def yeso():
    _l_(584329)

    DefaultLabel = _c_(584298, _n_(584296, "Label", lambda: Label), _n_(584297, "window", lambda: window), text="Default: Yes", font=50)
    _l_(584299)
    _c_(584302, _a_(584301, _n_(584300, "DefaultLabel", lambda: DefaultLabel), "place"), x=290,y=200)
    _l_(584303)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    _l_(584304)
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _l_(584305)
    num = "0123456789"
    _l_(584306)
    Symbols = "[]{}#()*;._-"
    _l_(584307)
    ans = _n_(584308, "upper_case", lambda: upper_case) + _n_(584309, "lower_case", lambda: lower_case) + _n_(584310, "num", lambda: num) + _n_(584311, "Symbols", lambda: Symbols)
    _l_(584312)
    lenght = _c_(584315, _n_(584313, "str", lambda: str), _n_(584314, "len_Entry", lambda: len_Entry))
    _l_(584316)
    password = _c_(584323, _a_(584317, "", "join"), _c_(584322, _a_(584319, _n_(584318, "random", lambda: random), "sample"), _n_(584320, "ans", lambda: ans) , _n_(584321, "len_Entry", lambda: len_Entry)))
    _l_(584324)
    _c_(584327, _n_(584325, "print", lambda: print), _n_(584326, "password", lambda: password))
    _l_(584328)


def noo():
    _l_(584359)

    DefaultLabel = _c_(584332, _n_(584330, "Label", lambda: Label), _n_(584331, "window", lambda: window), text="Default: No  ", font=50)
    _l_(584333)
    _c_(584336, _a_(584335, _n_(584334, "DefaultLabel", lambda: DefaultLabel), "place"), x=290,y=200)
    _l_(584337)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    _l_(584338)
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _l_(584339)
    num = "0123456789"
    _l_(584340)
    ans2 = _n_(584341, "upper_case", lambda: upper_case) + _n_(584342, "lower_case", lambda: lower_case) + _n_(584343, "num", lambda: num)
    _l_(584344)
    lenght = _n_(584345, "len_Entry", lambda: len_Entry)
    _l_(584346)
    password = _c_(584353, _a_(584347, "", "join"), _c_(584352, _a_(584349, _n_(584348, "random", lambda: random), "sample"), _n_(584350, "ans2", lambda: ans2) , _n_(584351, "lenght", lambda: lenght)))
    _l_(584354)
    _c_(584357, _n_(584355, "print", lambda: print), _n_(584356, "password", lambda: password))
    _l_(584358)

Symboletxt = _c_(584362, _n_(584360, "Label", lambda: Label), _n_(584361, "window", lambda: window),width=8, text="Symboles:", font=(30), bg='#0000FF')
_l_(584363)
_c_(584366, _a_(584365, _n_(584364, "Symboletxt", lambda: Symboletxt), "place"), x=0,y=200)
_l_(584367)
my_button = _c_(584371, _n_(584368, "Button", lambda: Button), _n_(584369, "window", lambda: window), text="Yes", bg='#00FF00',command=_n_(584370, "yeso", lambda: yeso))
_l_(584372)
_c_(584375, _a_(584374, _n_(584373, "my_button", lambda: my_button), "place"), x=120, y=200)
_l_(584376)
my2_button = _c_(584380, _n_(584377, "Button", lambda: Button), _n_(584378, "window", lambda: window), text="No", bg='#ff0000',command=_n_(584379, "noo", lambda: noo))
_l_(584381)
_c_(584384, _a_(584383, _n_(584382, "my2_button", lambda: my2_button), "place"), x=180, y=200)
_l_(584385)



_c_(584388, _a_(584387, _n_(584386, "window", lambda: window), "mainloop"))
_l_(584389)
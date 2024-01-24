# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60978050/python-script-works-fine-independently-however-when-called-from-an-external-sc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(706198)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(706200)

except ImportError:
    pass


tasks_list = [] 
_l_(706201) 

counter = 1
_l_(706202)

# Function for checking input error when 
# empty input is given in task field 
def inputError() :
    _l_(706213)



    if _c_(706205, _a_(706204, _n_(706203, "enterTaskField", lambda: enterTaskField), "get")) == "" :
        _l_(706211)



        _c_(706208, _a_(706207, _n_(706206, "messagebox", lambda: messagebox), "showerror"), "Input Error") 
        _l_(706209) 
        aux = 0
        _l_(706210)

        return aux
    aux = 1
    _l_(706212)

    return aux
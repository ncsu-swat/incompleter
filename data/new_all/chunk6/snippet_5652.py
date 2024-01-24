# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52281528/attributeerror-type-object-message-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
root = _c_(371206, _n_(371205, "Tk", lambda: Tk))
_l_(371207)
frame = _c_(371210, _n_(371208, "Frame", lambda: Frame), _n_(371209, "root", lambda: root))
_l_(371211)
labelText = _c_(371213, _n_(371212, "StringVar", lambda: StringVar))
_l_(371214)

display = _c_(371218, _n_(371215, "Label", lambda: Label), _n_(371216, "frame", lambda: frame), textvariable=_n_(371217, "labelText", lambda: labelText))
_l_(371219)
_c_(371222, _a_(371221, _n_(371220, "labelText", lambda: labelText), "set"), "Connecting to the server...")
_l_(371223)
_c_(371226, _a_(371225, _n_(371224, "display", lambda: display), "pack"))
_l_(371227)
_c_(371230, _a_(371229, _n_(371228, "frame", lambda: frame), "pack"))
_l_(371231)
_c_(371234, _a_(371233, _n_(371232, "display", lambda: display), "update"))
_l_(371235)


def Submit_Message(event):
    _l_(371244)

    Message_Get = _c_(371238, _a_(371237, _n_(371236, "Message", lambda: Message), "get"))
    _l_(371239)
    _c_(371242, _n_(371240, "print", lambda: print), _n_(371241, "Message_Get", lambda: Message_Get))
    _l_(371243)

def run_code_1():
    _l_(371274)

    _c_(371246, _n_(371245, "print", lambda: print), "Enter Message to send!")
    _l_(371247)
    Message = _c_(371249, _n_(371248, "StringVar", lambda: StringVar))
    _l_(371250)
    Message = _c_(371253, _n_(371251, "Text", lambda: Text), _n_(371252, "root", lambda: root))
    _l_(371254)
    Submit_Data_Button = _c_(371257, _n_(371255, "Button", lambda: Button), _n_(371256, "root", lambda: root), text="Submit")
    _l_(371258)
    _c_(371262, _a_(371260, _n_(371259, "Submit_Data_Button", lambda: Submit_Data_Button), "bind"), "<Button-1>", _n_(371261, "Submit_Message", lambda: Submit_Message))
    _l_(371263)
    _c_(371266, _a_(371265, _n_(371264, "Submit_Data_Button", lambda: Submit_Data_Button), "pack"))
    _l_(371267)
    _c_(371272, _a_(371269, _n_(371268, "Message", lambda: Message), "pack"), expand=_n_(371270, "YES", lambda: YES), fill=_n_(371271, "BOTH", lambda: BOTH))
    _l_(371273)


_c_(371276, _n_(371275, "run_code_1", lambda: run_code_1))
_l_(371277)

_c_(371280, _a_(371279, _n_(371278, "root", lambda: root), "mainloop"))
_l_(371281)
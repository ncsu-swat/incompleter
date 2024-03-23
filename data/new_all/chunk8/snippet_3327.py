# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75635608/getting-error-as-exception-in-tkinter-callback-and-attribute-error-nonetype-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(607273)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(607275)

except ImportError:
    pass
try:
    from googletrans import  Translator,LANGUAGES
    _l_(607277)

except ImportError:
    pass

def change(text="Type", src="English", dest="Hindi"):
    _l_(607296)

    text1=_n_(607278, "text", lambda: text)
    _l_(607279)
    src1=_n_(607280, "src", lambda: src)
    _l_(607281)
    dest1=_n_(607282, "dest", lambda: dest)
    _l_(607283)
    trans= _c_(607285, _n_(607284, "Translator", lambda: Translator))
    _l_(607286)
    trans1= _c_(607292, _a_(607288, _n_(607287, "trans", lambda: trans), "translate"), _n_(607289, "text", lambda: text),src=_n_(607290, "src1", lambda: src1),dest=_n_(607291, "dest1", lambda: dest1))
    _l_(607293)
    aux = _n_(607294, "trans1", lambda: trans1)
    _l_(607295)
    return aux

def data():
    _l_(607327)

    s = _c_(607299, _a_(607298, _n_(607297, "comb_sor", lambda: comb_sor), "get"))
    _l_(607300)
    d = _c_(607303, _a_(607302, _n_(607301, "comb_dest", lambda: comb_dest), "get"))
    _l_(607304)
    msg= _c_(607308, _a_(607306, _n_(607305, "Sor_txt", lambda: Sor_txt), "get"), 1.0,_n_(607307, "END", lambda: END))
    _l_(607309)
    textget = _c_(607314, _n_(607310, "change", lambda: change), text= _n_(607311, "msg", lambda: msg), src=_n_(607312, "s", lambda: s), dest=_n_(607313, "d", lambda: d))
    _l_(607315)
    _c_(607319, _a_(607317, _n_(607316, "dest_txt", lambda: dest_txt), "delete"), 1.0,_n_(607318, "END", lambda: END))
    _l_(607320)
    _c_(607325, _a_(607322, _n_(607321, "dest_txt", lambda: dest_txt), "insert"), _n_(607323, "END", lambda: END),_n_(607324, "textget", lambda: textget))
    _l_(607326)

root = _c_(607329, _n_(607328, "Tk", lambda: Tk))
_l_(607330)
_c_(607333, _a_(607332, _n_(607331, "root", lambda: root), "title"), "Translator")
_l_(607334)
_c_(607337, _a_(607336, _n_(607335, "root", lambda: root), "geometry"), "500x700")
_l_(607338)
_c_(607341, _a_(607340, _n_(607339, "root", lambda: root), "config"), bg='#f1f3f5')
_l_(607342)

lab_txt=_c_(607345, _n_(607343, "Label", lambda: Label), _n_(607344, "root", lambda: root), text="Translator", font=("Inter", 30, "bold"), bg="#f1f3f5", fg="#495057")
_l_(607346)
_c_(607349, _a_(607348, _n_(607347, "lab_txt", lambda: lab_txt), "place"), x=100, y=40, height=50, width=300)
_l_(607350)

frame = _c_(607356, _a_(607354, _c_(607353, _n_(607351, "Frame", lambda: Frame), _n_(607352, "root", lambda: root)), "pack"), side=_n_(607355, "BOTTOM", lambda: BOTTOM))
_l_(607357)

lab_txt=_c_(607360, _n_(607358, "Label", lambda: Label), _n_(607359, "root", lambda: root), text="Source Text", font=("Inter", 16, "bold"), bg="#f1f3f5", fg="#495057")
_l_(607361)
_c_(607364, _a_(607363, _n_(607362, "lab_txt", lambda: lab_txt), "place"), x=100, y=100, height=30, width=300)
_l_(607365)
Sor_txt = _c_(607369, _n_(607366, "Text", lambda: Text), _n_(607367, "frame", lambda: frame), font=("Inter", 18, "bold"), bg="#f1f3f5", wrap=_n_(607368, "WORD", lambda: WORD))
_l_(607370)
_c_(607373, _a_(607372, _n_(607371, "Sor_txt", lambda: Sor_txt), "place"), x=10, y=130, height=150, width=480)
_l_(607374)

list_text = _c_(607379, _n_(607375, "list", lambda: list), _c_(607378, _a_(607377, _n_(607376, "LANGUAGES", lambda: LANGUAGES), "values")))
_l_(607380)

comb_sor = _c_(607385, _a_(607382, _n_(607381, "ttk", lambda: ttk), "Combobox"), _n_(607383, "frame", lambda: frame), value=_n_(607384, "list_text", lambda: list_text))
_l_(607386)
_c_(607389, _a_(607388, _n_(607387, "comb_sor", lambda: comb_sor), "place"), x=10, y=300, height=40, width=150)
_l_(607390)
_c_(607393, _a_(607392, _n_(607391, "comb_sor", lambda: comb_sor), "set"), "English")
_l_(607394)

button_change = _c_(607399, _n_(607395, "Button", lambda: Button), _n_(607396, "frame", lambda: frame), text="Translate", relief=_n_(607397, "RAISED", lambda: RAISED), command=_n_(607398, "data", lambda: data))
_l_(607400)
_c_(607403, _a_(607402, _n_(607401, "button_change", lambda: button_change), "place"), x=170, y=300, height=40, width=150)
_l_(607404)

comb_dest = _c_(607409, _a_(607406, _n_(607405, "ttk", lambda: ttk), "Combobox"), _n_(607407, "frame", lambda: frame), value=_n_(607408, "list_text", lambda: list_text))
_l_(607410)
_c_(607413, _a_(607412, _n_(607411, "comb_dest", lambda: comb_dest), "place"), x=330, y=300, height=40, width=150)
_l_(607414)
_c_(607417, _a_(607416, _n_(607415, "comb_dest", lambda: comb_dest), "set"), "English")
_l_(607418)

lab_txt=_c_(607421, _n_(607419, "Label", lambda: Label), _n_(607420, "root", lambda: root), text="Destination Text", font=("Inter", 16, "bold"), bg="#f1f3f5", fg="#495057")
_l_(607422)
_c_(607425, _a_(607424, _n_(607423, "lab_txt", lambda: lab_txt), "place"), x=100, y=360, height=30, width=300)
_l_(607426)
dest_txt = _c_(607430, _n_(607427, "Text", lambda: Text), _n_(607428, "frame", lambda: frame), font=("Inter", 18, "bold"), bg="#f1f3f5", wrap=_n_(607429, "WORD", lambda: WORD))
_l_(607431)
_c_(607434, _a_(607433, _n_(607432, "dest_txt", lambda: dest_txt), "place"), x=10, y=400, height=150, width=480)
_l_(607435)

_c_(607438, _a_(607437, _n_(607436, "root", lambda: root), "mainloop"))
_l_(607439)
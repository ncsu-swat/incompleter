# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53278224/python-type-error-while-using-exec-for-creating-tkinter-checkbutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for ii,j in _c_(347611, _n_(347600, "zip", lambda: zip), _c_(347605, _n_(347601, "range", lambda: range), _c_(347604, _n_(347602, "len", lambda: len), _n_(347603, "files_list", lambda: files_list))),_c_(347610, _n_(347606, "range", lambda: range), 1,_c_(347609, _n_(347607, "len", lambda: len), _n_(347608, "files_list", lambda: files_list))+1)):
    _l_(347625)

    _c_(347614, _n_(347612, "exec", lambda: exec), "var%i=StringVar()"%_n_(347613, "j", lambda: j))
    _l_(347615)
    _c_(347619, _n_(347616, "exec", lambda: exec), "ch%i = Checkbutton(text=files_list[ii],variable=var%i)"%_n_(347617, "j", lambda: j)%_n_(347618, "j", lambda: j))
    _l_(347620)
    _c_(347623, _n_(347621, "exec", lambda: exec), "ch%i.grid(row=ii, column=0, sticky=W)"%_n_(347622, "j", lambda: j))
    _l_(347624)
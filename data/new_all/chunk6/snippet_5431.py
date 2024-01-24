# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53278224/python-type-error-while-using-exec-for-creating-tkinter-checkbutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for ii,j in _c_(372178, _n_(372167, "zip", lambda: zip), _c_(372172, _n_(372168, "range", lambda: range), _c_(372171, _n_(372169, "len", lambda: len), _n_(372170, "files_list", lambda: files_list))),_c_(372177, _n_(372173, "range", lambda: range), 1,_c_(372176, _n_(372174, "len", lambda: len), _n_(372175, "files_list", lambda: files_list))+1)):
    _l_(372192)

    _c_(372181, _n_(372179, "exec", lambda: exec), "var%i=StringVar()"%_n_(372180, "j", lambda: j))
    _l_(372182)
    _c_(372186, _n_(372183, "exec", lambda: exec), "ch%i = Checkbutton(text=files_list[ii],variable=var%i)"%_n_(372184, "j", lambda: j)%_n_(372185, "j", lambda: j))
    _l_(372187)
    _c_(372190, _n_(372188, "exec", lambda: exec), "ch%i.grid(row=ii, column=0, sticky=W)"%_n_(372189, "j", lambda: j))
    _l_(372191)
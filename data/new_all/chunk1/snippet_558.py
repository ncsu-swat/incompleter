# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23921781/name-error-name-apply-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(409918)

except ImportError:
    pass

class MultiListbox(_n_(409919, "Frame", lambda: Frame)):
    _l_(410220)

    def __init__(self, master, lists):
        _l_(410046)

        _c_(409924, _a_(409921, _n_(409920, "Frame", lambda: Frame), "__init__"), _n_(409922, "self", lambda: self), _n_(409923, "master", lambda: master))
        _l_(409925)
        _n_(409926, "self", lambda: self).lists = []
        _l_(409927)
        for l,w in _n_(409928, "lists", lambda: lists):
            _l_(410015)

            frame = _c_(409931, _n_(409929, "Frame", lambda: Frame), _n_(409930, "self", lambda: self)); _c_(409937, _a_(409933, _n_(409932, "frame", lambda: frame), "pack"), side=_n_(409934, "LEFT", lambda: LEFT), expand=_n_(409935, "YES", lambda: YES), fill=_n_(409936, "BOTH", lambda: BOTH))
            _l_(409938)
            _c_(409946, _a_(409944, _c_(409943, _n_(409939, "Label", lambda: Label), _n_(409940, "frame", lambda: frame), text=_n_(409941, "l", lambda: l), borderwidth=1, relief=_n_(409942, "RAISED", lambda: RAISED)), "pack"), fill=_n_(409945, "X", lambda: X))
            _l_(409947)
            lb = _c_(409953, _n_(409948, "Listbox", lambda: Listbox), _n_(409949, "frame", lambda: frame), width=_n_(409950, "w", lambda: w), borderwidth=0, selectborderwidth=0,
                 relief=_n_(409951, "FLAT", lambda: FLAT), exportselection=_n_(409952, "FALSE", lambda: FALSE))
            _l_(409954)
            _c_(409959, _a_(409956, _n_(409955, "lb", lambda: lb), "pack"), expand=_n_(409957, "YES", lambda: YES), fill=_n_(409958, "BOTH", lambda: BOTH))
            _l_(409960)
            _c_(409965, _a_(409963, _a_(409962, _n_(409961, "self", lambda: self), "lists"), "append"), _n_(409964, "lb", lambda: lb))
            _l_(409966)
            _c_(409975, _a_(409968, _n_(409967, "lb", lambda: lb), "bind"), '<B1-Motion>', lambda e, s=_n_(409969, "self", lambda: self): _c_(409974, _a_(409971, _n_(409970, "s", lambda: s), "_select"), _a_(409973, _n_(409972, "e", lambda: e), "y")))
            _l_(409976)
            _c_(409985, _a_(409978, _n_(409977, "lb", lambda: lb), "bind"), '<Button-1>', lambda e, s=_n_(409979, "self", lambda: self): _c_(409984, _a_(409981, _n_(409980, "s", lambda: s), "_select"), _a_(409983, _n_(409982, "e", lambda: e), "y")))
            _l_(409986)
            _c_(409989, _a_(409988, _n_(409987, "lb", lambda: lb), "bind"), '<Leave>', lambda e: 'break')
            _l_(409990)
            _c_(410001, _a_(409992, _n_(409991, "lb", lambda: lb), "bind"), '<B2-Motion>', lambda e, s=_n_(409993, "self", lambda: self): _c_(410000, _a_(409995, _n_(409994, "s", lambda: s), "_b2motion"), _a_(409997, _n_(409996, "e", lambda: e), "x"), _a_(409999, _n_(409998, "e", lambda: e), "y")))
            _l_(410002)
            _c_(410013, _a_(410004, _n_(410003, "lb", lambda: lb), "bind"), '<Button-2>', lambda e, s=_n_(410005, "self", lambda: self): _c_(410012, _a_(410007, _n_(410006, "s", lambda: s), "_button2"), _a_(410009, _n_(410008, "e", lambda: e), "x"), _a_(410011, _n_(410010, "e", lambda: e), "y")))
            _l_(410014)
        frame = _c_(410018, _n_(410016, "Frame", lambda: Frame), _n_(410017, "self", lambda: self)); _c_(410023, _a_(410020, _n_(410019, "frame", lambda: frame), "pack"), side=_n_(410021, "LEFT", lambda: LEFT), fill=_n_(410022, "Y", lambda: Y))
        _l_(410024)
        _c_(410031, _a_(410029, _c_(410028, _n_(410025, "Label", lambda: Label), _n_(410026, "frame", lambda: frame), borderwidth=1, relief=_n_(410027, "RAISED", lambda: RAISED)), "pack"), fill=_n_(410030, "X", lambda: X))
        _l_(410032)
        sb = _c_(410038, _n_(410033, "Scrollbar", lambda: Scrollbar), _n_(410034, "frame", lambda: frame), orient=_n_(410035, "VERTICAL", lambda: VERTICAL), command=_a_(410037, _n_(410036, "self", lambda: self), "_scroll"))
        _l_(410039)
        _c_(410044, _a_(410041, _n_(410040, "sb", lambda: sb), "pack"), expand=_n_(410042, "YES", lambda: YES), fill=_n_(410043, "Y", lambda: Y))
        _l_(410045)

    def yview(self, *args):
        _l_(410059)

        """connect the yview action together"""
        _c_(410051, _a_(410049, _a_(410048, _n_(410047, "self", lambda: self), "lb1"), "yview"), *_n_(410050, "args", lambda: args))
        _l_(410052)
        _c_(410057, _a_(410055, _a_(410054, _n_(410053, "self", lambda: self), "lb2"), "yview"), *_n_(410056, "args", lambda: args))
        _l_(410058)

    def _select(self, y):
        _l_(410077)

        row = _c_(410064, _a_(410062, _a_(410061, _n_(410060, "self", lambda: self), "lists")[0], "nearest"), _n_(410063, "y", lambda: y))
        _l_(410065)
        _c_(410069, _a_(410067, _n_(410066, "self", lambda: self), "selection_clear"), 0, _n_(410068, "END", lambda: END))
        _l_(410070)
        _c_(410074, _a_(410072, _n_(410071, "self", lambda: self), "selection_set"), _n_(410073, "row", lambda: row))
        _l_(410075)
        aux = 'break'
        _l_(410076)
        return aux

    def _button2(self, x, y):
        _l_(410087)

        for l in _a_(410079, _n_(410078, "self", lambda: self), "lists"):
            _l_(410085)

_c_(410084, _a_(410081, _n_(410080, "l", lambda: l), "scan_mark"), _n_(410082, "x", lambda: x), _n_(410083, "y", lambda: y))        aux = 'break'
        _l_(410086)
        return aux

    def _b2motion(self, x, y):
        _l_(410097)

        for l in _a_(410089, _n_(410088, "self", lambda: self), "lists"):
            _l_(410095)

_c_(410094, _a_(410091, _n_(410090, "l", lambda: l), "scan_dragto"), _n_(410092, "x", lambda: x), _n_(410093, "y", lambda: y))        aux = 'break'
        _l_(410096)
        return aux

    def _scroll(self, *args):
        _l_(410107)

        for l in _a_(410099, _n_(410098, "self", lambda: self), "lists"):
            _l_(410106)

            _c_(410104, _n_(410100, "apply", lambda: apply), _a_(410102, _n_(410101, "l", lambda: l), "yview"), _n_(410103, "args", lambda: args))
            _l_(410105)

    def curselection(self):
        _l_(410113)

        aux = _c_(410111, _a_(410110, _a_(410109, _n_(410108, "self", lambda: self), "lists")[0], "curselection"))
        _l_(410112)
        return aux

    def delete(self, first, last=None):
        _l_(410123)

        for l in _a_(410115, _n_(410114, "self", lambda: self), "lists"):
            _l_(410122)

            _c_(410120, _a_(410117, _n_(410116, "l", lambda: l), "delete"), _n_(410118, "first", lambda: first), _n_(410119, "last", lambda: last))
            _l_(410121)

    def get(self, first, last=None):
        _l_(410145)

        result = []
        _l_(410124)
        for l in _a_(410126, _n_(410125, "self", lambda: self), "lists"):
            _l_(410136)

            _c_(410134, _a_(410128, _n_(410127, "result", lambda: result), "append"), _c_(410133, _a_(410130, _n_(410129, "l", lambda: l), "get"), _n_(410131, "first", lambda: first),_n_(410132, "last", lambda: last)))
            _l_(410135)
        if _n_(410137, "last", lambda: last):
            _l_(410142)

return _c_(410141, _n_(410138, "apply", lambda: apply), _n_(410139, "map", lambda: map), [None] + _n_(410140, "result", lambda: result))        aux = _n_(410143, "result", lambda: result)
        _l_(410144)
        return aux

    def index(self, index):
        _l_(410152)

        _c_(410150, _a_(410148, _a_(410147, _n_(410146, "self", lambda: self), "lists")[0], "index"), _n_(410149, "index", lambda: index))
        _l_(410151)

    def insert(self, index, *elements):
        _l_(410168)

        for e in _n_(410153, "elements", lambda: elements):
            _l_(410155)

            i = 0
            _l_(410154)
        for l in _a_(410157, _n_(410156, "self", lambda: self), "lists"):
            _l_(410167)

            _c_(410163, _a_(410159, _n_(410158, "l", lambda: l), "insert"), _n_(410160, "index", lambda: index), _n_(410161, "e", lambda: e)[_n_(410162, "i", lambda: i)])
            _l_(410164)
            i = _n_(410165, "i", lambda: i) + 1
            _l_(410166)

    def size(self):
        _l_(410174)

        aux = _c_(410172, _a_(410171, _a_(410170, _n_(410169, "self", lambda: self), "lists")[0], "size"))
        _l_(410173)
        return aux

    def see(self, index):
        _l_(410183)

        for l in _a_(410176, _n_(410175, "self", lambda: self), "lists"):
            _l_(410182)

            _c_(410180, _a_(410178, _n_(410177, "l", lambda: l), "see"), _n_(410179, "index", lambda: index))
            _l_(410181)

    def selection_anchor(self, index):
        _l_(410192)

        for l in _a_(410185, _n_(410184, "self", lambda: self), "lists"):
            _l_(410191)

            _c_(410189, _a_(410187, _n_(410186, "l", lambda: l), "selection_anchor"), _n_(410188, "index", lambda: index))
            _l_(410190)

    def selection_clear(self, first, last=None):
        _l_(410202)

        for l in _a_(410194, _n_(410193, "self", lambda: self), "lists"):
            _l_(410201)

            _c_(410199, _a_(410196, _n_(410195, "l", lambda: l), "selection_clear"), _n_(410197, "first", lambda: first), _n_(410198, "last", lambda: last))
            _l_(410200)

    def selection_includes(self, index):
        _l_(410209)

        aux = _c_(410207, _a_(410205, _a_(410204, _n_(410203, "self", lambda: self), "lists")[0], "selection_includes"), _n_(410206, "index", lambda: index))
        _l_(410208)
        return aux

    def selection_set(self, first, last=None):
        _l_(410219)

        for l in _a_(410211, _n_(410210, "self", lambda: self), "lists"):
            _l_(410218)

            _c_(410216, _a_(410213, _n_(410212, "l", lambda: l), "selection_set"), _n_(410214, "first", lambda: first), _n_(410215, "last", lambda: last))
            _l_(410217)

if _n_(410221, "__name__", lambda: __name__) == '__main__':
    _l_(410297)

    tk = _c_(410223, _n_(410222, "Tk", lambda: Tk))
    _l_(410224)
    _c_(410229, _a_(410228, _c_(410227, _n_(410225, "Label", lambda: Label), _n_(410226, "tk", lambda: tk), text='MultiListbox'), "pack"))
    _l_(410230)
    mlb = _c_(410233, _n_(410231, "MultiListbox", lambda: MultiListbox), _n_(410232, "tk", lambda: tk), (('Clave', 20), ('Descripcion', 20), ('Existencia', 20)))
    _l_(410234)

    lineas = _c_(410240, _n_(410235, "len", lambda: len), _c_(410239, _a_(410238, _c_(410237, _n_(410236, "open", lambda: open), "productos-doc1.txt"), "readlines")))
    _l_(410241)
    totalLineas=_c_(410244, _n_(410242, "int", lambda: int), _n_(410243, "lineas", lambda: lineas))
    _l_(410245)

    try:
        _l_(410292)

        x = 0
        _l_(410246)
        while 0 != _n_(410247, "totalLineas", lambda: totalLineas):
            _l_(410284)

            abrir = _c_(410249, _n_(410248, "open", lambda: open), "productos-doc1.txt","r+")#ABRE EL ARCHIVO
            _l_(410250)#ABRE EL ARCHIVO
            leer = _c_(410253, _a_(410252, _n_(410251, "abrir", lambda: abrir), "readlines"))
            _l_(410254)
            renglon = _n_(410255, "leer", lambda: leer)[_n_(410256, "x", lambda: x)]
            _l_(410257)
            splitRenglon = _c_(410260, _a_(410259, _n_(410258, "renglon", lambda: renglon), "split"), "'")
            _l_(410261)
            clave = _n_(410262, "splitRenglon", lambda: splitRenglon)[0]
            _l_(410263)
            descripcion = _n_(410264, "splitRenglon", lambda: splitRenglon)[1]
            _l_(410265)
            existencia = _n_(410266, "splitRenglon", lambda: splitRenglon)[3]
            _l_(410267)
            _c_(410274, _a_(410269, _n_(410268, "mlb", lambda: mlb), "insert"), _n_(410270, "END", lambda: END), (_n_(410271, "clave", lambda: clave), _n_(410272, "descripcion", lambda: descripcion), _n_(410273, "existencia", lambda: existencia)))
            _l_(410275)
            _c_(410280, _a_(410277, _n_(410276, "mlb", lambda: mlb), "pack"), expand=_n_(410278, "YES", lambda: YES),fill=_n_(410279, "BOTH", lambda: BOTH))
            _l_(410281)

            x = _n_(410282, "x", lambda: x)+1
            _l_(410283)
    except _n_(410285, "IndexError", lambda: IndexError):
        _l_(410291)

        _c_(410289, _a_(410287, _n_(410286, "mlb", lambda: mlb), "insert"), _n_(410288, "END", lambda: END),"FINISH" )
        _l_(410290)

    _c_(410295, _a_(410294, _n_(410293, "tk", lambda: tk), "mainloop"))
    _l_(410296)
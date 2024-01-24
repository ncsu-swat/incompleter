# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66539234/typeerror-init-missing-1-required-positional-argument-parent
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(539880)

except ImportError:
    pass
try:
    import tkinter.ttk as ttk
    _l_(539882)

except ImportError:
    pass


class CollegeApp(_n_(539883, "Tk", lambda: Tk)):
    _l_(539932)

    def __init__(self):
        _l_(539922)

        _c_(539887, _a_(539885, _n_(539884, "Tk", lambda: Tk), "__init__"), _n_(539886, "self", lambda: self))
        _l_(539888)
        container = _c_(539892, _a_(539890, _n_(539889, "ttk", lambda: ttk), "Frame"), _n_(539891, "self", lambda: self))
        _l_(539893)
        _c_(539896, _a_(539895, _n_(539894, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(539897)
        _n_(539898, "self", lambda: self).frames = {}
        _l_(539899)
        for F in (_n_(539900, "StartPage", lambda: StartPage), _n_(539901, "PageTwo", lambda: PageTwo)):
            _l_(539916)

            frame = _c_(539905, _n_(539902, "F", lambda: F), _n_(539903, "container", lambda: container), _n_(539904, "self", lambda: self))
            _l_(539906)
            _a_(539908, _n_(539907, "self", lambda: self), "frames")[_n_(539909, "F", lambda: F)] = _n_(539910, "frame", lambda: frame)
            _l_(539911)
            _c_(539914, _a_(539913, _n_(539912, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(539915)
        _c_(539920, _a_(539918, _n_(539917, "self", lambda: self), "show_frame"), _n_(539919, "StartPage", lambda: StartPage))
        _l_(539921)

    def show_frame(self, cont):
        _l_(539931)

        frame = _a_(539924, _n_(539923, "self", lambda: self), "frames")[_n_(539925, "cont", lambda: cont)]
        _l_(539926)
        _c_(539929, _a_(539928, _n_(539927, "frame", lambda: frame), "tkraise"))
        _l_(539930)


class StartPage(_a_(539934, _n_(539933, "ttk", lambda: ttk), "Frame")):
    _l_(539983)

    def __init__(self, parent, controller):
        _l_(539949)

        _n_(539935, "self", lambda: self).controller = _n_(539936, "controller", lambda: controller)
        _l_(539937)
        _c_(539943, _a_(539940, _a_(539939, _n_(539938, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(539941, "self", lambda: self), _n_(539942, "parent", lambda: parent))
        _l_(539944)
        _c_(539947, _a_(539946, _n_(539945, "self", lambda: self), "startMenu"))
        _l_(539948)

    def startMenu(self):
        _l_(539982)

        heading = _c_(539952, _n_(539950, "Label", lambda: Label), _n_(539951, "self", lambda: self), text="College Tournament Points\n Count Software",
                        font=('Arial', 25))
        _l_(539953)
        _c_(539956, _a_(539955, _n_(539954, "heading", lambda: heading), "grid"), row=0, column=0, columnspan=2, padx=240, pady=40)
        _l_(539957)

        start_Btn = _c_(539965, _n_(539958, "Button", lambda: Button), _n_(539959, "self", lambda: self), text="Start", font="Arial 16", width=8,
                           command=lambda: _c_(539964, _a_(539962, _a_(539961, _n_(539960, "self", lambda: self), "controller"), "show_frame"), _n_(539963, "PageTwo", lambda: PageTwo)))
        _l_(539966)
        _c_(539969, _a_(539968, _n_(539967, "start_Btn", lambda: start_Btn), "grid"), row=1, column=0, padx=30)
        _l_(539970)

        exit_Btn = _c_(539974, _n_(539971, "Button", lambda: Button), _n_(539972, "self", lambda: self), text="EXIT", font="Arial 16", width=8,
                          command=_n_(539973, "exitButton", lambda: exitButton))
        _l_(539975)
        _c_(539978, _a_(539977, _n_(539976, "exit_Btn", lambda: exit_Btn), "grid"), row=1, column=1, padx=30)
        _l_(539979)

        def starting_Program():
            _l_(539981)

            pass
            _l_(539980)

class exitButton(_n_(539984, "Button", lambda: Button)):
    _l_(540002)

    def __init__(self, parent):
        _l_(540001)

        _c_(539989, _a_(539986, _n_(539985, "Button", lambda: Button), "__init__"), _n_(539987, "self", lambda: self), _n_(539988, "parent", lambda: parent))
        _l_(539990)
        _n_(539991, "self", lambda: self)[_n_(539992, "Button", lambda: Button)] = _a_(539994, _n_(539993, "parent", lambda: parent), "destroy")
        _l_(539995)
        _c_(539999, _a_(539997, _n_(539996, "self", lambda: self), "pack"), _n_(539998, "BOTTOM", lambda: BOTTOM))
        _l_(540000)


class PageTwo(_a_(540004, _n_(540003, "ttk", lambda: ttk), "Frame")):
    _l_(540042)

    def __init__(self, parent, controller):
        _l_(540019)

        _n_(540005, "self", lambda: self).controller = _n_(540006, "controller", lambda: controller)
        _l_(540007)
        _c_(540013, _a_(540010, _a_(540009, _n_(540008, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(540011, "self", lambda: self), _n_(540012, "parent", lambda: parent))
        _l_(540014)
        _c_(540017, _a_(540016, _n_(540015, "self", lambda: self), "make_widget"))
        _l_(540018)

    def make_widget(self):
        _l_(540041)

        _c_(540025, _a_(540024, _c_(540023, _a_(540021, _n_(540020, "ttk", lambda: ttk), "Label"), _n_(540022, "self", lambda: self), text='This is page two'), "grid"), padx=(20, 20), pady=(20, 20))
        _l_(540026)
        button1 = _c_(540035, _a_(540028, _n_(540027, "ttk", lambda: ttk), "Button"), _n_(540029, "self", lambda: self), text='Previous Page',
                             command=lambda: _c_(540034, _a_(540032, _a_(540031, _n_(540030, "self", lambda: self), "controller"), "show_frame"), _n_(540033, "StartPage", lambda: StartPage)))
        _l_(540036)
        _c_(540039, _a_(540038, _n_(540037, "button1", lambda: button1), "grid"))
        _l_(540040)


if _n_(540043, "__name__", lambda: __name__) == '__main__':
    _l_(540059)

    app = _c_(540045, _n_(540044, "CollegeApp", lambda: CollegeApp))
    _l_(540046)
    _c_(540049, _a_(540048, _n_(540047, "app", lambda: app), "geometry"), "800x500")
    _l_(540050)
    _c_(540053, _a_(540052, _n_(540051, "app", lambda: app), "title"), 'Points Counter')
    _l_(540054)
    _c_(540057, _a_(540056, _n_(540055, "app", lambda: app), "mainloop"))
    _l_(540058)
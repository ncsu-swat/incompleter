# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76254003/wndproc-return-value-cannot-be-converted-to-lresult-typeerror-wparam-is-simple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myschedule = []
_l_(384513)

def func():
    _l_(384597)

    try:
        import schedule
        _l_(384515)

    except ImportError:
        pass
    try:
        import time
        _l_(384517)

    except ImportError:
        pass
    try:
        import win10toast
        _l_(384519)

    except ImportError:
        pass


    noti=_c_(384522, _a_(384521, _n_(384520, "win10toast", lambda: win10toast), "ToastNotifier"))
    _l_(384523)

    choice="yes"
    _l_(384524)
    while _n_(384525, "choice", lambda: choice)=="yes":
        _l_(384571)

        title=_c_(384527, _n_(384526, "input", lambda: input), "enter the title")
        _l_(384528)
        message=_c_(384530, _n_(384529, "input", lambda: input), "enter the message")
        _l_(384531)
        tim=_c_(384533, _n_(384532, "input", lambda: input), "enter the time")
        _l_(384534)
        ms=[_n_(384535, "title", lambda: title),_n_(384536, "message", lambda: message),_n_(384537, "tim", lambda: tim)]
        _l_(384538)
        _c_(384542, _a_(384540, _n_(384539, "myschedule", lambda: myschedule), "append"), _n_(384541, "ms", lambda: ms))
        _l_(384543)

        choice = _c_(384545, _n_(384544, "input", lambda: input), "enter your choice:")
        _l_(384546)
        if _n_(384547, "choice", lambda: choice) == "yes":
            _l_(384570)

            title = _c_(384549, _n_(384548, "input", lambda: input), "enter the title")
            _l_(384550)
            message = _c_(384552, _n_(384551, "input", lambda: input), "enter the message")
            _l_(384553)
            tim = _c_(384555, _n_(384554, "input", lambda: input), "enter the time")
            _l_(384556)
            ms = [_n_(384557, "title", lambda: title), _n_(384558, "message", lambda: message), _n_(384559, "tim", lambda: tim)]
            _l_(384560)
            _c_(384564, _a_(384562, _n_(384561, "myschedule", lambda: myschedule), "append"), _n_(384563, "ms", lambda: ms))
            _l_(384565)
            choice = _c_(384567, _n_(384566, "input", lambda: input), "enter your choice:")
            _l_(384568)


        else:
            pass
            _l_(384569)


    for i in _n_(384572, "myschedule", lambda: myschedule):
        _l_(384596)


        def functionmaker():
            _l_(384579)

            _c_(384577, _a_(384574, _n_(384573, "noti", lambda: noti), "show_toast"), _n_(384575, "i", lambda: i)[0],_n_(384576, "i", lambda: i)[1],duration=12)
            _l_(384578)

        _c_(384589, _a_(384587, _c_(384586, _a_(384584, _a_(384583, _c_(384582, _a_(384581, _n_(384580, "schedule", lambda: schedule), "every")), "day"), "at"), _n_(384585, "i", lambda: i)[2]), "do"), _n_(384588, "functionmaker", lambda: functionmaker))
        _l_(384590)

        while True:
            _l_(384595)

            _c_(384593, _a_(384592, _n_(384591, "schedule", lambda: schedule), "run_pending"))
            _l_(384594)

_c_(384599, _n_(384598, "func", lambda: func))
_l_(384600)
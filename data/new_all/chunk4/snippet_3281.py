# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76219308/i-get-an-type-error-but-o-cant-figure-out-why
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(598028)

except ImportError:
    pass
try:
    import math
    _l_(598030)

except ImportError:
    pass
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
_l_(598031)
RED = "#e7305b"
_l_(598032)
GREEN = "#9bdeac"
_l_(598033)
YELLOW = "#f7f5dd"
_l_(598034)
FONT_NAME = "Courier"
_l_(598035)
WORK_MIN = 25
_l_(598036)
SHORT_BREAK_MIN = 5
_l_(598037)
LONG_BREAK_MIN = 20
_l_(598038)
reps = 0
_l_(598039)
timing = None
_l_(598040)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomo():
    _l_(598061)

    _c_(598044, _a_(598042, _n_(598041, "window", lambda: window), "after_cancel"), _n_(598043, "timing", lambda: timing))
    _l_(598045)
    _c_(598049, _a_(598047, _n_(598046, "canvas", lambda: canvas), "itemconfig"), _n_(598048, "timer", lambda: timer), text="00:00")
    _l_(598050)
    _c_(598053, _a_(598052, _n_(598051, "timer_text", lambda: timer_text), "config"), text="TIMER")
    _l_(598054)
    _c_(598057, _a_(598056, _n_(598055, "my_label", lambda: my_label), "config"), text="")
    _l_(598058)
    global reps
    _l_(598059)
    reps = 0
    _l_(598060)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    _l_(598098)

    global reps
    _l_(598062)
    reps += 1
    _l_(598063)
    short = _n_(598064, "SHORT_BREAK_MIN", lambda: SHORT_BREAK_MIN) * 60
    _l_(598065)
    long = _n_(598066, "LONG_BREAK_MIN", lambda: LONG_BREAK_MIN) * 60
    _l_(598067)
    work = _n_(598068, "WORK_MIN", lambda: WORK_MIN) * 60
    _l_(598069)
    if _n_(598070, "reps", lambda: reps) % 8 == 0:
        _l_(598097)

        _c_(598073, _n_(598071, "count_down", lambda: count_down), _n_(598072, "long", lambda: long))
        _l_(598074)
        _c_(598077, _a_(598076, _n_(598075, "timer_text", lambda: timer_text), "config"), text="Long Break")
        _l_(598078)
    elif _n_(598079, "reps", lambda: reps) % 2 == 0:
        _l_(598096)

        _c_(598082, _n_(598080, "count_down", lambda: count_down), _n_(598081, "short", lambda: short))
        _l_(598083)
        _c_(598086, _a_(598085, _n_(598084, "timer_text", lambda: timer_text), "config"), text="Short Break")
        _l_(598087)
    else:
        _c_(598090, _n_(598088, "count_down", lambda: count_down), _n_(598089, "work", lambda: work))
        _l_(598091)
        _c_(598094, _a_(598093, _n_(598092, "timer_text", lambda: timer_text), "config"), text="WORK :)")
        _l_(598095)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    _l_(598141)

    global time
    _l_(598099)
    count_minute = _c_(598103, _a_(598101, _n_(598100, "math", lambda: math), "floor"), _n_(598102, "count", lambda: count) / 60)
    _l_(598104)
    count_seconds = _n_(598105, "count", lambda: count) % 60
    _l_(598106)
    if _n_(598107, "count_seconds", lambda: count_seconds) < 10:
        _l_(598110)

        count_seconds = f"0{_n_(598108, 'count_seconds', lambda: count_seconds)}"
        _l_(598109)
    _c_(598116, _a_(598112, _n_(598111, "canvas", lambda: canvas), "itemconfig"), _n_(598113, "timer", lambda: timer), text=f"{_n_(598114, 'count_minute', lambda: count_minute)}:{_n_(598115, 'count_seconds', lambda: count_seconds)}")
    _l_(598117)
    if _n_(598118, "count", lambda: count) > 0:
        _l_(598140)

        timing = _c_(598123, _a_(598120, _n_(598119, "window", lambda: window), "after"), 1000, _n_(598121, "count_down", lambda: count_down), _n_(598122, "count", lambda: count) - 1)
        _l_(598124)
    else:
        if _n_(598125, "reps", lambda: reps) % 8 != 0 and _n_(598126, "reps", lambda: reps) % 2 == 0:
            _l_(598136)

            text = _c_(598129, _n_(598127, "int", lambda: int), _n_(598128, "reps", lambda: reps) / 2) * "✔"
            _l_(598130)
            _c_(598134, _a_(598132, _n_(598131, "my_label", lambda: my_label), "config"), text=_n_(598133, "text", lambda: text))
            _l_(598135)
        _c_(598138, _n_(598137, "start", lambda: start))
        _l_(598139)
# ---------------------------- UI SETUP ------------------------------- #


window = _c_(598143, _n_(598142, "Tk", lambda: Tk))
_l_(598144)
_c_(598147, _a_(598146, _n_(598145, "window", lambda: window), "title"), "Pomodoro")
_l_(598148)
_c_(598152, _a_(598150, _n_(598149, "window", lambda: window), "config"), padx=100, pady=50, bg=_n_(598151, "YELLOW", lambda: YELLOW))
_l_(598153)

canvas = _c_(598156, _n_(598154, "Canvas", lambda: Canvas), width=200, height=224, bg=_n_(598155, "YELLOW", lambda: YELLOW), highlightthickness=0)
_l_(598157)
tomato_img = _c_(598159, _n_(598158, "PhotoImage", lambda: PhotoImage), file="tomato.png")
_l_(598160)
_c_(598164, _a_(598162, _n_(598161, "canvas", lambda: canvas), "create_image"), 100, 112, image=_n_(598163, "tomato_img", lambda: tomato_img))
_l_(598165)
timer = _c_(598169, _a_(598167, _n_(598166, "canvas", lambda: canvas), "create_text"), 103, 138, text="00:00", fill="white", font=(_n_(598168, "FONT_NAME", lambda: FONT_NAME), 35, "bold"))
_l_(598170)
_c_(598173, _a_(598172, _n_(598171, "canvas", lambda: canvas), "grid"), row=1, column=1)
_l_(598174)

button_one = _c_(598177, _n_(598175, "Button", lambda: Button), text="Start", command=_n_(598176, "start", lambda: start))
_l_(598178)
_c_(598181, _a_(598180, _n_(598179, "button_one", lambda: button_one), "grid"), row=2, column=0)
_l_(598182)

button_two = _c_(598185, _n_(598183, "Button", lambda: Button), text="Reset", command=_n_(598184, "reset_pomo", lambda: reset_pomo))
_l_(598186)
_c_(598189, _a_(598188, _n_(598187, "button_two", lambda: button_two), "grid"), row=2, column=2)
_l_(598190)

my_label = _c_(598194, _n_(598191, "Label", lambda: Label), bg=_n_(598192, "YELLOW", lambda: YELLOW), fg=_n_(598193, "GREEN", lambda: GREEN))
_l_(598195)
_c_(598198, _a_(598197, _n_(598196, "my_label", lambda: my_label), "grid"), row=2, column=1)
_l_(598199)

timer_text = _c_(598204, _n_(598200, "Label", lambda: Label), text="TIMER", font=(_n_(598201, "FONT_NAME", lambda: FONT_NAME), 35, "bold"), fg=_n_(598202, "GREEN", lambda: GREEN), bg=_n_(598203, "YELLOW", lambda: YELLOW))
_l_(598205)
_c_(598208, _a_(598207, _n_(598206, "timer_text", lambda: timer_text), "grid"), row=0, column=1)
_l_(598209)

_c_(598212, _a_(598211, _n_(598210, "window", lambda: window), "mainloop"))
_l_(598213)
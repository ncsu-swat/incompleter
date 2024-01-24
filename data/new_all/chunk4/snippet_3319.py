# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75709003/attributeerror-module-emotions-has-no-attribute-emotion
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from greetings import greeting
    _l_(592862)

except ImportError:
    pass
try:
    from emotions import emotion
    _l_(592864)

except ImportError:
    pass

_c_(592867, _a_(592866, _n_(592865, "customtkinter", lambda: customtkinter), "set_appearance_mode"), "Dark")
_l_(592868)
_c_(592871, _a_(592870, _n_(592869, "customtkinter", lambda: customtkinter), "set_default_color_theme"), 'blue')
_l_(592872)

chosen_greeting = _c_(592875, _a_(592874, _n_(592873, "greeting", lambda: greeting), "choose_greeting"))
_l_(592876)

app = _c_(592879, _a_(592878, _n_(592877, "customtkinter", lambda: customtkinter), "CTk")) # Create screen
_l_(592880) # Create screen
screen_width = _c_(592883, _a_(592882, _n_(592881, "app", lambda: app), "winfo_screenwidth"))
_l_(592884)
screen_height = _c_(592887, _a_(592886, _n_(592885, "app", lambda: app), "winfo_screenheight"))
_l_(592888)
_c_(592893, _a_(592890, _n_(592889, "app", lambda: app), "geometry"), f"{_n_(592891, 'screen_width', lambda: screen_width)}x{_n_(592892, 'screen_height', lambda: screen_height)}")
_l_(592894)
_c_(592897, _a_(592896, _n_(592895, "app", lambda: app), "title"), "Login")
_l_(592898)


def check_emotion():
    _l_(592942)

    found_emotion = _c_(592901, _a_(592900, _n_(592899, "emotion", lambda: emotion), "check"))
    _l_(592902)
    if _n_(592903, "found_emotion", lambda: found_emotion) == '0004302X':
        _l_(592941)

        text = _c_(592906, _a_(592905, _n_(592904, "chat", lambda: chat), "cget"), "text")
        _l_(592907)
        text = _c_(592910, _a_(592909, _n_(592908, "emotion", lambda: emotion), "not_found"))
        _l_(592911)
        _c_(592915, _a_(592913, _n_(592912, "chat", lambda: chat), "configure"), text=_n_(592914, "text", lambda: text))
        _l_(592916)
    elif _n_(592917, "found_emotion", lambda: found_emotion) == '00492X':
        _l_(592940)

        the_emotion = _c_(592920, _a_(592919, _n_(592918, "emotion", lambda: emotion), "goodBad"))
        _l_(592921)
        if _n_(592922, "the_emotion", lambda: the_emotion) == 'bad':
            _l_(592939)

            _c_(592924, _n_(592923, "print", lambda: print), "bad")
            _l_(592925)
        elif _n_(592926, "the_emotion", lambda: the_emotion) == 'good':
            _l_(592938)

            _c_(592928, _n_(592927, "print", lambda: print), 'good')
            _l_(592929)
        elif _n_(592930, "the_emotion", lambda: the_emotion) == 'meh':
            _l_(592937)

            _c_(592932, _n_(592931, "print", lambda: print), 'meh')
            _l_(592933)
        else:
            _c_(592935, _n_(592934, "print", lambda: print), 'error')
            _l_(592936)

def HomeAI():
    _l_(593010)

    global chat
    _l_(592943)
    global text_given
    _l_(592944)

    _c_(592947, _a_(592946, _n_(592945, "app", lambda: app), "destroy"))
    _l_(592948)
    home = _c_(592951, _a_(592950, _n_(592949, "customtkinter", lambda: customtkinter), "CTk"))
    _l_(592952)
    _c_(592957, _a_(592954, _n_(592953, "home", lambda: home), "geometry"), f"{_n_(592955, 'screen_width', lambda: screen_width)}x{_n_(592956, 'screen_height', lambda: screen_height)}")
    _l_(592958)
    _c_(592961, _a_(592960, _n_(592959, "home", lambda: home), "title"), 'AI screen')
    _l_(592962)

    #AIChat = customtkinter.CTkScrollableFrame(master=home, width=1000, height=900)
    #AIChat.place(rely=0.45, relx=0.5, anchor=tkinter.CENTER)

    chat = _c_(592966, _a_(592964, _n_(592963, "customtkinter", lambda: customtkinter), "CTkLabel"), master=_n_(592965, "home", lambda: home), text="", font=('', 20))
    _l_(592967)
    _c_(592972, _a_(592969, _n_(592968, "chat", lambda: chat), "place"), relx=0.3, rely=0.3, anchor=_a_(592971, _n_(592970, "tkinter", lambda: tkinter), "CENTER"))
    _l_(592973)

    _c_(592976, _a_(592975, _n_(592974, "chat", lambda: chat), "cget"), "text")
    _l_(592977)
    _c_(592981, _a_(592979, _n_(592978, "chat", lambda: chat), "configure"), text=_n_(592980, "chosen_greeting", lambda: chosen_greeting))
    _l_(592982)

    text_given = _c_(592986, _a_(592984, _n_(592983, "customtkinter", lambda: customtkinter), "CTkEntry"), master=_n_(592985, "home", lambda: home), width=500, placeholder_text="Enter message", font=('', 20))
    _l_(592987)
    _c_(592992, _a_(592989, _n_(592988, "text_given", lambda: text_given), "place"), relx=0.85, rely=0.9, anchor=_a_(592991, _n_(592990, "tkinter", lambda: tkinter), "CENTER"))
    _l_(592993)

    submit = _c_(592998, _a_(592995, _n_(592994, "customtkinter", lambda: customtkinter), "CTkButton"), master=_n_(592996, "home", lambda: home), width=30, text="Enter", font=('', 20), command=_n_(592997, "check_emotion", lambda: check_emotion))
    _l_(592999)
    _c_(593004, _a_(593001, _n_(593000, "submit", lambda: submit), "place"), relx=0.7, rely=0.9, anchor=_a_(593003, _n_(593002, "tkinter", lambda: tkinter), "CENTER"))
    _l_(593005)




    _c_(593008, _a_(593007, _n_(593006, "home", lambda: home), "mainloop"))
    _l_(593009)
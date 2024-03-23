# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55066875/typeerror-register-user-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def register_user(self):
    _l_(671554)


    username_info = _c_(671510, _a_(671509, _a_(671508, _n_(671507, "self", lambda: self), "username"), "get"))
    _l_(671511)
    password_info = _c_(671515, _a_(671514, _a_(671513, _n_(671512, "self", lambda: self), "password"), "get"))
    _l_(671516)

    file = _c_(671518, _n_(671517, "open", lambda: open), r"C:\Users\ashita.gadagotti\Desktop\username_info.txt", "w+")
    _l_(671519)
    _c_(671523, _a_(671521, _n_(671520, "file", lambda: file), "write"), _n_(671522, "username_info", lambda: username_info) + "\n")
    _l_(671524)
    _c_(671528, _a_(671526, _n_(671525, "file", lambda: file), "write"), _n_(671527, "password_info", lambda: password_info))
    _l_(671529)
    _c_(671532, _a_(671531, _n_(671530, "file", lambda: file), "close"))
    _l_(671533)

    _c_(671537, _a_(671535, _n_(671534, "username_entry", lambda: username_entry), "delete"), 0, _n_(671536, "END", lambda: END))
    _l_(671538)
    _c_(671542, _a_(671540, _n_(671539, "password_entry", lambda: password_entry), "delete"), 0, _n_(671541, "END", lambda: END))
    _l_(671543)

    _c_(671552, _a_(671551, _c_(671550, _n_(671544, "Label", lambda: Label), _n_(671545, "self", lambda: self), text="Registration Success.Please log in with the new credentials.", fg="green", font=("calibri", 11),command = lambda: _c_(671549, _a_(671547, _n_(671546, "master", lambda: master), "switch_frame"), _n_(671548, "login_page", lambda: login_page))), "pack"))
    _l_(671553)

def login_verify(self):
    _l_(671608)

    username1 = _c_(671558, _a_(671557, _a_(671556, _n_(671555, "self", lambda: self), "username_entry1"), "get"))
    _l_(671559)
    password1 = _c_(671563, _a_(671562, _a_(671561, _n_(671560, "self", lambda: self), "password_entry1"), "get"))
    _l_(671564)

    _c_(671568, _a_(671566, _n_(671565, "username_entry1", lambda: username_entry1), "delete"), 0, _n_(671567, "END", lambda: END))
    _l_(671569)
    _c_(671573, _a_(671571, _n_(671570, "password_entry1", lambda: password_entry1), "delete"), 0, _n_(671572, "END", lambda: END))
    _l_(671574)

    logindetails = _c_(671577, _a_(671576, _n_(671575, "os", lambda: os), "listdir"), r"C:\Users\ashita.gadagotti\Desktop\username_info.txt")
    _l_(671578)
    if _n_(671579, "username1", lambda: username1) == _n_(671580, "logindetails", lambda: logindetails):
        _l_(671607)

        file1 = _c_(671583, _n_(671581, "open", lambda: open), _n_(671582, "username1", lambda: username1), "r")
        _l_(671584)
        verify = _c_(671589, _a_(671588, _c_(671587, _a_(671586, _n_(671585, "file1", lambda: file1), "read")), "splitlines"))
        _l_(671590)
        if _n_(671591, "password1", lambda: password1) in _n_(671592, "verify", lambda: verify):
            _l_(671602)

            _c_(671596, _a_(671594, _n_(671593, "master", lambda: master), "switch_frame"), _n_(671595, "SearchPage", lambda: SearchPage))
            _l_(671597)
        else:
            _c_(671600, _a_(671599, _n_(671598, "tm", lambda: tm), "showerror"), "Login error","password has not been recognized")
            _l_(671601)
    else:
        _c_(671605, _a_(671604, _n_(671603, "tm", lambda: tm), "showerror"), "Login error","User not found!")
        _l_(671606)

class searchpage(_a_(671610, _n_(671609, "tk", lambda: tk), "Frame")):
    _l_(671637)

    def __init__(self, master):
        _l_(671636)

        _c_(671616, _a_(671613, _a_(671612, _n_(671611, "tk", lambda: tk), "Frame"), "__init__"), _n_(671614, "self", lambda: self), _n_(671615, "master", lambda: master))
        _l_(671617)
        _c_(671623, _a_(671622, _c_(671621, _a_(671619, _n_(671618, "tk", lambda: tk), "Label"), _n_(671620, "self", lambda: self), text="SearchPage"), "grid"), row = 0)
        _l_(671624)
        _c_(671629, _a_(671628, _c_(671627, _a_(671626, _n_(671625, "tk", lambda: tk), "Entry")), "grid"), row = 1)
        _l_(671630)
        _c_(671634, _a_(671632, _n_(671631, "tk", lambda: tk), "Button"), _n_(671633, "self", lambda: self), text="Search")
        _l_(671635)

if _n_(671638, "__name__", lambda: __name__) == "__main__":
    _l_(671654)

    app = _c_(671640, _n_(671639, "SampleApp", lambda: SampleApp))
    _l_(671641)
    _c_(671644, _a_(671643, _n_(671642, "app", lambda: app), "title"), "Equiniti Search Engine")
    _l_(671645)
    _c_(671648, _a_(671647, _n_(671646, "app", lambda: app), "geometry"), '1280x720')
    _l_(671649)
    _c_(671652, _a_(671651, _n_(671650, "app", lambda: app), "mainloop"))
    _l_(671653)
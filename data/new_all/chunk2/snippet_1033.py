# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52043575/attribute-error-window-has-no-object-namee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(452682)

except ImportError:
    pass


class Window:
    _l_(452949)

    def __init__(self, master):
        _l_(452724)

        _n_(452683, "self", lambda: self).master = _n_(452684, "master", lambda: master)
        _l_(452685)
        _c_(452688, _a_(452687, _n_(452686, "root", lambda: root), "title"), "Sign Up or Login")
        _l_(452689)
        _c_(452692, _a_(452691, _n_(452690, "root", lambda: root), "minsize"), width=300, height=300)
        _l_(452693)
        _c_(452696, _a_(452695, _n_(452694, "root", lambda: root), "maxsize"), width=300,height=300)
        _l_(452697)

        _n_(452698, "self", lambda: self).login_button = _c_(452703, _n_(452699, "Button", lambda: Button), _n_(452700, "master", lambda: master), text = "Login", width=18,height=4, command=_a_(452702, _n_(452701, "self", lambda: self), "LoginPage"))
        _l_(452704)
        _n_(452705, "self", lambda: self).signup_button = _c_(452710, _n_(452706, "Button", lambda: Button), _n_(452707, "master", lambda: master), text = "Sign Up", width=18,height=4, command=_a_(452709, _n_(452708, "self", lambda: self), "SignupPage"))
        _l_(452711)

        _c_(452716, _a_(452714, _a_(452713, _n_(452712, "self", lambda: self), "login_button"), "place"), relx=0.5, rely=0.3, anchor=_n_(452715, "CENTER", lambda: CENTER))
        _l_(452717)
        _c_(452722, _a_(452720, _a_(452719, _n_(452718, "self", lambda: self), "signup_button"), "place"), relx=0.5, rely=0.7, anchor=_n_(452721, "CENTER", lambda: CENTER))
        _l_(452723)

    def LoginPage(self):
        _l_(452795)


        _c_(452727, _a_(452726, _n_(452725, "root", lambda: root), "title"), "Login")
        _l_(452728)
        _c_(452732, _a_(452731, _a_(452730, _n_(452729, "self", lambda: self), "login_button"), "place_forget"))
        _l_(452733)
        _c_(452737, _a_(452736, _a_(452735, _n_(452734, "self", lambda: self), "signup_button"), "place_forget"))
        _l_(452738)

        _n_(452739, "self", lambda: self).text_username = _c_(452742, _n_(452740, "Label", lambda: Label), _n_(452741, "root", lambda: root), text = "Username : ")
        _l_(452743)
        _n_(452744, "self", lambda: self).text_password = _c_(452747, _n_(452745, "Label", lambda: Label), _n_(452746, "root", lambda: root), text = "Password : ")
        _l_(452748)

        _n_(452749, "self", lambda: self).usernameE = _c_(452752, _n_(452750, "Entry", lambda: Entry), _n_(452751, "root", lambda: root))
        _l_(452753)
        _n_(452754, "self", lambda: self).passwordE = _c_(452757, _n_(452755, "Entry", lambda: Entry), _n_(452756, "root", lambda: root))
        _l_(452758)

        _c_(452763, _a_(452761, _a_(452760, _n_(452759, "self", lambda: self), "text_username"), "place"), relx=0.3, rely= 0.4, anchor=_n_(452762, "CENTER", lambda: CENTER))
        _l_(452764)
        _c_(452769, _a_(452767, _a_(452766, _n_(452765, "self", lambda: self), "text_password"), "place"), relx=0.3, rely= 0.6, anchor=_n_(452768, "CENTER", lambda: CENTER))
        _l_(452770)

        _c_(452775, _a_(452773, _a_(452772, _n_(452771, "self", lambda: self), "usernameE"), "place"), relx=0.65,rely= 0.4, anchor=_n_(452774, "CENTER", lambda: CENTER))
        _l_(452776)
        _c_(452781, _a_(452779, _a_(452778, _n_(452777, "self", lambda: self), "passwordE"), "place"), relx=0.65,rely= 0.6, anchor=_n_(452780, "CENTER", lambda: CENTER))
        _l_(452782)

        _n_(452783, "self", lambda: self).submit_button_login = _c_(452788, _n_(452784, "Button", lambda: Button), _n_(452785, "root", lambda: root), text="Submit", command=_a_(452787, _n_(452786, "self", lambda: self), "SubmitInfo"))
        _l_(452789)
        _c_(452793, _a_(452792, _a_(452791, _n_(452790, "self", lambda: self), "submit_button_login"), "place"), relx=0.7,rely=0.7)
        _l_(452794)



    def SignupPage(self):
        _l_(452906)


        _c_(452798, _a_(452797, _n_(452796, "root", lambda: root), "title"), "Sign Up")
        _l_(452799)
        _c_(452803, _a_(452802, _a_(452801, _n_(452800, "self", lambda: self), "login_button"), "place_forget"))
        _l_(452804)
        _c_(452808, _a_(452807, _a_(452806, _n_(452805, "self", lambda: self), "signup_button"), "place_forget"))
        _l_(452809)

        _n_(452810, "self", lambda: self).text_name = _c_(452813, _n_(452811, "Label", lambda: Label), _n_(452812, "root", lambda: root), text = "Name :")
        _l_(452814)
        _n_(452815, "self", lambda: self).text_age = _c_(452818, _n_(452816, "Label", lambda: Label), _n_(452817, "root", lambda: root), text = "Age :")
        _l_(452819)
        _n_(452820, "self", lambda: self).text_username = _c_(452823, _n_(452821, "Label", lambda: Label), _n_(452822, "root", lambda: root), text = "Username :")
        _l_(452824)
        _n_(452825, "self", lambda: self).text_password = _c_(452828, _n_(452826, "Label", lambda: Label), _n_(452827, "root", lambda: root), text = "Password :")
        _l_(452829)

        _c_(452834, _a_(452832, _a_(452831, _n_(452830, "self", lambda: self), "text_name"), "place"), relx=0.2, rely=0.2, anchor=_n_(452833, "CENTER", lambda: CENTER))
        _l_(452835)
        _c_(452840, _a_(452838, _a_(452837, _n_(452836, "self", lambda: self), "text_age"), "place"), relx=0.2,rely=0.4, anchor=_n_(452839, "CENTER", lambda: CENTER))
        _l_(452841)
        _c_(452846, _a_(452844, _a_(452843, _n_(452842, "self", lambda: self), "text_username"), "place"), relx=0.2,rely=0.6,anchor=_n_(452845, "CENTER", lambda: CENTER))
        _l_(452847)
        _c_(452852, _a_(452850, _a_(452849, _n_(452848, "self", lambda: self), "text_password"), "place"), relx=0.2,rely=0.8,anchor=_n_(452851, "CENTER", lambda: CENTER))
        _l_(452853)

        _n_(452854, "self", lambda: self).nameE = _c_(452857, _n_(452855, "Entry", lambda: Entry), _n_(452856, "root", lambda: root))
        _l_(452858)
        _n_(452859, "self", lambda: self).ageE = _c_(452862, _n_(452860, "Entry", lambda: Entry), _n_(452861, "root", lambda: root))
        _l_(452863)
        _n_(452864, "self", lambda: self).usernameE2 = _c_(452867, _n_(452865, "Entry", lambda: Entry), _n_(452866, "root", lambda: root))
        _l_(452868)
        _n_(452869, "self", lambda: self).passwordE2 = _c_(452872, _n_(452870, "Entry", lambda: Entry), _n_(452871, "root", lambda: root))
        _l_(452873)

        _c_(452877, _a_(452876, _a_(452875, _n_(452874, "self", lambda: self), "nameE"), "place"), relx= 0.4, rely=0.2)
        _l_(452878)
        _c_(452882, _a_(452881, _a_(452880, _n_(452879, "self", lambda: self), "ageE"), "place"), relx=0.4,rely=0.4)
        _l_(452883)
        _c_(452887, _a_(452886, _a_(452885, _n_(452884, "self", lambda: self), "usernameE2"), "place"), relx=0.4,rely=0.6)
        _l_(452888)
        _c_(452892, _a_(452891, _a_(452890, _n_(452889, "self", lambda: self), "passwordE2"), "place"), relx=0.4,rely=0.8)
        _l_(452893)

        _n_(452894, "self", lambda: self).submit_button_signup = _c_(452899, _n_(452895, "Button", lambda: Button), _n_(452896, "root", lambda: root), text="Submit", command=_a_(452898, _n_(452897, "self", lambda: self), "SubmitInfo"))
        _l_(452900)
        _c_(452904, _a_(452903, _a_(452902, _n_(452901, "self", lambda: self), "submit_button_signup"), "place"), relx= 0.7, rely=0.9)
        _l_(452905)

    def SubmitInfo(self):
        _l_(452948)


        _n_(452907, "self", lambda: self).username_login = _c_(452911, _a_(452910, _a_(452909, _n_(452908, "self", lambda: self), "usernameE"), "get"))
        _l_(452912)
        _n_(452913, "self", lambda: self).password_login = _c_(452917, _a_(452916, _a_(452915, _n_(452914, "self", lambda: self), "passwordE"), "get"))
        _l_(452918)
        _n_(452919, "self", lambda: self).name_signup = _c_(452923, _a_(452922, _a_(452921, _n_(452920, "self", lambda: self), "nameE"), "get"))
        _l_(452924)
        _n_(452925, "self", lambda: self).age_signup = _c_(452929, _a_(452928, _a_(452927, _n_(452926, "self", lambda: self), "ageE"), "get"))
        _l_(452930)
        _n_(452931, "self", lambda: self).username_signup = _c_(452935, _a_(452934, _a_(452933, _n_(452932, "self", lambda: self), "usernameE2"), "get"))
        _l_(452936)
        _n_(452937, "self", lambda: self).password_signup = _c_(452941, _a_(452940, _a_(452939, _n_(452938, "self", lambda: self), "passwordE2"), "get"))
        _l_(452942)
        _c_(452946, _n_(452943, "print", lambda: print), _a_(452945, _n_(452944, "self", lambda: self), "username_login"))
        _l_(452947)


root = _c_(452951, _n_(452950, "Tk", lambda: Tk))
_l_(452952)

run = _c_(452955, _n_(452953, "Window", lambda: Window), _n_(452954, "root", lambda: root))
_l_(452956)

_c_(452959, _a_(452958, _n_(452957, "root", lambda: root), "mainloop"))
_l_(452960)
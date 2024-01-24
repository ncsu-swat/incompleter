# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53286181/typeerror-book-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class main_menu(_n_(344601, "Screen", lambda: Screen)):
    _l_(344753)

    def __init__(self, **kwargs):
        _l_(344749)

        _c_(344605, _a_(344603, _n_(344602, "super", lambda: super)(), "__init__"), **_n_(344604, "kwargs", lambda: kwargs))
        _l_(344606)
        _n_(344607, "self", lambda: self).pic = _a_(344609, _n_(344608, "self", lambda: self), "ids")["pic"]
        _l_(344610)
        _n_(344611, "self", lambda: self).pic1 = _a_(344613, _n_(344612, "self", lambda: self), "ids")["pic1"]
        _l_(344614)
        _n_(344615, "self", lambda: self).ac=_a_(344617, _n_(344616, "self", lambda: self), "ids")["ac"]
        _l_(344618)
        _n_(344619, "self", lambda: self).sd=_a_(344621, _n_(344620, "self", lambda: self), "ids")["sd"]
        _l_(344622)
        _c_(344625, _n_(344623, "print", lambda: print), _n_(344624, "phone", lambda: phone))
        _l_(344626)

        #self.ac.text=self.user_text.text
        #print(self.l.user_text.text,"jkckhjkfgh")

        _n_(344627, "self", lambda: self).lst = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
        _l_(344628)
        _n_(344629, "self", lambda: self).sql="select * from snm"
        _l_(344630)
        _c_(344635, _a_(344632, _n_(344631, "cursor", lambda: cursor), "execute"), _a_(344634, _n_(344633, "self", lambda: self), "sql"))
        _l_(344636)
        _n_(344637, "self", lambda: self).result = _c_(344640, _a_(344639, _n_(344638, "cursor", lambda: cursor), "fetchall"))
        _l_(344641)


        _c_(344665, _a_(344644, _a_(344643, _n_(344642, "self", lambda: self), "pic"), "add_widget"), _c_(344664, _n_(344645, "Button", lambda: Button), text = _c_(344649, _a_(344646, "               {}     ", "format"), _a_(344648, _n_(344647, "self", lambda: self), "result")[0][0])  + '\n' +
                                        _c_(344655, _a_(344650, "                  {} , {} ", "format"), _a_(344652, _n_(344651, "self", lambda: self), "result")[0][2],_a_(344654, _n_(344653, "self", lambda: self), "result")[0][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(344659, _a_(344656, "               {}", "format"), _a_(344658, _n_(344657, "self", lambda: self), "result")[0][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(344661, _n_(344660, "self", lambda: self), "lst")[0]
                                   ,on_press=_a_(344663, _n_(344662, "self", lambda: self), "book")
                                   ))
        _l_(344666)




        _c_(344690, _a_(344669, _a_(344668, _n_(344667, "self", lambda: self), "pic"), "add_widget"), _c_(344689, _n_(344670, "Button", lambda: Button), text=_c_(344674, _a_(344671, "               {}     ", "format"), _a_(344673, _n_(344672, "self", lambda: self), "result")[1][0]) + '\n' +
                                        _c_(344680, _a_(344675, "                  {} , {} ", "format"), _a_(344677, _n_(344676, "self", lambda: self), "result")[1][2], _a_(344679, _n_(344678, "self", lambda: self), "result")[1][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(344684, _a_(344681, "               {}", "format"), _a_(344683, _n_(344682, "self", lambda: self), "result")[1][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(344686, _n_(344685, "self", lambda: self), "lst")[1]
                                   ,on_press=_a_(344688, _n_(344687, "self", lambda: self), "book")
                                   ))
        _l_(344691)




        _c_(344715, _a_(344694, _a_(344693, _n_(344692, "self", lambda: self), "pic"), "add_widget"), _c_(344714, _n_(344695, "Button", lambda: Button), text=_c_(344699, _a_(344696, "               {}     ", "format"), _a_(344698, _n_(344697, "self", lambda: self), "result")[2][0]) + '\n' +
                                        _c_(344705, _a_(344700, "                  {} , {} ", "format"), _a_(344702, _n_(344701, "self", lambda: self), "result")[2][2], _a_(344704, _n_(344703, "self", lambda: self), "result")[2][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(344709, _a_(344706, "              {}", "format"), _a_(344708, _n_(344707, "self", lambda: self), "result")[2][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(344711, _n_(344710, "self", lambda: self), "lst")[2]
                                   ,on_press=_a_(344713, _n_(344712, "self", lambda: self), "book")
                                   ))
        _l_(344716)




        _c_(344740, _a_(344719, _a_(344718, _n_(344717, "self", lambda: self), "pic"), "add_widget"), _c_(344739, _n_(344720, "Button", lambda: Button), text=_c_(344724, _a_(344721, "               {}     ", "format"), _a_(344723, _n_(344722, "self", lambda: self), "result")[3][0]) + '\n' +
                                        _c_(344730, _a_(344725, "                  {} , {} ", "format"), _a_(344727, _n_(344726, "self", lambda: self), "result")[3][2], _a_(344729, _n_(344728, "self", lambda: self), "result")[3][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(344734, _a_(344731, "               {}", "format"), _a_(344733, _n_(344732, "self", lambda: self), "result")[3][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(344736, _n_(344735, "self", lambda: self), "lst")[3]
                                   ,on_press=_a_(344738, _n_(344737, "self", lambda: self), "book")
                                   ))
        _l_(344741)
        _n_(344742, "self", lambda: self).h = 4
        _l_(344743)
        _a_(344745, _n_(344744, "self", lambda: self), "pic").size = (100, _a_(344747, _n_(344746, "self", lambda: self), "h") *600)
        _l_(344748)
    def book(self):
        _l_(344752)

        _n_(344750, "sm", lambda: sm).current="book_ticket"
        _l_(344751)
class PopUp(_n_(344754, "Popup", lambda: Popup)):
    _l_(344766)

    def set(self):
        _l_(344765)

        _n_(344755, "self", lambda: self).title = 'Wrong Login Details'
        _l_(344756)
        _n_(344757, "self", lambda: self).content = _c_(344759, _n_(344758, "Label", lambda: Label), text = 'You have entered wrong Login Details',font_size=30)
        _l_(344760)
        _n_(344761, "self", lambda: self).size_hint = (None,None)
        _l_(344762)
        _n_(344763, "self", lambda: self).size = (600,250)
        _l_(344764)
class book_ticket(_n_(344767, "Screen", lambda: Screen)):
    _l_(344774)

    def __init__(self,**kwargs):
        _l_(344773)

        _c_(344771, _a_(344769, _n_(344768, "super", lambda: super)(), "__init__"), **_n_(344770, "kwargs", lambda: kwargs))
        _l_(344772)
t1=_c_(344776, _n_(344775, "signin", lambda: signin), name='signin')
_l_(344777)
t2=_c_(344779, _n_(344778, "details", lambda: details), name='details')
_l_(344780)
t3=_c_(344782, _n_(344781, "main_menu", lambda: main_menu), name="main_menu")
_l_(344783)
t4=_c_(344785, _n_(344784, "book_ticket", lambda: book_ticket), name="book_ticket")
_l_(344786)
_c_(344789, _n_(344787, "print", lambda: print), _n_(344788, "phone", lambda: phone))
_l_(344790)
_c_(344795, _n_(344791, "print", lambda: print), _c_(344794, _n_(344792, "type", lambda: type), _n_(344793, "t1", lambda: t1)))
_l_(344796)
            #print(t1.user_text.text,phone,23)
            #create local login applic def Start(self):
sm = _c_(344798, _n_(344797, "ScreenManager", lambda: ScreenManager))
_l_(344799)
_c_(344803, _a_(344801, _n_(344800, "sm", lambda: sm), "add_widget"), _n_(344802, "t1", lambda: t1))
_l_(344804)
_c_(344808, _a_(344806, _n_(344805, "sm", lambda: sm), "add_widget"), _n_(344807, "t2", lambda: t2))
_l_(344809)
_c_(344813, _a_(344811, _n_(344810, "sm", lambda: sm), "add_widget"), _n_(344812, "t3", lambda: t3))
_l_(344814)
_c_(344818, _a_(344816, _n_(344815, "sm", lambda: sm), "add_widget"), _n_(344817, "t4", lambda: t4))
_l_(344819)
class main(_n_(344820, "App", lambda: App)):
    _l_(344825)

    def build(self):
        _l_(344824)

        aux = _c_(344822, _n_(344821, "main_menu", lambda: main_menu))
        _l_(344823)
        return aux
_c_(344829, _a_(344828, _c_(344827, _n_(344826, "main", lambda: main)), "run"))
_l_(344830)
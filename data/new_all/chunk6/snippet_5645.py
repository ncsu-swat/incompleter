# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53286181/typeerror-book-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class main_menu(_n_(340668, "Screen", lambda: Screen)):
    _l_(340820)

    def __init__(self, **kwargs):
        _l_(340816)

        _c_(340672, _a_(340670, _n_(340669, "super", lambda: super)(), "__init__"), **_n_(340671, "kwargs", lambda: kwargs))
        _l_(340673)
        _n_(340674, "self", lambda: self).pic = _a_(340676, _n_(340675, "self", lambda: self), "ids")["pic"]
        _l_(340677)
        _n_(340678, "self", lambda: self).pic1 = _a_(340680, _n_(340679, "self", lambda: self), "ids")["pic1"]
        _l_(340681)
        _n_(340682, "self", lambda: self).ac=_a_(340684, _n_(340683, "self", lambda: self), "ids")["ac"]
        _l_(340685)
        _n_(340686, "self", lambda: self).sd=_a_(340688, _n_(340687, "self", lambda: self), "ids")["sd"]
        _l_(340689)
        _c_(340692, _n_(340690, "print", lambda: print), _n_(340691, "phone", lambda: phone))
        _l_(340693)

        #self.ac.text=self.user_text.text
        #print(self.l.user_text.text,"jkckhjkfgh")

        _n_(340694, "self", lambda: self).lst = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
        _l_(340695)
        _n_(340696, "self", lambda: self).sql="select * from snm"
        _l_(340697)
        _c_(340702, _a_(340699, _n_(340698, "cursor", lambda: cursor), "execute"), _a_(340701, _n_(340700, "self", lambda: self), "sql"))
        _l_(340703)
        _n_(340704, "self", lambda: self).result = _c_(340707, _a_(340706, _n_(340705, "cursor", lambda: cursor), "fetchall"))
        _l_(340708)


        _c_(340732, _a_(340711, _a_(340710, _n_(340709, "self", lambda: self), "pic"), "add_widget"), _c_(340731, _n_(340712, "Button", lambda: Button), text = _c_(340716, _a_(340713, "               {}     ", "format"), _a_(340715, _n_(340714, "self", lambda: self), "result")[0][0])  + '\n' +
                                        _c_(340722, _a_(340717, "                  {} , {} ", "format"), _a_(340719, _n_(340718, "self", lambda: self), "result")[0][2],_a_(340721, _n_(340720, "self", lambda: self), "result")[0][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(340726, _a_(340723, "               {}", "format"), _a_(340725, _n_(340724, "self", lambda: self), "result")[0][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(340728, _n_(340727, "self", lambda: self), "lst")[0]
                                   ,on_press=_a_(340730, _n_(340729, "self", lambda: self), "book")
                                   ))
        _l_(340733)




        _c_(340757, _a_(340736, _a_(340735, _n_(340734, "self", lambda: self), "pic"), "add_widget"), _c_(340756, _n_(340737, "Button", lambda: Button), text=_c_(340741, _a_(340738, "               {}     ", "format"), _a_(340740, _n_(340739, "self", lambda: self), "result")[1][0]) + '\n' +
                                        _c_(340747, _a_(340742, "                  {} , {} ", "format"), _a_(340744, _n_(340743, "self", lambda: self), "result")[1][2], _a_(340746, _n_(340745, "self", lambda: self), "result")[1][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(340751, _a_(340748, "               {}", "format"), _a_(340750, _n_(340749, "self", lambda: self), "result")[1][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(340753, _n_(340752, "self", lambda: self), "lst")[1]
                                   ,on_press=_a_(340755, _n_(340754, "self", lambda: self), "book")
                                   ))
        _l_(340758)




        _c_(340782, _a_(340761, _a_(340760, _n_(340759, "self", lambda: self), "pic"), "add_widget"), _c_(340781, _n_(340762, "Button", lambda: Button), text=_c_(340766, _a_(340763, "               {}     ", "format"), _a_(340765, _n_(340764, "self", lambda: self), "result")[2][0]) + '\n' +
                                        _c_(340772, _a_(340767, "                  {} , {} ", "format"), _a_(340769, _n_(340768, "self", lambda: self), "result")[2][2], _a_(340771, _n_(340770, "self", lambda: self), "result")[2][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(340776, _a_(340773, "              {}", "format"), _a_(340775, _n_(340774, "self", lambda: self), "result")[2][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(340778, _n_(340777, "self", lambda: self), "lst")[2]
                                   ,on_press=_a_(340780, _n_(340779, "self", lambda: self), "book")
                                   ))
        _l_(340783)




        _c_(340807, _a_(340786, _a_(340785, _n_(340784, "self", lambda: self), "pic"), "add_widget"), _c_(340806, _n_(340787, "Button", lambda: Button), text=_c_(340791, _a_(340788, "               {}     ", "format"), _a_(340790, _n_(340789, "self", lambda: self), "result")[3][0]) + '\n' +
                                        _c_(340797, _a_(340792, "                  {} , {} ", "format"), _a_(340794, _n_(340793, "self", lambda: self), "result")[3][2], _a_(340796, _n_(340795, "self", lambda: self), "result")[3][3])
                                        + "\n\n               Seating Capacity  :"
                                        + _c_(340801, _a_(340798, "               {}", "format"), _a_(340800, _n_(340799, "self", lambda: self), "result")[3][1])
                                   ,font_size=30
                                   ,font_name="font1"
                                   ,background_normal=_a_(340803, _n_(340802, "self", lambda: self), "lst")[3]
                                   ,on_press=_a_(340805, _n_(340804, "self", lambda: self), "book")
                                   ))
        _l_(340808)
        _n_(340809, "self", lambda: self).h = 4
        _l_(340810)
        _a_(340812, _n_(340811, "self", lambda: self), "pic").size = (100, _a_(340814, _n_(340813, "self", lambda: self), "h") *600)
        _l_(340815)
    def book(self):
        _l_(340819)

        _n_(340817, "sm", lambda: sm).current="book_ticket"
        _l_(340818)
class PopUp(_n_(340821, "Popup", lambda: Popup)):
    _l_(340833)

    def set(self):
        _l_(340832)

        _n_(340822, "self", lambda: self).title = 'Wrong Login Details'
        _l_(340823)
        _n_(340824, "self", lambda: self).content = _c_(340826, _n_(340825, "Label", lambda: Label), text = 'You have entered wrong Login Details',font_size=30)
        _l_(340827)
        _n_(340828, "self", lambda: self).size_hint = (None,None)
        _l_(340829)
        _n_(340830, "self", lambda: self).size = (600,250)
        _l_(340831)
class book_ticket(_n_(340834, "Screen", lambda: Screen)):
    _l_(340841)

    def __init__(self,**kwargs):
        _l_(340840)

        _c_(340838, _a_(340836, _n_(340835, "super", lambda: super)(), "__init__"), **_n_(340837, "kwargs", lambda: kwargs))
        _l_(340839)
t1=_c_(340843, _n_(340842, "signin", lambda: signin), name='signin')
_l_(340844)
t2=_c_(340846, _n_(340845, "details", lambda: details), name='details')
_l_(340847)
t3=_c_(340849, _n_(340848, "main_menu", lambda: main_menu), name="main_menu")
_l_(340850)
t4=_c_(340852, _n_(340851, "book_ticket", lambda: book_ticket), name="book_ticket")
_l_(340853)
_c_(340856, _n_(340854, "print", lambda: print), _n_(340855, "phone", lambda: phone))
_l_(340857)
_c_(340862, _n_(340858, "print", lambda: print), _c_(340861, _n_(340859, "type", lambda: type), _n_(340860, "t1", lambda: t1)))
_l_(340863)
            #print(t1.user_text.text,phone,23)
            #create local login applic def Start(self):
sm = _c_(340865, _n_(340864, "ScreenManager", lambda: ScreenManager))
_l_(340866)
_c_(340870, _a_(340868, _n_(340867, "sm", lambda: sm), "add_widget"), _n_(340869, "t1", lambda: t1))
_l_(340871)
_c_(340875, _a_(340873, _n_(340872, "sm", lambda: sm), "add_widget"), _n_(340874, "t2", lambda: t2))
_l_(340876)
_c_(340880, _a_(340878, _n_(340877, "sm", lambda: sm), "add_widget"), _n_(340879, "t3", lambda: t3))
_l_(340881)
_c_(340885, _a_(340883, _n_(340882, "sm", lambda: sm), "add_widget"), _n_(340884, "t4", lambda: t4))
_l_(340886)
class main(_n_(340887, "App", lambda: App)):
    _l_(340892)

    def build(self):
        _l_(340891)

        aux = _c_(340889, _n_(340888, "main_menu", lambda: main_menu))
        _l_(340890)
        return aux
_c_(340896, _a_(340895, _c_(340894, _n_(340893, "main", lambda: main)), "run"))
_l_(340897)
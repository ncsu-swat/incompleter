# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44447862/attributeerror-in-python-regarding-classes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(355702)

except ImportError:
    pass

DEFAULT_FONT = 'Helvetica, 16'
_l_(355703)


class UserInterface:
    _l_(355758)

    def __init__(self):
        _l_(355733)

        _n_(355704, "self", lambda: self)._root_window = _c_(355707, _a_(355706, _n_(355705, "tkinter", lambda: tkinter), "Tk"))
        _l_(355708)

        _n_(355709, "self", lambda: self)._canvas = _c_(355714, _a_(355711, _n_(355710, "tkinter", lambda: tkinter), "Canvas"), master=_a_(355713, _n_(355712, "self", lambda: self), "_root_window"),
                                      width=400,
                                      height=400,
                                      background='#2A722E')
        _l_(355715)

        _c_(355727, _a_(355718, _a_(355717, _n_(355716, "self", lambda: self), "_canvas"), "grid"), row=0,
                          column=0,
                          padx=30,
                          pady=30,
                          sticky=_a_(355720, _n_(355719, "tkinter", lambda: tkinter), "W") + _a_(355722, _n_(355721, "tkinter", lambda: tkinter), "E") + _a_(355724, _n_(355723, "tkinter", lambda: tkinter), "N") + _a_(355726, _n_(355725, "tkinter", lambda: tkinter), "S"))
        _l_(355728)

        _c_(355731, _a_(355730, _n_(355729, "self", lambda: self), "_ask_user_input"))
        _l_(355732)

    def run(self):
        _l_(355739)

        _c_(355737, _a_(355736, _a_(355735, _n_(355734, "self", lambda: self), "_root_window"), "mainloop"))
        _l_(355738)

    def _ask_user_input(self):
        _l_(355757)

        user_input = _c_(355741, _n_(355740, "UserInput", lambda: UserInput))
        _l_(355742)
        _c_(355745, _a_(355744, _n_(355743, "user_input", lambda: user_input), "show"))
        _l_(355746)

        if _c_(355749, _a_(355748, _n_(355747, "user_input", lambda: user_input), "ok_is_clicked")):
            _l_(355756)

            input_list = _c_(355752, _a_(355751, _n_(355750, "user_input", lambda: user_input), "get_input_list"))
            _l_(355753)
            aux = _n_(355754, "input_list", lambda: input_list)
            _l_(355755)
            return aux


class UserInput:
    _l_(355952)

    def __init__(self):
        _l_(355893)

        _n_(355759, "self", lambda: self)._user_input = _c_(355762, _a_(355761, _n_(355760, "tkinter", lambda: tkinter), "Toplevel"))
        _l_(355763)

        row_num = _c_(355769, _a_(355765, _n_(355764, "tkinter", lambda: tkinter), "Label"), master=_a_(355767, _n_(355766, "self", lambda: self), "_user_input"),
                                text='Specify a row number 4-16:',
                                font=_n_(355768, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355770)
        _c_(355775, _a_(355772, _n_(355771, "row_num", lambda: row_num), "grid"), row=0,
                     column=0,
                     padx=10,
                     pady=10,
                     sticky=_a_(355774, _n_(355773, "tkinter", lambda: tkinter), "W"))
        _l_(355776)

        _n_(355777, "self", lambda: self)._row_num_entry = _c_(355783, _a_(355779, _n_(355778, "tkinter", lambda: tkinter), "Entry"), master=_a_(355781, _n_(355780, "self", lambda: self), "_user_input"),
                                            width=15,
                                            font=_n_(355782, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355784)
        _c_(355790, _a_(355787, _a_(355786, _n_(355785, "self", lambda: self), "_row_num_entry"), "grid"), row=0,
                                 column=1,
                                 padx=10,
                                 pady=10,
                                 sticky=_a_(355789, _n_(355788, "tkinter", lambda: tkinter), "E"))
        _l_(355791)

        col_num = _c_(355797, _a_(355793, _n_(355792, "tkinter", lambda: tkinter), "Label"), master=_a_(355795, _n_(355794, "self", lambda: self), "_user_input"),
                                text='Specify a column number 4-16:',
                                font=_n_(355796, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355798)
        _c_(355803, _a_(355800, _n_(355799, "col_num", lambda: col_num), "grid"), row=1,
                     column=0,
                     padx=10,
                     pady=10,
                     sticky=_a_(355802, _n_(355801, "tkinter", lambda: tkinter), "W"))
        _l_(355804)

        _n_(355805, "self", lambda: self)._col_num_entry = _c_(355811, _a_(355807, _n_(355806, "tkinter", lambda: tkinter), "Entry"), master=_a_(355809, _n_(355808, "self", lambda: self), "_user_input"),
                                            width=15,
                                            font=_n_(355810, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355812)
        _c_(355818, _a_(355815, _a_(355814, _n_(355813, "self", lambda: self), "_col_num_entry"), "grid"), row=1,
                                 column=1,
                                 padx=10,
                                 pady=10, sticky=_a_(355817, _n_(355816, "tkinter", lambda: tkinter), "E"))
        _l_(355819)

        first_player = _c_(355825, _a_(355821, _n_(355820, "tkinter", lambda: tkinter), "Label"), master=_a_(355823, _n_(355822, "self", lambda: self), "_user_input"),
                                     text='Specify the first player B/W:',
                                     font=_n_(355824, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355826)
        _c_(355831, _a_(355828, _n_(355827, "first_player", lambda: first_player), "grid"), row=2,
                          column=0,
                          padx=10,
                          pady=10,
                          sticky=_a_(355830, _n_(355829, "tkinter", lambda: tkinter), "W"))
        _l_(355832)

        _n_(355833, "self", lambda: self)._first_player_entry = _c_(355839, _a_(355835, _n_(355834, "tkinter", lambda: tkinter), "Entry"), master=_a_(355837, _n_(355836, "self", lambda: self), "_user_input"),
                                                 width=15,
                                                 font=_n_(355838, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355840)
        _c_(355846, _a_(355843, _a_(355842, _n_(355841, "self", lambda: self), "_first_player_entry"), "grid"), row=2,
                                      column=1,
                                      padx=10,
                                      pady=10,
                                      sticky=_a_(355845, _n_(355844, "tkinter", lambda: tkinter), "W"))
        _l_(355847)

        win_condition = _c_(355853, _a_(355849, _n_(355848, "tkinter", lambda: tkinter), "Label"), master=_a_(355851, _n_(355850, "self", lambda: self), "_user_input"),
                                      text='Specify a winning condition, < or >:',
                                      font=_n_(355852, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355854)
        _c_(355859, _a_(355856, _n_(355855, "win_condition", lambda: win_condition), "grid"), row=3,
                           column=0,
                           padx=10,
                           pady=10,
                           sticky=_a_(355858, _n_(355857, "tkinter", lambda: tkinter), "W"))
        _l_(355860)

        _n_(355861, "self", lambda: self)._win_condition_entry = _c_(355867, _a_(355863, _n_(355862, "tkinter", lambda: tkinter), "Entry"), master=_a_(355865, _n_(355864, "self", lambda: self), "_user_input"),
                                                  width=15,
                                                  font=_n_(355866, "DEFAULT_FONT", lambda: DEFAULT_FONT))
        _l_(355868)
        _c_(355874, _a_(355871, _a_(355870, _n_(355869, "self", lambda: self), "_win_condition_entry"), "grid"), row=3,
                                       column=1,
                                       padx=10,
                                       pady=10,
                                       sticky=_a_(355873, _n_(355872, "tkinter", lambda: tkinter), "E"))
        _l_(355875)

        ok_button = _c_(355883, _a_(355877, _n_(355876, "tkinter", lambda: tkinter), "Button"), master=_a_(355879, _n_(355878, "self", lambda: self), "_user_input"),
                                   text='OK',
                                   font=_n_(355880, "DEFAULT_FONT", lambda: DEFAULT_FONT),
                                   command=_a_(355882, _n_(355881, "self", lambda: self), "_ok_button_clicked"))
        _l_(355884)
        _c_(355887, _a_(355886, _n_(355885, "ok_button", lambda: ok_button), "grid"), row=4,
                       columnspan=2,
                       padx=40,
                       pady=40)
        _l_(355888)

        _n_(355889, "self", lambda: self)._ok_clicked = False
        _l_(355890)
        _n_(355891, "self", lambda: self)._input_list = []
        _l_(355892)

    def show(self) -> None:
        _l_(355904)

        _c_(355897, _a_(355896, _a_(355895, _n_(355894, "self", lambda: self), "_user_input"), "grab_set"))
        _l_(355898)
        _c_(355902, _a_(355901, _a_(355900, _n_(355899, "self", lambda: self), "_user_input"), "wait_window"))
        _l_(355903)

    def ok_is_clicked(self) -> _n_(355905, "bool", lambda: bool):
        _l_(355909)

        aux = _a_(355907, _n_(355906, "self", lambda: self), "_ok_clicked")
        _l_(355908)
        return aux

    def _ok_button_clicked(self):
        _l_(355946)

        _n_(355910, "self", lambda: self)._ok_clicked = True
        _l_(355911)

        row_num = _c_(355915, _a_(355914, _a_(355913, _n_(355912, "self", lambda: self), "_row_num_entry"), "get"))
        _l_(355916)
        col_num = _c_(355920, _a_(355919, _a_(355918, _n_(355917, "self", lambda: self), "_col_num_entry"), "get"))
        _l_(355921)
        starter = _c_(355925, _a_(355924, _a_(355923, _n_(355922, "self", lambda: self), "_first_player_entry"), "get"))
        _l_(355926)
        winning = _c_(355930, _a_(355929, _a_(355928, _n_(355927, "self", lambda: self), "_win_condition_entry"), "get"))
        _l_(355931)

        _c_(355939, _a_(355934, _a_(355933, _n_(355932, "self", lambda: self), "_input_list"), "extend"), [_n_(355935, "row_num", lambda: row_num), _n_(355936, "col_num", lambda: col_num), _n_(355937, "starter", lambda: starter), _n_(355938, "winning", lambda: winning)])
        _l_(355940)

        _c_(355944, _a_(355943, _a_(355942, _n_(355941, "self", lambda: self), "_user_input"), "destroy"))
        _l_(355945)

    def get_input_list(self) -> _n_(355947, "list", lambda: list):
        _l_(355951)

        aux = _a_(355949, _n_(355948, "self", lambda: self), "_input_list")
        _l_(355950)
        return aux


if _n_(355953, "__name__", lambda: __name__) == '__main__':
    _l_(355961)

    game = _c_(355955, _n_(355954, "UserInterface", lambda: UserInterface))
    _l_(355956)
    _c_(355959, _a_(355958, _n_(355957, "game", lambda: game), "run"))
    _l_(355960)
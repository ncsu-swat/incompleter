# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68279152/tkinter-button-attributeerror-when-trying-to-use-a-class-method-for-the-comman
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SelectUserPage(_a_(433718, _n_(433717, "tk", lambda: tk), "Frame")):
    _l_(433899)

    def __init__(self, master):
        _l_(433898)

        _c_(433724, _a_(433721, _a_(433720, _n_(433719, "tk", lambda: tk), "Frame"), "__init__"), _n_(433722, "self", lambda: self), _n_(433723, "master", lambda: master))
        _l_(433725)
    
        # Create label which instructs user how to select their profile
        instruct_label = _c_(433729, _a_(433727, _n_(433726, "tk", lambda: tk), "Label"), _n_(433728, "self", lambda: self), text = "Enter your username from the records below")
        _l_(433730)
        _c_(433733, _a_(433732, _n_(433731, "instruct_label", lambda: instruct_label), "grid"), row = 0, column = 0, columnspan = 2, pady = 10)
        _l_(433734)
    
        # Create text entry box with which the user can enter their username
        username_entry_label = _c_(433740, _a_(433739, _c_(433738, _a_(433736, _n_(433735, "tk", lambda: tk), "Label"), _n_(433737, "self", lambda: self), text = "Username"), "grid"), row = 1, column = 0, 
padx = 5)
        _l_(433741)
        _n_(433742, "self", lambda: self).username_entry = _c_(433746, _a_(433744, _n_(433743, "tk", lambda: tk), "Entry"), _n_(433745, "self", lambda: self), width = 30)
        _l_(433747)
        _c_(433751, _a_(433750, _a_(433749, _n_(433748, "self", lambda: self), "username_entry"), "grid"), row = 1, column = 1)
        _l_(433752)
    
        # Create a button which can be used to select a user once username has been entered
        select_button = _c_(433759, _a_(433754, _n_(433753, "tk", lambda: tk), "Button"), _n_(433755, "self", lambda: self), text = "Select User", width = 30, borderwidth = 
                                  _n_(433756, "BTN_BORD_WIDTH", lambda: BTN_BORD_WIDTH),
                                  command = _a_(433758, _n_(433757, "self", lambda: self), "select_user"))
        _l_(433760)
        _c_(433763, _a_(433762, _n_(433761, "select_button", lambda: select_button), "grid"), row = 2, column = 0, columnspan = 2, pady = (15, 5))
        _l_(433764)
    
        # Create a back button
        back_button = _c_(433773, _a_(433766, _n_(433765, "tk", lambda: tk), "Button"), _n_(433767, "self", lambda: self), text = "Back", width = 30, borderwidth = _n_(433768, "BTN_BORD_WIDTH", lambda: BTN_BORD_WIDTH),
                                command = lambda: _c_(433772, _a_(433770, _n_(433769, "master", lambda: master), "change_frame"), _n_(433771, "LoginPage", lambda: LoginPage)))
        _l_(433774)
        _c_(433777, _a_(433776, _n_(433775, "back_button", lambda: back_button), "grid"), row = 3, column = 0, columnspan = 2, pady = 5)
        _l_(433778)
    
        # Display stored user records
        conn = _c_(433781, _a_(433780, _n_(433779, "sql", lambda: sql), "connect"), "application data/database.db")
        _l_(433782)
        c = _c_(433785, _a_(433784, _n_(433783, "conn", lambda: conn), "cursor"))
        _l_(433786)
    
        _c_(433789, _a_(433788, _n_(433787, "c", lambda: c), "execute"), "SELECT * FROM user_info")
        _l_(433790)
        records = _c_(433793, _a_(433792, _n_(433791, "c", lambda: c), "fetchall"))
        _l_(433794)
    
        _c_(433797, _a_(433796, _n_(433795, "conn", lambda: conn), "commit"))
        _l_(433798)
        _c_(433801, _a_(433800, _n_(433799, "conn", lambda: conn), "close"))
        _l_(433802)
    
        username_col = "Username" + "\n"
        _l_(433803)
        user_ID_col = "User_ID" + "\n"
        _l_(433804)
        for record in _n_(433805, "records", lambda: records):
            _l_(433814)

            username_col += _c_(433808, _n_(433806, "str", lambda: str), _n_(433807, "record", lambda: record)[0]) + "\n"
            _l_(433809)
            user_ID_col += _c_(433812, _n_(433810, "str", lambda: str), _n_(433811, "record", lambda: record)[1]) + "\n"
            _l_(433813)
    
        usernames_label = _c_(433819, _a_(433816, _n_(433815, "tk", lambda: tk), "Label"), _n_(433817, "self", lambda: self), text = _n_(433818, "username_col", lambda: username_col))
        _l_(433820)
        _c_(433823, _a_(433822, _n_(433821, "usernames_label", lambda: usernames_label), "grid"), row = 4, column = 0, pady = 10)
        _l_(433824)
    
        user_ID_label = _c_(433829, _a_(433826, _n_(433825, "tk", lambda: tk), "Label"), _n_(433827, "self", lambda: self), text = _n_(433828, "user_ID_col", lambda: user_ID_col))
        _l_(433830)
        _c_(433833, _a_(433832, _n_(433831, "user_ID_label", lambda: user_ID_label), "grid"), row = 4, column = 1, pady = 10)
        _l_(433834)
    
        # Configure frame to horizontally centre widgets
        _c_(433837, _a_(433836, _n_(433835, "self", lambda: self), "grid_columnconfigure"), 0, weight = 1)
        _l_(433838)
        _c_(433841, _a_(433840, _n_(433839, "self", lambda: self), "grid_columnconfigure"), 1, weight = 1)
        _l_(433842)
    
        # Create function which selects a user if they exist in the records
        def select_user(self):
            _l_(433897)

            username = _c_(433846, _a_(433845, _a_(433844, _n_(433843, "self", lambda: self), "username_entry"), "get"))
            _l_(433847)
            if _n_(433848, "username", lambda: username) == "":
                _l_(433850)

                aux = ""
                _l_(433849)
                return aux
        
            conn = _c_(433853, _a_(433852, _n_(433851, "sql", lambda: sql), "connect"), "application data/database")
            _l_(433854)
            c = _c_(433857, _a_(433856, _n_(433855, "conn", lambda: conn), "cursor"))
            _l_(433858)
        
            _c_(433861, _a_(433860, _n_(433859, "c", lambda: c), "execute"), "SELECT username, user_ID FROM user_info")
            _l_(433862)
            records = _c_(433865, _a_(433864, _n_(433863, "c", lambda: c), "fetchall"))
            _l_(433866)
        
            for record in _n_(433867, "records", lambda: records):
                _l_(433888)

                if _n_(433868, "record", lambda: record)[0] == _n_(433869, "username", lambda: username):
                    _l_(433887)

                    _a_(433871, _n_(433870, "master", lambda: master), "username") == _n_(433872, "username", lambda: username)
                    _l_(433873)
                    _a_(433875, _n_(433874, "master", lambda: master), "user_ID") == _n_(433876, "record", lambda: record)[1]
                    _l_(433877)
                
                    _c_(433880, _a_(433879, _n_(433878, "c", lambda: c), "close"))
                    _l_(433881)
                
                    _c_(433885, _a_(433883, _n_(433882, "master", lambda: master), "change_frame"), _n_(433884, "HomePage", lambda: HomePage))
                    _l_(433886)
            _c_(433894, _a_(433891, _a_(433890, _n_(433889, "self", lambda: self), "username_entry"), "delete"), 0, _a_(433893, _n_(433892, "tk", lambda: tk), "END"))
            _l_(433895)
            aux = ""
            _l_(433896)
            return aux
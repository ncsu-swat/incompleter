# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47372780/how-to-debug-typeerror-object-of-type-stringvar-has-no-len-in-python
##


# Functions

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def validate_password(first_pwd, second_pwd):
    _l_(687835)

    """
    validates if password is acceptable
    """

    min_length = 8
    _l_(687719)

    number_of_tests = 6
    _l_(687720)
    test1 = 0 #Both entered passwords are identical.
    _l_(687721) #Both entered passwords are identical.
    test2 = 0 #The password is >= 8 characters in length.
    _l_(687722) #The password is >= 8 characters in length.
    test3 = 0 #if first and last chars are alpha then both must be different
    _l_(687723) #if first and last chars are alpha then both must be different
    test4 = 0 #There are no more than 2 vowels in the password.
    _l_(687724) #There are no more than 2 vowels in the password.
    test5 = 0 #The password has at least 1 alphabetic character
    _l_(687725) #The password has at least 1 alphabetic character
              #in either upper or lower case.
    test6 = 0 #Not all alphabetic characters are in the same
    _l_(687726) #Not all alphabetic characters are in the same
              #case (either all upper or all lower).

    # test1
    if _n_(687727, "first_pwd", lambda: first_pwd) == _n_(687728, "second_pwd", lambda: second_pwd):
        _l_(687730)

        test1 = 1
        _l_(687729)

    password = _n_(687731, "first_pwd", lambda: first_pwd)
    _l_(687732)
    pwd_length = _c_(687735, _n_(687733, "len", lambda: len), _n_(687734, "password", lambda: password))
    _l_(687736)

    # test2
    if _n_(687737, "pwd_length", lambda: pwd_length) >= 8:
        _l_(687739)

        test2 = 1
        _l_(687738)

    # test3

    same = 0
    _l_(687740)

    if _c_(687743, _a_(687742, _n_(687741, "password", lambda: password)[0], "isalpha")) and _c_(687747, _a_(687746, _n_(687744, "password", lambda: password)[_n_(687745, "pwd_length", lambda: pwd_length)-1], "isalpha")):
        _l_(687766)

        if _n_(687748, "password", lambda: password)[0] == _c_(687752, _a_(687751, _n_(687749, "password", lambda: password)[_n_(687750, "pwd_length", lambda: pwd_length)-1], "upper")):
            _l_(687754)

            same = 1
            _l_(687753)
        if _n_(687755, "password", lambda: password)[0] == _c_(687759, _a_(687758, _n_(687756, "password", lambda: password)[_n_(687757, "pwd_length", lambda: pwd_length)-1], "lower")):
            _l_(687761)

            same = 1
            _l_(687760)
        if _n_(687762, "same", lambda: same) == 0:
            _l_(687764)

            test3 = 1
            _l_(687763)

    else:
        test3 = 1
        _l_(687765)


    # test4
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    _l_(687767)
    count = 0
    _l_(687768)
    max_vowels = 2
    _l_(687769)
    for vowel in _n_(687770, "vowels", lambda: vowels):
        _l_(687777)

        count = _n_(687771, "count", lambda: count) + _c_(687775, _a_(687773, _n_(687772, "password", lambda: password), "count"), _n_(687774, "vowel", lambda: vowel))
        _l_(687776)

    if _n_(687778, "count", lambda: count) <= _n_(687779, "max_vowels", lambda: max_vowels):
        _l_(687781)

        test4 = 1
        _l_(687780)

    alpha_chars = []
    _l_(687782)

    # test5
    for char in _n_(687783, "password", lambda: password):
        _l_(687794)

        if _c_(687786, _a_(687785, _n_(687784, "char", lambda: char), "isalpha")):
            _l_(687793)

            _c_(687790, _a_(687788, _n_(687787, "alpha_chars", lambda: alpha_chars), "append"), _n_(687789, "char", lambda: char))
            _l_(687791)
            test5 = 1
            _l_(687792)


    # test6
    alpha_count = _c_(687797, _n_(687795, "len", lambda: len), _n_(687796, "alpha_chars", lambda: alpha_chars))
    _l_(687798)
    upper_count = 0
    _l_(687799)
    lower_count = 0
    _l_(687800)
    for char in _n_(687801, "alpha_chars", lambda: alpha_chars):
        _l_(687816)

        if _n_(687802, "char", lambda: char) == _c_(687805, _a_(687804, _n_(687803, "char", lambda: char), "upper")):
            _l_(687808)

            upper_count = _n_(687806, "upper_count", lambda: upper_count) + 1
            _l_(687807)
        if _n_(687809, "char", lambda: char) == _c_(687812, _a_(687811, _n_(687810, "char", lambda: char), "lower")):
            _l_(687815)

            lower_count = _n_(687813, "lower_count", lambda: lower_count) + 1
            _l_(687814)

    if _n_(687817, "alpha_count", lambda: alpha_count) != _n_(687818, "upper_count", lambda: upper_count) and \
       _n_(687819, "alpha_count", lambda: alpha_count) != _n_(687820, "lower_count", lambda: lower_count):
        _l_(687822)

        test6 = 1
        _l_(687821)

    test_count = _n_(687823, "test1", lambda: test1) + _n_(687824, "test2", lambda: test2) + _n_(687825, "test3", lambda: test3) + _n_(687826, "test4", lambda: test4) \
                 + _n_(687827, "test5", lambda: test5) + _n_(687828, "test6", lambda: test6)
    _l_(687829)

    if _n_(687830, "test_count", lambda: test_count) == _n_(687831, "number_of_tests", lambda: number_of_tests):
        _l_(687833)

        aux = True
        _l_(687832)
        return aux
    aux = False
    _l_(687834)



    return aux
try:
    from tkinter import *
    _l_(687837)

except ImportError:
    pass

root_window = _c_(687839, _n_(687838, "Tk", lambda: Tk))
_l_(687840)

# window title
_c_(687843, _a_(687842, _n_(687841, "root_window", lambda: root_window), "title"), "Title")
_l_(687844)

# window size
_c_(687847, _a_(687846, _n_(687845, "root_window", lambda: root_window), "geometry"), "400x200")
_l_(687848)

# label asking for password
pwd_label = _c_(687851, _n_(687849, "Label", lambda: Label), _n_(687850, "root_window", lambda: root_window), text="Please enter your password")
_l_(687852)
_c_(687855, _a_(687854, _n_(687853, "pwd_label", lambda: pwd_label), "pack"))
_l_(687856)

# pwd entry boxes

pwd1 = _c_(687858, _n_(687857, "StringVar", lambda: StringVar))
_l_(687859)
pwd1_text = _c_(687863, _n_(687860, "Entry", lambda: Entry), _n_(687861, "root_window", lambda: root_window),textvariable=_n_(687862, "pwd1", lambda: pwd1)) 
_l_(687864) 
_c_(687867, _a_(687866, _n_(687865, "pwd1_text", lambda: pwd1_text), "pack"))
_l_(687868)

pwd2 = _c_(687870, _n_(687869, "StringVar", lambda: StringVar))
_l_(687871)
pwd2_text = _c_(687875, _n_(687872, "Entry", lambda: Entry), _n_(687873, "root_window", lambda: root_window),textvariable=_n_(687874, "pwd2", lambda: pwd2)) 
_l_(687876) 
_c_(687879, _a_(687878, _n_(687877, "pwd2_text", lambda: pwd2_text), "pack"))
_l_(687880)

# pwd check button
check_btn = _c_(687887, _n_(687881, "Button", lambda: Button), _n_(687882, "root_window", lambda: root_window),text="Change Password",command=lambda: _c_(687886, _n_(687883, "validate_password", lambda: validate_password), _n_(687884, "pwd1", lambda: pwd1), _n_(687885, "pwd2", lambda: pwd2))) 
_l_(687888) 
_c_(687891, _a_(687890, _n_(687889, "check_btn", lambda: check_btn), "pack")) 
_l_(687892) 




_c_(687895, _a_(687894, _n_(687893, "root_window", lambda: root_window), "mainloop"))
_l_(687896)

##
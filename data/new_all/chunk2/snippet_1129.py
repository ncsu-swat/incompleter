# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37265229/python-filenotfounderror-winerror-3-the-system-cannot-find-the-path-specifie
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shutil
    _l_(472244)

except ImportError:
    pass
try:
    import os
    _l_(472246)

except ImportError:
    pass
try:
    import time
    _l_(472248)

except ImportError:
    pass

with _c_(472250, _n_(472249, "open", lambda: open), 'program_started.txt', 'r+') as program_started_file:
    _l_(472372)

    # If program was previously started, runs instructions. If not, continues as normal
    program_started = _c_(472253, _a_(472252, _n_(472251, "program_started_file", lambda: program_started_file), "read"))
    _l_(472254)
    if _n_(472255, "program_started", lambda: program_started) == 'False':
        _l_(472371)

        # Gets src path file and dst path file, write only
        src_file = _c_(472257, _n_(472256, "open", lambda: open), 'path_src.txt', 'w')
        _l_(472258)
        dst_file = _c_(472260, _n_(472259, "open", lambda: open), 'path_dst.txt', 'w')
        _l_(472261)
        # Gets src and dst paths
        src_path = _c_(472263, _n_(472262, "input", lambda: input), 'Enter source path: ') 
        _l_(472264) 
        dst_path = _c_(472266, _n_(472265, "input", lambda: input), 'Enter destination path: ')
        _l_(472267)
        # Writes src and dst paths to txt file
        _c_(472271, _a_(472269, _n_(472268, "src_file", lambda: src_file), "write"), _n_(472270, "src_path", lambda: src_path))
        _l_(472272)
        _c_(472276, _a_(472274, _n_(472273, "dst_file", lambda: dst_file), "write"), _n_(472275, "dst_path", lambda: dst_path))
        _l_(472277)
        # Moves to beginning of document
        _c_(472280, _a_(472279, _n_(472278, "program_started_file", lambda: program_started_file), "seek"), 0)
        _l_(472281)
        # Writes 'True' in front of prevous 'False'
        _c_(472284, _a_(472283, _n_(472282, "program_started_file", lambda: program_started_file), "write"), 'True')
        _l_(472285)
        # Removes 'False'
        _c_(472288, _a_(472287, _n_(472286, "program_started_file", lambda: program_started_file), "truncate"))
        _l_(472289)
        # Displays 'Completed' message
        _c_(472291, _n_(472290, "print", lambda: print), "Completed getting source and destination paths")
        _l_(472292)
    elif _n_(472293, "program_started", lambda: program_started) == 'True':
        _l_(472370)

        # Gets src path file and dst path file, read only
        src_file = _c_(472295, _n_(472294, "open", lambda: open), 'path_src.txt', 'r')
        _l_(472296)
        dst_file = _c_(472298, _n_(472297, "open", lambda: open), 'path_dst.txt', 'r')
        _l_(472299)
        # Checks if flash drive is plugged in
        while True:
            _l_(472366)

            if _c_(472302, _a_(472301, _n_(472300, "os", lambda: os), "system"), 'cd D:') == 0:
                _l_(472365)

                # Stores src path and dst path in string
                src = _c_(472305, _a_(472304, _n_(472303, "src_file", lambda: src_file), "read"))
                _l_(472306)
                dst = _c_(472309, _a_(472308, _n_(472307, "dst_file", lambda: dst_file), "read"))
                _l_(472310)
                # If a 2nd backup has been made, removes first and renames 2nd
                if _c_(472315, _a_(472313, _a_(472312, _n_(472311, "os", lambda: os), "path"), "isdir"), _n_(472314, "dst", lambda: dst) + "_2") == True:
                    _l_(472337)

                    _c_(472319, _a_(472317, _n_(472316, "os", lambda: os), "rmdir"), _n_(472318, "dst", lambda: dst))
                    _l_(472320)
                    _c_(472325, _a_(472322, _n_(472321, "os", lambda: os), "rename"), _n_(472323, "dst", lambda: dst) + "_2", _n_(472324, "dst", lambda: dst))
                    _l_(472326)
                    dst = _n_(472327, "dst", lambda: dst) + "_2"
                    _l_(472328)
                 # If only a 1st backup was made, creates a 2nd
                elif _c_(472333, _a_(472331, _a_(472330, _n_(472329, "os", lambda: os), "path"), "isdir"), _n_(472332, "dst", lambda: dst)) == True:
                    _l_(472336)

                    dst = _n_(472334, "dst", lambda: dst) + "_2"
                    _l_(472335)
                # Copies data
                _c_(472339, _n_(472338, "print", lambda: print), 'Backing up...', end='')
                _l_(472340)
                _c_(472345, _a_(472342, _n_(472341, "shutil", lambda: shutil), "copytree"), _n_(472343, "src", lambda: src), _n_(472344, "dst", lambda: dst))
                _l_(472346)
                _c_(472348, _n_(472347, "print", lambda: print), 'Completed')
                _l_(472349)
                # Sleeps for 20 minutes
                for x in _c_(472351, _n_(472350, "range", lambda: range), 1,12):
                    _l_(472360)

                    _c_(472354, _n_(472352, "print", lambda: print), "Second: ", _n_(472353, "x", lambda: x))
                    _l_(472355)
                    _c_(472358, _a_(472357, _n_(472356, "time", lambda: time), "sleep"), 1)
                    _l_(472359)
            else:
                # If no flash drive is detected, tries again in 5 minutes. 
                _c_(472363, _a_(472362, _n_(472361, "time", lambda: time), "sleep"), 600)
                _l_(472364)
    else:
        # Error message if program_started.txt != true or false
        _c_(472368, _n_(472367, "print", lambda: print), "Error: program_started.txt must only contain either 'True' or 'False'.")
        _l_(472369)
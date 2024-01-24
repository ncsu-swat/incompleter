# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44179168/typeerror-cant-convert-int-object-to-str-implicitly-when-trying-to-print-a
# Imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(684692)

except ImportError:
    pass
try:
    import os
    _l_(684694)

except ImportError:
    pass

# Main Vars
gmName = "TXT Adventure"
_l_(684695)
gmFileName = "txtAdventure"
_l_(684696)
gmVersion = "2.5.0"
_l_(684697)
gmSplit = "--------"
_l_(684698)

# Player Vars
plHealth = 100
_l_(684699)
plHealthO = 100 # Original Health
_l_(684700) # Original Health
plName = "N/A"
_l_(684701)

# Character Vars
ch1 = "Tom"
_l_(684702)
ch2 = "Josh"
_l_(684703)
ch3 = "Demitrie"
_l_(684704)

# Enemy Vars - en<num>H = heath of enemy
en1 = "Sand Viper"
_l_(684705)
en1H = "5"
_l_(684706)
en2 = "Water Venom Moth"
_l_(684707)
en2H = "7"
_l_(684708)
en3 = "Giant Ant"
_l_(684709)
en3H = "10"
_l_(684710)

# Game
_c_(684712, _n_(684711, "print", lambda: print), "Finished Loading!")
_l_(684713)
_c_(684716, _n_(684714, "print", lambda: print), _n_(684715, "gmSplit", lambda: gmSplit))
_l_(684717)
cont = _c_(684719, _n_(684718, "input", lambda: input), "Press Enter To Continue..")
_l_(684720)
_c_(684723, _n_(684721, "print", lambda: print), _n_(684722, "gmSplit", lambda: gmSplit))
_l_(684724)
_c_(684726, _n_(684725, "print", lambda: print), "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Space from loading screen
_l_(684727) # Space from loading screen
_c_(684730, _n_(684728, "print", lambda: print), "Welcome to " + _n_(684729, "gmName", lambda: gmName) + "!")
_l_(684731)
_c_(684734, _n_(684732, "print", lambda: print), "You are playing on version: " + _n_(684733, "gmVersion", lambda: gmVersion))
_l_(684735)
_c_(684738, _n_(684736, "print", lambda: print), _n_(684737, "gmSplit", lambda: gmSplit))
_l_(684739)
plName = _c_(684741, _n_(684740, "input", lambda: input), "Who are you, son?\n--> ")
_l_(684742)
if _n_(684743, "plName", lambda: plName) == "":
    _l_(684756)

    exit = _c_(684745, _n_(684744, "input", lambda: input), "Invalid Name, Press enter to restart.. ")
    _l_(684746)
    _c_(684750, _a_(684748, _n_(684747, "os", lambda: os), "startfile"), _n_(684749, "gmName", lambda: gmName) + '.py')
    _l_(684751)
    _c_(684754, _a_(684753, _n_(684752, "sys", lambda: sys), "exit"), 0)
    _l_(684755)
if _n_(684757, "plName", lambda: plName) == " ":
    _l_(684770)

    exit = _c_(684759, _n_(684758, "input", lambda: input), "Invalid Name, Press enter to restart.. ")
    _l_(684760)
    _c_(684764, _a_(684762, _n_(684761, "os", lambda: os), "startfile"), _n_(684763, "gmName", lambda: gmName) + '.py')
    _l_(684765)
    _c_(684768, _a_(684767, _n_(684766, "sys", lambda: sys), "exit"), 0)
    _l_(684769)
cont = _c_(684773, _n_(684771, "input", lambda: input), "Press Enter to continue, " + _n_(684772, "plName", lambda: plName) + "!")
_l_(684774)
_c_(684777, _n_(684775, "print", lambda: print), _n_(684776, "gmSplit", lambda: gmSplit))
_l_(684778)
_c_(684782, _n_(684779, "print", lambda: print), _n_(684780, "ch1", lambda: ch1) + ": Well hello, " + _n_(684781, "plName", lambda: plName) + ". Nice to see you!")
_l_(684783)
cont = _c_(684786, _n_(684784, "input", lambda: input), "Press Enter to continue, " + _n_(684785, "plName", lambda: plName) + "!")
_l_(684787)
_c_(684790, _n_(684788, "print", lambda: print), _n_(684789, "gmSplit", lambda: gmSplit))
_l_(684791)
option = _c_(684793, _n_(684792, "input", lambda: input), "What do you want to do?\n1 = Play\n2 = Exit\n--> ")
_l_(684794)
if _n_(684795, "option", lambda: option) == "1":
    _l_(685166)

    cont = _c_(684798, _n_(684796, "input", lambda: input), "Press Enter to continue, " + _n_(684797, "plName", lambda: plName) + "!")
    _l_(684799)
    _c_(684802, _n_(684800, "print", lambda: print), _n_(684801, "gmSplit", lambda: gmSplit))
    _l_(684803)
    plAge = _c_(684806, _n_(684804, "input", lambda: input), "What is your age, " + _n_(684805, "plName", lambda: plName) + "?" + "\n--> ")
    _l_(684807)
    _c_(684810, _n_(684808, "print", lambda: print), _n_(684809, "gmSplit", lambda: gmSplit))
    _l_(684811)
    option2 = _c_(684815, _n_(684812, "input", lambda: input), "So you are " + _n_(684813, "plName", lambda: plName) + " and you are " + _n_(684814, "plAge", lambda: plAge) + " years old?\n1 = True\n2 = False\n--> ")
    _l_(684816)
    if _n_(684817, "option2", lambda: option2) == "1":
        _l_(685138)


        # Start of the game
        _c_(684820, _n_(684818, "print", lambda: print), _n_(684819, "gmSplit", lambda: gmSplit))
        _l_(684821)
        _c_(684825, _n_(684822, "print", lambda: print), "Well welcome to " + _n_(684823, "gmName", lambda: gmName) + ", " + _n_(684824, "plName", lambda: plName) + "!")
        _l_(684826)
        _c_(684829, _n_(684827, "print", lambda: print), _n_(684828, "gmSplit", lambda: gmSplit))
        _l_(684830)
        start = _c_(684832, _n_(684831, "input", lambda: input), "Press Enter To Start The Game..")
        _l_(684833)
        _c_(684836, _n_(684834, "print", lambda: print), _n_(684835, "gmSplit", lambda: gmSplit))
        _l_(684837)
        _c_(684840, _n_(684838, "print", lambda: print), _n_(684839, "ch1", lambda: ch1) + ": Hi there traveler, we are from far away lands!")
        _l_(684841)
        cont = _c_(684843, _n_(684842, "input", lambda: input), "Press Enter To Continue..")
        _l_(684844)
        _c_(684847, _n_(684845, "print", lambda: print), _n_(684846, "gmSplit", lambda: gmSplit))
        _l_(684848)
        _c_(684851, _n_(684849, "print", lambda: print), _n_(684850, "ch2", lambda: ch2) + ": Like the scally said, we' came from a long way away ay!")
        _l_(684852)
        cont = _c_(684854, _n_(684853, "input", lambda: input), "Press Enter To Continue..")
        _l_(684855)
        _c_(684858, _n_(684856, "print", lambda: print), _n_(684857, "gmSplit", lambda: gmSplit))
        _l_(684859)
        _c_(684863, _n_(684860, "print", lambda: print), _n_(684861, "ch1", lambda: ch1) + " + " + _n_(684862, "ch2", lambda: ch2) + ": I WILL KILL UUU!")
        _l_(684864)
        cont = _c_(684866, _n_(684865, "input", lambda: input), "Press Enter To Continue..")
        _l_(684867)
        _c_(684870, _n_(684868, "print", lambda: print), _n_(684869, "gmSplit", lambda: gmSplit))
        _l_(684871)
        option = _c_(684875, _n_(684872, "input", lambda: input), _n_(684873, "ch3", lambda: ch3) + ": Break it up you to! Don't you think, " + _n_(684874, "plName", lambda: plName) + "!\n1 = True\n2 = False\n--> ")
        _l_(684876)
        if _n_(684877, "option", lambda: option) == "1":
            _l_(684903)

            _c_(684881, _n_(684878, "print", lambda: print), _n_(684879, "ch3", lambda: ch3) + ": Well thank you, " + _n_(684880, "plName", lambda: plName) + ".")
            _l_(684882)
            _c_(684886, _n_(684883, "print", lambda: print), _n_(684884, "ch1", lambda: ch1) + " + " + _n_(684885, "ch2", lambda: ch2) + ": Ugh...")
            _l_(684887)
            _c_(684890, _n_(684888, "print", lambda: print), _n_(684889, "gmSplit", lambda: gmSplit))
            _l_(684891)
        else:
            _c_(684894, _n_(684892, "print", lambda: print), _n_(684893, "ch3", lambda: ch3) + ": Oh, i'm sorry, did I upset you..")
            _l_(684895)
            cont = _c_(684897, _n_(684896, "input", lambda: input), "Press Enter To Continue..")
            _l_(684898)
            _c_(684901, _n_(684899, "print", lambda: print), _n_(684900, "gmSplit", lambda: gmSplit))
            _l_(684902)
        _c_(684906, _n_(684904, "print", lambda: print), _n_(684905, "ch3", lambda: ch3) + ": Well anyway, they are still fighting..")
        _l_(684907)
        _c_(684911, _n_(684908, "print", lambda: print), _n_(684909, "ch1", lambda: ch1) + " + " + _n_(684910, "ch2", lambda: ch2) + ": ARAGHHH!")
        _l_(684912)
        _c_(684915, _n_(684913, "print", lambda: print), _n_(684914, "gmSplit", lambda: gmSplit))
        _l_(684916)
        cont = _c_(684918, _n_(684917, "input", lambda: input), "Press Enter To Continue..")
        _l_(684919)
        _c_(684922, _n_(684920, "print", lambda: print), _n_(684921, "gmSplit", lambda: gmSplit))
        _l_(684923)
        _c_(684928, _n_(684924, "print", lambda: print), _n_(684925, "ch1", lambda: ch1) + " + " + _n_(684926, "ch2", lambda: ch2) + " + " + _n_(684927, "ch3", lambda: ch3) + ": Okay lets start the adventure!")
        _l_(684929)
        cont = _c_(684931, _n_(684930, "input", lambda: input), "Press Enter To Continue..")
        _l_(684932)
        way = _c_(684936, _n_(684933, "input", lambda: input), _n_(684934, "ch1", lambda: ch1) + ": Okay, " + _n_(684935, "plName", lambda: plName) + ". What way are we going?\n1 = North\n2 = South\n--> ")
        _l_(684937)
        if _n_(684938, "way", lambda: way) == "1":
            _l_(685017)

            _c_(684941, _n_(684939, "print", lambda: print), _n_(684940, "ch1", lambda: ch1) + ": Okay, lets go north!")
            _l_(684942)
        elif _n_(684943, "way", lambda: way) == "2":
            _l_(685016)

            _c_(684946, _n_(684944, "print", lambda: print), _n_(684945, "ch1", lambda: ch1) + ": Okay, lets go south!")
            _l_(684947)
            _c_(684950, _n_(684948, "print", lambda: print), _n_(684949, "gmSplit", lambda: gmSplit))
            _l_(684951)
            cont = _c_(684953, _n_(684952, "input", lambda: input), "Press Enter To Continue..")
            _l_(684954)
            _c_(684957, _n_(684955, "print", lambda: print), _n_(684956, "gmSplit", lambda: gmSplit))
            _l_(684958)
            _c_(684961, _n_(684959, "print", lambda: print), _n_(684960, "ch3", lambda: ch3) + ": But I dont like going south, it's scary that way..")
            _l_(684962)
            _c_(684965, _n_(684963, "print", lambda: print), _n_(684964, "gmSplit", lambda: gmSplit))
            _l_(684966)
            cont = _c_(684968, _n_(684967, "input", lambda: input), "Press Enter To Continue..")
            _l_(684969)
            _c_(684972, _n_(684970, "print", lambda: print), _n_(684971, "gmSplit", lambda: gmSplit))
            _l_(684973)
            _c_(684978, _n_(684974, "print", lambda: print), _n_(684975, "ch1", lambda: ch1) + " + " + _n_(684976, "ch2", lambda: ch2) + ": Shut up, " + _n_(684977, "ch3", lambda: ch3) + "!")
            _l_(684979)
            _c_(684983, _n_(684980, "print", lambda: print), _n_(684981, "ch3", lambda: ch3) + ": Please don't go this way, " + _n_(684982, "plName", lambda: plName) + " :(")
            _l_(684984)
            option = _c_(684986, _n_(684985, "input", lambda: input), "1 = Continue South\n2 = Go North insted\n--> ")
            _l_(684987)
            if _n_(684988, "option", lambda: option) == "1":
                _l_(685009)

                plHealth -= 5
                _l_(684989)
                _c_(684992, _n_(684990, "print", lambda: print), _n_(684991, "gmSplit", lambda: gmSplit))
                _l_(684993)
                _c_(684997, _n_(684994, "print", lambda: print), _n_(684995, "ch3", lambda: ch3) + ": Why, " + _n_(684996, "plName", lambda: plName) + ". Why did you do this!")
                _l_(684998)
                _c_(685001, _n_(684999, "print", lambda: print), _n_(685000, "gmSplit", lambda: gmSplit))
                _l_(685002)
                _c_(685007, _n_(685003, "print", lambda: print), "*" + _n_(685004, "ch3", lambda: ch3) + " slaps you, your health goes from " + _n_(685005, "plHealthO", lambda: plHealthO) + " to: " + _n_(685006, "plHealth", lambda: plHealth) + "!")
                _l_(685008)
        else:
            _c_(685011, _n_(685010, "print", lambda: print), "You picked an invalid choice!")
            _l_(685012)
            exit = _c_(685014, _n_(685013, "input", lambda: input), "Press enter to re-do choice!")
            _l_(685015)
        _c_(685020, _n_(685018, "print", lambda: print), _n_(685019, "gmSplit", lambda: gmSplit))
        _l_(685021)
        _c_(685025, _n_(685022, "print", lambda: print), "You have encounterd a wild: " + _n_(685023, "en1", lambda: en1) + "! It has " + _n_(685024, "en1H", lambda: en1H) + " health!")
        _l_(685026)
        option = _c_(685028, _n_(685027, "input", lambda: input), "What do you want to do?\n1 = Attack\n2 = Run\n--> ")
        _l_(685029)
        if _n_(685030, "option", lambda: option) == "1":
            _l_(685111)

            en1H = "3"
            _l_(685031)
            plHealth -= 2
            _l_(685032)
            _c_(685036, _n_(685033, "print", lambda: print), "The " + _n_(685034, "en1", lambda: en1) + "'s health has gone down to: " + _n_(685035, "en1H", lambda: en1H) + "!")
            _l_(685037)
            cont = _c_(685039, _n_(685038, "input", lambda: input), "Press Enter To Continue..")
            _l_(685040)
            _c_(685043, _n_(685041, "print", lambda: print), _n_(685042, "gmSplit", lambda: gmSplit))
            _l_(685044)
            _c_(685047, _n_(685045, "print", lambda: print), "The " + _n_(685046, "en1", lambda: en1) + " attacked you!")
            _l_(685048)
            cont = _c_(685050, _n_(685049, "input", lambda: input), "Press Enter To Continue..")
            _l_(685051)
            _c_(685054, _n_(685052, "print", lambda: print), _n_(685053, "gmSplit", lambda: gmSplit))
            _l_(685055)
            _c_(685059, _n_(685056, "print", lambda: print), "Your health was: " + _n_(685057, "plHealthO", lambda: plHealthO) + "But now it has gone down to: " + _n_(685058, "plHealth", lambda: plHealth) + "!")
            _l_(685060)
            cont = _c_(685062, _n_(685061, "input", lambda: input), "Press Enter To Continue..")
            _l_(685063)
            _c_(685066, _n_(685064, "print", lambda: print), _n_(685065, "gmSplit", lambda: gmSplit))
            _l_(685067)
            _c_(685071, _n_(685068, "print", lambda: print), _n_(685069, "ch1", lambda: ch1) + " + " + _n_(685070, "ch2", lambda: ch2) + " Helped  you and killed the beast!")
            _l_(685072)
            cont = _c_(685074, _n_(685073, "input", lambda: input), "Press Enter To Continue..")
            _l_(685075)
            _c_(685078, _n_(685076, "print", lambda: print), _n_(685077, "gmSplit", lambda: gmSplit))
            _l_(685079)
            _c_(685081, _n_(685080, "print", lambda: print), "Okay, where do you want to go now?")
            _l_(685082)
            option = _c_(685084, _n_(685083, "input", lambda: input), "1 = Keep Heading Forward\n2 = Camp for the night\n--> ")
            _l_(685085)
        elif _n_(685086, "option", lambda: option) == "2":
            _l_(685110)

            exit = _c_(685089, _n_(685087, "input", lambda: input), _n_(685088, "en1", lambda: en1))
            _l_(685090)
        else:
            _c_(685092, _n_(685091, "print", lambda: print), "You chose an invalid choice!")
            _l_(685093)
            _c_(685096, _n_(685094, "print", lambda: print), _n_(685095, "gmSplit", lambda: gmSplit))
            _l_(685097)
            restart = _c_(685099, _n_(685098, "input", lambda: input), "Press enter to restart..")
            _l_(685100)
            _c_(685104, _a_(685102, _n_(685101, "os", lambda: os), "startfile"), _n_(685103, "gmFileName", lambda: gmFileName) + '.py')
            _l_(685105)
            _c_(685108, _a_(685107, _n_(685106, "sys", lambda: sys), "exit"), 0)
            _l_(685109)
    elif _n_(685112, "option2", lambda: option2) == "2":
        _l_(685137)

        exit = _c_(685114, _n_(685113, "input", lambda: input), "Press enter to restart.. ")
        _l_(685115)
        _c_(685119, _a_(685117, _n_(685116, "os", lambda: os), "startfile"), _n_(685118, "gmFileName", lambda: gmFileName) + '.py')
        _l_(685120)
        _c_(685123, _a_(685122, _n_(685121, "sys", lambda: sys), "exit"), 0)
        _l_(685124)
    else:
        exit = _c_(685126, _n_(685125, "input", lambda: input), "Press enter to restart.. ")
        _l_(685127)
        _c_(685131, _a_(685129, _n_(685128, "os", lambda: os), "startfile"), _n_(685130, "gmFileName", lambda: gmFileName) + '.py')
        _l_(685132)
        _c_(685135, _a_(685134, _n_(685133, "sys", lambda: sys), "exit"), 0)
        _l_(685136)
elif _n_(685139, "option", lambda: option) == "2":
    _l_(685165)

    exit = _c_(685142, _n_(685140, "input", lambda: input), "Press enter to exit " + _n_(685141, "gmName", lambda: gmName) + ".. ")
    _l_(685143)
    _c_(685147, _a_(685145, _n_(685144, "os", lambda: os), "startfile"), _n_(685146, "gmFileName", lambda: gmFileName) + '.py')
    _l_(685148)
    _c_(685151, _a_(685150, _n_(685149, "sys", lambda: sys), "exit"), 0)
    _l_(685152)
else:
        exit = _c_(685154, _n_(685153, "input", lambda: input), "Press enter to restart.. ")
        _l_(685155)
        _c_(685159, _a_(685157, _n_(685156, "os", lambda: os), "startfile"), _n_(685158, "gmFileName", lambda: gmFileName) + '.py')
        _l_(685160)
        _c_(685163, _a_(685162, _n_(685161, "sys", lambda: sys), "exit"), 0)
        _l_(685164)
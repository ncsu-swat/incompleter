# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71558427/typeerror-write-argument-must-be-str-not-int-error-continues-to-appear
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import winsound
    _l_(622152)

except ImportError:
    pass
try:
    import random
    _l_(622154)

except ImportError:
    pass
try:
    import sys
    _l_(622156)

except ImportError:
    pass
try:
    import time
    _l_(622158)

except ImportError:
    pass


# Slowtype function


def HandleSounds(SoundToPlay, kplaying):
    _l_(622184)

    if _n_(622159, "SoundToPlay", lambda: SoundToPlay) == 'No':
        _l_(622183)

        aux = ""
        _l_(622160)
        return aux
    else:
        sound2Play = f"./sounds/{_n_(622161, 'SoundToPlay', lambda: SoundToPlay)}"
        _l_(622162)
        if _n_(622163, "kplaying", lambda: kplaying):
            _l_(622182)

            _c_(622171, _a_(622165, _n_(622164, "winsound", lambda: winsound), "PlaySound"), _n_(622166, "sound2Play", lambda: sound2Play), _a_(622168, _n_(622167, "winsound", lambda: winsound), "SND_ALIAS") | _a_(622170, _n_(622169, "winsound", lambda: winsound), "SND_ASYNC"))
            _l_(622172)
        else:
            _c_(622180, _a_(622174, _n_(622173, "winsound", lambda: winsound), "PlaySound"), _n_(622175, "sound2Play", lambda: sound2Play), _a_(622177, _n_(622176, "winsound", lambda: winsound), "SND_ALIAS") | _a_(622179, _n_(622178, "winsound", lambda: winsound), "SND_ASYNC"))
            _l_(622181)



def slow_type(t, speed):
    _l_(622222)


    _c_(622186, _n_(622185, "HandleSounds", lambda: HandleSounds), "Typing.wav", True)
    _l_(622187)

    for l in _n_(622188, "t", lambda: t):
        _l_(622212)

        _c_(622193, _a_(622191, _a_(622190, _n_(622189, "sys", lambda: sys), "stdout"), "write"), _n_(622192, "l", lambda: l))
        _l_(622194)
        _c_(622198, _a_(622197, _a_(622196, _n_(622195, "sys", lambda: sys), "stdout"), "flush"))
        _l_(622199)
        _c_(622202, _a_(622201, _n_(622200, "time", lambda: time), "sleep"), .1)
        _l_(622203)
        _c_(622210, _a_(622205, _n_(622204, "time", lambda: time), "sleep"), _c_(622208, _a_(622207, _n_(622206, "random", lambda: random), "random")) * 10.0 / _n_(622209, "speed", lambda: speed))
        _l_(622211)
    _c_(622217, _a_(622214, _n_(622213, "winsound", lambda: winsound), "PlaySound"), None, _a_(622216, _n_(622215, "winsound", lambda: winsound), "SND_ALIAS"))
    _l_(622218)
    _c_(622220, _n_(622219, "print", lambda: print), '')
    _l_(622221)



# loadMap contains the long descriptions which tell the player where they are and what directions/ actions they have. It also contains the actual map.
# The sound file being played using the playsound module seems to play first before the program runs, just throwing that out there.



def loadMap():
    _l_(622452)

    _c_(622225, _n_(622223, "slow_type", lambda: slow_type), "Welcome poor lost soul.", _n_(622224, "mediumText", lambda: mediumText))
    _l_(622226)

    _c_(622229, _n_(622227, "slow_type", lambda: slow_type), "It seems you have been trapped on the grounds of an old estate which has been left to rot and decay within the sands of time.", _n_(622228, "mediumText", lambda: mediumText))
    _l_(622230)

    _c_(622233, _n_(622231, "slow_type", lambda: slow_type), "You have 13 hours to escape, unlock the doors, solve the puzzles and find your way out.", _n_(622232, "mediumText", lambda: mediumText))
    _l_(622234)

    _c_(622237, _n_(622235, "slow_type", lambda: slow_type), "Escape or die trying, the choice is yours.", _n_(622236, "mediumText", lambda: mediumText))
    _l_(622238)

    _c_(622241, _n_(622239, "slow_type", lambda: slow_type), "May the gods be with you...", _n_(622240, "mediumText", lambda: mediumText))
    _l_(622242)

    R1ld = ("I am in the Parlor, how did I end up in this place? ", _n_(622243, "mediumText", lambda: mediumText))
    _l_(622244)

    ("Available directions are east.", _n_(622245, "mediumText", lambda: mediumText))
    _l_(622246)

    R2ld = ("R2 - I am currently in the Grand Library, it seems these books haven't been touched in ages. ", _n_(622247, "mediumText", lambda: mediumText))
    _l_(622248)

    ("Available directions are north or south.", _n_(622249, "mediumText", lambda: mediumText))
    _l_(622250)

    R3ld = ("R3 - I made it to the study. There is old paper everywhere. ", _n_(622251, "mediumText", lambda: mediumText))
    _l_(622252)

    ("Available directions are west or north.", _n_(622253, "mediumText", lambda: mediumText))
    _l_(622254)

    R4ld = ("R4 -Ah, the old servants quarters. There is an odd looking pedestal in the far corner of the room. ", _n_(622255, "mediumText", lambda: mediumText))
    _l_(622256)

    ("Move the dials or leave the room: ", _n_(622257, "mediumText", lambda: mediumText))
    _l_(622258)

    ("Available directions are east or west", _n_(622259, "mediumText", lambda: mediumText))
    _l_(622260)

    R5ld = ("R5 - I am in the kitchen, it reeks of food, a century past its expiration date. ", _n_(622261, "mediumText", lambda: mediumText))
    _l_(622262)

    ("Available directions are west or north", _n_(622263, "mediumText", lambda: mediumText))
    _l_(622264)

    R6ld = ("R6 - This is just a sitting room, There is an odd contraption on the wall. ", _n_(622265, "mediumText", lambda: mediumText))
    _l_(622266)

    ("Available directions are west or south. ", _n_(622267, "mediumText", lambda: mediumText))
    _l_(622268)

    ("Enter the time of moonrise and sunset: ", _n_(622269, "mediumText", lambda: mediumText))
    _l_(622270)

    S7ld = ("R7 - You are now on the second story. ", _n_(622271, "mediumText", lambda: mediumText))
    _l_(622272)

    ("Available directions are west or north", _n_(622273, "mediumText", lambda: mediumText))
    _l_(622274)

    H8ld = ("Proceed down the hallway or go down a level? ", _n_(622275, "mediumText", lambda: mediumText))
    _l_(622276)

    ("Available directions are north or south.", _n_(622277, "mediumText", lambda: mediumText))
    _l_(622278)

    R9ld = ("You proceeded down the hall to the bathroom. ", _n_(622279, "mediumText", lambda: mediumText))
    _l_(622280)

    ("Available directions are east or south.", _n_(622281, "mediumText", lambda: mediumText))
    _l_(622282)

    R10ld = ("Turn around and go into the hall? ", _n_(622283, "mediumText", lambda: mediumText))
    _l_(622284)

    ("There's a code written on the wall, it reads as follows: 1874 ", _n_(622285, "mediumText", lambda: mediumText))
    _l_(622286)

    ("Available directions are east or west.", _n_(622287, "mediumText", lambda: mediumText))
    _l_(622288)

    R11ld = ("You went back into the hall and entered the Porcelain Doll room. The dolls won't stop blinking. ", _n_(622289, "mediumText", lambda: mediumText))
    _l_(622290)

    ("Available directions are east or west.", _n_(622291, "mediumText", lambda: mediumText))
    _l_(622292)

    R12ld = ("You exited the Porcelain Doll room and entered the Funeral Parlor/Dining Room. ", _n_(622293, "mediumText", lambda: mediumText))
    _l_(622294)

    ("Available directions are east or west.", _n_(622295, "mediumText", lambda: mediumText))
    _l_(622296)

    R13ld = ("You left the Funeral Parlor and proceeded to the Laundry Room. ", _n_(622297, "mediumText", lambda: mediumText))
    _l_(622298)

    ("Available directions are south or west.", _n_(622299, "mediumText", lambda: mediumText))
    _l_(622300)

    R14ld = ("You entered the Storage Room. ", _n_(622301, "mediumText", lambda: mediumText))
    _l_(622302)

    ("Available directions are south or north.", _n_(622303, "mediumText", lambda: mediumText))
    _l_(622304)

    E15ld = ("Exit the Storage Room? ", _n_(622305, "mediumText", lambda: mediumText))
    _l_(622306)

    ("Available directions are east or west.", _n_(622307, "mediumText", lambda: mediumText))
    _l_(622308)

    R16ld = ("You exited the Storage Room. ", _n_(622309, "mediumText", lambda: mediumText))
    _l_(622310)

    ("Available directions are  south or north.", _n_(622311, "mediumText", lambda: mediumText))
    _l_(622312)

    S17ld = ("Go upstairs to the Third Floor? ", _n_(622313, "mediumText", lambda: mediumText))
    _l_(622314)

    ("Available directions are south or east.", _n_(622315, "mediumText", lambda: mediumText))
    _l_(622316)

    H18ld = ("You went upstairs, you now find yourself on the Third Floor. ", _n_(622317, "mediumText", lambda: mediumText))
    _l_(622318)
    ("Available directions are north or west.", _n_(622319, "mediumText", lambda: mediumText))
    _l_(622320)

    R19ld = ("Proceed down the hallway? ", _n_(622321, "mediumText", lambda: mediumText))
    _l_(622322)

    ("Available directions are south and west.", _n_(622323, "mediumText", lambda: mediumText))
    _l_(622324)

    R20ld = ("You proceeded down the hall, the stench of mildew is overwhelming. ", _n_(622325, "mediumText", lambda: mediumText))
    _l_(622326)

    ("Available directions are north or west.", _n_(622327, "mediumText", lambda: mediumText))
    _l_(622328)

    R21ld = ("You decided to enter the first bedroom, It reeks of rot and mildew. ", _n_(622329, "mediumText", lambda: mediumText))
    _l_(622330)

    ("Your available directions are south and east.", _n_(622331, "mediumText", lambda: mediumText))
    _l_(622332)

    R22ld = ("You exited the first bedroom and entered the second bedroom. ", _n_(622333, "mediumText", lambda: mediumText))
    _l_(622334)
    ("You wrote down a weird combination etched into the plaster of the wall. ", _n_(622335, "mediumText", lambda: mediumText))
    _l_(622336)

    ("Right 1 time (dial 1), Left 3 times (dial 2), Left 2 times (dial 3), Right 4 times (Dial 4). ", _n_(622337, "mediumText", lambda: mediumText))
    _l_(622338)

    ("(Hint: Try this combination at the pedestal in the Servants Quarters.) ", _n_(622339, "mediumText", lambda: mediumText))
    _l_(622340)

    ("Available directions are south or north.", _n_(622341, "mediumText", lambda: mediumText))
    _l_(622342)

    E23ld = ("Exit the Room? ", _n_(622343, "mediumText", lambda: mediumText))
    _l_(622344)
    ("Available directions are north or west.", _n_(622345, "mediumText", lambda: mediumText))
    _l_(622346)

    H24ld = ("You decided to exit the room and headed back into the hallway. ", _n_(622347, "mediumText", lambda: mediumText))
    _l_(622348)
    ("Available directions are south or east.", _n_(622349, "mediumText", lambda: mediumText))
    _l_(622350)

    R25ld = ("Enter the Guest Bedroom? ", _n_(622351, "mediumText", lambda: mediumText))
    _l_(622352)

    ("Available directions are south or east", _n_(622353, "mediumText", lambda: mediumText))
    _l_(622354)

    R26ld = ("You decided the enter the Guest Bedroom, nothing to see here. ", _n_(622355, "mediumText", lambda: mediumText))
    _l_(622356)
    ("Just old dusty furniture, not worth sitting on. ", _n_(622357, "mediumText", lambda: mediumText))
    _l_(622358)

    ("Available directions are south or north.", _n_(622359, "mediumText", lambda: mediumText))
    _l_(622360)

    R27ld = ("You left the guest bedroom and proceeded down the hall to the Painting Gallery. ", _n_(622361, "mediumText", lambda: mediumText))
    _l_(622362)
    ("Available directions are south or east", _n_(622363, "mediumText", lambda: mediumText))
    _l_(622364)

    R28ld = ("You left the Painting Gallery and entered an Empty Bedroom. ", _n_(622365, "mediumText", lambda: mediumText))
    _l_(622366)
    (" The room is empty, Aside from a set of numbers. ", _n_(622367, "mediumText", lambda: mediumText))
    _l_(622368)

    ("The numbers represent the moonrise time and the time of sunset: 11:27, 6:12. ", _n_(622369, "mediumText", lambda: mediumText))
    _l_(622370)

    ("These numbers could be a clue to the weird lock contraption in the sitting room on the main floor. ", _n_(622371, "mediumText", lambda: mediumText))
    _l_(622372)

    ("You can go either north or east.", _n_(622373, "mediumText", lambda: mediumText))
    _l_(622374)

    S29ld = ("Go upstairs? ", _n_(622375, "mediumText", lambda: mediumText))
    _l_(622376)
    ("Available directions are south or west.", _n_(622377, "mediumText", lambda: mediumText))
    _l_(622378)

    H30ld = ("You are now in the 4th floor hallway. You can go north or west.", _n_(622379, "mediumText", lambda: mediumText))
    _l_(622380)

    R31ld = ("You left the hallway and entered the first room you could open. ", _n_(622381, "mediumText", lambda: mediumText))
    _l_(622382)
    ("You entered the Sitting Room, Maybe you should take a rest. ", _n_(622383, "mediumText", lambda: mediumText))
    _l_(622384)

    ("You can go either east or west.", _n_(622385, "mediumText", lambda: mediumText))
    _l_(622386)

    R32ld = ("You left the confines of the Sitting Room and entered the Smoking Room. ", _n_(622387, "mediumText", lambda: mediumText))
    _l_(622388)
    ("It smells like old cigars.", _n_(622389, "mediumText", lambda: mediumText))
    _l_(622390)

    ("You can go south or east", _n_(622391, "mediumText", lambda: mediumText))
    _l_(622392)

    R33ld = ("You left the Smoking Room and entered the Game Room", _n_(622393, "mediumText", lambda: mediumText))
    _l_(622394)
    (" You can go either south or west.", _n_(622395, "mediumText", lambda: mediumText))
    _l_(622396)

    R34ld = ("You left the Game Room and opened the Master Bedroom. ", _n_(622397, "mediumText", lambda: mediumText))
    _l_(622398)
    ("There is another weird puzzle", _n_(622399, "mediumText", lambda: mediumText))
    _l_(622400)

    ("Your available directions are south or east. ", _n_(622401, "mediumText", lambda: mediumText))
    _l_(622402)

    R35ld = ("You left the Master Bedroom and entered the Balcony. The moon is full. ", _n_(622403, "mediumText", lambda: mediumText))
    _l_(622404)
    ("Directions are south & east.", _n_(622405, "mediumText", lambda: mediumText))
    _l_(622406)

    R36ld = ("You left the Balcony and went back to the Parlor. ", _n_(622407, "mediumText", lambda: mediumText))
    _l_(622408)
    ("You can now leave the manor, proceed? ", _n_(622409, "mediumText", lambda: mediumText))
    _l_(622410)

    ("Please enter the code to escape: ", _n_(622411, "mediumText", lambda: mediumText))
    _l_(622412)



    # Manor Floor plan
    manorMap = {"R1": {"LocDesc": _n_(622413, "R1ld", lambda: R1ld), "e": "R2", "w": "No", "n": "No", "s": "No", "lock": "No", "count": 0},

                "R2": {"LocDesc": _n_(622414, "R2ld", lambda: R2ld), "e": "No", "w": "No", "n": "R1", "s": "R3", "puzzle": "No", "count": 0, "lock": "No"},

                "R3": {"LocDesc": _n_(622415, "R3ld", lambda: R3ld), "e": "No", "w": "R2", "n": "R4", "s": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R4": {"LocDesc": _n_(622416, "R4ld", lambda: R4ld), "e": "R5", "w": "R3", "n": "No", "s": "No", "puzzle": "Rewire",
                       "solution": "Rewire", "lock": "No",
                       "count": 0},

                "R5": {"LocDesc": _n_(622417, "R5ld", lambda: R5ld), "e": "No", "w": "R4", "n": "R6", "s": "No", "puzzle": "No",
                       "lock": "No",
                       "count": 0},

                "R6": {"LocDesc": _n_(622418, "R6ld", lambda: R6ld), "e": "No", "w": "R5", "n": "No", "s": "R7", "Lock": "The Sun & The Moon",
                       "Puzzle": "No", "count": 0},

                "R7": {"LocDesc": _n_(622419, "S7ld", lambda: S7ld), "e": "No", "w": "R6", "n": "R8", "s": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R8": {"LocDesc": _n_(622420, "H8ld", lambda: H8ld), "e": "No", "w": "No", "n": "R9", "s": "R7", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R9": {"LocDesc": _n_(622421, "R9ld", lambda: R9ld), "e": "R10", "w": "No", "s": "R8", "n": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R10": {"LocDesc": _n_(622422, "R10ld", lambda: R10ld), "e": "R11", "w": "R9", "s": "No", "n": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R11": {"LocDesc": _n_(622423, "R11ld", lambda: R11ld), "e": "R12", "w": "R10", "s": "No", "n": "No", "lock": "No", "puzzle": "No",
                        "count": 0},

                "R12": {"LocDesc": _n_(622424, "R12ld", lambda: R12ld), "e": "R13", "w": "R11", "s": "No", "n": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R13": {"LocDesc": _n_(622425, "R13ld", lambda: R13ld), "s": "R12", "n": "No", "e": "No", "w": "R14", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R14": {"LocDesc": _n_(622426, "R14ld", lambda: R14ld), "s": "R15", "n": "R13", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R15": {"LocDesc": _n_(622427, "E15ld", lambda: E15ld), "s": "No", "n": "No", "e": "R14", "w": "R16", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R16": {"LocDesc": _n_(622428, "R16ld", lambda: R16ld), "s": "R15", "n": "R17", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R17": {"LocDesc": _n_(622429, "S17ld", lambda: S17ld), "s": "R16", "n": "No", "e": "R18", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R18": {"LocDesc": _n_(622430, "H18ld", lambda: H18ld), "s": "No", "n": "R17", "e": "No", "w": "R19", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R19": {"LocDesc": _n_(622431, "R19ld", lambda: R19ld), "s": "R20", "n": "No", "e": "No", "w": "R18", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R20": {"LocDesc": _n_(622432, "R20ld", lambda: R20ld), "s": "No", "n": "R19", "e": "No", "w": "R21", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R21": {"LocDesc": _n_(622433, "R21ld", lambda: R21ld), "s": "R22", "n": "No", "e": "R20", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R22": {"LocDesc": _n_(622434, "R22ld", lambda: R22ld), "s": "R23", "n": "R21", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "E23": {"LocDesc": _n_(622435, "E23ld", lambda: E23ld), "s": "No", "n": "R22", "e": "No", "w": "R24", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R24": {"LocDesc": _n_(622436, "H24ld", lambda: H24ld), "s": "R25", "n": "No", "e": "R23", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R25": {"LocDesc": _n_(622437, "R25ld", lambda: R25ld), "s": "R24", "n": "No", "e": "R26", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R26": {"LocDesc": _n_(622438, "R26ld", lambda: R26ld), "s": "R27", "n": "R25", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R27": {"LocDesc": _n_(622439, "R27ld", lambda: R27ld), "s": "R28", "n": "No", "e": "No", "w": "R26", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R28": {"LocDesc": _n_(622440, "R28ld", lambda: R28ld), "s": "No", "n": "R27", "e": "R29", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R29": {"LocDesc": _n_(622441, "S29ld", lambda: S29ld), "s": "R28", "n": "No", "e": "No", "w": "R30", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R30": {"LocDesc": _n_(622442, "H30ld", lambda: H30ld), "s": "No", "n": "R31", "e": "No", "w": "R29", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R31": {"LocDesc": _n_(622443, "R31ld", lambda: R31ld), "s": "No", "n": "No", "e": "R32", "w": "R30", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R32": {"LocDesc": _n_(622444, "R32ld", lambda: R32ld), "s": "R33", "n": "No", "e": "R31", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R33": {"LocDesc": _n_(622445, "R33ld", lambda: R33ld), "s": "R34", "n": "No", "e": "No", "w": "R32", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R34": {"LocDesc": _n_(622446, "R34ld", lambda: R34ld), "s": "R35", "n": "No", "e": "R33", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R35": {"LocDesc": _n_(622447, "R35ld", lambda: R35ld), "s": "R36", "n": "No", "e": "R34", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R36": {"LocDesc": _n_(622448, "R36ld", lambda: R36ld), "s": "No", "n": "R1", "e": "No", "w": "R35", "puzzle": "No", "lock": "No",
                        "count": 0}}
    _l_(622449)
    aux = _n_(622450, "manorMap", lambda: manorMap)
    _l_(622451)

    return aux


def checkDirection(direction, currLock):
    _l_(622467)

    LowerD = _c_(622455, _a_(622454, _n_(622453, "direction", lambda: direction), "casefold"))
    _l_(622456)
    newSpot = _c_(622460, _a_(622458, _n_(622457, "currLock", lambda: currLock), "get"), _n_(622459, "LowerD", lambda: LowerD))
    _l_(622461)

    # print(newSpot)
    if _n_(622462, "newSpot", lambda: newSpot) != "No":
        _l_(622466)

        aux = _n_(622463, "newSpot", lambda: newSpot)
        _l_(622464)

        return aux

    else:
        aux = None
        _l_(622465)

        return aux



slowText = 60
_l_(622468)
mediumText = 200
_l_(622469)
fastText = 300
_l_(622470)
superSlowText = 25
_l_(622471)



maplist = _c_(622473, _n_(622472, "loadMap", lambda: loadMap))
_l_(622474)

startLoc = "R1"
_l_(622475)

prePlayerLoc = _n_(622476, "startLoc", lambda: startLoc)
_l_(622477)

playerLoc = _n_(622478, "startLoc", lambda: startLoc)
_l_(622479)

keepPlaying = True
_l_(622480)


'''def HandleLock1():
    if solvePuzzle == "R36" and input(prompt).isnumeric() == "1874":

        if input(prompt) == "1874":
            print("You Escaped, congratulations! (type q to exit.)")

    if solvePuzzle == "R6" and input(prompt).isnumeric() == "11:27, 6:12":

        if input(prompt) == "11:27" "6:12":
            print("password accepted")'''
_l_(622481)



'''def HandlePuzzle2():
    if solvePuzzle == "R34" and input(prompt).islower() == "eternity":

        if input(prompt) == "eternity":
            print("Password excepted.")

    if solvePuzzle == "R4" and input(prompt).isupper() == "Right , Left , Left, Right":

        if input(prompt) == "Right , Left , Left, Right":
            print("Puzzle Complete!")'''
_l_(622482)



while _n_(622483, "keepPlaying", lambda: keepPlaying):
    _l_(622538)


    currLoc = _c_(622487, _a_(622485, _n_(622484, "maplist", lambda: maplist), "get"), _n_(622486, "playerLoc", lambda: playerLoc))
    _l_(622488)

    lockName = _c_(622491, _a_(622490, _n_(622489, "currLoc", lambda: currLoc), "get"), "lock")
    _l_(622492)

    puzzleName = _c_(622495, _a_(622494, _n_(622493, "currLoc", lambda: currLoc), "get"), "puzzle")
    _l_(622496)

    _n_(622497, "currLoc", lambda: currLoc)["count"] += 1
    _l_(622498)

    _c_(622502, _n_(622499, "print", lambda: print), f"Lock : {_n_(622500, 'lockName', lambda: lockName)} and Puzzle : {_n_(622501, 'puzzleName', lambda: puzzleName)}")
    _l_(622503)

    '''HandleSounds("rain_thunder.mp3", True)'''
    _l_(622504)

    _c_(622510, _n_(622505, "slow_type", lambda: slow_type), _c_(622508, _a_(622507, _n_(622506, "currLoc", lambda: currLoc), "get"), 'LocDesc'), _n_(622509, "mediumText", lambda: mediumText))
    _l_(622511)

    prompt = "\n" + "Lost Soul" + ", What will be your next action? : " + ", Make your choice wisely: "
    _l_(622512)

    playerAction = _c_(622515, _n_(622513, "input", lambda: input), _n_(622514, "prompt", lambda: prompt))
    _l_(622516)

    prevPlayerLoc = _n_(622517, "currLoc", lambda: currLoc)
    _l_(622518)

    if _c_(622521, _a_(622520, _n_(622519, "playerAction", lambda: playerAction), "lower")) == "q":
        _l_(622537)

        keepPlaying = False
        _l_(622522)

    else:

        newLoc = _c_(622528, _n_(622523, "checkDirection", lambda: checkDirection), _c_(622526, _a_(622525, _n_(622524, "playerAction", lambda: playerAction), "lower")), _n_(622527, "currLoc", lambda: currLoc))
        _l_(622529)

        if _n_(622530, "playerLoc", lambda: playerLoc) is not None:
            _l_(622536)


            playerLoc = _n_(622531, "newLoc", lambda: newLoc)
            _l_(622532)

        else:
            _c_(622534, _n_(622533, "print", lambda: print), "This action cannot be completed! Carry on!")
            _l_(622535)
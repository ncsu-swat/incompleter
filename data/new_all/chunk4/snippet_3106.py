# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45897118/attribute-error-python-from-a-new-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import utils
        _l_(615744)

except ImportError:
        pass
try:
        import sys
        _l_(615746)

except ImportError:
        pass


TOTAL_ROOMS = 500
_l_(615747)
rooms = []
_l_(615748)
suite = []
_l_(615749)
reservations = []
_l_(615750)
reservationParts = []
_l_(615751)
roomNum = 0
_l_(615752)
suiteOut = ""
_l_(615753)
suiteF = ""
_l_(615754)
name = ""
_l_(615755)
userInput = ""
_l_(615756)
suiteT = " and is a suite"
_l_(615757)
_c_(615761, _a_(615760, _a_(615759, _n_(615758, "utils", lambda: utils), "users"), "append"), "foo:hello")
_l_(615762)


userInput = _c_(615764, _n_(615763, "input", lambda: input), ">>> ")
_l_(615765)
while True:
        _l_(615918)

        if _n_(615766, "userInput", lambda: userInput) == "new -r":
                _l_(615917)

                _n_(615767, "utils", lambda: utils).username = _c_(615769, _n_(615768, "input", lambda: input), "admin$ -u>>> ")
                _l_(615770)
                _n_(615771, "utils", lambda: utils).password = _c_(615773, _n_(615772, "input", lambda: input), "admin$ -p>>> ")
                _l_(615774)
                _n_(615775, "utils", lambda: utils).credentials = _a_(615777, _n_(615776, "utils", lambda: utils), "username") + ":" + _a_(615779, _n_(615778, "utils", lambda: utils), "password")
                _l_(615780)
                if _c_(615785, _a_(615782, _n_(615781, "utils", lambda: utils), "isUser"), credentialsInput=_a_(615784, _n_(615783, "utils", lambda: utils), "credentials")):
                        _l_(615888)

                        userInput = _c_(615787, _n_(615786, "input", lambda: input), "rsr# -n ")
                        _l_(615788)
                        reservationParts = _c_(615791, _a_(615790, _n_(615789, "userInput", lambda: userInput), "split"))
                        _l_(615792)
                        roomNum = _n_(615793, "reservationParts", lambda: reservationParts)[0]
                        _l_(615794)
                        name = _n_(615795, "reservationParts", lambda: reservationParts)[1]
                        _l_(615796)
                        if _n_(615797, "name", lambda: name) in _n_(615798, "rooms", lambda: rooms):
                                _l_(615809)

                                _c_(615800, _n_(615799, "print", lambda: print), ">>> Room is occupied")
                                _l_(615801)
                        elif _n_(615802, "name", lambda: name) in _a_(615804, _n_(615803, "utils", lambda: utils), "roomName"):
                                _l_(615808)

                                _c_(615806, _n_(615805, "print", lambda: print), ">>> Room is occupied")
                                _l_(615807)
                        _c_(615813, _a_(615811, _n_(615810, "rooms", lambda: rooms), "append"), _n_(615812, "roomNum", lambda: roomNum))
                        _l_(615814)
                        _c_(615819, _a_(615817, _a_(615816, _n_(615815, "utils", lambda: utils), "roomName"), "append"), _n_(615818, "name", lambda: name))
                        _l_(615820)
                        _n_(615821, "utils", lambda: utils).loopCount = 0
                        _l_(615822)
                        if "--suite" in _n_(615823, "userInput", lambda: userInput):
                                _l_(615836)

                                _c_(615826, _a_(615825, _n_(615824, "suite", lambda: suite), "append"), True)
                                _l_(615827)
                                suiteOut = _n_(615828, "suiteT", lambda: suiteT)
                                _l_(615829)
                        else:
                                _c_(615832, _a_(615831, _n_(615830, "suite", lambda: suite), "append"), False)
                                _l_(615833)
                                suiteOut = _n_(615834, "suiteF", lambda: suiteF)
                                _l_(615835)
                        _c_(615847, _a_(615838, _n_(615837, "reservations", lambda: reservations), "append"), "Room " + _n_(615839, "roomNum", lambda: roomNum) + " is filled by " +
                                            _c_(615845, _a_(615842, _a_(615841, _n_(615840, "utils", lambda: utils), "roomName"), "__getitem__"), _a_(615844, _n_(615843, "utils", lambda: utils), "loopCount")) + _n_(615846, "suiteOut", lambda: suiteOut))
                        _l_(615848)
                        for ints in _n_(615849, "rooms", lambda: rooms):
                                _l_(615878)

                                if _c_(615854, _a_(615851, _n_(615850, "suite", lambda: suite), "__getitem__"), _a_(615853, _n_(615852, "utils", lambda: utils), "loopCount")):
                                        _l_(615859)

                                        suiteOut = _n_(615855, "suiteT", lambda: suiteT)
                                        _l_(615856)
                                else:
                                        suiteOut = _n_(615857, "suiteF", lambda: suiteF)
                                        _l_(615858)
                                _c_(615871, _a_(615862, _a_(615861, _n_(615860, "sys", lambda: sys), "stdout"), "write"), "Room " + _n_(615863, "ints", lambda: ints) + " is filled by " +
                                                 _c_(615869, _a_(615866, _a_(615865, _n_(615864, "utils", lambda: utils), "roomName"), "__getitem__"), _a_(615868, _n_(615867, "utils", lambda: utils), "loopCount")) + _n_(615870, "suiteOut", lambda: suiteOut))
                                _l_(615872)
                                _c_(615874, _n_(615873, "print", lambda: print))
                                _l_(615875)
                                _n_(615876, "utils", lambda: utils).loopCount += 1
                                _l_(615877)
                        userInput = _c_(615880, _n_(615879, "input", lambda: input), ">>> ")
                        _l_(615881)
                        if _n_(615882, "userInput", lambda: userInput) == "quit()":
                                _l_(615884)

                                break
                                _l_(615883)
                else:
                        _c_(615886, _n_(615885, "print", lambda: print), "Invalid Credentials")
                        _l_(615887)
        elif _n_(615889, "userInput", lambda: userInput) == "new -u":
                _l_(615916)

                if _c_(615892, _a_(615891, _n_(615890, "utils", lambda: utils), "runCredentialCheck")):
                        _l_(615912)

                        _n_(615893, "utils", lambda: utils).username = _c_(615895, _n_(615894, "input", lambda: input), "new -u -u>>> ")
                        _l_(615896)
                        _n_(615897, "utils", lambda: utils).password = _c_(615899, _n_(615898, "input", lambda: input), "new -u -p>>> ")
                        _l_(615900)
                        _c_(615907, _a_(615902, _n_(615901, "utils", lambda: utils), "registerUser"), creds=(_a_(615904, _n_(615903, "utils", lambda: utils), "username") + ":" + _a_(615906, _n_(615905, "utils", lambda: utils), "password")))
                        _l_(615908)
                else:
                    _c_(615910, _n_(615909, "print", lambda: print), "Invalid Credentials")
                    _l_(615911)
                userInput = _c_(615914, _n_(615913, "input", lambda: input), ">>> ")
                _l_(615915)
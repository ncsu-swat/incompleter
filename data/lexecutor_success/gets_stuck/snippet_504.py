# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class myDate:
    _l_(1546833)


    def __init__(self):
        _l_(1546540)

        _n_(1546488, "self", lambda: self).day = 0
        _l_(1546489)
        _n_(1546490, "self", lambda: self).month = 0
        _l_(1546491)
        _n_(1546492, "self", lambda: self).year = 0
        _l_(1546493)
        ## for checking valid days month and year
        while (True):
            _l_(1546508)

            d = _c_(1546497, _n_(1546494, "int", lambda: int), _c_(1546496, _n_(1546495, "input", lambda: input), "Enter The day :- "))
            _l_(1546498)
            if (_n_(1546499, "d", lambda: d) > 31):
                _l_(1546507)

                _c_(1546501, _n_(1546500, "print", lambda: print), "Plz 1 To 30 value Enter ........")
                _l_(1546502)
            else:
                _n_(1546503, "self", lambda: self).day = _n_(1546504, "d", lambda: d)
                _l_(1546505)
                break
                _l_(1546506)

        while (True):
            _l_(1546523)

            m = _c_(1546512, _n_(1546509, "int", lambda: int), _c_(1546511, _n_(1546510, "input", lambda: input), "Enter The Month :- "))
            _l_(1546513)
            if (_n_(1546514, "m", lambda: m) > 13):
                _l_(1546522)

                _c_(1546516, _n_(1546515, "print", lambda: print), "Plz 1 To 12 value Enter ........")
                _l_(1546517)
            else:
                _n_(1546518, "self", lambda: self).month = _n_(1546519, "m", lambda: m)
                _l_(1546520)
                break
                _l_(1546521)

        while (True):
            _l_(1546539)

            y = _c_(1546527, _n_(1546524, "int", lambda: int), _c_(1546526, _n_(1546525, "input", lambda: input), "Enter The Year :- "))
            _l_(1546528)
            if (_n_(1546529, "y", lambda: y) > 9999 and _n_(1546530, "y", lambda: y) < 0000):
                _l_(1546538)

                _c_(1546532, _n_(1546531, "print", lambda: print), "Plz 0000 To 9999 value Enter ........")
                _l_(1546533)
            else:
                _n_(1546534, "self", lambda: self).year = _n_(1546535, "y", lambda: y)
                _l_(1546536)
                break
                _l_(1546537)
    ## method for aday ands cnttract days
    def adayDays(self, n):
        _l_(1546774)

        ## aday days to date day
        nd = _a_(1546542, _n_(1546541, "self", lambda: self), "day") + _n_(1546543, "n", lambda: n)
        _l_(1546544)
        _c_(1546547, _n_(1546545, "print", lambda: print), _n_(1546546, "nd", lambda: nd))
        _l_(1546548)
        ## check days subtract from date
        if _n_(1546549, "nd", lambda: nd) == 0:
            _l_(1546773)

            if(_a_(1546551, _n_(1546550, "self", lambda: self), "year") % 4 == 0):
                _l_(1546574)

                if(_a_(1546553, _n_(1546552, "self", lambda: self), "month") == 3):
                    _l_(1546562)

                    _n_(1546554, "self", lambda: self).day = 29
                    _l_(1546555)
                    _n_(1546556, "self", lambda: self).month -= 1
                    _l_(1546557)
                    _n_(1546558, "self", lambda: self).year = _a_(1546560, _n_(1546559, "self", lambda: self), "year")
                    _l_(1546561)
            else:
                if(_a_(1546564, _n_(1546563, "self", lambda: self), "month") == 3):
                    _l_(1546573)

                    _n_(1546565, "self", lambda: self).day = 28
                    _l_(1546566)
                    _n_(1546567, "self", lambda: self).month -= 1
                    _l_(1546568)
                    _n_(1546569, "self", lambda: self).year = _a_(1546571, _n_(1546570, "self", lambda: self), "year")
                    _l_(1546572)
            if  (_a_(1546576, _n_(1546575, "self", lambda: self), "month") == 5) or (_a_(1546578, _n_(1546577, "self", lambda: self), "month") == 7) or (_a_(1546580, _n_(1546579, "self", lambda: self), "month") == 8) or (_a_(1546582, _n_(1546581, "self", lambda: self), "month") == 10) or (_a_(1546584, _n_(1546583, "self", lambda: self), "month") == 12):
                _l_(1546619)

                _n_(1546585, "self", lambda: self).day = 30
                _l_(1546586)
                _n_(1546587, "self", lambda: self).month -= 1
                _l_(1546588)
                _n_(1546589, "self", lambda: self).year = _a_(1546591, _n_(1546590, "self", lambda: self), "year")
                _l_(1546592)
            elif (_a_(1546594, _n_(1546593, "self", lambda: self), "month") == 2) or (_a_(1546596, _n_(1546595, "self", lambda: self), "month") == 4) or (_a_(1546598, _n_(1546597, "self", lambda: self), "month") == 6) or (_a_(1546600, _n_(1546599, "self", lambda: self), "month") == 9) or (_a_(1546602, _n_(1546601, "self", lambda: self), "month") == 11):
                _l_(1546618)

                _n_(1546603, "self", lambda: self).day = 31
                _l_(1546604)
                _n_(1546605, "self", lambda: self).month -= 1
                _l_(1546606)
                _n_(1546607, "self", lambda: self).year = _a_(1546609, _n_(1546608, "self", lambda: self), "year")
                _l_(1546610)

            elif(_a_(1546612, _n_(1546611, "self", lambda: self), "month") == 1):
                _l_(1546617)

                _n_(1546613, "self", lambda: self).month = 12
                _l_(1546614)
                _n_(1546615, "self", lambda: self).year -= 1    
                _l_(1546616)    
        ## nd == 0 if condition over
        ## after subtract days to day io goes into negative then
        elif _n_(1546620, "nd", lambda: nd) < 0 :
            _l_(1546772)

            n = _c_(1546623, _n_(1546621, "abs", lambda: abs), _n_(1546622, "n", lambda: n))## return positive if no is negative
            _l_(1546624)## return positive if no is negative
            for i in _c_(1546627, _n_(1546625, "range", lambda: range), _n_(1546626, "n", lambda: n),0,-1):
                _l_(1546684)

                
                if _a_(1546629, _n_(1546628, "self", lambda: self), "day") == 0:
                    _l_(1546683)


                    if _a_(1546631, _n_(1546630, "self", lambda: self), "month") == 1:
                        _l_(1546680)

                        _n_(1546632, "self", lambda: self).day = 30
                        _l_(1546633)
                        
                        _n_(1546634, "self", lambda: self).month = 12
                        _l_(1546635)
                        _n_(1546636, "self", lambda: self).year -= 1
                        _l_(1546637)
                    else:
                        _n_(1546638, "self", lambda: self).month -= 1
                        _l_(1546639)
                        if(_a_(1546641, _n_(1546640, "self", lambda: self), "month") == 1) or (_a_(1546643, _n_(1546642, "self", lambda: self), "month") == 3)or (_a_(1546645, _n_(1546644, "self", lambda: self), "month") == 5) or (_a_(1546647, _n_(1546646, "self", lambda: self), "month") == 7) or (_a_(1546649, _n_(1546648, "self", lambda: self), "month") == 8) or (_a_(1546651, _n_(1546650, "self", lambda: self), "month") == 10) or (_a_(1546653, _n_(1546652, "self", lambda: self), "month") ==12):
                            _l_(1546679)

                            _n_(1546654, "self", lambda: self).day = 30
                            _l_(1546655)
                        elif(_a_(1546657, _n_(1546656, "self", lambda: self), "month") == 4)or (_a_(1546659, _n_(1546658, "self", lambda: self), "month") == 6) or (_a_(1546661, _n_(1546660, "self", lambda: self), "month") == 9) or (_a_(1546663, _n_(1546662, "self", lambda: self), "month") == 11):
                            _l_(1546678)

                            _n_(1546664, "self", lambda: self).day = 29
                            _l_(1546665)
                        elif(_a_(1546667, _n_(1546666, "self", lambda: self), "month") == 2):
                            _l_(1546677)

                            if(_a_(1546669, _n_(1546668, "self", lambda: self), "year") % 4 == 0):
                                _l_(1546676)

                                _a_(1546671, _n_(1546670, "self", lambda: self), "day") == 28
                                _l_(1546672)
                            else:
                                _a_(1546674, _n_(1546673, "self", lambda: self), "day") == 27
                                _l_(1546675)
                else:
                    _n_(1546681, "self", lambda: self).day -= 1
                    _l_(1546682)

        ## enf of elif negative days
        ## adaying days to DATE
        else:
            cnt = 0
            _l_(1546685)
            while (True):
                _l_(1546771)


                if _a_(1546687, _n_(1546686, "self", lambda: self), "month") == 2:
                    _l_(1546770)

                    
                    if(_a_(1546689, _n_(1546688, "self", lambda: self), "year") % 4 == 0):
                        _l_(1546714)

                        if(_n_(1546690, "nd", lambda: nd) > 29):
                            _l_(1546701)

                            cnt = _n_(1546691, "nd", lambda: nd) - 29
                            _l_(1546692)
                            nd = _n_(1546693, "cnt", lambda: cnt)
                            _l_(1546694)
                            _n_(1546695, "self", lambda: self).month += 1
                            _l_(1546696)
                        else:
                            _n_(1546697, "self", lambda: self).day = _n_(1546698, "nd", lambda: nd)
                            _l_(1546699)
                            break
                            _l_(1546700)
                ## if not leap year then
                    else:  
                    
                        if(_n_(1546702, "nd", lambda: nd) > 28):
                            _l_(1546713)

                            cnt = _n_(1546703, "nd", lambda: nd) - 28
                            _l_(1546704)
                            nd = _n_(1546705, "cnt", lambda: cnt)
                            _l_(1546706)
                            _n_(1546707, "self", lambda: self).month += 1
                            _l_(1546708)
                        else:
                            _n_(1546709, "self", lambda: self).day = _n_(1546710, "nd", lambda: nd)
                            _l_(1546711)
                            break
                            _l_(1546712)
                ## checking month other than february month
                elif(_a_(1546716, _n_(1546715, "self", lambda: self), "month") == 1) or (_a_(1546718, _n_(1546717, "self", lambda: self), "month") == 3) or (_a_(1546720, _n_(1546719, "self", lambda: self), "month") == 5) or (_a_(1546722, _n_(1546721, "self", lambda: self), "month") == 7) or (_a_(1546724, _n_(1546723, "self", lambda: self), "month") == 8) or (_a_(1546726, _n_(1546725, "self", lambda: self), "month") == 10) or (_a_(1546728, _n_(1546727, "self", lambda: self), "month") == 12):
                    _l_(1546769)

                    if(_n_(1546729, "nd", lambda: nd) > 31):
                        _l_(1546747)

                        cnt = _n_(1546730, "nd", lambda: nd) - 31
                        _l_(1546731)
                        nd = _n_(1546732, "cnt", lambda: cnt)
                        _l_(1546733)

                        if(_a_(1546735, _n_(1546734, "self", lambda: self), "month") == 12):
                            _l_(1546742)

                            _n_(1546736, "self", lambda: self).month = 1
                            _l_(1546737)
                            _n_(1546738, "self", lambda: self).year += 1
                            _l_(1546739)
                        else:
                            _n_(1546740, "self", lambda: self).month += 1
                            _l_(1546741)
                    else:
                        _n_(1546743, "self", lambda: self).day = _n_(1546744, "nd", lambda: nd)
                        _l_(1546745)
                        break
                        _l_(1546746)

                elif(_a_(1546749, _n_(1546748, "self", lambda: self), "month") == 4) or (_a_(1546751, _n_(1546750, "self", lambda: self), "month") == 6) or (_a_(1546753, _n_(1546752, "self", lambda: self), "month") == 9) or (_a_(1546755, _n_(1546754, "self", lambda: self), "month") == 11):
                    _l_(1546768)

                    if(_n_(1546756, "nd", lambda: nd) > 30):
                        _l_(1546767)

                        cnt = _n_(1546757, "nd", lambda: nd) - 30
                        _l_(1546758)
                        nd = _n_(1546759, "cnt", lambda: cnt)
                        _l_(1546760)
                        _n_(1546761, "self", lambda: self).month += 1
                        _l_(1546762)

                    else:
                        _n_(1546763, "self", lambda: self).day = _n_(1546764, "nd", lambda: nd)
                        _l_(1546765)
                        break
                        _l_(1546766)
    ## end of else condition for adaying days
    def formatDate(self,frmt):
        _l_(1546832)


        if(_n_(1546775, "frmt", lambda: frmt) == 1):
            _l_(1546827)

            ff=_c_(1546779, _n_(1546776, "str", lambda: str), _a_(1546778, _n_(1546777, "self", lambda: self), "day"))+"-"+_c_(1546783, _n_(1546780, "str", lambda: str), _a_(1546782, _n_(1546781, "self", lambda: self), "month"))+"-"+_c_(1546787, _n_(1546784, "str", lambda: str), _a_(1546786, _n_(1546785, "self", lambda: self), "year"))
            _l_(1546788)
        elif(_n_(1546789, "frmt", lambda: frmt) == 2):
            _l_(1546826)

            ff=_c_(1546793, _n_(1546790, "str", lambda: str), _a_(1546792, _n_(1546791, "self", lambda: self), "month"))+"-"+_c_(1546797, _n_(1546794, "str", lambda: str), _a_(1546796, _n_(1546795, "self", lambda: self), "day"))+"-"+_c_(1546801, _n_(1546798, "str", lambda: str), _a_(1546800, _n_(1546799, "self", lambda: self), "year"))
            _l_(1546802)
        elif(_n_(1546803, "frmt", lambda: frmt) == 3):
            _l_(1546825)

            ff =_c_(1546807, _n_(1546804, "str", lambda: str), _a_(1546806, _n_(1546805, "self", lambda: self), "year")),"-",_c_(1546811, _n_(1546808, "str", lambda: str), _a_(1546810, _n_(1546809, "self", lambda: self), "month")),"-",_c_(1546815, _n_(1546812, "str", lambda: str), _a_(1546814, _n_(1546813, "self", lambda: self), "day"))
            _l_(1546816)
        elif(_n_(1546817, "frmt", lambda: frmt) == 0):
            _l_(1546824)

            _c_(1546819, _n_(1546818, "print", lambda: print), "Thanky You.....................")
            _l_(1546820)
        else:
            _c_(1546822, _n_(1546821, "print", lambda: print), "Enter Correct Choice.......")
            _l_(1546823)
        _c_(1546830, _n_(1546828, "print", lambda: print), _n_(1546829, "ff", lambda: ff))
        _l_(1546831)

dt = _c_(1546835, _n_(1546834, "myDate", lambda: myDate))
_l_(1546836)
nday = _c_(1546840, _n_(1546837, "int", lambda: int), _c_(1546839, _n_(1546838, "input", lambda: input), "Enter No. For Aday or SUBTRACT Days :: "))
_l_(1546841)
_c_(1546845, _a_(1546843, _n_(1546842, "dt", lambda: dt), "adayDays"), _n_(1546844, "nday", lambda: nday))
_l_(1546846)
_c_(1546848, _n_(1546847, "print", lambda: print), "1 : day-month-year")
_l_(1546849)
_c_(1546851, _n_(1546850, "print", lambda: print), "2 : month-day-year")
_l_(1546852)
_c_(1546854, _n_(1546853, "print", lambda: print), "3 : year-month-day")
_l_(1546855)
_c_(1546857, _n_(1546856, "print", lambda: print), "0 : EXIT")
_l_(1546858)
frmt = _c_(1546862, _n_(1546859, "int", lambda: int), _c_(1546861, _n_(1546860, "input", lambda: input), "Enter Your Choice :: "))
_l_(1546863)
_c_(1546867, _a_(1546865, _n_(1546864, "dt", lambda: dt), "formatDate"), _n_(1546866, "frmt", lambda: frmt))
_l_(1546868)


# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51775820/showing-typeerror-unsupported-operand-types-for-int-and-nonetype
#A python program to illustrate Caesar Cipher Technique

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys, random
    _l_(707636)

except ImportError:
    pass

class Process:
    _l_(707976)


    def main():
        _l_(707721)

        _c_(707638, _n_(707637, "print", lambda: print), "\nA python program to illustrate Caesar Cipher Technique.")
        _l_(707639)
        myMode = _c_(707641, _n_(707640, "getMode", lambda: getMode))
        _l_(707642)
        if _n_(707643, "myMode", lambda: myMode) == 'Encrypt':
            _l_(707720)

            myMessage = _c_(707645, _n_(707644, "input", lambda: input), "\nEnter the Text You want to be Converted...\n\n")
            _l_(707646)
            myKey = _c_(707648, _n_(707647, "getKey", lambda: getKey))
            _l_(707649)
            translated = _c_(707653, _n_(707650, "encryptMessage", lambda: encryptMessage), _n_(707651, "myKey", lambda: myKey), _n_(707652, "myMessage", lambda: myMessage))   
            _l_(707654)   
            _c_(707657, _n_(707655, "print", lambda: print), "\nYour Mode        : " + _n_(707656, "myMode", lambda: myMode))
            _l_(707658)
            _c_(707661, _n_(707659, "print", lambda: print), "\nYour Text        : " + _n_(707660, "myMessage", lambda: myMessage))
            _l_(707662)
            _c_(707665, _n_(707663, "print", lambda: print), "\nKey              : " + _n_(707664, "myKey", lambda: myKey))
            _l_(707666)
            _c_(707669, _n_(707667, "print", lambda: print), "\nEncrypted Text   : " + _n_(707668, "translated", lambda: translated))
            _l_(707670)
            _c_(707675, _n_(707671, "Testing", lambda: Testing), _n_(707672, "myKey", lambda: myKey), _n_(707673, "myMessage", lambda: myMessage), _n_(707674, "translated", lambda: translated))
            _l_(707676)
            _c_(707678, _n_(707677, "Exit", lambda: Exit))
            _l_(707679)
        elif _n_(707680, "myMode", lambda: myMode) == 'Decrypt':
            _l_(707719)

            myMessage = _c_(707682, _n_(707681, "input", lambda: input), "\nEnter the Cipher Text You want to be Decrypted...\n\n")
            _l_(707683)
            Key = _c_(707685, _n_(707684, "keyVal", lambda: keyVal))
            _l_(707686)
            myKey = _n_(707687, "Key", lambda: Key)
            _l_(707688)
            translated = _c_(707692, _n_(707689, "decryptMessage", lambda: decryptMessage), _n_(707690, "myKey", lambda: myKey), _n_(707691, "myMessage", lambda: myMessage))
            _l_(707693)
            _c_(707696, _n_(707694, "print", lambda: print), "\nYour Mode        : " + _n_(707695, "myMode", lambda: myMode))
            _l_(707697)
            _c_(707700, _n_(707698, "print", lambda: print), "\nYour Cipher Text : " + _n_(707699, "myMessage", lambda: myMessage))
            _l_(707701)
            _c_(707704, _n_(707702, "print", lambda: print), "\nKey              : " + _n_(707703, "myKey", lambda: myKey))
            _l_(707705)
            _c_(707708, _n_(707706, "print", lambda: print), "\nDecrypted Text   : " + _n_(707707, "translated", lambda: translated))
            _l_(707709)
            _c_(707711, _n_(707710, "Exit", lambda: Exit))
            _l_(707712)
        else :
            _c_(707714, _n_(707713, "print", lambda: print), "\ntWrong Choice Please Try Again ... \n\n")
            _l_(707715)
            _c_(707717, _n_(707716, "main", lambda: main))
            _l_(707718)


    def getMode():
        _l_(707754)

        mode = _c_(707725, _a_(707724, _c_(707723, _n_(707722, "input", lambda: input), "\nEnter Your Choice for Caesar Cipher Technique\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n"), "lower"))
        _l_(707726)
        if _n_(707727, "mode", lambda: mode) in _c_(707729, _a_(707728, 'encrypt e decrypt d', "split")):
            _l_(707749)

            if _n_(707730, "mode", lambda: mode) in _c_(707732, _a_(707731, 'encrypt e', "split")):
                _l_(707742)

                mode = 'Encrypt'
                _l_(707733)
            elif _n_(707734, "mode", lambda: mode) in _c_(707736, _a_(707735, 'decrypt d', "split")):
                _l_(707741)

                mode = 'Decrypt'
                _l_(707737)
            else:
                _c_(707739, _n_(707738, "getMode", lambda: getMode))
                _l_(707740)
        else:
            _c_(707744, _n_(707743, "print", lambda: print), "\nOops! Wrong Choice, Please choose Again...\n\n")
            _l_(707745)
            _c_(707747, _n_(707746, "getMode", lambda: getMode))
            _l_(707748)
        myMode = _n_(707750, "mode", lambda: mode)
        _l_(707751)
        aux = _n_(707752, "myMode", lambda: myMode)
        _l_(707753)
        return aux


    def getKey():
        _l_(707758)

        _c_(707756, _n_(707755, "keyMode", lambda: keyMode))
        _l_(707757)


    def keyMode():
        _l_(707775)

        keyMode = _c_(707760, _n_(707759, "input", lambda: input), "\nWant to give Key Manually? or Want it to be Auto Generated?\ni.e. Type ('Yes' for Manual or 'Auto' for Auto Generated Key)\n\n")
        _l_(707761)
        if _n_(707762, "keyMode", lambda: keyMode) == 'Yes':
            _l_(707774)

            _c_(707764, _n_(707763, "keyManual", lambda: keyManual))
            _l_(707765)
        elif _n_(707766, "keyMode", lambda: keyMode) =='Auto':
            _l_(707773)

            _c_(707768, _n_(707767, "keyAuto", lambda: keyAuto))
            _l_(707769)
        else:
            _c_(707771, _n_(707770, "print", lambda: print), "\nOops! Wrong Choice, Please Try Again...\n\n")
            _l_(707772)


    def keyManual():
        _l_(707806)

        key = 0
        _l_(707776)
        minimum = 1
        _l_(707777)
        maximum = 26
        _l_(707778)
        keyMode = 'Manual'
        _l_(707779)
        key = _c_(707785, _n_(707780, "int", lambda: int), _c_(707784, _n_(707781, "input", lambda: input), "\nEnter Your Choice Between %s & %s to be Shift Number as a Key:\n\n" %(_n_(707782, "minimum", lambda: minimum), _n_(707783, "maximum", lambda: maximum))))
        _l_(707786)
        if (_n_(707787, "key", lambda: key) >= _n_(707788, "minimum", lambda: minimum) and _n_(707789, "key", lambda: key) <= _n_(707790, "maximum", lambda: maximum)):
            _l_(707801)

            aux = _n_(707791, "key", lambda: key)
            _l_(707792)
            return aux
        else:
            _c_(707796, _n_(707793, "print", lambda: print), "\nOops! Wrong Choice, Please choose between %s & %s, Try Again...\n\n" %(_n_(707794, "minimum", lambda: minimum), _n_(707795, "maximum", lambda: maximum)))
            _l_(707797)
            _c_(707799, _n_(707798, "keyManual", lambda: keyManual))
            _l_(707800)
        myKey = _c_(707804, _n_(707802, "int", lambda: int), _n_(707803, "key", lambda: key))
        _l_(707805)


    def keyAuto():
        _l_(707820)

        minimum = 1
        _l_(707807)
        maximum = 26
        _l_(707808)
        total = _n_(707809, "maximum", lambda: maximum) + 1
        _l_(707810)
        keyMode = 'Auto'
        _l_(707811)
        myKey = _c_(707816, _a_(707813, _n_(707812, "random", lambda: random), "randint"), _n_(707814, "minimum", lambda: minimum), _n_(707815, "total", lambda: total))
        _l_(707817)
        aux = _n_(707818, "myKey", lambda: myKey)
        _l_(707819)
        return aux


    def keyVal():
        _l_(707847)

        key = 0
        _l_(707821)
        minimum = 1
        _l_(707822)
        maximum = 26
        _l_(707823)
        keyMode = 'Validation'
        _l_(707824)
        key = _c_(707828, _n_(707825, "int", lambda: int), _c_(707827, _n_(707826, "input", lambda: input), "\nEnter the Key provided to You...\n\n"))
        _l_(707829)
        if (_n_(707830, "key", lambda: key) >= _n_(707831, "minimum", lambda: minimum) and _n_(707832, "key", lambda: key) <= _n_(707833, "maximum", lambda: maximum)):
            _l_(707842)

            aux = _n_(707834, "key", lambda: key)
            _l_(707835)
            return aux
        else:
            _c_(707837, _n_(707836, "print", lambda: print), "\nOops! Wrong Key, Please Try Again...\n\n")
            _l_(707838)
            _c_(707840, _n_(707839, "keyVal", lambda: keyVal))
            _l_(707841)
        myKey = _c_(707845, _n_(707843, "int", lambda: int), _n_(707844, "key", lambda: key))
        _l_(707846)


    def Testing(myKey, myMessage, translated):
        _l_(707897)

        Test = _c_(707849, _n_(707848, "input", lambda: input), "\nDo you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")
        _l_(707850)
        if _n_(707851, "Test", lambda: Test) == 'Yes':
            _l_(707896)

            myMode = 'Decrypt'
            _l_(707852)
            Key = _n_(707853, "myKey", lambda: myKey)
            _l_(707854)
            myKey = _n_(707855, "Key", lambda: Key)
            _l_(707856)
            Encrypted = _n_(707857, "translated", lambda: translated)
            _l_(707858)
            myMessage = _n_(707859, "Encrypted", lambda: Encrypted)
            _l_(707860)
            translated = _c_(707864, _n_(707861, "decryptMessage", lambda: decryptMessage), _n_(707862, "myKey", lambda: myKey), _n_(707863, "myMessage", lambda: myMessage))
            _l_(707865)
            _c_(707868, _n_(707866, "print", lambda: print), "\nYour Mode        : " + _n_(707867, "myMode", lambda: myMode))
            _l_(707869)
            _c_(707872, _n_(707870, "print", lambda: print), "\nYour Cipher Text : " + _n_(707871, "myMessage", lambda: myMessage))
            _l_(707873)
            _c_(707876, _n_(707874, "print", lambda: print), "\nKey              : " + _n_(707875, "myKey", lambda: myKey))
            _l_(707877)
            _c_(707880, _n_(707878, "print", lambda: print), "\nDecrypted Text   : " + _n_(707879, "translated", lambda: translated))
            _l_(707881)
        elif _n_(707882, "Test", lambda: Test) == 'No':
            _l_(707895)

            _c_(707884, _n_(707883, "print", lambda: print), "\nThank You...!\n")
            _l_(707885)
        else:
            _c_(707887, _n_(707886, "print", lambda: print), "\nWrong Choice Please Try Again ... \n\n")
            _l_(707888)
            _c_(707893, _n_(707889, "Testing", lambda: Testing), _n_(707890, "myKey", lambda: myKey), _n_(707891, "myMessage", lambda: myMessage), _n_(707892, "translated", lambda: translated))
            _l_(707894)


    def encryptMessage(key, message):
        _l_(707903)

        aux = _c_(707901, _n_(707898, "translateMessage", lambda: translateMessage), _n_(707899, "key", lambda: key), _n_(707900, "message", lambda: message), 'Encrypt')
        _l_(707902)
        return aux


    def decryptMessage(key, message):
        _l_(707909)

        aux = _c_(707907, _n_(707904, "translateMessage", lambda: translateMessage), _n_(707905, "key", lambda: key), _n_(707906, "message", lambda: message), 'Decrypt')
        _l_(707908)
        return aux


    def translateMessage(key, message, mode):
        _l_(707963)

        translated = ''
        _l_(707910)
        if _n_(707911, "mode", lambda: mode) == 'Decrypt':
            _l_(707914)

            key = -_n_(707912, "key", lambda: key)
            _l_(707913)
        for symbol in _n_(707915, "message", lambda: message):
            _l_(707960)

            if _c_(707918, _a_(707917, _n_(707916, "symbol", lambda: symbol), "isalpha")):
                _l_(707959)

                num = _c_(707921, _n_(707919, "ord", lambda: ord), _n_(707920, "symbol", lambda: symbol))
                _l_(707922)
                num += _n_(707923, "key", lambda: key)
                _l_(707924)
                if _c_(707927, _a_(707926, _n_(707925, "symbol", lambda: symbol), "isupper")):
                    _l_(707952)

                    if _n_(707928, "num", lambda: num) > _c_(707930, _n_(707929, "ord", lambda: ord), 'Z'):
                        _l_(707937)

                        num -= 26
                        _l_(707931)
                    elif _n_(707932, "num", lambda: num) < _c_(707934, _n_(707933, "ord", lambda: ord), 'A'):
                        _l_(707936)

                        num += 26
                        _l_(707935)
                elif _c_(707940, _a_(707939, _n_(707938, "symbol", lambda: symbol), "islower")):
                    _l_(707951)

                    if _n_(707941, "num", lambda: num) > _c_(707943, _n_(707942, "ord", lambda: ord), 'z'):
                        _l_(707950)

                        num -= 26
                        _l_(707944)
                    elif _n_(707945, "num", lambda: num) < _c_(707947, _n_(707946, "ord", lambda: ord), 'a'):
                        _l_(707949)

                        num += 26
                        _l_(707948)
                translated += _c_(707955, _n_(707953, "chr", lambda: chr), _n_(707954, "num", lambda: num))
                _l_(707956)
            else:
                translated += _n_(707957, "symbol", lambda: symbol)
                _l_(707958)
        aux = _n_(707961, "translated", lambda: translated)
        _l_(707962)
        return aux


    def Exit():
        _l_(707975)

        Exit = _c_(707965, _n_(707964, "input", lambda: input), "\nDo You want to Run the Program again? (Type 'Yes'/'No')\n\n")
        _l_(707966)
        if _n_(707967, "Exit", lambda: Exit) == 'Yes':
            _l_(707974)

            _c_(707969, _n_(707968, "main", lambda: main))
            _l_(707970)
        else:
            _c_(707972, _n_(707971, "print", lambda: print), "\n          --/--\--/End\--/--\-- \n\n")
            _l_(707973)

_c_(707979, _a_(707978, _n_(707977, "Process", lambda: Process), "main"))
_l_(707980)

_c_(707982, _n_(707981, "input", lambda: input))
_l_(707983)
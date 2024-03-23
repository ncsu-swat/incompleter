# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51775820/showing-typeerror-unsupported-operand-types-for-int-and-nonetype
#A python program to illustrate Caesar Cipher Technique

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys, random
    _l_(704894)

except ImportError:
    pass

class Process:
    _l_(705234)


    def main():
        _l_(704979)

        _c_(704896, _n_(704895, "print", lambda: print), "\nA python program to illustrate Caesar Cipher Technique.")
        _l_(704897)
        myMode = _c_(704899, _n_(704898, "getMode", lambda: getMode))
        _l_(704900)
        if _n_(704901, "myMode", lambda: myMode) == 'Encrypt':
            _l_(704978)

            myMessage = _c_(704903, _n_(704902, "input", lambda: input), "\nEnter the Text You want to be Converted...\n\n")
            _l_(704904)
            myKey = _c_(704906, _n_(704905, "getKey", lambda: getKey))
            _l_(704907)
            translated = _c_(704911, _n_(704908, "encryptMessage", lambda: encryptMessage), _n_(704909, "myKey", lambda: myKey), _n_(704910, "myMessage", lambda: myMessage))   
            _l_(704912)   
            _c_(704915, _n_(704913, "print", lambda: print), "\nYour Mode        : " + _n_(704914, "myMode", lambda: myMode))
            _l_(704916)
            _c_(704919, _n_(704917, "print", lambda: print), "\nYour Text        : " + _n_(704918, "myMessage", lambda: myMessage))
            _l_(704920)
            _c_(704923, _n_(704921, "print", lambda: print), "\nKey              : " + _n_(704922, "myKey", lambda: myKey))
            _l_(704924)
            _c_(704927, _n_(704925, "print", lambda: print), "\nEncrypted Text   : " + _n_(704926, "translated", lambda: translated))
            _l_(704928)
            _c_(704933, _n_(704929, "Testing", lambda: Testing), _n_(704930, "myKey", lambda: myKey), _n_(704931, "myMessage", lambda: myMessage), _n_(704932, "translated", lambda: translated))
            _l_(704934)
            _c_(704936, _n_(704935, "Exit", lambda: Exit))
            _l_(704937)
        elif _n_(704938, "myMode", lambda: myMode) == 'Decrypt':
            _l_(704977)

            myMessage = _c_(704940, _n_(704939, "input", lambda: input), "\nEnter the Cipher Text You want to be Decrypted...\n\n")
            _l_(704941)
            Key = _c_(704943, _n_(704942, "keyVal", lambda: keyVal))
            _l_(704944)
            myKey = _n_(704945, "Key", lambda: Key)
            _l_(704946)
            translated = _c_(704950, _n_(704947, "decryptMessage", lambda: decryptMessage), _n_(704948, "myKey", lambda: myKey), _n_(704949, "myMessage", lambda: myMessage))
            _l_(704951)
            _c_(704954, _n_(704952, "print", lambda: print), "\nYour Mode        : " + _n_(704953, "myMode", lambda: myMode))
            _l_(704955)
            _c_(704958, _n_(704956, "print", lambda: print), "\nYour Cipher Text : " + _n_(704957, "myMessage", lambda: myMessage))
            _l_(704959)
            _c_(704962, _n_(704960, "print", lambda: print), "\nKey              : " + _n_(704961, "myKey", lambda: myKey))
            _l_(704963)
            _c_(704966, _n_(704964, "print", lambda: print), "\nDecrypted Text   : " + _n_(704965, "translated", lambda: translated))
            _l_(704967)
            _c_(704969, _n_(704968, "Exit", lambda: Exit))
            _l_(704970)
        else :
            _c_(704972, _n_(704971, "print", lambda: print), "\ntWrong Choice Please Try Again ... \n\n")
            _l_(704973)
            _c_(704975, _n_(704974, "main", lambda: main))
            _l_(704976)


    def getMode():
        _l_(705012)

        mode = _c_(704983, _a_(704982, _c_(704981, _n_(704980, "input", lambda: input), "\nEnter Your Choice for Caesar Cipher Technique\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n"), "lower"))
        _l_(704984)
        if _n_(704985, "mode", lambda: mode) in _c_(704987, _a_(704986, 'encrypt e decrypt d', "split")):
            _l_(705007)

            if _n_(704988, "mode", lambda: mode) in _c_(704990, _a_(704989, 'encrypt e', "split")):
                _l_(705000)

                mode = 'Encrypt'
                _l_(704991)
            elif _n_(704992, "mode", lambda: mode) in _c_(704994, _a_(704993, 'decrypt d', "split")):
                _l_(704999)

                mode = 'Decrypt'
                _l_(704995)
            else:
                _c_(704997, _n_(704996, "getMode", lambda: getMode))
                _l_(704998)
        else:
            _c_(705002, _n_(705001, "print", lambda: print), "\nOops! Wrong Choice, Please choose Again...\n\n")
            _l_(705003)
            _c_(705005, _n_(705004, "getMode", lambda: getMode))
            _l_(705006)
        myMode = _n_(705008, "mode", lambda: mode)
        _l_(705009)
        aux = _n_(705010, "myMode", lambda: myMode)
        _l_(705011)
        return aux


    def getKey():
        _l_(705016)

        _c_(705014, _n_(705013, "keyMode", lambda: keyMode))
        _l_(705015)


    def keyMode():
        _l_(705033)

        keyMode = _c_(705018, _n_(705017, "input", lambda: input), "\nWant to give Key Manually? or Want it to be Auto Generated?\ni.e. Type ('Yes' for Manual or 'Auto' for Auto Generated Key)\n\n")
        _l_(705019)
        if _n_(705020, "keyMode", lambda: keyMode) == 'Yes':
            _l_(705032)

            _c_(705022, _n_(705021, "keyManual", lambda: keyManual))
            _l_(705023)
        elif _n_(705024, "keyMode", lambda: keyMode) =='Auto':
            _l_(705031)

            _c_(705026, _n_(705025, "keyAuto", lambda: keyAuto))
            _l_(705027)
        else:
            _c_(705029, _n_(705028, "print", lambda: print), "\nOops! Wrong Choice, Please Try Again...\n\n")
            _l_(705030)


    def keyManual():
        _l_(705064)

        key = 0
        _l_(705034)
        minimum = 1
        _l_(705035)
        maximum = 26
        _l_(705036)
        keyMode = 'Manual'
        _l_(705037)
        key = _c_(705043, _n_(705038, "int", lambda: int), _c_(705042, _n_(705039, "input", lambda: input), "\nEnter Your Choice Between %s & %s to be Shift Number as a Key:\n\n" %(_n_(705040, "minimum", lambda: minimum), _n_(705041, "maximum", lambda: maximum))))
        _l_(705044)
        if (_n_(705045, "key", lambda: key) >= _n_(705046, "minimum", lambda: minimum) and _n_(705047, "key", lambda: key) <= _n_(705048, "maximum", lambda: maximum)):
            _l_(705059)

            aux = _n_(705049, "key", lambda: key)
            _l_(705050)
            return aux
        else:
            _c_(705054, _n_(705051, "print", lambda: print), "\nOops! Wrong Choice, Please choose between %s & %s, Try Again...\n\n" %(_n_(705052, "minimum", lambda: minimum), _n_(705053, "maximum", lambda: maximum)))
            _l_(705055)
            _c_(705057, _n_(705056, "keyManual", lambda: keyManual))
            _l_(705058)
        myKey = _c_(705062, _n_(705060, "int", lambda: int), _n_(705061, "key", lambda: key))
        _l_(705063)


    def keyAuto():
        _l_(705078)

        minimum = 1
        _l_(705065)
        maximum = 26
        _l_(705066)
        total = _n_(705067, "maximum", lambda: maximum) + 1
        _l_(705068)
        keyMode = 'Auto'
        _l_(705069)
        myKey = _c_(705074, _a_(705071, _n_(705070, "random", lambda: random), "randint"), _n_(705072, "minimum", lambda: minimum), _n_(705073, "total", lambda: total))
        _l_(705075)
        aux = _n_(705076, "myKey", lambda: myKey)
        _l_(705077)
        return aux


    def keyVal():
        _l_(705105)

        key = 0
        _l_(705079)
        minimum = 1
        _l_(705080)
        maximum = 26
        _l_(705081)
        keyMode = 'Validation'
        _l_(705082)
        key = _c_(705086, _n_(705083, "int", lambda: int), _c_(705085, _n_(705084, "input", lambda: input), "\nEnter the Key provided to You...\n\n"))
        _l_(705087)
        if (_n_(705088, "key", lambda: key) >= _n_(705089, "minimum", lambda: minimum) and _n_(705090, "key", lambda: key) <= _n_(705091, "maximum", lambda: maximum)):
            _l_(705100)

            aux = _n_(705092, "key", lambda: key)
            _l_(705093)
            return aux
        else:
            _c_(705095, _n_(705094, "print", lambda: print), "\nOops! Wrong Key, Please Try Again...\n\n")
            _l_(705096)
            _c_(705098, _n_(705097, "keyVal", lambda: keyVal))
            _l_(705099)
        myKey = _c_(705103, _n_(705101, "int", lambda: int), _n_(705102, "key", lambda: key))
        _l_(705104)


    def Testing(myKey, myMessage, translated):
        _l_(705155)

        Test = _c_(705107, _n_(705106, "input", lambda: input), "\nDo you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")
        _l_(705108)
        if _n_(705109, "Test", lambda: Test) == 'Yes':
            _l_(705154)

            myMode = 'Decrypt'
            _l_(705110)
            Key = _n_(705111, "myKey", lambda: myKey)
            _l_(705112)
            myKey = _n_(705113, "Key", lambda: Key)
            _l_(705114)
            Encrypted = _n_(705115, "translated", lambda: translated)
            _l_(705116)
            myMessage = _n_(705117, "Encrypted", lambda: Encrypted)
            _l_(705118)
            translated = _c_(705122, _n_(705119, "decryptMessage", lambda: decryptMessage), _n_(705120, "myKey", lambda: myKey), _n_(705121, "myMessage", lambda: myMessage))
            _l_(705123)
            _c_(705126, _n_(705124, "print", lambda: print), "\nYour Mode        : " + _n_(705125, "myMode", lambda: myMode))
            _l_(705127)
            _c_(705130, _n_(705128, "print", lambda: print), "\nYour Cipher Text : " + _n_(705129, "myMessage", lambda: myMessage))
            _l_(705131)
            _c_(705134, _n_(705132, "print", lambda: print), "\nKey              : " + _n_(705133, "myKey", lambda: myKey))
            _l_(705135)
            _c_(705138, _n_(705136, "print", lambda: print), "\nDecrypted Text   : " + _n_(705137, "translated", lambda: translated))
            _l_(705139)
        elif _n_(705140, "Test", lambda: Test) == 'No':
            _l_(705153)

            _c_(705142, _n_(705141, "print", lambda: print), "\nThank You...!\n")
            _l_(705143)
        else:
            _c_(705145, _n_(705144, "print", lambda: print), "\nWrong Choice Please Try Again ... \n\n")
            _l_(705146)
            _c_(705151, _n_(705147, "Testing", lambda: Testing), _n_(705148, "myKey", lambda: myKey), _n_(705149, "myMessage", lambda: myMessage), _n_(705150, "translated", lambda: translated))
            _l_(705152)


    def encryptMessage(key, message):
        _l_(705161)

        aux = _c_(705159, _n_(705156, "translateMessage", lambda: translateMessage), _n_(705157, "key", lambda: key), _n_(705158, "message", lambda: message), 'Encrypt')
        _l_(705160)
        return aux


    def decryptMessage(key, message):
        _l_(705167)

        aux = _c_(705165, _n_(705162, "translateMessage", lambda: translateMessage), _n_(705163, "key", lambda: key), _n_(705164, "message", lambda: message), 'Decrypt')
        _l_(705166)
        return aux


    def translateMessage(key, message, mode):
        _l_(705221)

        translated = ''
        _l_(705168)
        if _n_(705169, "mode", lambda: mode) == 'Decrypt':
            _l_(705172)

            key = -_n_(705170, "key", lambda: key)
            _l_(705171)
        for symbol in _n_(705173, "message", lambda: message):
            _l_(705218)

            if _c_(705176, _a_(705175, _n_(705174, "symbol", lambda: symbol), "isalpha")):
                _l_(705217)

                num = _c_(705179, _n_(705177, "ord", lambda: ord), _n_(705178, "symbol", lambda: symbol))
                _l_(705180)
                num += _n_(705181, "key", lambda: key)
                _l_(705182)
                if _c_(705185, _a_(705184, _n_(705183, "symbol", lambda: symbol), "isupper")):
                    _l_(705210)

                    if _n_(705186, "num", lambda: num) > _c_(705188, _n_(705187, "ord", lambda: ord), 'Z'):
                        _l_(705195)

                        num -= 26
                        _l_(705189)
                    elif _n_(705190, "num", lambda: num) < _c_(705192, _n_(705191, "ord", lambda: ord), 'A'):
                        _l_(705194)

                        num += 26
                        _l_(705193)
                elif _c_(705198, _a_(705197, _n_(705196, "symbol", lambda: symbol), "islower")):
                    _l_(705209)

                    if _n_(705199, "num", lambda: num) > _c_(705201, _n_(705200, "ord", lambda: ord), 'z'):
                        _l_(705208)

                        num -= 26
                        _l_(705202)
                    elif _n_(705203, "num", lambda: num) < _c_(705205, _n_(705204, "ord", lambda: ord), 'a'):
                        _l_(705207)

                        num += 26
                        _l_(705206)
                translated += _c_(705213, _n_(705211, "chr", lambda: chr), _n_(705212, "num", lambda: num))
                _l_(705214)
            else:
                translated += _n_(705215, "symbol", lambda: symbol)
                _l_(705216)
        aux = _n_(705219, "translated", lambda: translated)
        _l_(705220)
        return aux


    def Exit():
        _l_(705233)

        Exit = _c_(705223, _n_(705222, "input", lambda: input), "\nDo You want to Run the Program again? (Type 'Yes'/'No')\n\n")
        _l_(705224)
        if _n_(705225, "Exit", lambda: Exit) == 'Yes':
            _l_(705232)

            _c_(705227, _n_(705226, "main", lambda: main))
            _l_(705228)
        else:
            _c_(705230, _n_(705229, "print", lambda: print), "\n          --/--\--/End\--/--\-- \n\n")
            _l_(705231)

_c_(705237, _a_(705236, _n_(705235, "Process", lambda: Process), "main"))
_l_(705238)

_c_(705240, _n_(705239, "input", lambda: input))
_l_(705241)
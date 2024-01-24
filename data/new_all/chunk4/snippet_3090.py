# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47702659/attribute-error-problems-with-python-hangman-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(622906)

except ImportError:
    pass

name = _c_(622908, _n_(622907, "input", lambda: input), "Hello, my name is H.A.N.K.M.A.N! What is yours?: ")
_l_(622909)
_c_(622912, _n_(622910, "print", lambda: print), "Hello, "+_n_(622911, "name", lambda: name)," do you wanna play Hangman? Yes? Well why didn't you say so? Lets Goooooooo!")
_l_(622913)

def extractwords(filename,number):
    _l_(622960)

    myfile=_c_(622916, _n_(622914, "open", lambda: open), _n_(622915, "filename", lambda: filename)+".txt","r")
    _l_(622917)
    details=_c_(622920, _a_(622919, _n_(622918, "myfile", lambda: myfile), "readlines"))
    _l_(622921)
    _c_(622924, _a_(622923, _n_(622922, "myfile", lambda: myfile), "close"))
    _l_(622925)
    words=[]
    _l_(622926)
    for i in _n_(622927, "details", lambda: details):
        _l_(622957)

        for item in _c_(622930, _a_(622929, _n_(622928, "i", lambda: i), "split")):
            _l_(622956)

            letter=True
            _l_(622931)
            for j in _n_(622932, "item", lambda: item):
                _l_(622938)

                if _c_(622935, _a_(622934, _n_(622933, "j", lambda: j), "isalpha"))==False:
                    _l_(622937)

                    letter = False
                    _l_(622936)
            item = _c_(622941, _a_(622940, _n_(622939, "item", lambda: item), "lower"))
            _l_(622942)
            if _c_(622945, _n_(622943, "len", lambda: len), _n_(622944, "item", lambda: item))==_n_(622946, "number", lambda: number) and _n_(622947, "letter", lambda: letter)==True and _n_(622948, "item", lambda: item) not in _n_(622949, "words", lambda: words):
                _l_(622955)

                _c_(622953, _a_(622951, _n_(622950, "words", lambda: words), "append"), _n_(622952, "item", lambda: item))
                _l_(622954)
    aux = _n_(622958, "words", lambda: words)
    _l_(622959)
    return aux
player = "y"
_l_(622961)
while _n_(622962, "player", lambda: player) =="y":
    _l_(623106)

    complete=0
    _l_(622963)
    guessed=[]
    _l_(622964)
    errors=""
    _l_(622965)
    characters = _c_(622968, _a_(622967, _n_(622966, "random", lambda: random), "randint"), 5,9)
    _l_(622969)
    tries = _n_(622970, "characters", lambda: characters)+3
    _l_(622971)

    wordlist=_c_(622974, _n_(622972, "extractwords", lambda: extractwords), "wordlist",_n_(622973, "characters", lambda: characters))
    _l_(622975)
    word=_c_(622979, _a_(622977, _n_(622976, "random", lambda: random), "choice"), _n_(622978, "wordlist", lambda: wordlist))
    _l_(622980)
    _c_(622983, _n_(622981, "print", lambda: print), "Testing word:",_n_(622982, "word", lambda: word))
    _l_(622984)
    _c_(622989, _n_(622985, "print", lambda: print), "You have "+ _c_(622988, _n_(622986, "str", lambda: str), _n_(622987, "tries", lambda: tries))+" tries left")
    _l_(622990)

    letters=[]
    _l_(622991)
    for i in _n_(622992, "word", lambda: word):
        _l_(622998)

        _c_(622996, _a_(622994, _n_(622993, "letters", lambda: letters), "append"), _n_(622995, "i", lambda: i))
        _l_(622997)

    hword=[]
    _l_(622999)
    for i in _c_(623002, _n_(623000, "range", lambda: range), 0,_n_(623001, "characters", lambda: characters)):
        _l_(623007)

        _c_(623005, _a_(623004, _n_(623003, "hword", lambda: hword), "append"), "-")
        _l_(623006)

    dashes=""
    _l_(623008)
    for i in _n_(623009, "hword", lambda: hword):
        _l_(623013)

        dashes = _n_(623010, "dashes", lambda: dashes)+_n_(623011, "i", lambda: i)
        _l_(623012)

    _c_(623016, _n_(623014, "print", lambda: print), "The word you need to guess is ",_n_(623015, "dashes", lambda: dashes))
    _l_(623017)
    while _n_(623018, "complete", lambda: complete) < _n_(623019, "characters", lambda: characters) and _n_(623020, "tries", lambda: tries) > 0:
        _l_(623099)

        guess = _c_(623022, _n_(623021, "input", lambda: input), "Please input your letter: ")
        _l_(623023)
        if _n_(623024, "guess", lambda: guess) in _n_(623025, "word", lambda: word):
            _l_(623098)

            _c_(623029, _a_(623027, _n_(623026, "guessed", lambda: guessed), "append"), _n_(623028, "dashes", lambda: dashes))
            _l_(623030)
            _c_(623032, _n_(623031, "print", lambda: print), "Noice job! You guessed the right letter!")
            _l_(623033)
            tries=_n_(623034, "tries", lambda: tries)-1
            _l_(623035)
            _c_(623040, _n_(623036, "print", lambda: print), "You have "+ _c_(623039, _n_(623037, "str", lambda: str), _n_(623038, "tries", lambda: tries))+" tries left")
            _l_(623041)
            _c_(623044, _n_(623042, "print", lambda: print), _n_(623043, "dashes", lambda: dashes))
            _l_(623045)
            if _c_(623048, _n_(623046, "len", lambda: len), _n_(623047, "guessed", lambda: guessed)) == _c_(623051, _n_(623049, "len", lambda: len), _n_(623050, "word", lambda: word)):
                _l_(623058)

                _c_(623053, _n_(623052, "print", lambda: print), "What? How did this happen? Yuu must have been cheating!Just Kidding! You did a good job on finding the word, so a GOOD JOB is in order!")
                _l_(623054)
                layer = _c_(623056, _n_(623055, "input", lambda: input), "Would you like to play again? y/n: ")
                _l_(623057)
        elif _a_(623060, _n_(623059, "guess", lambda: guess), "isalpha") and _n_(623061, "guess", lambda: guess) not in _n_(623062, "word", lambda: word):
            _l_(623097)

            tries=_n_(623063, "tries", lambda: tries)-1
            _l_(623064)
            _c_(623066, _n_(623065, "print", lambda: print), "I am sorry, but your guess is a number / not part of the word that I am thinking off. Please have another go!")
            _l_(623067)
            _c_(623071, _a_(623069, _n_(623068, "errors", lambda: errors), "append"), _n_(623070, "guess", lambda: guess))
            _l_(623072)
            _c_(623075, _n_(623073, "print", lambda: print), "The letters you entered so far:", _n_(623074, "errors", lambda: errors))
            _l_(623076)
            _c_(623081, _n_(623077, "print", lambda: print), "You have "+ _c_(623080, _n_(623078, "str", lambda: str), _n_(623079, "tries", lambda: tries))+" tries left")
            _l_(623082)
        elif _c_(623085, _n_(623083, "len", lambda: len), _n_(623084, "guess", lambda: guess))!=1 or "abcdefghiklmnoopqestuvwxyz":
            _l_(623096)

            _c_(623087, _n_(623086, "print", lambda: print), "Please enter a valid/single letter.")
            _l_(623088)
        elif _n_(623089, "guess", lambda: guess) in _n_(623090, "guessed", lambda: guessed):
            _l_(623095)

            _c_(623092, _n_(623091, "print", lambda: print), "Please enter a letter that you havent entered previously. ")
            _l_(623093)
        else:
            pass
            _l_(623094)
    if _n_(623100, "tries", lambda: tries)==0:
        _l_(623105)

        _c_(623103, _n_(623101, "print", lambda: print), "You lose!The word you were supposed to guess was ",_n_(623102, "word", lambda: word))
        _l_(623104)
player = _c_(623108, _n_(623107, "input", lambda: input), "Would you like to play again? y/n: ")
_l_(623109)
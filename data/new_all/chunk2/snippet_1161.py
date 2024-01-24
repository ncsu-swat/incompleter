# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28253282/python-3-typeerror-type-str-doesnt-support-the-buffer-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(437947)

except ImportError:
    pass
try:
    import string
    _l_(437949)

except ImportError:
    pass

WORDLIST_FILENAME = "words.txt"
_l_(437950)

def loadWords():
    _l_(437974)

    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    _c_(437952, _n_(437951, "print", lambda: print), "Loading word list from file...")
    _l_(437953)
    # inFile: file
    inFile = _c_(437956, _n_(437954, "open", lambda: open), _n_(437955, "WORDLIST_FILENAME", lambda: WORDLIST_FILENAME), 'rb', 0)
    _l_(437957)
    # line: string
    line = _c_(437960, _a_(437959, _n_(437958, "inFile", lambda: inFile), "readline"))
    _l_(437961)
    # wordlist: list of strings
    wordlist = _c_(437964, _a_(437963, _n_(437962, "line", lambda: line), "split"))
    _l_(437965)
    _c_(437970, _n_(437966, "print", lambda: print), "  ", _c_(437969, _n_(437967, "len", lambda: len), _n_(437968, "wordlist", lambda: wordlist)), "words loaded.")
    _l_(437971)
    aux = _n_(437972, "wordlist", lambda: wordlist)
    _l_(437973)
    return aux

def chooseWord(wordlist):
    _l_(437980)

    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    aux = _c_(437978, _a_(437976, _n_(437975, "random", lambda: random), "choice"), _n_(437977, "wordlist", lambda: wordlist))
    _l_(437979)
    return aux

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = _c_(437982, _n_(437981, "loadWords", lambda: loadWords))
_l_(437983)

def isWordGuessed(secretWord, lettersGuessed):
    _l_(437992)

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    _l_(437984)

    for x in _n_(437985, "secretWord", lambda: secretWord) :
        _l_(437990)

        if _n_(437986, "x", lambda: x) not in _n_(437987, "lettersGuessed", lambda: lettersGuessed) :
            _l_(437989)

            aux = False
            _l_(437988)
            return aux
    aux = True
    _l_(437991)
    return aux



def getGuessedWord(secretWord, lettersGuessed):
    _l_(438023)

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    _l_(437993)

    guessedWord=['_']*_c_(437996, _n_(437994, "len", lambda: len), _n_(437995, "secretWord", lambda: secretWord))
    _l_(437997)
    for x in _n_(437998, "lettersGuessed", lambda: lettersGuessed) :
        _l_(438018)

##      1**   find the occurences of x in secretWord
        occurences = []
        _l_(437999)
        for i, j in _c_(438002, _n_(438000, "enumerate", lambda: enumerate), _n_(438001, "secretWord", lambda: secretWord)):
            _l_(438011)

            if _n_(438003, "j", lambda: j) == _n_(438004, "x", lambda: x):
                _l_(438010)

                _c_(438008, _a_(438006, _n_(438005, "occurences", lambda: occurences), "append"), _n_(438007, "i", lambda: i))
                _l_(438009)
##      2* go to the same indices in guessedWord and replace them by x 
        for i in _n_(438012, "occurences", lambda: occurences) :
            _l_(438017)

            _n_(438013, "guessedWord", lambda: guessedWord)[_n_(438014, "i", lambda: i)]=_n_(438015, "x", lambda: x);
            _l_(438016)
    aux = _c_(438021, _a_(438019, '', "join"), _n_(438020, "guessedWord", lambda: guessedWord))
    _l_(438022)

    return aux



def getAvailableLetters(lettersGuessed):
    _l_(438045)


    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    _l_(438024)

    available_Letters=[]
    _l_(438025)
    all_letters=_c_(438029, _n_(438026, "list", lambda: list), _a_(438028, _n_(438027, "string", lambda: string), "ascii_lowercase"))
    _l_(438030)
    for x in _n_(438031, "all_letters", lambda: all_letters) :
        _l_(438040)

        if (_n_(438032, "x", lambda: x) not in _n_(438033, "lettersGuessed", lambda: lettersGuessed)):
            _l_(438039)

            _c_(438037, _a_(438035, _n_(438034, "available_Letters", lambda: available_Letters), "append"), _n_(438036, "x", lambda: x))
            _l_(438038)
    aux = _c_(438043, _a_(438041, '', "join"), _n_(438042, "available_Letters", lambda: available_Letters))
    _l_(438044)
    return aux


def hangman(secretWord):
    _l_(438124)

    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    _l_(438046)

    _c_(438048, _n_(438047, "print", lambda: print), " Welcome to the game, Hangman!")
    _l_(438049)
    _c_(438051, _n_(438050, "print", lambda: print), "I am thinking of a word that is 4 letters long.")
    _l_(438052)
    number_of_guesses = 8
    _l_(438053)
    lettersGuessed = []
    _l_(438054)
    while True :
        _l_(438123)

        _c_(438056, _n_(438055, "print", lambda: print), "--------------------------------")
        _l_(438057)
        _c_(438060, _n_(438058, "print", lambda: print), "You have " , _n_(438059, "number_of_guesses", lambda: number_of_guesses) , "left !")
        _l_(438061)
        _c_(438066, _n_(438062, "print", lambda: print), "Available letters : " , _c_(438065, _n_(438063, "getAvailableLetters", lambda: getAvailableLetters), _n_(438064, "lettersGuessed", lambda: lettersGuessed)) )
        _l_(438067)
        _c_(438069, _n_(438068, "print", lambda: print), "Please guess a letter : ")
        _l_(438070)
        guess = _c_(438072, _n_(438071, "input", lambda: input))
        _l_(438073)

        while True:
            _l_(438104)

            _c_(438075, _n_(438074, "print", lambda: print), "Please guess a letter : ")
            _l_(438076)
            if _n_(438077, "guess", lambda: guess) in _n_(438078, "lettersGuessed", lambda: lettersGuessed):
                _l_(438103)

                _c_(438084, _n_(438079, "print", lambda: print), "Oops ! you've already guessed that letter :" , _c_(438083, _n_(438080, "getGuessedWord", lambda: getGuessedWord), _n_(438081, "secretWord", lambda: secretWord), _n_(438082, "lettersGuessed", lambda: lettersGuessed)))
                _l_(438085)
                break 
                _l_(438086) 
            else :
                if(_n_(438087, "guess", lambda: guess) in _n_(438088, "secretWord", lambda: secretWord) ) :
                    _l_(438102)

                    _c_(438092, _a_(438090, _n_(438089, "lettersGuessed", lambda: lettersGuessed), "append"), _n_(438091, "guess", lambda: guess))
                    _l_(438093)
                    _c_(438099, _n_(438094, "print", lambda: print), "Good guess:", _c_(438098, _n_(438095, "getGuessedWord", lambda: getGuessedWord), _n_(438096, "secretWord", lambda: secretWord), _n_(438097, "lettersGuessed", lambda: lettersGuessed)) )
                    _l_(438100)
                else :
                    number_of_guesses-=1
                    _l_(438101)


        _c_(438106, _n_(438105, "print", lambda: print), "---------------------------------")
        _l_(438107)
        if(_n_(438108, "number_of_guesses", lambda: number_of_guesses) == 0) :
            _l_(438113)

            _c_(438110, _n_(438109, "print", lambda: print), " Sorry, you ran out of guesses. The word was else. ")
            _l_(438111)
            break
            _l_(438112)
        if_c_(438117, _n_(438114, "isWordGuessed", lambda: isWordGuessed), _n_(438115, "secretWord", lambda: secretWord), _n_(438116, "lettersGuessed", lambda: lettersGuessed)):
            _l_(438122)

            _c_(438119, _n_(438118, "print", lambda: print), " Congratulations, you won!")
            _l_(438120)
            break
            _l_(438121)


secretWord = _c_(438129, _a_(438128, _c_(438127, _n_(438125, "chooseWord", lambda: chooseWord), _n_(438126, "wordlist", lambda: wordlist)), "lower"))
_l_(438130)
_c_(438133, _n_(438131, "hangman", lambda: hangman), _n_(438132, "secretWord", lambda: secretWord))
_l_(438134)
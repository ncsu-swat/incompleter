# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61198226/problem-in-pycharm-hangman-game-beginner-here-obviously-typeerror-object-of
# HANGMAN

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(363875)

except ImportError:
    pass
try:
    import time
    _l_(363877)

except ImportError:
    pass

hangman_pics = ['+-------+\n'
                '|       |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '|       |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '|\      |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '/       |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '/\      |\n'
                '        |\n'
                '===========]\n'

                ]
_l_(363878)

words = [
    "king",
    "fang",
    "long",
    "fast",
    "girl",
    "cats",
    "free",
    "bird",
    "band",
    "skin",
    "pour",
    "smart",
    "games",
    "perch",
    "clamp",
    "clock",
    "photo",
    "friar",
    "flute",
    "first",
    "candy",
    "mouth",
]
_l_(363879)

win = False
_l_(363880)
guesses = []
_l_(363881)


def get_word():
    _l_(363889)

    word = _c_(363885, _a_(363883, _n_(363882, "random", lambda: random), "choice"), _n_(363884, "words", lambda: words))
    _l_(363886)
    aux = _n_(363887, "word", lambda: word)
    _l_(363888)
    return aux


def hidden_word(word, guesses):
    _l_(363899)

    blanks = ''
    _l_(363890)
    for i in _n_(363891, "word", lambda: word):
        _l_(363896)

        blanks += f'{_n_(363892, "i", lambda: i)} ' if _n_(363893, 'i', lambda: i) in _n_(363894, 'guesses', lambda: guesses) else '_ '
        _l_(363895)
    aux = _n_(363897, 'blanks', lambda: blanks)
    _l_(363898)
    return aux


def get_guess():
    _l_(363936)

    global guess
    _l_(363900)
    guess = _a_(363903, _c_(363902, _n_(363901, 'input', lambda: input), '\nYour guess: '), 'lower')
    _l_(363904)
    _c_(363909, _n_(363905, 'print', lambda: print), _c_(363908, _n_(363906, 'len', lambda: len), _n_(363907, 'guess', lambda: guess)))
    _l_(363910)
    if _c_(363913, _n_(363911, 'len', lambda: len), _n_(363912, 'guess', lambda: guess)) != 1:
        _l_(363930)

        _c_(363915, _n_(363914, 'print', lambda: print), f'\n{"- - - - - " * 2}\nOnly guess one letter!\n{"- - - - - " * 2}\n')
        _l_(363916)
    elif _n_(363917, 'guess', lambda: guess) not in 'qwertyuiopasdfghjklzxcvbnm':
        _l_(363929)

        _c_(363919, _n_(363918, 'print', lambda: print), f'\n{"- - - - - " * 2}\nOnly guess letters!\n{"- - - - - " * 2}\n')
        _l_(363920)
    elif _n_(363921, 'guess', lambda: guess) in _n_(363922, 'guesses', lambda: guesses):
        _l_(363928)

        _c_(363924, _n_(363923, 'print', lambda: print), f'\n{"- - - - - " * 2}\nYou already guessed that, idiot.\n{"- - - - - " * 2}\n')
        _l_(363925)
    else:
        aux = _n_(363926, 'guess', lambda: guess)
        _l_(363927)
        return aux
    _c_(363934, _a_(363932, _n_(363931, 'guesses', lambda: guesses), 'append'), _n_(363933, 'guess', lambda: guess))
    _l_(363935)


def correct_guess():
    _l_(363958)

    global lives_lost
    _l_(363937)
    lives_lost = 0
    _l_(363938)
    while True:
        _l_(363957)

        if _c_(363940, _n_(363939, 'get_guess', lambda: get_guess)) in _n_(363941, 'guesses', lambda: guesses):
            _l_(363956)

            _c_(363944, _n_(363942, 'print', lambda: print), f'\n{"- - - - - - " * 2}\nNice, {_n_(363943, "guess", lambda: guess)} is in the word.\n{"- - - - - - " * 2}\n')
            _l_(363945)
        elif _n_(363946, 'guess', lambda: guess) not in _c_(363949, _a_(363948, _n_(363947, 'word', lambda: word), 'lower')):
            _l_(363955)

            lives_lost += 1
            _l_(363950)
            _c_(363953, _n_(363951, 'print', lambda: print), f'\n{"- - - - " * 2}\n"{_n_(363952, "guess", lambda: guess)}" is not in the word.\n{"- - - - " * 2}\n')
            _l_(363954)


def display_pic():
    _l_(363971)

    _c_(363962, _n_(363959, 'print', lambda: print), _n_(363960, 'hangman_pics', lambda: hangman_pics)[_n_(363961, 'lives_lost', lambda: lives_lost)])
    _l_(363963)
    _c_(363969, _n_(363964, 'print', lambda: print), _c_(363968, _n_(363965, 'hidden_word', lambda: hidden_word), _n_(363966, 'word', lambda: word), _n_(363967, 'guesses', lambda: guesses)))
    _l_(363970)


def win_or_not():
    _l_(363982)

    win = _c_(363978, _n_(363972, 'all', lambda: all), (_n_(363973, 'item', lambda: item) in _n_(363974, 'guesses', lambda: guesses) for item in _c_(363977, _n_(363975, 'list', lambda: list), _n_(363976, 'word', lambda: word))))
    _l_(363979)
    aux = _n_(363980, 'win', lambda: win)
    _l_(363981)
    return aux


while True:
    _l_(364027)

    lives_lost = 0
    _l_(363983)
    word = _c_(363985, _n_(363984, 'get_word', lambda: get_word))
    _l_(363986)
    _c_(363991, _n_(363987, 'print', lambda: print), f'\n\nGuess a letter. You have 6 lives. You lose a life every time you guess wrong.\n\n{"-----" * 10} '
          f'\nThis word has {_c_(363990, _n_(363988, "len", lambda: len), _n_(363989, "word", lambda: word))} letters. \n{"-----" * 10}\n')
    _l_(363992)
    _c_(363994, _n_(363993, 'display_pic', lambda: display_pic))
    _l_(363995)
    while True:
        _l_(364026)

        _c_(363997, _n_(363996, 'get_guess', lambda: get_guess))
        _l_(363998)
        _c_(364001, _n_(363999, 'print', lambda: print), _n_(364000, 'guess', lambda: guess))
        _l_(364002)
        _c_(364004, _n_(364003, 'correct_guess', lambda: correct_guess))
        _l_(364005)
        _c_(364007, _n_(364006, 'display_pic', lambda: display_pic))
        _l_(364008)
        if _c_(364010, _n_(364009, 'win_or_not', lambda: win_or_not)) is True:
            _l_(364025)

            _c_(364013, _n_(364011, 'print', lambda: print), f'\n{"- - - - - " * 4}\ngood job you won. the word is "{_n_(364012, "word", lambda: word)}".\n{"- - - - - " * 4}')
            _l_(364014)
            break
            _l_(364015)
        elif _n_(364016, 'lives_lost', lambda: lives_lost) == 5 and _c_(364018, _n_(364017, 'win_or_not', lambda: win_or_not)) is False:
            _l_(364024)

            _c_(364021, _n_(364019, 'print', lambda: print), f'\n{"- - - - - " * 2}\nYOU LOSE. the word was "{_n_(364020, "word", lambda: word)}"\n{"- - - - - " * 2}')
            _l_(364022)
            break
            _l_(364023)
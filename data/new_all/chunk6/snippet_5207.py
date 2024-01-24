# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61198226/problem-in-pycharm-hangman-game-beginner-here-obviously-typeerror-object-of
# HANGMAN

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(354303)

except ImportError:
    pass
try:
    import time
    _l_(354305)

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
_l_(354306)

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
_l_(354307)

win = False
_l_(354308)
guesses = []
_l_(354309)


def get_word():
    _l_(354317)

    word = _c_(354313, _a_(354311, _n_(354310, "random", lambda: random), "choice"), _n_(354312, "words", lambda: words))
    _l_(354314)
    aux = _n_(354315, "word", lambda: word)
    _l_(354316)
    return aux


def hidden_word(word, guesses):
    _l_(354327)

    blanks = ''
    _l_(354318)
    for i in _n_(354319, "word", lambda: word):
        _l_(354324)

        blanks += f'{_n_(354320, "i", lambda: i)} ' if _n_(354321, 'i', lambda: i) in _n_(354322, 'guesses', lambda: guesses) else '_ '
        _l_(354323)
    aux = _n_(354325, 'blanks', lambda: blanks)
    _l_(354326)
    return aux


def get_guess():
    _l_(354364)

    global guess
    _l_(354328)
    guess = _a_(354331, _c_(354330, _n_(354329, 'input', lambda: input), '\nYour guess: '), 'lower')
    _l_(354332)
    _c_(354337, _n_(354333, 'print', lambda: print), _c_(354336, _n_(354334, 'len', lambda: len), _n_(354335, 'guess', lambda: guess)))
    _l_(354338)
    if _c_(354341, _n_(354339, 'len', lambda: len), _n_(354340, 'guess', lambda: guess)) != 1:
        _l_(354358)

        _c_(354343, _n_(354342, 'print', lambda: print), f'\n{"- - - - - " * 2}\nOnly guess one letter!\n{"- - - - - " * 2}\n')
        _l_(354344)
    elif _n_(354345, 'guess', lambda: guess) not in 'qwertyuiopasdfghjklzxcvbnm':
        _l_(354357)

        _c_(354347, _n_(354346, 'print', lambda: print), f'\n{"- - - - - " * 2}\nOnly guess letters!\n{"- - - - - " * 2}\n')
        _l_(354348)
    elif _n_(354349, 'guess', lambda: guess) in _n_(354350, 'guesses', lambda: guesses):
        _l_(354356)

        _c_(354352, _n_(354351, 'print', lambda: print), f'\n{"- - - - - " * 2}\nYou already guessed that, idiot.\n{"- - - - - " * 2}\n')
        _l_(354353)
    else:
        aux = _n_(354354, 'guess', lambda: guess)
        _l_(354355)
        return aux
    _c_(354362, _a_(354360, _n_(354359, 'guesses', lambda: guesses), 'append'), _n_(354361, 'guess', lambda: guess))
    _l_(354363)


def correct_guess():
    _l_(354386)

    global lives_lost
    _l_(354365)
    lives_lost = 0
    _l_(354366)
    while True:
        _l_(354385)

        if _c_(354368, _n_(354367, 'get_guess', lambda: get_guess)) in _n_(354369, 'guesses', lambda: guesses):
            _l_(354384)

            _c_(354372, _n_(354370, 'print', lambda: print), f'\n{"- - - - - - " * 2}\nNice, {_n_(354371, "guess", lambda: guess)} is in the word.\n{"- - - - - - " * 2}\n')
            _l_(354373)
        elif _n_(354374, 'guess', lambda: guess) not in _c_(354377, _a_(354376, _n_(354375, 'word', lambda: word), 'lower')):
            _l_(354383)

            lives_lost += 1
            _l_(354378)
            _c_(354381, _n_(354379, 'print', lambda: print), f'\n{"- - - - " * 2}\n"{_n_(354380, "guess", lambda: guess)}" is not in the word.\n{"- - - - " * 2}\n')
            _l_(354382)


def display_pic():
    _l_(354399)

    _c_(354390, _n_(354387, 'print', lambda: print), _n_(354388, 'hangman_pics', lambda: hangman_pics)[_n_(354389, 'lives_lost', lambda: lives_lost)])
    _l_(354391)
    _c_(354397, _n_(354392, 'print', lambda: print), _c_(354396, _n_(354393, 'hidden_word', lambda: hidden_word), _n_(354394, 'word', lambda: word), _n_(354395, 'guesses', lambda: guesses)))
    _l_(354398)


def win_or_not():
    _l_(354410)

    win = _c_(354406, _n_(354400, 'all', lambda: all), (_n_(354401, 'item', lambda: item) in _n_(354402, 'guesses', lambda: guesses) for item in _c_(354405, _n_(354403, 'list', lambda: list), _n_(354404, 'word', lambda: word))))
    _l_(354407)
    aux = _n_(354408, 'win', lambda: win)
    _l_(354409)
    return aux


while True:
    _l_(354455)

    lives_lost = 0
    _l_(354411)
    word = _c_(354413, _n_(354412, 'get_word', lambda: get_word))
    _l_(354414)
    _c_(354419, _n_(354415, 'print', lambda: print), f'\n\nGuess a letter. You have 6 lives. You lose a life every time you guess wrong.\n\n{"-----" * 10} '
          f'\nThis word has {_c_(354418, _n_(354416, "len", lambda: len), _n_(354417, "word", lambda: word))} letters. \n{"-----" * 10}\n')
    _l_(354420)
    _c_(354422, _n_(354421, 'display_pic', lambda: display_pic))
    _l_(354423)
    while True:
        _l_(354454)

        _c_(354425, _n_(354424, 'get_guess', lambda: get_guess))
        _l_(354426)
        _c_(354429, _n_(354427, 'print', lambda: print), _n_(354428, 'guess', lambda: guess))
        _l_(354430)
        _c_(354432, _n_(354431, 'correct_guess', lambda: correct_guess))
        _l_(354433)
        _c_(354435, _n_(354434, 'display_pic', lambda: display_pic))
        _l_(354436)
        if _c_(354438, _n_(354437, 'win_or_not', lambda: win_or_not)) is True:
            _l_(354453)

            _c_(354441, _n_(354439, 'print', lambda: print), f'\n{"- - - - - " * 4}\ngood job you won. the word is "{_n_(354440, "word", lambda: word)}".\n{"- - - - - " * 4}')
            _l_(354442)
            break
            _l_(354443)
        elif _n_(354444, 'lives_lost', lambda: lives_lost) == 5 and _c_(354446, _n_(354445, 'win_or_not', lambda: win_or_not)) is False:
            _l_(354452)

            _c_(354449, _n_(354447, 'print', lambda: print), f'\n{"- - - - - " * 2}\nYOU LOSE. the word was "{_n_(354448, "word", lambda: word)}"\n{"- - - - - " * 2}')
            _l_(354450)
            break
            _l_(354451)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60761057/typeerror-nonetype-object-is-not-iterable-even-though-it-is-set
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(663443)

except ImportError:
    pass
try:
    import time
    _l_(663445)

except ImportError:
    pass


def login():
    _l_(663471)

    while True:
        _l_(663470)

        username = _c_(663447, _n_(663446, "input", lambda: input), 'What is your username? ')
        _l_(663448)
        password = _c_(663450, _n_(663449, "input", lambda: input), 'What is your password? ')
        _l_(663451)
        if _n_(663452, "username", lambda: username) not in ('User1', 'User2', 'User3', 'User4', 'User5'):
            _l_(663457)

            _c_(663454, _n_(663453, "print", lambda: print), 'Incorrect username, try again')
            _l_(663455)
            continue
            _l_(663456)

        if _n_(663458, "password", lambda: password) != "pwd":
            _l_(663463)

            _c_(663460, _n_(663459, "print", lambda: print), 'Incorrect password, try again')
            _l_(663461)
            continue
            _l_(663462)

        _c_(663466, _n_(663464, "print", lambda: print), f'Welcome, {_n_(663465, "username", lambda: username)} you have been successfully logged in.')
        _l_(663467)
        aux = _n_(663468, 'username', lambda: username)
        _l_(663469)
        return aux


def roll():
    _l_(663496)

    die1 = _c_(663474, _a_(663473, _n_(663472, 'random', lambda: random), 'randint'), 1, 6)
    _l_(663475)
    die2 = _c_(663478, _a_(663477, _n_(663476, 'random', lambda: random), 'randint'), 1, 6)
    _l_(663479)
    change = 10 if (_n_(663480, 'die1', lambda: die1) + _n_(663481, 'die2', lambda: die2)) % 2 == 0 else -5
    _l_(663482)
    points = _n_(663483, 'die1', lambda: die1) + _n_(663484, 'die2', lambda: die2) + _n_(663485, 'change', lambda: change)
    _l_(663486)
    if _n_(663487, 'die1', lambda: die1) == _n_(663488, 'die2', lambda: die2):
        _l_(663493)

        points += _c_(663491, _a_(663490, _n_(663489, 'random', lambda: random), 'randint'), 1, 6)
        _l_(663492)
    aux = _n_(663494, 'points', lambda: points)
    _l_(663495)
    return aux


def game(user1, user2):
    _l_(663554)

    player1_points = 0
    _l_(663497)
    player2_points = 0
    _l_(663498)
    for i in _c_(663500, _n_(663499, 'range', lambda: range), 1,5):
        _l_(663525)

        player1_points += _c_(663502, _n_(663501, 'roll', lambda: roll))
        _l_(663503)
        _c_(663507, _n_(663504, 'print', lambda: print), f'After this round {_n_(663505, "user1", lambda: user1)} you now have: {_n_(663506, "player1_points", lambda: player1_points)} Points')
        _l_(663508)
        _c_(663511, _a_(663510, _n_(663509, 'time', lambda: time), 'sleep'), 1)
        _l_(663512)
        player2_points += _c_(663514, _n_(663513, 'roll', lambda: roll))
        _l_(663515)
        _c_(663519, _n_(663516, 'print', lambda: print), f'After this round {_n_(663517, "user2", lambda: user2)} you now have: {_n_(663518, "player2_points", lambda: player2_points)} Points')
        _l_(663520)
        _c_(663523, _a_(663522, _n_(663521, 'time', lambda: time), 'sleep'), 1)
        _l_(663524)

    player1TieBreak = _n_(663526, 'player1_points', lambda: player1_points)
    _l_(663527)
    player2TieBreak = _n_(663528, 'player2_points', lambda: player2_points)
    _l_(663529)
    if _n_(663530, 'player1_points', lambda: player1_points) == _n_(663531, 'player2TieBreak', lambda: player2TieBreak):
        _l_(663553)

        player1TieBreak = _c_(663534, _a_(663533, _n_(663532, 'random', lambda: random), 'randint'), 1,6)
        _l_(663535)
        player2TieBreak = _c_(663538, _a_(663537, _n_(663536, 'random', lambda: random), 'randint'), 1,6)
        _l_(663539)
        if _n_(663540, 'player1TieBreak', lambda: player1TieBreak) > _n_(663541, 'player2TieBreak', lambda: player2TieBreak):
            _l_(663552)

            aux = (_n_(663542, 'player1_points', lambda: player1_points), _n_(663543, 'player1_win', lambda: player1_win)), (_n_(663544, 'player2_points', lambda: player2_points), not _n_(663545, 'player2_win', lambda: player2_win))
            _l_(663546)
            return aux
        else:
            aux = (_n_(663547, 'player2_points', lambda: player2_points), _n_(663548, 'player2_win', lambda: player2_win)), (_n_(663549, 'player1_points', lambda: player1_points), not _n_(663550, 'player1_win', lambda: player1_win))
            _l_(663551)
            return aux


def add_winner(winner):
    _l_(663562)

    with _c_(663556, _n_(663555, 'open', lambda: open), 'Winner.txt', 'a') as f:
        _l_(663561)

        _c_(663559, _a_(663558, _n_(663557, 'f', lambda: f), 'write'), '{winner[0]},{winner[1]}\n')
        _l_(663560)


def get_leaderboard():
    _l_(663573)

    with _c_(663564, _n_(663563, 'open', lambda: open), 'Leaderboard.txt', 'r') as f:
        _l_(663572)

        aux = [_c_(663567, _a_(663566, _n_(663565, 'line', lambda: line), 'replace'), '\n','') for line in _c_(663570, _a_(663569, _n_(663568, 'f', lambda: f), 'readlines'))]
        _l_(663571)
        return aux


def update_leaderboard(leaderboard, winner):
    _l_(663603)

    for idx, item in _c_(663576, _n_(663574, 'enumerate', lambda: enumerate), _n_(663575, 'leaderboard', lambda: leaderboard)):
        _l_(663598)

        if _c_(663579, _a_(663578, _n_(663577, 'item', lambda: item), 'split'), ', ')[1] == _n_(663580, 'winner', lambda: winner)[1] and _c_(663585, _n_(663581, 'int', lambda: int), _c_(663584, _a_(663583, _n_(663582, 'item', lambda: item), 'split'), ', ')[0]) < _c_(663588, _n_(663586, 'int', lambda: int), _n_(663587, 'winner', lambda: winner)[0]):
            _l_(663597)

            _n_(663589, 'leaderboard', lambda: leaderboard)[_n_(663590, 'idx', lambda: idx)] = _c_(663594, _a_(663591, '{}, {}', 'format'), _n_(663592, 'winner', lambda: winner)[0], _n_(663593, 'winner', lambda: winner)[1])
            _l_(663595)
        else:
            pass
            _l_(663596)
    _c_(663601, _a_(663600, _n_(663599, 'leaderboard', lambda: leaderboard), 'sort'), reverse=True)
    _l_(663602)


def save_leaderboard(leaderboard):
    _l_(663614)

    with _c_(663605, _n_(663604, 'open', lambda: open), 'Leaderboard.txt', 'w') as f:
        _l_(663613)

        for item in _n_(663606, 'leaderboard', lambda: leaderboard):
            _l_(663612)

            _c_(663610, _a_(663608, _n_(663607, 'f', lambda: f), 'write'), f'{_n_(663609, "item", lambda: item)}\n')
            _l_(663611)


def main():
    _l_(663653)

    user1 = _c_(663616, _n_(663615, 'login', lambda: login))
    _l_(663617)
    user2 = _c_(663619, _n_(663618, 'login', lambda: login))
    _l_(663620)
    (player1, player1_win), (player2, player2_win) = _c_(663624, _n_(663621, 'game', lambda: game), _n_(663622, 'user1', lambda: user1), _n_(663623, 'user2', lambda: user2))
    _l_(663625)
    if _n_(663626, 'player1_win', lambda: player1_win):
        _l_(663633)

        winner = (_n_(663627, 'player1', lambda: player1), _n_(663628, 'user1', lambda: user1))
        _l_(663629)
    else:
        winner = (_n_(663630, 'player2', lambda: player2), _n_(663631, 'user2', lambda: user2))
        _l_(663632)
    _c_(663635, _n_(663634, 'print', lambda: print), 'Well done, {winner[1]} you won with {winner[0]} Points')
    _l_(663636)
    _c_(663639, _n_(663637, 'add_winner', lambda: add_winner), _n_(663638, 'winner', lambda: winner))
    _l_(663640)
    leaderboard = _c_(663642, _n_(663641, 'get_leaderboard', lambda: get_leaderboard))
    _l_(663643)
    _c_(663647, _n_(663644, 'update_leaderboard', lambda: update_leaderboard), _n_(663645, 'leaderboard', lambda: leaderboard), _n_(663646, 'winner', lambda: winner))
    _l_(663648)
    _c_(663651, _n_(663649, 'save_leaderboard', lambda: save_leaderboard), _n_(663650, 'leaderboard', lambda: leaderboard))
    _l_(663652)



_c_(663655, _n_(663654, 'main', lambda: main))
_l_(663656)
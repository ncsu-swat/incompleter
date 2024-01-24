# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60761057/typeerror-nonetype-object-is-not-iterable-even-though-it-is-set
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(688118)

except ImportError:
    pass
try:
    import time
    _l_(688120)

except ImportError:
    pass


def login():
    _l_(688146)

    while True:
        _l_(688145)

        username = _c_(688122, _n_(688121, "input", lambda: input), 'What is your username? ')
        _l_(688123)
        password = _c_(688125, _n_(688124, "input", lambda: input), 'What is your password? ')
        _l_(688126)
        if _n_(688127, "username", lambda: username) not in ('User1', 'User2', 'User3', 'User4', 'User5'):
            _l_(688132)

            _c_(688129, _n_(688128, "print", lambda: print), 'Incorrect username, try again')
            _l_(688130)
            continue
            _l_(688131)

        if _n_(688133, "password", lambda: password) != "pwd":
            _l_(688138)

            _c_(688135, _n_(688134, "print", lambda: print), 'Incorrect password, try again')
            _l_(688136)
            continue
            _l_(688137)

        _c_(688141, _n_(688139, "print", lambda: print), f'Welcome, {_n_(688140, "username", lambda: username)} you have been successfully logged in.')
        _l_(688142)
        aux = _n_(688143, 'username', lambda: username)
        _l_(688144)
        return aux


def roll():
    _l_(688171)

    die1 = _c_(688149, _a_(688148, _n_(688147, 'random', lambda: random), 'randint'), 1, 6)
    _l_(688150)
    die2 = _c_(688153, _a_(688152, _n_(688151, 'random', lambda: random), 'randint'), 1, 6)
    _l_(688154)
    change = 10 if (_n_(688155, 'die1', lambda: die1) + _n_(688156, 'die2', lambda: die2)) % 2 == 0 else -5
    _l_(688157)
    points = _n_(688158, 'die1', lambda: die1) + _n_(688159, 'die2', lambda: die2) + _n_(688160, 'change', lambda: change)
    _l_(688161)
    if _n_(688162, 'die1', lambda: die1) == _n_(688163, 'die2', lambda: die2):
        _l_(688168)

        points += _c_(688166, _a_(688165, _n_(688164, 'random', lambda: random), 'randint'), 1, 6)
        _l_(688167)
    aux = _n_(688169, 'points', lambda: points)
    _l_(688170)
    return aux


def game(user1, user2):
    _l_(688229)

    player1_points = 0
    _l_(688172)
    player2_points = 0
    _l_(688173)
    for i in _c_(688175, _n_(688174, 'range', lambda: range), 1,5):
        _l_(688200)

        player1_points += _c_(688177, _n_(688176, 'roll', lambda: roll))
        _l_(688178)
        _c_(688182, _n_(688179, 'print', lambda: print), f'After this round {_n_(688180, "user1", lambda: user1)} you now have: {_n_(688181, "player1_points", lambda: player1_points)} Points')
        _l_(688183)
        _c_(688186, _a_(688185, _n_(688184, 'time', lambda: time), 'sleep'), 1)
        _l_(688187)
        player2_points += _c_(688189, _n_(688188, 'roll', lambda: roll))
        _l_(688190)
        _c_(688194, _n_(688191, 'print', lambda: print), f'After this round {_n_(688192, "user2", lambda: user2)} you now have: {_n_(688193, "player2_points", lambda: player2_points)} Points')
        _l_(688195)
        _c_(688198, _a_(688197, _n_(688196, 'time', lambda: time), 'sleep'), 1)
        _l_(688199)

    player1TieBreak = _n_(688201, 'player1_points', lambda: player1_points)
    _l_(688202)
    player2TieBreak = _n_(688203, 'player2_points', lambda: player2_points)
    _l_(688204)
    if _n_(688205, 'player1_points', lambda: player1_points) == _n_(688206, 'player2TieBreak', lambda: player2TieBreak):
        _l_(688228)

        player1TieBreak = _c_(688209, _a_(688208, _n_(688207, 'random', lambda: random), 'randint'), 1,6)
        _l_(688210)
        player2TieBreak = _c_(688213, _a_(688212, _n_(688211, 'random', lambda: random), 'randint'), 1,6)
        _l_(688214)
        if _n_(688215, 'player1TieBreak', lambda: player1TieBreak) > _n_(688216, 'player2TieBreak', lambda: player2TieBreak):
            _l_(688227)

            aux = (_n_(688217, 'player1_points', lambda: player1_points), _n_(688218, 'player1_win', lambda: player1_win)), (_n_(688219, 'player2_points', lambda: player2_points), not _n_(688220, 'player2_win', lambda: player2_win))
            _l_(688221)
            return aux
        else:
            aux = (_n_(688222, 'player2_points', lambda: player2_points), _n_(688223, 'player2_win', lambda: player2_win)), (_n_(688224, 'player1_points', lambda: player1_points), not _n_(688225, 'player1_win', lambda: player1_win))
            _l_(688226)
            return aux


def add_winner(winner):
    _l_(688237)

    with _c_(688231, _n_(688230, 'open', lambda: open), 'Winner.txt', 'a') as f:
        _l_(688236)

        _c_(688234, _a_(688233, _n_(688232, 'f', lambda: f), 'write'), '{winner[0]},{winner[1]}\n')
        _l_(688235)


def get_leaderboard():
    _l_(688248)

    with _c_(688239, _n_(688238, 'open', lambda: open), 'Leaderboard.txt', 'r') as f:
        _l_(688247)

        aux = [_c_(688242, _a_(688241, _n_(688240, 'line', lambda: line), 'replace'), '\n','') for line in _c_(688245, _a_(688244, _n_(688243, 'f', lambda: f), 'readlines'))]
        _l_(688246)
        return aux


def update_leaderboard(leaderboard, winner):
    _l_(688278)

    for idx, item in _c_(688251, _n_(688249, 'enumerate', lambda: enumerate), _n_(688250, 'leaderboard', lambda: leaderboard)):
        _l_(688273)

        if _c_(688254, _a_(688253, _n_(688252, 'item', lambda: item), 'split'), ', ')[1] == _n_(688255, 'winner', lambda: winner)[1] and _c_(688260, _n_(688256, 'int', lambda: int), _c_(688259, _a_(688258, _n_(688257, 'item', lambda: item), 'split'), ', ')[0]) < _c_(688263, _n_(688261, 'int', lambda: int), _n_(688262, 'winner', lambda: winner)[0]):
            _l_(688272)

            _n_(688264, 'leaderboard', lambda: leaderboard)[_n_(688265, 'idx', lambda: idx)] = _c_(688269, _a_(688266, '{}, {}', 'format'), _n_(688267, 'winner', lambda: winner)[0], _n_(688268, 'winner', lambda: winner)[1])
            _l_(688270)
        else:
            pass
            _l_(688271)
    _c_(688276, _a_(688275, _n_(688274, 'leaderboard', lambda: leaderboard), 'sort'), reverse=True)
    _l_(688277)


def save_leaderboard(leaderboard):
    _l_(688289)

    with _c_(688280, _n_(688279, 'open', lambda: open), 'Leaderboard.txt', 'w') as f:
        _l_(688288)

        for item in _n_(688281, 'leaderboard', lambda: leaderboard):
            _l_(688287)

            _c_(688285, _a_(688283, _n_(688282, 'f', lambda: f), 'write'), f'{_n_(688284, "item", lambda: item)}\n')
            _l_(688286)


def main():
    _l_(688328)

    user1 = _c_(688291, _n_(688290, 'login', lambda: login))
    _l_(688292)
    user2 = _c_(688294, _n_(688293, 'login', lambda: login))
    _l_(688295)
    (player1, player1_win), (player2, player2_win) = _c_(688299, _n_(688296, 'game', lambda: game), _n_(688297, 'user1', lambda: user1), _n_(688298, 'user2', lambda: user2))
    _l_(688300)
    if _n_(688301, 'player1_win', lambda: player1_win):
        _l_(688308)

        winner = (_n_(688302, 'player1', lambda: player1), _n_(688303, 'user1', lambda: user1))
        _l_(688304)
    else:
        winner = (_n_(688305, 'player2', lambda: player2), _n_(688306, 'user2', lambda: user2))
        _l_(688307)
    _c_(688310, _n_(688309, 'print', lambda: print), 'Well done, {winner[1]} you won with {winner[0]} Points')
    _l_(688311)
    _c_(688314, _n_(688312, 'add_winner', lambda: add_winner), _n_(688313, 'winner', lambda: winner))
    _l_(688315)
    leaderboard = _c_(688317, _n_(688316, 'get_leaderboard', lambda: get_leaderboard))
    _l_(688318)
    _c_(688322, _n_(688319, 'update_leaderboard', lambda: update_leaderboard), _n_(688320, 'leaderboard', lambda: leaderboard), _n_(688321, 'winner', lambda: winner))
    _l_(688323)
    _c_(688326, _n_(688324, 'save_leaderboard', lambda: save_leaderboard), _n_(688325, 'leaderboard', lambda: leaderboard))
    _l_(688327)



_c_(688330, _n_(688329, 'main', lambda: main))
_l_(688331)
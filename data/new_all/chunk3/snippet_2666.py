# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67387301/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(553771)

except ImportError:
    pass
try:
    from _thread import *
    _l_(553773)

except ImportError:
    pass
try:
    import pickle
    _l_(553775)

except ImportError:
    pass
try:
    from game import Game
    _l_(553777)

except ImportError:
    pass

server = '192.168.100.5' # The server.py script has to be runing on this machine
_l_(553778) # The server.py script has to be runing on this machine
port = 5555
_l_(553779)

s = _c_(553786, _a_(553781, _n_(553780, "socket", lambda: socket), "socket"), _a_(553783, _n_(553782, "socket", lambda: socket), "AF_INET"), _a_(553785, _n_(553784, "socket", lambda: socket), "SOCK_STREAM"))
_l_(553787)

try:
    _l_(553801)

    _c_(553792, _a_(553789, _n_(553788, "s", lambda: s), "bind"), (_n_(553790, "server", lambda: server), _n_(553791, "port", lambda: port)))
    _l_(553793)
except _a_(553795, _n_(553794, "socket", lambda: socket), "error") as e:
    _l_(553800)

    _c_(553798, _n_(553796, "print", lambda: print), _n_(553797, "e", lambda: e))
    _l_(553799)

_c_(553804, _a_(553803, _n_(553802, "s", lambda: s), "listen"), 2) # This listen for two clint connections
_l_(553805) # This listen for two clint connections
_c_(553807, _n_(553806, "print", lambda: print), 'Waiting for a connection, Server Started')
_l_(553808)

games = {}
_l_(553809)
id_count = 0
_l_(553810)

def threaded_client(connection, player, game_id):
    _l_(553881)

    # Each client has one version of this function running in the background at the same time
    global id_count
    _l_(553811)
    _c_(553820, _a_(553813, _n_(553812, "connection", lambda: connection), "send"), _c_(553819, _a_(553815, _n_(553814, "str", lambda: str), "encode"), _c_(553818, _n_(553816, "str", lambda: str), _n_(553817, "player", lambda: player))))
    _l_(553821)

    reply = ''
    _l_(553822)
    while True:
        _l_(553864)

        try:
            _l_(553863)

            data = _c_(553827, _a_(553826, _c_(553825, _a_(553824, _n_(553823, "connection", lambda: connection), "recv"), 4096), "decode")) # it Receives string from the client
            _l_(553828) # it Receives string from the client

            if _n_(553829, "game_id", lambda: game_id) in _n_(553830, "games", lambda: games):
                _l_(553860)

                # This checks if the game still exists, because if the client disconnects from the game we'll delete it
                game = _n_(553831, "games", lambda: games)[_n_(553832, "game_id", lambda: game_id)]
                _l_(553833)

                if not _n_(553834, "data", lambda: data):
                    _l_(553858)

                    break
                    _l_(553835)
                else:
                    if _n_(553836, "data", lambda: data) == 'reset':
                        _l_(553849)

                        _c_(553839, _a_(553838, _n_(553837, "game", lambda: game), "reset_moves"))
                        _l_(553840)
                    elif _n_(553841, "data", lambda: data) != 'get':
                        _l_(553848)

                        _c_(553846, _a_(553843, _n_(553842, "game", lambda: game), "play"), _n_(553844, "player", lambda: player), _n_(553845, "data", lambda: data))
                        _l_(553847)
                    
                    _c_(553856, _a_(553851, _n_(553850, "connection", lambda: connection), "sendall"), _c_(553855, _a_(553853, _n_(553852, "pickle", lambda: pickle), "dumps"), _n_(553854, "game", lambda: game)))
                    _l_(553857)
            else:
                break
                _l_(553859)
        except:
            _l_(553862)

            break
            _l_(553861)
    _c_(553866, _n_(553865, "print", lambda: print), 'Lost connection')
    _l_(553867)
    try:
        _l_(553875)

        del games[game_id]
        _l_(553868)
        _c_(553871, _n_(553869, "print", lambda: print), 'Closing game:', _n_(553870, "game_id", lambda: game_id))
        _l_(553872)
    except:
        _l_(553874)

        pass
        _l_(553873)
    id_count -= 1 # One client was closed
    _l_(553876) # One client was closed
    _c_(553879, _a_(553878, _n_(553877, "connection", lambda: connection), "close"))
    _l_(553880)

while True:
    _l_(553916)

    connection, address = _c_(553884, _a_(553883, _n_(553882, "s", lambda: s), "accept")) # connection -> new socket object; address -> address of the sockect from the other device
    _l_(553885) # connection -> new socket object; address -> address of the sockect from the other device
    _c_(553888, _n_(553886, "print", lambda: print), 'Connected to: ', _n_(553887, "address", lambda: address))
    _l_(553889)

    id_count += 1
    _l_(553890)
    player = 0
    _l_(553891)
    game_id = (_n_(553892, "id_count", lambda: id_count) - 1) // 2 # This will make a single game id for every two people that connect to the server
    _l_(553893) # This will make a single game id for every two people that connect to the server
    if _n_(553894, "id_count", lambda: id_count) % 2 == 1:
        _l_(553908)

        # if the result is 0, it means that there are even clients playing the game, but if it is 1,
        # it means that there are odd clients playing the game
        _n_(553895, "games", lambda: games)[_n_(553896, "game_id", lambda: game_id)] = _c_(553899, _n_(553897, "Game", lambda: Game), _n_(553898, "game_id", lambda: game_id)) # It creates a new game when there are odd clients
        _l_(553900) # It creates a new game when there are odd clients
        _c_(553902, _n_(553901, "print", lambda: print), 'Creating a new game...')
        _l_(553903)
    else:
        _n_(553904, "games", lambda: games)[_n_(553905, "game_id", lambda: game_id)].ready = True
        _l_(553906)
        player = 1
        _l_(553907)

    # start_new_thread(function, arguments)
    _c_(553914, _n_(553909, "start_new_thread", lambda: start_new_thread), _n_(553910, "threaded_client", lambda: threaded_client), (_n_(553911, "connection", lambda: connection), _n_(553912, "player", lambda: player), _n_(553913, "game_id", lambda: game_id)))
    _l_(553915)
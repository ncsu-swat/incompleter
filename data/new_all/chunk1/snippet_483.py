# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59298759/typeerror-nonetype-object-is-not-subscriptable-for-a-dictionary-in-my-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(394479)

    _c_(394445, _n_(394442, "print", lambda: print), _c_(394444, _n_(394443, "render_introduction", lambda: render_introduction)))
    _l_(394446)
    world = _c_(394448, _n_(394447, "create_world", lambda: create_world))
    _l_(394449)
    while _n_(394450, "world", lambda: world)['status'] == 'playing':
        _l_(394472)

        _c_(394455, _n_(394451, "print", lambda: print), _c_(394454, _n_(394452, "render", lambda: render), _n_(394453, "world", lambda: world)))  #line 316
        _l_(394456)  #line 316
        options = _c_(394459, _n_(394457, "get_options", lambda: get_options), _n_(394458, "world", lambda: world))
        _l_(394460)
        command = _c_(394463, _n_(394461, "choose", lambda: choose), _n_(394462, "options", lambda: options))
        _l_(394464)
        _c_(394470, _n_(394465, "print", lambda: print), _c_(394469, _n_(394466, "update", lambda: update), _n_(394467, "world", lambda: world), _n_(394468, "command", lambda: command)))
        _l_(394471)
    _c_(394477, _n_(394473, "print", lambda: print), _c_(394476, _n_(394474, "render_ending", lambda: render_ending), _n_(394475, "world", lambda: world)))
    _l_(394478)
if _n_(394480, "__name__", lambda: __name__) == '__main__':
    _l_(394484)

    _c_(394482, _n_(394481, "main", lambda: main)) #line323
    _l_(394483) #line323
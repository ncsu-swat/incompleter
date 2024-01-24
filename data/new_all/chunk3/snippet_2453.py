# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17002379/checking-collisions-for-each-sprite-in-a-group-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if not _n_(545674, "game_over", lambda: game_over):
    _l_(545698)

    _c_(545676, _n_(545675, "move_coins", lambda: move_coins))
    _l_(545677)
    _c_(545679, _n_(545678, "move_pointer", lambda: move_pointer))
    _l_(545680)
    if _c_(545686, _a_(545683, _a_(545682, _n_(545681, "pygame", lambda: pygame), "sprite"), "spritecollideany"), _n_(545684, "pointer", lambda: pointer), _n_(545685, "coin_group", lambda: coin_group)):
        _l_(545697)

        _c_(545692, _n_(545687, "print_text", lambda: print_text), _c_(545691, _a_(545690, _a_(545689, _n_(545688, "pygame", lambda: pygame), "font"), "Font"), None,16), 0, 0, "Collision!")
        _l_(545693)
        _c_(545695, _n_(545694, "check_collision", lambda: check_collision))
        _l_(545696)
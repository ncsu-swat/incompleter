# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57246202/how-to-fix-attributeerror-class-object-has-no-attribute-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def apartment_movement():
    _l_(529882)


    keys = _c_(529755, _a_(529754, _a_(529753, _n_(529752, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(529756)

    boundary = _c_(529762, _a_(529759, _a_(529758, _n_(529757, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(529760, "scarn", lambda: scarn), _n_(529761, "apartment_walls", lambda: apartment_walls), False, False)
    _l_(529763)

    if _n_(529764, "boundary", lambda: boundary):
        _l_(529777)

        _n_(529765, "scarn", lambda: scarn).left = False
        _l_(529766)
        _n_(529767, "scarn", lambda: scarn).right = False
        _l_(529768)
        _n_(529769, "scarn", lambda: scarn).up = False
        _l_(529770)
        _n_(529771, "scarn", lambda: scarn).down = False
        _l_(529772)
        _n_(529773, "scarn", lambda: scarn).standing = False
        _l_(529774)
        _n_(529775, "scarn", lambda: scarn).sleeping = False
        _l_(529776)
    if not _n_(529778, "boundary", lambda: boundary):
        _l_(529881)

        if _n_(529779, "keys", lambda: keys)[_a_(529781, _n_(529780, "pygame", lambda: pygame), "K_LEFT")] and _a_(529783, _n_(529782, "scarn", lambda: scarn), "x") > 110 - _a_(529785, _n_(529784, "scarn", lambda: scarn), "width") - _a_(529787, _n_(529786, "scarn", lambda: scarn), "vel"):
            _l_(529880)

            _n_(529788, "scarn", lambda: scarn).x -= _n_(529789, "scarn", lambda: scarn).vel
            _l_(529790)
            _n_(529791, "scarn", lambda: scarn).left = True
            _l_(529792)
            _n_(529793, "scarn", lambda: scarn).right = False
            _l_(529794)
            _n_(529795, "scarn", lambda: scarn).up = False
            _l_(529796)
            _n_(529797, "scarn", lambda: scarn).down = False
            _l_(529798)
            _n_(529799, "scarn", lambda: scarn).standing = False
            _l_(529800)
            _n_(529801, "scarn", lambda: scarn).sleeping = False
            _l_(529802)
        elif _n_(529803, "keys", lambda: keys)[_a_(529805, _n_(529804, "pygame", lambda: pygame), "K_RIGHT")] and _a_(529807, _n_(529806, "scarn", lambda: scarn), "x") < 795 - _a_(529809, _n_(529808, "scarn", lambda: scarn), "width") - _a_(529811, _n_(529810, "scarn", lambda: scarn), "vel"):
            _l_(529879)

            _n_(529812, "scarn", lambda: scarn).x += _n_(529813, "scarn", lambda: scarn).vel
            _l_(529814)
            _n_(529815, "scarn", lambda: scarn).right = True
            _l_(529816)
            _n_(529817, "scarn", lambda: scarn).left = False
            _l_(529818)
            _n_(529819, "scarn", lambda: scarn).up = False
            _l_(529820)
            _n_(529821, "scarn", lambda: scarn).down = False
            _l_(529822)
            _n_(529823, "scarn", lambda: scarn).standing = False
            _l_(529824)
            _n_(529825, "scarn", lambda: scarn).sleeping = False
            _l_(529826)
        elif _n_(529827, "keys", lambda: keys)[_a_(529829, _n_(529828, "pygame", lambda: pygame), "K_UP")] and _a_(529831, _n_(529830, "scarn", lambda: scarn), "y") > 130 - _a_(529833, _n_(529832, "scarn", lambda: scarn), "height") - _a_(529835, _n_(529834, "scarn", lambda: scarn), "vel"):
            _l_(529878)

            _n_(529836, "scarn", lambda: scarn).y -= _n_(529837, "scarn", lambda: scarn).vel
            _l_(529838)
            _n_(529839, "scarn", lambda: scarn).up = True
            _l_(529840)
            _n_(529841, "scarn", lambda: scarn).right = False
            _l_(529842)
            _n_(529843, "scarn", lambda: scarn).left = False
            _l_(529844)
            _n_(529845, "scarn", lambda: scarn).down = False
            _l_(529846)
            _n_(529847, "scarn", lambda: scarn).standing = False
            _l_(529848)
            _n_(529849, "scarn", lambda: scarn).sleeping = False
            _l_(529850)
        elif _n_(529851, "keys", lambda: keys)[_a_(529853, _n_(529852, "pygame", lambda: pygame), "K_DOWN")] and _a_(529855, _n_(529854, "scarn", lambda: scarn), "y") < 540 - _a_(529857, _n_(529856, "scarn", lambda: scarn), "height") - _a_(529859, _n_(529858, "scarn", lambda: scarn), "vel"):
            _l_(529877)

            _n_(529860, "scarn", lambda: scarn).y += _n_(529861, "scarn", lambda: scarn).vel
            _l_(529862)
            _n_(529863, "scarn", lambda: scarn).down = True
            _l_(529864)
            _n_(529865, "scarn", lambda: scarn).right = False
            _l_(529866)
            _n_(529867, "scarn", lambda: scarn).left = False
            _l_(529868)
            _n_(529869, "scarn", lambda: scarn).up = False
            _l_(529870)
            _n_(529871, "scarn", lambda: scarn).standing = False
            _l_(529872)
            _n_(529873, "scarn", lambda: scarn).sleeping = False
            _l_(529874)
        else:  # clarifies the player is not moving left or right
            _n_(529875, "scarn", lambda: scarn).walkCount = 0
            _l_(529876)


class apartment_walls(_a_(529885, _a_(529884, _n_(529883, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(529959)


    def __init__(self):
        _l_(529958)

        _c_(529891, _a_(529889, _a_(529888, _a_(529887, _n_(529886, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(529890, "self", lambda: self))
        _l_(529892)
        _n_(529893, "self", lambda: self).boundary1 = _c_(529896, _a_(529895, _n_(529894, "pygame", lambda: pygame), "Rect"), 243, 60, 8, 275)
        _l_(529897)
        _n_(529898, "self", lambda: self).boundary2 = _c_(529901, _a_(529900, _n_(529899, "pygame", lambda: pygame), "Rect"), 510, 60, 8, 275)
        _l_(529902)
        _n_(529903, "self", lambda: self).boundary3 = _c_(529906, _a_(529905, _n_(529904, "pygame", lambda: pygame), "Rect"), 243, 421, 215, 5)
        _l_(529907)
        _n_(529908, "self", lambda: self).boundary4 = _c_(529911, _a_(529910, _n_(529909, "pygame", lambda: pygame), "Rect"), 243, 330, 220, 5)
        _l_(529912)
        _n_(529913, "self", lambda: self).boundary5 = _c_(529916, _a_(529915, _n_(529914, "pygame", lambda: pygame), "Rect"), 510, 421, 145, 5)
        _l_(529917)
        _n_(529918, "self", lambda: self).boundary6 = _c_(529921, _a_(529920, _n_(529919, "pygame", lambda: pygame), "Rect"), 510, 330, 145, 5)
        _l_(529922)
        _n_(529923, "self", lambda: self).boundary7 = _c_(529926, _a_(529925, _n_(529924, "pygame", lambda: pygame), "Rect"), 700, 421, 57, 5)
        _l_(529927)
        _n_(529928, "self", lambda: self).boundary8 = _c_(529931, _a_(529930, _n_(529929, "pygame", lambda: pygame), "Rect"), 700, 330, 57, 5)
        _l_(529932)
        _n_(529933, "self", lambda: self).boundary9 = _c_(529936, _a_(529935, _n_(529934, "pygame", lambda: pygame), "Rect"), 43, 410, 120, 10)
        _l_(529937)
        _n_(529938, "self", lambda: self).boundary10 = _c_(529941, _a_(529940, _n_(529939, "pygame", lambda: pygame), "Rect"), 510, 335, 5, 90)
        _l_(529942)
        _n_(529943, "self", lambda: self).boundary11 = _c_(529946, _a_(529945, _n_(529944, "pygame", lambda: pygame), "Rect"), 460, 335, 5, 90)
        _l_(529947)
        _n_(529948, "self", lambda: self).boundary12 = _c_(529951, _a_(529950, _n_(529949, "pygame", lambda: pygame), "Rect"), 700, 335, 5, 90)
        _l_(529952)
        _n_(529953, "self", lambda: self).boundary13 = _c_(529956, _a_(529955, _n_(529954, "pygame", lambda: pygame), "Rect"), 650, 335, 5, 90)
        _l_(529957)


def draw_apartment():
    _l_(529989)


    _c_(529963, _a_(529961, _n_(529960, "win", lambda: win), "blit"), _n_(529962, "bg", lambda: bg), (0, 0))
    _l_(529964)
    _c_(529968, _a_(529966, _n_(529965, "win", lambda: win), "blit"), _n_(529967, "bed", lambda: bed), (322, 120))
    _l_(529969)

    _c_(529975, _a_(529972, _a_(529971, _n_(529970, "pygame", lambda: pygame), "draw"), "rect"), _n_(529973, "win", lambda: win), _n_(529974, "black", lambda: black), (200, 470, 100, 10), 0)
    _l_(529976)
    _c_(529982, _a_(529979, _a_(529978, _n_(529977, "pygame", lambda: pygame), "draw"), "polygon"), _n_(529980, "win", lambda: win), _n_(529981, "black", lambda: black), [(180, 473), (200, 488), (200, 458)], 0)
    _l_(529983)

    _c_(529987, _a_(529985, _n_(529984, "scarn", lambda: scarn), "draw"), _n_(529986, "win", lambda: win))
    _l_(529988)


class Scarn(_a_(529992, _a_(529991, _n_(529990, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(530072)


    def __init__(self, x, y, width, height):
        _l_(530071)

        _c_(529998, _a_(529996, _a_(529995, _a_(529994, _n_(529993, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(529997, "self", lambda: self))
        _l_(529999)
        # loads sprites for animations
        _n_(530000, "self", lambda: self).rect = _c_(530007, _a_(530002, _n_(530001, "pygame", lambda: pygame), "Rect"), _c_(530006, _a_(530005, _a_(530004, _n_(530003, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Forward Standing.png')), _c_(530014, _a_(530009, _n_(530008, "pygame", lambda: pygame), "Rect"), _c_(530013, _a_(530012, _a_(530011, _n_(530010, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Backward Standing.png')), _c_(530025, _a_(530016, _n_(530015, "pygame", lambda: pygame), "Rect"), [_c_(530020, _a_(530019, _a_(530018, _n_(530017, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Up 1.png'), _c_(530024, _a_(530023, _a_(530022, _n_(530021, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Up 2.png')]), [
                        _c_(530029, _a_(530028, _a_(530027, _n_(530026, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Down 1.png'), _c_(530033, _a_(530032, _a_(530031, _n_(530030, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Down 2.png')], [
                        _c_(530037, _a_(530036, _a_(530035, _n_(530034, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Right 1.png'), _c_(530041, _a_(530040, _a_(530039, _n_(530038, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Right 2.png'),
                        _c_(530045, _a_(530044, _a_(530043, _n_(530042, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Right 3.png'),
                        _c_(530049, _a_(530048, _a_(530047, _n_(530046, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Right 4.png')], [_c_(530053, _a_(530052, _a_(530051, _n_(530050, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Left 1.png'),
                                                                          _c_(530057, _a_(530056, _a_(530055, _n_(530054, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Left 2.png'),
                                                                          _c_(530061, _a_(530060, _a_(530059, _n_(530058, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Left 3.png'),
                                                                          _c_(530065, _a_(530064, _a_(530063, _n_(530062, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Left 4.png')], _c_(530069, _a_(530068, _a_(530067, _n_(530066, "pygame", lambda: pygame), "image"), "load"), 'Michael Scarn Sleeping.png')
        _l_(530070)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(635903)

except ImportError:
    pass
try:
    import car
    _l_(635905)

except ImportError:
    pass
try:
    import debris
    _l_(635907)

except ImportError:
    pass

_c_(635910, _a_(635909, _n_(635908, "pygame", lambda: pygame), "init"))
_l_(635911)

#screen settings
WIDTH = 1000
_l_(635912)
HEIGHT = 400
_l_(635913)

screen = _c_(635919, _a_(635916, _a_(635915, _n_(635914, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(635917, "WIDTH", lambda: WIDTH), _n_(635918, "HEIGHT", lambda: HEIGHT)))
_l_(635920)
_c_(635924, _a_(635923, _a_(635922, _n_(635921, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(635925)
_c_(635928, _a_(635927, _n_(635926, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(635929)

#fps
FPS = 120
_l_(635930)
clock = _c_(635934, _a_(635933, _a_(635932, _n_(635931, "pygame", lambda: pygame), "time"), "Clock"))
_l_(635935)

#load images
bg = _c_(635941, _a_(635940, _c_(635939, _a_(635938, _a_(635937, _n_(635936, "pygame", lambda: pygame), "image"), "load"), 'background/street.png'), "convert_alpha")) # background
_l_(635942) # background

#define game variables


######################CAR/DEBRIS##########################

player = _c_(635945, _a_(635944, _n_(635943, "car", lambda: car), "Player"), 1, 5)
_l_(635946)
debris = _c_(635949, _a_(635948, _n_(635947, "debris", lambda: debris), "Debris"), 1, 5)
_l_(635950)

##########################################################

#groups
bullet_group = _c_(635954, _a_(635953, _a_(635952, _n_(635951, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(635955)
debris_group = _c_(635959, _a_(635958, _a_(635957, _n_(635956, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(635960)

_c_(635964, _a_(635962, _n_(635961, "debris_group", lambda: debris_group), "add"), _n_(635963, "debris", lambda: debris))
_l_(635965)

#game runs here
run = True
_l_(635966)
while _n_(635967, "run", lambda: run):
    _l_(636073)


    #draw street
    _c_(635971, _a_(635969, _n_(635968, "screen", lambda: screen), "blit"), _n_(635970, "bg", lambda: bg), [0, 0])
    _l_(635972)

    #update groups
    _c_(635975, _a_(635974, _n_(635973, "bullet_group", lambda: bullet_group), "update"))
    _l_(635976)
    _c_(635980, _a_(635978, _n_(635977, "bullet_group", lambda: bullet_group), "draw"), _n_(635979, "screen", lambda: screen))
    _l_(635981)

    #draw debris
    _c_(635984, _a_(635983, _n_(635982, "debris", lambda: debris), "draw"))
    _l_(635985)

    #draw car
    _c_(635988, _a_(635987, _n_(635986, "player", lambda: player), "draw"))
    _l_(635989)
    _c_(635992, _a_(635991, _n_(635990, "player", lambda: player), "move"))
    _l_(635993)

    for event in _c_(635997, _a_(635996, _a_(635995, _n_(635994, "pygame", lambda: pygame), "event"), "get")):
        _l_(636057)

        if _a_(635999, _n_(635998, "event", lambda: event), "type") == _a_(636001, _n_(636000, "pygame", lambda: pygame), "QUIT"):
            _l_(636003)

            run = False
            _l_(636002)

        #check if key is down
        if _a_(636005, _n_(636004, "event", lambda: event), "type") == _a_(636007, _n_(636006, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(636037)

            if _a_(636009, _n_(636008, "event", lambda: event), "key") == _a_(636011, _n_(636010, "pygame", lambda: pygame), "K_ESCAPE"):
                _l_(636013)

                run = False
                _l_(636012)
            if _a_(636015, _n_(636014, "event", lambda: event), "key") == _a_(636017, _n_(636016, "pygame", lambda: pygame), "K_a"):
                _l_(636020)

                _n_(636018, "player", lambda: player).movingLeft = True
                _l_(636019)
            if _a_(636022, _n_(636021, "event", lambda: event), "key") == _a_(636024, _n_(636023, "pygame", lambda: pygame), "K_d"):
                _l_(636027)

                _n_(636025, "player", lambda: player).movingRight = True
                _l_(636026)
            if _a_(636029, _n_(636028, "event", lambda: event), "key") == _a_(636031, _n_(636030, "pygame", lambda: pygame), "K_SPACE"):
                _l_(636036)

                _c_(636034, _a_(636033, _n_(636032, "player", lambda: player), "shoot"))
                _l_(636035)

        #check if key is up
        if _a_(636039, _n_(636038, "event", lambda: event), "type") == _a_(636041, _n_(636040, "pygame", lambda: pygame), "KEYUP"):
            _l_(636056)

            if _a_(636043, _n_(636042, "event", lambda: event), "key") == _a_(636045, _n_(636044, "pygame", lambda: pygame), "K_a"):
                _l_(636048)

                _n_(636046, "player", lambda: player).movingLeft = False
                _l_(636047)
            if _a_(636050, _n_(636049, "event", lambda: event), "key") == _a_(636052, _n_(636051, "pygame", lambda: pygame), "K_d"):
                _l_(636055)

                _n_(636053, "player", lambda: player).movingRight = False
                _l_(636054)

    #update the display
    _c_(636061, _a_(636060, _a_(636059, _n_(636058, "pygame", lambda: pygame), "display"), "update"))
    _l_(636062)
    _c_(636066, _a_(636065, _a_(636064, _n_(636063, "pygame", lambda: pygame), "display"), "flip"))
    _l_(636067)
    _c_(636071, _a_(636069, _n_(636068, "clock", lambda: clock), "tick"), _n_(636070, "FPS", lambda: FPS))
    _l_(636072)

_c_(636076, _a_(636075, _n_(636074, "pygame", lambda: pygame), "quit"))
_l_(636077)
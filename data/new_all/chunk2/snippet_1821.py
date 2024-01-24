# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51813378/attributeerror-worker-object-has-no-attribute-idf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, random
    _l_(461938)

except ImportError:
    pass
try:
    import sys
    _l_(461940)

except ImportError:
    pass

WHITE = (255, 255, 255)
_l_(461941)
GREEN = (20, 255, 140)
_l_(461942)
GREY = (210, 210 ,210)
_l_(461943)
RED = (255, 0, 0)
_l_(461944)
PURPLE = (255, 0, 255)
_l_(461945)

SCREENWIDTH=1000
_l_(461946)
SCREENHEIGHT=578
_l_(461947)

IMG_BACKGROUND = "background.jpg"
_l_(461948)
IMG_WORKER_RUNNING = "images/workers/worker_1.png"
_l_(461949)
IMG_WORKER_IDLE = "images/workers/worker_2.png"
_l_(461950)
IMG_WORKER_ACCIDENT = "images/workers/accident.png"
_l_(461951)


class Background(_a_(461954, _a_(461953, _n_(461952, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(461988)

    def __init__(self, image_file, location, *groups):
        _l_(461987)

        # we set a _layer attribute before adding this sprite to the sprite groups
        # we want the background to be actually in the back
        _n_(461955, "self", lambda: self)._layer = -1
        _l_(461956)
        _c_(461963, _a_(461960, _a_(461959, _a_(461958, _n_(461957, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(461961, "self", lambda: self), _n_(461962, "groups", lambda: groups))
        _l_(461964)
        # let's resize the background image now and only once
        _n_(461965, "self", lambda: self).image = _c_(461978, _a_(461968, _a_(461967, _n_(461966, "pygame", lambda: pygame), "transform"), "scale"), _c_(461975, _a_(461974, _c_(461973, _a_(461971, _a_(461970, _n_(461969, "pygame", lambda: pygame), "image"), "load"), _n_(461972, "image_file", lambda: image_file)), "convert")), (_n_(461976, "SCREENWIDTH", lambda: SCREENWIDTH), _n_(461977, "SCREENHEIGHT", lambda: SCREENHEIGHT)))
        _l_(461979)
        _n_(461980, "self", lambda: self).rect = _c_(461985, _a_(461983, _a_(461982, _n_(461981, "self", lambda: self), "image"), "get_rect"), topleft=_n_(461984, "location", lambda: location))
        _l_(461986)


class GeoFence(_a_(461991, _a_(461990, _n_(461989, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(462056)

    def __init__(self, idf, rect, risk_level, *groups):
        _l_(462055)

        # we set a _layer attribute before adding this sprite to the sprite groups
        _n_(461992, "self", lambda: self)._layer = 1
        _l_(461993)
        _c_(462000, _a_(461997, _a_(461996, _a_(461995, _n_(461994, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(461998, "self", lambda: self), _n_(461999, "groups", lambda: groups))
        _l_(462001)
        _n_(462002, "self", lambda: self).image = _c_(462010, _a_(462005, _a_(462004, _n_(462003, "pygame", lambda: pygame), "surface"), "Surface"), (_a_(462007, _n_(462006, "rect", lambda: rect), "width"), _a_(462009, _n_(462008, "rect", lambda: rect), "height")))
        _l_(462011)
        _c_(462016, _a_(462014, _a_(462013, _n_(462012, "self", lambda: self), "image"), "fill"), _n_(462015, "GREEN", lambda: GREEN))
        _l_(462017)
        _n_(462018, "self", lambda: self).rect = _n_(462019, "rect", lambda: rect)
        _l_(462020)
        _n_(462021, "self", lambda: self).idf = _n_(462022, "idf", lambda: idf)
        _l_(462023)
        _n_(462024, "self", lambda: self).risk_level = _n_(462025, "risk_level", lambda: risk_level)
        _l_(462026)
        _n_(462027, "self", lambda: self).font = _c_(462031, _a_(462030, _a_(462029, _n_(462028, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 20)
        _l_(462032)
        text = _c_(462038, _a_(462035, _a_(462034, _n_(462033, "self", lambda: self), "font"), "render"), _n_(462036, "risk_level", lambda: risk_level), 1, (255,0,0), _n_(462037, "GREEN", lambda: GREEN))
        _l_(462039)
        text_rect = _c_(462046, _a_(462041, _n_(462040, "text", lambda: text), "get_rect"), center=(_a_(462043, _n_(462042, "rect", lambda: rect), "width")/2, _a_(462045, _n_(462044, "rect", lambda: rect), "height")/2))
        _l_(462047)
        _c_(462053, _a_(462050, _a_(462049, _n_(462048, "self", lambda: self), "image"), "blit"), _n_(462051, "text", lambda: text), _n_(462052, "text_rect", lambda: text_rect))
        _l_(462054)



class Worker(_a_(462059, _a_(462058, _n_(462057, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(462444)


    # we introduce to possible states: RUNNING and IDLE
    RUNNING = 0
    _l_(462060)
    IDLE = 1
    _l_(462061)
    ACCIDENT = 2
    _l_(462062)
    NUMBER_OF_ACCIDENTS = 0
    _l_(462063)
    image_cache = {}
    _l_(462064)

    def __init__(self, image_running, image_idle, image_accident, location, *groups):
        _l_(462147)


        _n_(462065, "self", lambda: self).font = _c_(462069, _a_(462068, _a_(462067, _n_(462066, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 10)
        _l_(462070)

        # each state has it's own image
        _n_(462071, "self", lambda: self).images = {
            _a_(462073, _n_(462072, "Worker", lambda: Worker), "RUNNING"): _c_(462081, _a_(462076, _a_(462075, _n_(462074, "pygame", lambda: pygame), "transform"), "scale"), _c_(462080, _a_(462078, _n_(462077, "self", lambda: self), "get_image"), _n_(462079, "image_running", lambda: image_running)), (45, 45)),
            _a_(462083, _n_(462082, "Worker", lambda: Worker), "IDLE"): _c_(462091, _a_(462086, _a_(462085, _n_(462084, "pygame", lambda: pygame), "transform"), "scale"), _c_(462090, _a_(462088, _n_(462087, "self", lambda: self), "get_image"), _n_(462089, "image_idle", lambda: image_idle)), (20, 45)),
            _a_(462093, _n_(462092, "Worker", lambda: Worker), "ACCIDENT"): _c_(462101, _a_(462096, _a_(462095, _n_(462094, "pygame", lambda: pygame), "transform"), "scale"), _c_(462100, _a_(462098, _n_(462097, "self", lambda: self), "get_image"), _n_(462099, "image_accident", lambda: image_accident)), (40, 40))
        }
        _l_(462102)

        # we set a _layer attribute before adding this sprite to the sprite groups
        # we want the workers on top
        _n_(462103, "self", lambda: self)._layer = 2
        _l_(462104)
        _c_(462111, _a_(462108, _a_(462107, _a_(462106, _n_(462105, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(462109, "self", lambda: self), _n_(462110, "groups", lambda: groups))
        _l_(462112)

        # let's keep track of the state and how long we are in this state already            
        _n_(462113, "self", lambda: self).state = _a_(462115, _n_(462114, "Worker", lambda: Worker), "IDLE")
        _l_(462116)
        _n_(462117, "self", lambda: self).ticks_in_state = 0
        _l_(462118)

        _n_(462119, "self", lambda: self).image = _a_(462121, _n_(462120, "self", lambda: self), "images")[_a_(462123, _n_(462122, "self", lambda: self), "state")]
        _l_(462124)
        _n_(462125, "self", lambda: self).rect = _c_(462130, _a_(462128, _a_(462127, _n_(462126, "self", lambda: self), "image"), "get_rect"), topleft=_n_(462129, "location", lambda: location))
        _l_(462131)

        _n_(462132, "self", lambda: self).direction = _c_(462136, _a_(462135, _a_(462134, _n_(462133, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
        _l_(462137)
        _n_(462138, "self", lambda: self).speed = _c_(462141, _a_(462140, _n_(462139, "random", lambda: random), "randint"), 1, 3)
        _l_(462142)
        _c_(462145, _a_(462144, _n_(462143, "self", lambda: self), "set_random_direction"))
        _l_(462146)


    def set_random_direction(self):
        _l_(462227)

        # random new direction or standing still
        vec = _c_(462157, _a_(462150, _a_(462149, _n_(462148, "pygame", lambda: pygame), "math"), "Vector2"), _c_(462153, _a_(462152, _n_(462151, "random", lambda: random), "randint"), -100,100), _c_(462156, _a_(462155, _n_(462154, "random", lambda: random), "randint"), -100,100)) if _c_(462160, _a_(462159, _n_(462158, "random", lambda: random), "randint"), 0, 5) > 1 else _c_(462164, _a_(462163, _a_(462162, _n_(462161, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
        _l_(462165)

        # check the new vector and decide if we are running or fooling around
        length = _c_(462168, _a_(462167, _n_(462166, "vec", lambda: vec), "length"))
        _l_(462169)
        speed = _c_(462181, _n_(462170, "sum", lambda: sum), (_c_(462175, _n_(462171, "abs", lambda: abs), _c_(462174, _n_(462172, "int", lambda: int), _n_(462173, "v", lambda: v))) for v in _c_(462178, _a_(462177, _n_(462176, "vec", lambda: vec), "normalize")) * _a_(462180, _n_(462179, "self", lambda: self), "speed"))) if _n_(462182, "length", lambda: length) > 0 else 0
        _l_(462183)

        if (_n_(462184, "length", lambda: length) == 0 or _n_(462185, "speed", lambda: speed) == 0) and (_a_(462187, _n_(462186, "self", lambda: self), "state") != _a_(462189, _n_(462188, "Worker", lambda: Worker), "ACCIDENT")):
            _l_(462215)

            new_state = _a_(462191, _n_(462190, "Worker", lambda: Worker), "IDLE")
            _l_(462192)
            _n_(462193, "self", lambda: self).direction = _c_(462197, _a_(462196, _a_(462195, _n_(462194, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
            _l_(462198)
        elif _a_(462200, _n_(462199, "self", lambda: self), "state") != _a_(462202, _n_(462201, "Worker", lambda: Worker), "ACCIDENT"):
            _l_(462214)

            new_state = _a_(462204, _n_(462203, "Worker", lambda: Worker), "RUNNING")
            _l_(462205)
            _n_(462206, "self", lambda: self).direction = _c_(462209, _a_(462208, _n_(462207, "vec", lambda: vec), "normalize"))
            _l_(462210)
        else:
            new_state = _a_(462212, _n_(462211, "Worker", lambda: Worker), "ACCIDENT")
            _l_(462213)

        _n_(462216, "self", lambda: self).ticks_in_state = 0
        _l_(462217)
        _n_(462218, "self", lambda: self).state = _n_(462219, "new_state", lambda: new_state)
        _l_(462220)

        # use the right image for the current state
        _n_(462221, "self", lambda: self).image = _a_(462223, _n_(462222, "self", lambda: self), "images")[_a_(462225, _n_(462224, "self", lambda: self), "state")]
        _l_(462226)


    def update(self, screen):
        _l_(462313)

        _n_(462228, "self", lambda: self).ticks_in_state += 1
        _l_(462229)
        # the longer we are in a certain state, the more likely is we change direction
        if _c_(462234, _a_(462231, _n_(462230, "random", lambda: random), "randint"), 0, _a_(462233, _n_(462232, "self", lambda: self), "ticks_in_state")) > 70:
            _l_(462239)

            _c_(462237, _a_(462236, _n_(462235, "self", lambda: self), "set_random_direction"))
            _l_(462238)

        # now let's multiply our direction with our speed and move the rect
        vec = [_c_(462242, _n_(462240, "int", lambda: int), _n_(462241, "v", lambda: v)) for v in _a_(462244, _n_(462243, "self", lambda: self), "direction") * _a_(462246, _n_(462245, "self", lambda: self), "speed")]
        _l_(462247)
        _c_(462252, _a_(462250, _a_(462249, _n_(462248, "self", lambda: self), "rect"), "move_ip"), *_n_(462251, "vec", lambda: vec))
        _l_(462253)

        # if we're going outside the screen, change direction
        if not _c_(462260, _a_(462257, _c_(462256, _a_(462255, _n_(462254, "screen", lambda: screen), "get_rect")), "contains"), _a_(462259, _n_(462258, "self", lambda: self), "rect")):
            _l_(462265)

            _n_(462261, "self", lambda: self).direction = _a_(462263, _n_(462262, "self", lambda: self), "direction") * -1
            _l_(462264)

        # Check distances between workers and fences
        w_dist = {}
        _l_(462266)
        for w in _n_(462267, "workers", lambda: workers):
            _l_(462292)

            f_dist = {}
            _l_(462268)
            for f in _n_(462269, "fences", lambda: fences):
                _l_(462286)

                if _n_(462270, "f", lambda: f) != _n_(462271, "self", lambda: self):
                    _l_(462285)

                    distance_meters = _c_(462278, _a_(462273, _n_(462272, "self", lambda: self), "rect_distance"), _a_(462275, _n_(462274, "w", lambda: w), "rect"), _a_(462277, _n_(462276, "f", lambda: f), "rect"))
                    _l_(462279)
                    _n_(462280, "f_dist_meters", lambda: f_dist_meters)[_a_(462282, _n_(462281, "f", lambda: f), "idf")] = _n_(462283, "distance", lambda: distance)
                    _l_(462284)
            _n_(462287, "w_dist", lambda: w_dist)[_a_(462289, _n_(462288, "w", lambda: w), "idw")] = _n_(462290, "f_dist", lambda: f_dist)
            _l_(462291)
        _c_(462299, _a_(462295, _a_(462294, _n_(462293, "pygame", lambda: pygame), "display"), "set_caption"), _c_(462298, _n_(462296, "str", lambda: str), _n_(462297, "w_dist", lambda: w_dist)[1][1]))
        _l_(462300)

        # Risk handling
        _c_(462303, _a_(462302, _n_(462301, "self", lambda: self), "handle_risks"))
        _l_(462304)

        _c_(462311, _a_(462307, _a_(462306, _n_(462305, "self", lambda: self), "rect"), "clamp_ip"), _c_(462310, _a_(462309, _n_(462308, "screen", lambda: screen), "get_rect")))
        _l_(462312)


    def handle_risks(self):
        _l_(462338)

        for s in _c_(462319, _a_(462316, _a_(462315, _n_(462314, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(462317, "self", lambda: self), _n_(462318, "fences", lambda: fences), False):
            _l_(462337)

            if _n_(462320, "s", lambda: s) != _n_(462321, "self", lambda: self):
                _l_(462336)

                _n_(462322, "self", lambda: self).speed = 0
                _l_(462323)
                _n_(462324, "self", lambda: self).state = _a_(462326, _n_(462325, "Worker", lambda: Worker), "ACCIDENT")
                _l_(462327)
                _n_(462328, "self", lambda: self).image = _a_(462330, _n_(462329, "self", lambda: self), "images")[_a_(462332, _n_(462331, "self", lambda: self), "state")]
                _l_(462333)
                _n_(462334, "Worker", lambda: Worker).NUMBER_OF_ACCIDENTS += 1
                _l_(462335)


    # Distance between workers and geo-fences
    def rect_distance(self, rect1, rect2):
        _l_(462428)

        x1, y1 = _a_(462340, _n_(462339, "rect1", lambda: rect1), "topleft")
        _l_(462341)
        x1b, y1b = _a_(462343, _n_(462342, "rect1", lambda: rect1), "bottomright")
        _l_(462344)
        x2, y2 = _a_(462346, _n_(462345, "rect2", lambda: rect2), "topleft")
        _l_(462347)
        x2b, y2b = _a_(462349, _n_(462348, "rect2", lambda: rect2), "bottomright")
        _l_(462350)
        left = _n_(462351, "x2b", lambda: x2b) < _n_(462352, "x1", lambda: x1)
        _l_(462353)
        right = _n_(462354, "x1b", lambda: x1b) < _n_(462355, "x2", lambda: x2)
        _l_(462356)
        top = _n_(462357, "y2b", lambda: y2b) < _n_(462358, "y1", lambda: y1)
        _l_(462359)
        bottom = _n_(462360, "y1b", lambda: y1b) < _n_(462361, "y2", lambda: y2)
        _l_(462362)
        if _n_(462363, "bottom", lambda: bottom) and _n_(462364, "left", lambda: left):
            _l_(462427)

            aux = _c_(462371, _a_(462366, _n_(462365, "math", lambda: math), "hypot"), _n_(462367, "x2b", lambda: x2b)-_n_(462368, "x1", lambda: x1), _n_(462369, "y2", lambda: y2)-_n_(462370, "y1b", lambda: y1b))
            _l_(462372)
            return aux
        elif _n_(462373, "left", lambda: left) and _n_(462374, "top", lambda: top):
            _l_(462426)

            aux = _c_(462381, _a_(462376, _n_(462375, "math", lambda: math), "hypot"), _n_(462377, "x2b", lambda: x2b)-_n_(462378, "x1", lambda: x1), _n_(462379, "y2b", lambda: y2b)-_n_(462380, "y1", lambda: y1))
            _l_(462382)
            return aux
        elif _n_(462383, "top", lambda: top) and _n_(462384, "right", lambda: right):
            _l_(462425)

            aux = _c_(462391, _a_(462386, _n_(462385, "math", lambda: math), "hypot"), _n_(462387, "x2", lambda: x2)-_n_(462388, "x1b", lambda: x1b), _n_(462389, "y2b", lambda: y2b)-_n_(462390, "y1", lambda: y1))
            _l_(462392)
            return aux
        elif _n_(462393, "right", lambda: right) and _n_(462394, "bottom", lambda: bottom):
            _l_(462424)

            aux = _c_(462401, _a_(462396, _n_(462395, "math", lambda: math), "hypot"), _n_(462397, "x2", lambda: x2)-_n_(462398, "x1b", lambda: x1b), _n_(462399, "y2", lambda: y2)-_n_(462400, "y1b", lambda: y1b))
            _l_(462402)
            return aux
        elif _n_(462403, "left", lambda: left):
            _l_(462423)

            aux = _n_(462404, "x1", lambda: x1) - _n_(462405, "x2b", lambda: x2b)
            _l_(462406)
            return aux
        elif _n_(462407, "right", lambda: right):
            _l_(462422)

            aux = _n_(462408, "x2", lambda: x2) - _n_(462409, "x1b", lambda: x1b)
            _l_(462410)
            return aux
        elif _n_(462411, "top", lambda: top):
            _l_(462421)

            aux = _n_(462412, "y1", lambda: y1) - _n_(462413, "y2b", lambda: y2b)
            _l_(462414)
            return aux
        elif _n_(462415, "bottom", lambda: bottom):
            _l_(462420)

            aux = _n_(462416, "y2", lambda: y2) - _n_(462417, "y1b", lambda: y1b)
            _l_(462418)
            return aux
        else:
            aux = 0
            _l_(462419)
            return aux


    def get_image(self,key):
        _l_(462443)

        if not _n_(462429, "key", lambda: key) in _n_(462430, "image_cache", lambda: image_cache):
            _l_(462439)

            _n_(462431, "image_cache", lambda: image_cache)[_n_(462432, "key", lambda: key)] = _c_(462437, _a_(462435, _a_(462434, _n_(462433, "pygame", lambda: pygame), "image"), "load"), _n_(462436, "key", lambda: key))
            _l_(462438)
        aux = _n_(462440, "image_cache", lambda: image_cache)[_n_(462441, "key", lambda: key)]
        _l_(462442)
        return aux


_c_(462447, _a_(462446, _n_(462445, "pygame", lambda: pygame), "init"))
_l_(462448)

all_sprites = _c_(462452, _a_(462451, _a_(462450, _n_(462449, "pygame", lambda: pygame), "sprite"), "LayeredUpdates"))
_l_(462453)
workers = _c_(462457, _a_(462456, _a_(462455, _n_(462454, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(462458)
fences = _c_(462462, _a_(462461, _a_(462460, _n_(462459, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(462463)

screen = _c_(462469, _a_(462466, _a_(462465, _n_(462464, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(462467, "SCREENWIDTH", lambda: SCREENWIDTH), _n_(462468, "SCREENHEIGHT", lambda: SCREENHEIGHT)))
_l_(462470)
_c_(462474, _a_(462473, _a_(462472, _n_(462471, "pygame", lambda: pygame), "display"), "set_caption"), "TEST")
_l_(462475)

# create multiple workers
for pos in ((30,30), (50, 400), (200, 100), (700, 200)):
    _l_(462486)

    _c_(462484, _n_(462476, "Worker", lambda: Worker), _n_(462477, "IMG_WORKER_RUNNING", lambda: IMG_WORKER_RUNNING), _n_(462478, "IMG_WORKER_IDLE", lambda: IMG_WORKER_IDLE), _n_(462479, "IMG_WORKER_ACCIDENT", lambda: IMG_WORKER_ACCIDENT), _n_(462480, "pos", lambda: pos), _n_(462481, "all_sprites", lambda: all_sprites), _n_(462482, "workers", lambda: workers), _n_(462483, "fences", lambda: fences))
    _l_(462485)

# create multiple geo-fences
idf = 1
_l_(462487)
risks = ["H","M","L"]
_l_(462488)
for rect in (_c_(462491, _a_(462490, _n_(462489, "pygame", lambda: pygame), "Rect"), 510,150,75,52), _c_(462494, _a_(462493, _n_(462492, "pygame", lambda: pygame), "Rect"), 450,250,68,40), _c_(462497, _a_(462496, _n_(462495, "pygame", lambda: pygame), "Rect"), 450,370,68,48),
             _c_(462501, _a_(462499, _n_(462498, "pygame", lambda: pygame), "Rect"), 0,0,20,_n_(462500, "SCREENHEIGHT", lambda: SCREENHEIGHT)),_c_(462505, _a_(462503, _n_(462502, "pygame", lambda: pygame), "Rect"), 0,0,_n_(462504, "SCREENWIDTH", lambda: SCREENWIDTH),20),
             _c_(462510, _a_(462507, _n_(462506, "pygame", lambda: pygame), "Rect"), _n_(462508, "SCREENWIDTH", lambda: SCREENWIDTH)-20,0,20,_n_(462509, "SCREENHEIGHT", lambda: SCREENHEIGHT)),_c_(462515, _a_(462512, _n_(462511, "pygame", lambda: pygame), "Rect"), 0,_n_(462513, "SCREENHEIGHT", lambda: SCREENHEIGHT)-20,_n_(462514, "SCREENWIDTH", lambda: SCREENWIDTH),20)):
    _l_(462530)

    risk = _n_(462516, "risks", lambda: risks)[_c_(462519, _a_(462518, _n_(462517, "random", lambda: random), "randint"), 0,2)]
    _l_(462520)
    _c_(462527, _n_(462521, "GeoFence", lambda: GeoFence), _n_(462522, "idf", lambda: idf), _n_(462523, "rect", lambda: rect), _n_(462524, "risk", lambda: risk), _n_(462525, "all_sprites", lambda: all_sprites), _n_(462526, "fences", lambda: fences))
    _l_(462528)
    idf += 1
    _l_(462529)

# and the background
_c_(462534, _n_(462531, "Background", lambda: Background), _n_(462532, "IMG_BACKGROUND", lambda: IMG_BACKGROUND), [0,0], _n_(462533, "all_sprites", lambda: all_sprites))
_l_(462535)

carryOn = True
_l_(462536)
clock = _c_(462540, _a_(462539, _a_(462538, _n_(462537, "pygame", lambda: pygame), "time"), "Clock"))
_l_(462541)
while _n_(462542, "carryOn", lambda: carryOn):
    _l_(462585)

    for event in _c_(462546, _a_(462545, _a_(462544, _n_(462543, "pygame", lambda: pygame), "event"), "get")):
        _l_(462565)

        if _a_(462548, _n_(462547, "event", lambda: event), "type")==_a_(462550, _n_(462549, "pygame", lambda: pygame), "QUIT"):
            _l_(462564)

            carryOn = False
            _l_(462551)
            _c_(462555, _a_(462554, _a_(462553, _n_(462552, "pygame", lambda: pygame), "display"), "quit"))
            _l_(462556)
            _c_(462559, _a_(462558, _n_(462557, "pygame", lambda: pygame), "quit"))
            _l_(462560)
            _c_(462562, _n_(462561, "quit", lambda: quit))
            _l_(462563)

    _c_(462569, _a_(462567, _n_(462566, "all_sprites", lambda: all_sprites), "update"), _n_(462568, "screen", lambda: screen))
    _l_(462570)
    _c_(462574, _a_(462572, _n_(462571, "all_sprites", lambda: all_sprites), "draw"), _n_(462573, "screen", lambda: screen))
    _l_(462575)

    _c_(462579, _a_(462578, _a_(462577, _n_(462576, "pygame", lambda: pygame), "display"), "flip"))
    _l_(462580)

    _c_(462583, _a_(462582, _n_(462581, "clock", lambda: clock), "tick"), 20)
    _l_(462584)
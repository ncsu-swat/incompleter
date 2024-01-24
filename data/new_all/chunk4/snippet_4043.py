# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63819205/self-rect-pygame-rectx-y-width-height-typeerror-argument-must-be-rect-style
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(636611)

except ImportError:
    pass
_c_(636614, _a_(636613, _n_(636612, "pygame", lambda: pygame), "init"))
_l_(636615)

# Build The Screen
window = _c_(636619, _a_(636618, _a_(636617, _n_(636616, "pygame", lambda: pygame), "display"), "set_mode"), (700,500))
_l_(636620)

# Name Screen
_c_(636624, _a_(636623, _a_(636622, _n_(636621, "pygame", lambda: pygame), "display"), "set_caption"), "Noobs first Game")
_l_(636625)

bg = _c_(636629, _a_(636628, _a_(636627, _n_(636626, "pygame", lambda: pygame), "image"), "load"), "skybg1.png")
_l_(636630)
bg_shift = 0
_l_(636631)


# Class Player
class player:
    _l_(636718)

    def __init__(self,x,y,width,height,color):
        _l_(636680)

        _n_(636632, "self", lambda: self).x = _n_(636633, "x", lambda: x)
        _l_(636634)
        _n_(636635, "self", lambda: self).y = _n_(636636, "y", lambda: y)
        _l_(636637)
        _n_(636638, "self", lambda: self).width = _n_(636639, "width", lambda: width)
        _l_(636640)
        _n_(636641, "self", lambda: self).height = _n_(636642, "height", lambda: height)
        _l_(636643)
        _n_(636644, "self", lambda: self).speed = 4
        _l_(636645)
        _n_(636646, "self", lambda: self).color = _n_(636647, "color", lambda: color)
        _l_(636648)
        _n_(636649, "self", lambda: self).rect = _c_(636656, _a_(636651, _n_(636650, "pygame", lambda: pygame), "Rect"), _n_(636652, "x", lambda: x),_n_(636653, "y", lambda: y),_n_(636654, "width", lambda: width),_n_(636655, "height", lambda: height))
        _l_(636657)
        _n_(636658, "self", lambda: self).ss1 = _c_(636662, _a_(636661, _a_(636660, _n_(636659, "pygame", lambda: pygame), "image"), "load"), "heroplane1.png")
        _l_(636663)
        _n_(636664, "self", lambda: self).ss1 = _c_(636678, _a_(636667, _a_(636666, _n_(636665, "pygame", lambda: pygame), "transform"), "scale"), _a_(636669, _n_(636668, "self", lambda: self), "ss1"),(_c_(636673, _a_(636672, _a_(636671, _n_(636670, "self", lambda: self), "ss1"), "get_width"))//9,_c_(636677, _a_(636676, _a_(636675, _n_(636674, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(636679)
    def draw(self):
        _l_(636717)

        _a_(636682, _n_(636681, "self", lambda: self), "rect").topleft=(_a_(636684, _n_(636683, "self", lambda: self), "x"),_a_(636686, _n_(636685, "self", lambda: self), "y"))
        _l_(636687)
        _c_(636696, _a_(636690, _a_(636689, _n_(636688, "pygame", lambda: pygame), "draw"), "rect"), _n_(636691, "window", lambda: window),_a_(636693, _n_(636692, "self", lambda: self), "color"),_a_(636695, _n_(636694, "self", lambda: self), "rect"))
        _l_(636697)

        player_rect = _c_(636704, _a_(636700, _a_(636699, _n_(636698, "self", lambda: self), "ss1"), "get_rect"), center = _a_(636703, _a_(636702, _n_(636701, "self", lambda: self), "rect"), "center"))
        _l_(636705)
        _n_(636706, "player_rect", lambda: player_rect).centerx += -7
        _l_(636707)
        _n_(636708, "player_rect", lambda: player_rect).centery += -6
        _l_(636709)
        _c_(636715, _a_(636711, _n_(636710, "window", lambda: window), "blit"), _a_(636713, _n_(636712, "self", lambda: self), "ss1"),_n_(636714, "player_rect", lambda: player_rect))
        _l_(636716)

# Class Enemy
class enemy:
    _l_(636805)

    def __init__(self,x,y,width,height,color):
        _l_(636767)

        _n_(636719, "self", lambda: self).x = _n_(636720, "x", lambda: x)
        _l_(636721)
        _n_(636722, "self", lambda: self).y = _n_(636723, "y", lambda: y)
        _l_(636724)
        _n_(636725, "self", lambda: self).width = _n_(636726, "width", lambda: width)
        _l_(636727)
        _n_(636728, "self", lambda: self).height = _n_(636729, "height", lambda: height)
        _l_(636730)
        _n_(636731, "self", lambda: self).speed = 4
        _l_(636732)
        _n_(636733, "self", lambda: self).color = _n_(636734, "color", lambda: color)
        _l_(636735)
        _n_(636736, "self", lambda: self).rect = _c_(636743, _a_(636738, _n_(636737, "pygame", lambda: pygame), "Rect"), _n_(636739, "x", lambda: x),_n_(636740, "y", lambda: y),_n_(636741, "width", lambda: width),_n_(636742, "height", lambda: height))
        _l_(636744)
        _n_(636745, "self", lambda: self).ss1 = _c_(636749, _a_(636748, _a_(636747, _n_(636746, "pygame", lambda: pygame), "image"), "load"), "enemyplane1.png")
        _l_(636750)
        _n_(636751, "self", lambda: self).ss1 = _c_(636765, _a_(636754, _a_(636753, _n_(636752, "pygame", lambda: pygame), "transform"), "scale"), _a_(636756, _n_(636755, "self", lambda: self), "ss1"),(_c_(636760, _a_(636759, _a_(636758, _n_(636757, "self", lambda: self), "ss1"), "get_width"))//9,_c_(636764, _a_(636763, _a_(636762, _n_(636761, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(636766)
    def draw(self):
        _l_(636804)

        _a_(636769, _n_(636768, "self", lambda: self), "rect").topleft = (_a_(636771, _n_(636770, "self", lambda: self), "x"),_a_(636773, _n_(636772, "self", lambda: self), "y"))
        _l_(636774)
        _c_(636783, _a_(636777, _a_(636776, _n_(636775, "pygame", lambda: pygame), "draw"), "rect"), _n_(636778, "window", lambda: window),_a_(636780, _n_(636779, "self", lambda: self), "color"),_a_(636782, _n_(636781, "self", lambda: self), "rect"))
        _l_(636784)

        enemy_rect = _c_(636791, _a_(636787, _a_(636786, _n_(636785, "self", lambda: self), "ss1"), "get_rect"), center = _a_(636790, _a_(636789, _n_(636788, "self", lambda: self), "rect"), "center"))
        _l_(636792)
        _n_(636793, "enemy_rect", lambda: enemy_rect).centerx += -2
        _l_(636794)
        _n_(636795, "enemy_rect", lambda: enemy_rect).centery += -6
        _l_(636796)
        _c_(636802, _a_(636798, _n_(636797, "window", lambda: window), "blit"), _a_(636800, _n_(636799, "self", lambda: self), "ss1"),_n_(636801, "enemy_rect", lambda: enemy_rect))
        _l_(636803)


# Class Enemy2
class enemy2:
    _l_(636890)

    def __init__(self,x,y,width,height,color):
        _l_(636852)

        _n_(636806, "self", lambda: self).x = _n_(636807, "x", lambda: x)
        _l_(636808)
        _n_(636809, "self", lambda: self).y = _n_(636810, "y", lambda: y)
        _l_(636811)
        _n_(636812, "self", lambda: self).width = _n_(636813, "width", lambda: width)
        _l_(636814)
        _n_(636815, "self", lambda: self).height = _n_(636816, "height", lambda: height)
        _l_(636817)
        _n_(636818, "self", lambda: self).color = _n_(636819, "color", lambda: color)
        _l_(636820)
        _n_(636821, "self", lambda: self).rect = _c_(636828, _a_(636823, _n_(636822, "pygame", lambda: pygame), "Rect"), _n_(636824, "x", lambda: x),_n_(636825, "y", lambda: y),_n_(636826, "width", lambda: width),_n_(636827, "height", lambda: height))
        _l_(636829)
        _n_(636830, "self", lambda: self).ss1 = _c_(636834, _a_(636833, _a_(636832, _n_(636831, "pygame", lambda: pygame), "image"), "load"), "enemyplane2.png")
        _l_(636835)
        _n_(636836, "self", lambda: self).ss1 = _c_(636850, _a_(636839, _a_(636838, _n_(636837, "pygame", lambda: pygame), "transform"), "scale"), _a_(636841, _n_(636840, "self", lambda: self), "ss1"),(_c_(636845, _a_(636844, _a_(636843, _n_(636842, "self", lambda: self), "ss1"), "get_width"))//9,_c_(636849, _a_(636848, _a_(636847, _n_(636846, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(636851)
    def draw(self):
        _l_(636889)

        _a_(636854, _n_(636853, "self", lambda: self), "rect").topleft = (_a_(636856, _n_(636855, "self", lambda: self), "x"),_a_(636858, _n_(636857, "self", lambda: self), "y"))
        _l_(636859)
        _c_(636868, _a_(636862, _a_(636861, _n_(636860, "pygame", lambda: pygame), "draw"), "rect"), _n_(636863, "window", lambda: window),_a_(636865, _n_(636864, "self", lambda: self), "color"),_a_(636867, _n_(636866, "self", lambda: self), "rect"))
        _l_(636869)

        enemy2_rect = _c_(636876, _a_(636872, _a_(636871, _n_(636870, "self", lambda: self), "ss1"), "get_rect"), center = _a_(636875, _a_(636874, _n_(636873, "self", lambda: self), "rect"), "center"))
        _l_(636877)
        _n_(636878, "enemy2_rect", lambda: enemy2_rect).centerx += -4
        _l_(636879)
        _n_(636880, "enemy2_rect", lambda: enemy2_rect).centery += -6
        _l_(636881)
        _c_(636887, _a_(636883, _n_(636882, "window", lambda: window), "blit"), _a_(636885, _n_(636884, "self", lambda: self), "ss1"),_n_(636886, "enemy2_rect", lambda: enemy2_rect))
        _l_(636888)


# Class Enemy3
class enemy3:
    _l_(636975)

    def __init__(self,x,y,width,height,color):
        _l_(636937)

        _n_(636891, "self", lambda: self).x = _n_(636892, "x", lambda: x)
        _l_(636893)
        _n_(636894, "self", lambda: self).y = _n_(636895, "y", lambda: y)
        _l_(636896)
        _n_(636897, "self", lambda: self).width = _n_(636898, "width", lambda: width)
        _l_(636899)
        _n_(636900, "self", lambda: self).height = _n_(636901, "height", lambda: height)
        _l_(636902)
        _n_(636903, "self", lambda: self).color = _n_(636904, "color", lambda: color)
        _l_(636905)
        _n_(636906, "self", lambda: self).rect = _c_(636913, _a_(636908, _n_(636907, "pygame", lambda: pygame), "Rect"), _n_(636909, "x", lambda: x),_n_(636910, "y", lambda: y),_n_(636911, "width", lambda: width),_n_(636912, "height", lambda: height))
        _l_(636914)
        _n_(636915, "self", lambda: self).ss1 = _c_(636919, _a_(636918, _a_(636917, _n_(636916, "pygame", lambda: pygame), "image"), "load"), "enemyplane3.png")
        _l_(636920)
        _n_(636921, "self", lambda: self).ss1 = _c_(636935, _a_(636924, _a_(636923, _n_(636922, "pygame", lambda: pygame), "transform"), "scale"), _a_(636926, _n_(636925, "self", lambda: self), "ss1"),(_c_(636930, _a_(636929, _a_(636928, _n_(636927, "self", lambda: self), "ss1"), "get_width"))//9,_c_(636934, _a_(636933, _a_(636932, _n_(636931, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(636936)
    def draw(self):
        _l_(636974)

        _a_(636939, _n_(636938, "self", lambda: self), "rect").topleft = (_a_(636941, _n_(636940, "self", lambda: self), "x"),_a_(636943, _n_(636942, "self", lambda: self), "y"))
        _l_(636944)
        _c_(636953, _a_(636947, _a_(636946, _n_(636945, "pygame", lambda: pygame), "draw"), "rect"), _n_(636948, "window", lambda: window),_a_(636950, _n_(636949, "self", lambda: self), "color"),_a_(636952, _n_(636951, "self", lambda: self), "rect"))
        _l_(636954)

        enemy3_rect = _c_(636961, _a_(636957, _a_(636956, _n_(636955, "self", lambda: self), "ss1"), "get_rect"), center = _a_(636960, _a_(636959, _n_(636958, "self", lambda: self), "rect"), "center"))
        _l_(636962)
        _n_(636963, "enemy3_rect", lambda: enemy3_rect).centerx += -4
        _l_(636964)
        _n_(636965, "enemy3_rect", lambda: enemy3_rect).centery += -6
        _l_(636966)
        _c_(636972, _a_(636968, _n_(636967, "window", lambda: window), "blit"), _a_(636970, _n_(636969, "self", lambda: self), "ss1"),_n_(636971, "enemy3_rect", lambda: enemy3_rect))
        _l_(636973)



class projectile(_n_(636976, "object", lambda: object)):
    _l_(637023)

    def __init__(self, x, y,color):
        _l_(637007)

        _n_(636977, "self", lambda: self).x = _n_(636978, "x", lambda: x)
        _l_(636979)
        _n_(636980, "self", lambda: self).y = _n_(636981, "y", lambda: y)
        _l_(636982)
        _n_(636983, "self", lambda: self).slash = _c_(636987, _a_(636986, _a_(636985, _n_(636984, "pygame", lambda: pygame), "image"), "load"), "herogun1.png")
        _l_(636988)
        _n_(636989, "self", lambda: self).rect  = _c_(636993, _a_(636992, _a_(636991, _n_(636990, "self", lambda: self), "slash"), "get_rect"))
        _l_(636994)
        _a_(636996, _n_(636995, "self", lambda: self), "rect").topleft = ( _a_(636998, _n_(636997, "self", lambda: self), "x"), _a_(637000, _n_(636999, "self", lambda: self), "y") )
        _l_(637001)
        _n_(637002, "self", lambda: self).speed = 10
        _l_(637003)
        _n_(637004, "self", lambda: self).color = _n_(637005, "color", lambda: color)
        _l_(637006)

    def draw(self, window):
        _l_(637022)

        _a_(637009, _n_(637008, "self", lambda: self), "rect").topleft = ( _a_(637011, _n_(637010, "self", lambda: self), "x"),_a_(637013, _n_(637012, "self", lambda: self), "y") )
        _l_(637014)

        _c_(637020, _a_(637016, _n_(637015, "window", lambda: window), "blit"), _n_(637017, "slash", lambda: slash), _a_(637019, _n_(637018, "self", lambda: self), "rect"))
        _l_(637021)


class enemygun:
    _l_(637108)

    def __init__(self,x,y,width,height,color):
        _l_(637070)

        _n_(637024, "self", lambda: self).x = _n_(637025, "x", lambda: x)
        _l_(637026)
        _n_(637027, "self", lambda: self).y = _n_(637028, "y", lambda: y)
        _l_(637029)
        _n_(637030, "self", lambda: self).width = _n_(637031, "width", lambda: width)
        _l_(637032)
        _n_(637033, "self", lambda: self).height = _n_(637034, "height", lambda: height)
        _l_(637035)
        _n_(637036, "self", lambda: self).color = _n_(637037, "color", lambda: color)
        _l_(637038)
        _n_(637039, "self", lambda: self).rect = _c_(637046, _a_(637041, _n_(637040, "pygame", lambda: pygame), "Rect"), _n_(637042, "x", lambda: x),_n_(637043, "y", lambda: y),_n_(637044, "width", lambda: width),_n_(637045, "height", lambda: height))
        _l_(637047)
        _n_(637048, "self", lambda: self).ss1 = _c_(637052, _a_(637051, _a_(637050, _n_(637049, "pygame", lambda: pygame), "image"), "load"), "enemygun1.png")
        _l_(637053)
        _n_(637054, "self", lambda: self).ss1 = _c_(637068, _a_(637057, _a_(637056, _n_(637055, "pygame", lambda: pygame), "transform"), "scale"), _a_(637059, _n_(637058, "self", lambda: self), "ss1"),(_c_(637063, _a_(637062, _a_(637061, _n_(637060, "self", lambda: self), "ss1"), "get_width"))//11,_c_(637067, _a_(637066, _a_(637065, _n_(637064, "self", lambda: self), "ss1"), "get_height"))//11))
        _l_(637069)
    def draw(self):
        _l_(637107)

        _a_(637072, _n_(637071, "self", lambda: self), "rect").topleft = (_a_(637074, _n_(637073, "self", lambda: self), "x"),_a_(637076, _n_(637075, "self", lambda: self), "y"))
        _l_(637077)
        _c_(637086, _a_(637080, _a_(637079, _n_(637078, "pygame", lambda: pygame), "draw"), "rect"), _n_(637081, "window", lambda: window),_a_(637083, _n_(637082, "self", lambda: self), "color"),_a_(637085, _n_(637084, "self", lambda: self), "rect"))
        _l_(637087)

        enemy3_rect = _c_(637094, _a_(637090, _a_(637089, _n_(637088, "self", lambda: self), "ss1"), "get_rect"), center = _a_(637093, _a_(637092, _n_(637091, "self", lambda: self), "rect"), "center"))
        _l_(637095)
        _n_(637096, "enemy3_rect", lambda: enemy3_rect).centerx += -7
        _l_(637097)
        _n_(637098, "enemy3_rect", lambda: enemy3_rect).centery += -2
        _l_(637099)
        _c_(637105, _a_(637101, _n_(637100, "window", lambda: window), "blit"), _a_(637103, _n_(637102, "self", lambda: self), "ss1"),_n_(637104, "enemy3_rect", lambda: enemy3_rect))
        _l_(637106)
# Color
white = (255,255,255)
_l_(637109)

# Draw Player
playerman = _c_(637112, _n_(637110, "player", lambda: player), 5,250,90,40,_n_(637111, "white", lambda: white))
_l_(637113)

# For Enemy
enemy1 = _c_(637116, _n_(637114, "enemy", lambda: enemy), 400,100,90,40,_n_(637115, "white", lambda: white))
_l_(637117)
enemy4 = _c_(637120, _n_(637118, "enemy", lambda: enemy), 400,400,90,40,_n_(637119, "white", lambda: white))
_l_(637121)

# For Enemy2
enemy21 = _c_(637124, _n_(637122, "enemy2", lambda: enemy2), 400,300,90,40,_n_(637123, "white", lambda: white))
_l_(637125)

# For Enemy3
ememy31 = _c_(637128, _n_(637126, "enemy3", lambda: enemy3), 400,400,90,40,_n_(637127, "white", lambda: white))
_l_(637129)

egun1 = _c_(637132, _n_(637130, "enemygun", lambda: enemygun), 250,300,30,20,_n_(637131, "white", lambda: white))
_l_(637133)

enemys = [_n_(637134, "enemy1", lambda: enemy1),_n_(637135, "enemy4", lambda: enemy4)]
_l_(637136)


# enemys
enemyGroup = _c_(637140, _a_(637139, _a_(637138, _n_(637137, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(637141)
level1 = [
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",]
_l_(637142)


for iy, row in _c_(637145, _n_(637143, "enumerate", lambda: enumerate), _n_(637144, "level1", lambda: level1)):
    _l_(637162)

    for ix, col in _c_(637148, _n_(637146, "enumerate", lambda: enumerate), _n_(637147, "row", lambda: row)):
        _l_(637161)

        if _n_(637149, "col", lambda: col) == "1":
            _l_(637160)

            new_enemy = _c_(637153, _n_(637150, "enemy", lambda: enemy), _n_(637151, "ix", lambda: ix)*70,_n_(637152, "iy", lambda: iy)*70,90,40,(255,255,255))
            _l_(637154)
            _c_(637158, _a_(637156, _n_(637155, "enemys", lambda: enemys), "append"), _n_(637157, "new_enemy", lambda: new_enemy))
            _l_(637159)



# Redrawwinodw
def redrawwindow():
    _l_(637209)

    _c_(637165, _a_(637164, _n_(637163, "window", lambda: window), "fill"), (0,0,0))
    _l_(637166)

    bg_width = _c_(637169, _a_(637168, _n_(637167, "bg", lambda: bg), "get_width"))
    _l_(637170)
    bg_offset = _n_(637171, "bg_shift", lambda: bg_shift) % _n_(637172, "bg_width", lambda: bg_width) 
    _l_(637173) 
    
    _c_(637178, _a_(637175, _n_(637174, "window", lambda: window), "blit"), _n_(637176, "bg", lambda: bg), (-_n_(637177, "bg_offset", lambda: bg_offset), 0)) 
    _l_(637179) 
    _c_(637185, _a_(637181, _n_(637180, "window", lambda: window), "blit"), _n_(637182, "bg", lambda: bg), (_n_(637183, "bg_width", lambda: bg_width) - _n_(637184, "bg_offset", lambda: bg_offset), 0))
    _l_(637186)

    
    # Draw playerman
    _c_(637189, _a_(637188, _n_(637187, "playerman", lambda: playerman), "draw"))
    _l_(637190)

    # Draw enemy
    for enemy in _n_(637191, "enemys", lambda: enemys):
        _l_(637196)

        _c_(637194, _a_(637193, _n_(637192, "enemy", lambda: enemy), "draw"))
        _l_(637195)

    # Draw enemy2
    _c_(637199, _a_(637198, _n_(637197, "enemy21", lambda: enemy21), "draw"))
    _l_(637200)

    # Draw enemy3
    _c_(637203, _a_(637202, _n_(637201, "ememy31", lambda: ememy31), "draw"))
    _l_(637204)


    # Draw enemygun
    _c_(637207, _a_(637206, _n_(637205, "egun1", lambda: egun1), "draw"))
    _l_(637208)
 





# FPS Cnd Clock
fps = (30)
_l_(637210)
clock = _c_(637214, _a_(637213, _a_(637212, _n_(637211, "pygame", lambda: pygame), "time"), "Clock"))
_l_(637215)


bullets = []
_l_(637216)

# Main Loop
run = True
_l_(637217)
while _n_(637218, "run", lambda: run):
    _l_(637391)

    _c_(637222, _a_(637220, _n_(637219, "clock", lambda: clock), "tick"), _n_(637221, "fps", lambda: fps))
    _l_(637223)
    for event in _c_(637227, _a_(637226, _a_(637225, _n_(637224, "pygame", lambda: pygame), "event"), "get")):
        _l_(637234)

        if _a_(637229, _n_(637228, "event", lambda: event), "type") == _a_(637231, _n_(637230, "pygame", lambda: pygame), "QUIT"):
            _l_(637233)

            run = False
            _l_(637232)


    keys = _c_(637238, _a_(637237, _a_(637236, _n_(637235, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(637239)

    if _n_(637240, "keys", lambda: keys)[_a_(637242, _n_(637241, "pygame", lambda: pygame), "K_f")]:
        _l_(637283)

         
        for bullet in _n_(637243, "bullets", lambda: bullets):
            _l_(637260)

            if _a_(637245, _n_(637244, "bullet", lambda: bullet), "x") < 500 and _a_(637247, _n_(637246, "bullet", lambda: bullet), "x") > 0:
                _l_(637259)

                _n_(637248, "bullet", lambda: bullet).x += _n_(637249, "bullet", lambda: bullet).speed 
                _l_(637250) 
            else:
                _c_(637257, _a_(637252, _n_(637251, "bullets", lambda: bullets), "pop"), _c_(637256, _a_(637254, _n_(637253, "bullets", lambda: bullets), "index"), _n_(637255, "bullet", lambda: bullet)))
                _l_(637258)
        if _c_(637263, _n_(637261, "len", lambda: len), _n_(637262, "bullets", lambda: bullets)) < 2:
            _l_(637282)

            _c_(637280, _a_(637265, _n_(637264, "bullets", lambda: bullets), "append"), _c_(637279, _n_(637266, "projectile", lambda: projectile), _c_(637272, _n_(637267, "round", lambda: round), _a_(637269, _n_(637268, "playerman", lambda: playerman), "x")+_a_(637271, _n_(637270, "playerman", lambda: playerman), "width")//2),_c_(637278, _n_(637273, "round", lambda: round), _a_(637275, _n_(637274, "playerman", lambda: playerman), "y") + _a_(637277, _n_(637276, "playerman", lambda: playerman), "height")-54),(0,0,0)))
            _l_(637281)



    for enemy in _n_(637284, "enemys", lambda: enemys):
        _l_(637288)

        _n_(637285, "enemy", lambda: enemy).x -= _n_(637286, "enemy", lambda: enemy).speed
        _l_(637287)
    


    bg_shift += _c_(637290, _n_(637289, "round", lambda: round), 3/2)
    _l_(637291)


    # Keys For Playerman
    keys = _c_(637295, _a_(637294, _a_(637293, _n_(637292, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(637296)

    if _n_(637297, "keys", lambda: keys)[_a_(637299, _n_(637298, "pygame", lambda: pygame), "K_a")] and _a_(637301, _n_(637300, "playerman", lambda: playerman), "x") > _a_(637303, _n_(637302, "playerman", lambda: playerman), "speed"):
        _l_(637307)

        _n_(637304, "playerman", lambda: playerman).x -= _n_(637305, "playerman", lambda: playerman).speed
        _l_(637306)

    if _n_(637308, "keys", lambda: keys)[_a_(637310, _n_(637309, "pygame", lambda: pygame), "K_d")] and _a_(637312, _n_(637311, "playerman", lambda: playerman), "x") < 260 - _a_(637314, _n_(637313, "playerman", lambda: playerman), "width") - _a_(637316, _n_(637315, "playerman", lambda: playerman), "speed"):
        _l_(637320)

        _n_(637317, "playerman", lambda: playerman).x += _n_(637318, "playerman", lambda: playerman).speed
        _l_(637319)


    if _n_(637321, "keys", lambda: keys)[_a_(637323, _n_(637322, "pygame", lambda: pygame), "K_w")] and _a_(637325, _n_(637324, "playerman", lambda: playerman), "y") > _a_(637327, _n_(637326, "playerman", lambda: playerman), "speed"):
        _l_(637331)

        _n_(637328, "playerman", lambda: playerman).y -= _n_(637329, "playerman", lambda: playerman).speed
        _l_(637330)


    if _n_(637332, "keys", lambda: keys)[_a_(637334, _n_(637333, "pygame", lambda: pygame), "K_s")] and _a_(637336, _n_(637335, "playerman", lambda: playerman), "y") < 500 - _a_(637338, _n_(637337, "playerman", lambda: playerman), "height") - _a_(637340, _n_(637339, "playerman", lambda: playerman), "speed"):
        _l_(637344)

        _n_(637341, "playerman", lambda: playerman).y += _n_(637342, "playerman", lambda: playerman).speed
        _l_(637343)


    if _n_(637345, "keys", lambda: keys)[_a_(637347, _n_(637346, "pygame", lambda: pygame), "K_SPACE")]:
        _l_(637353)

        if _a_(637349, _n_(637348, "playerman", lambda: playerman), "left"):
            _l_(637352)

            facing = -1
            _l_(637350)
        else:
            facing = 1
            _l_(637351)

    if _c_(637356, _n_(637354, "len", lambda: len), _n_(637355, "bullets", lambda: bullets)) < 5:
        _l_(637376)

        _c_(637374, _a_(637358, _n_(637357, "bullets", lambda: bullets), "append"), _c_(637373, _n_(637359, "player", lambda: player), _c_(637365, _n_(637360, "round", lambda: round), _a_(637362, _n_(637361, "playerman", lambda: playerman), "x")+_a_(637364, _n_(637363, "playerman", lambda: playerman), "width")//2), _c_(637371, _n_(637366, "round", lambda: round), _a_(637368, _n_(637367, "playerman", lambda: playerman), "y") + _a_(637370, _n_(637369, "playerman", lambda: playerman), "height")//2), 6, (255,255,255), _n_(637372, "white", lambda: white))) 
        _l_(637375) 
# Update And Other Sutff    
    _c_(637378, _n_(637377, "redrawwindow", lambda: redrawwindow))
    _l_(637379)
    for bullet in _n_(637380, "bullets", lambda: bullets):
        _l_(637385)

        _c_(637383, _a_(637382, _n_(637381, "bullet", lambda: bullet), "draw"))
        _l_(637384)

    
    _c_(637389, _a_(637388, _a_(637387, _n_(637386, "pygame", lambda: pygame), "display"), "update"))
    _l_(637390)
_c_(637394, _a_(637393, _n_(637392, "pygame", lambda: pygame), "quit"))
_l_(637395)
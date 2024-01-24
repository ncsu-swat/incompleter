# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63819205/self-rect-pygame-rectx-y-width-height-typeerror-argument-must-be-rect-style
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(633139)

except ImportError:
    pass
_c_(633142, _a_(633141, _n_(633140, "pygame", lambda: pygame), "init"))
_l_(633143)

# Build The Screen
window = _c_(633147, _a_(633146, _a_(633145, _n_(633144, "pygame", lambda: pygame), "display"), "set_mode"), (700,500))
_l_(633148)

# Name Screen
_c_(633152, _a_(633151, _a_(633150, _n_(633149, "pygame", lambda: pygame), "display"), "set_caption"), "Noobs first Game")
_l_(633153)

bg = _c_(633157, _a_(633156, _a_(633155, _n_(633154, "pygame", lambda: pygame), "image"), "load"), "skybg1.png")
_l_(633158)
bg_shift = 0
_l_(633159)


# Class Player
class player:
    _l_(633246)

    def __init__(self,x,y,width,height,color):
        _l_(633208)

        _n_(633160, "self", lambda: self).x = _n_(633161, "x", lambda: x)
        _l_(633162)
        _n_(633163, "self", lambda: self).y = _n_(633164, "y", lambda: y)
        _l_(633165)
        _n_(633166, "self", lambda: self).width = _n_(633167, "width", lambda: width)
        _l_(633168)
        _n_(633169, "self", lambda: self).height = _n_(633170, "height", lambda: height)
        _l_(633171)
        _n_(633172, "self", lambda: self).speed = 4
        _l_(633173)
        _n_(633174, "self", lambda: self).color = _n_(633175, "color", lambda: color)
        _l_(633176)
        _n_(633177, "self", lambda: self).rect = _c_(633184, _a_(633179, _n_(633178, "pygame", lambda: pygame), "Rect"), _n_(633180, "x", lambda: x),_n_(633181, "y", lambda: y),_n_(633182, "width", lambda: width),_n_(633183, "height", lambda: height))
        _l_(633185)
        _n_(633186, "self", lambda: self).ss1 = _c_(633190, _a_(633189, _a_(633188, _n_(633187, "pygame", lambda: pygame), "image"), "load"), "heroplane1.png")
        _l_(633191)
        _n_(633192, "self", lambda: self).ss1 = _c_(633206, _a_(633195, _a_(633194, _n_(633193, "pygame", lambda: pygame), "transform"), "scale"), _a_(633197, _n_(633196, "self", lambda: self), "ss1"),(_c_(633201, _a_(633200, _a_(633199, _n_(633198, "self", lambda: self), "ss1"), "get_width"))//9,_c_(633205, _a_(633204, _a_(633203, _n_(633202, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(633207)
    def draw(self):
        _l_(633245)

        _a_(633210, _n_(633209, "self", lambda: self), "rect").topleft=(_a_(633212, _n_(633211, "self", lambda: self), "x"),_a_(633214, _n_(633213, "self", lambda: self), "y"))
        _l_(633215)
        _c_(633224, _a_(633218, _a_(633217, _n_(633216, "pygame", lambda: pygame), "draw"), "rect"), _n_(633219, "window", lambda: window),_a_(633221, _n_(633220, "self", lambda: self), "color"),_a_(633223, _n_(633222, "self", lambda: self), "rect"))
        _l_(633225)

        player_rect = _c_(633232, _a_(633228, _a_(633227, _n_(633226, "self", lambda: self), "ss1"), "get_rect"), center = _a_(633231, _a_(633230, _n_(633229, "self", lambda: self), "rect"), "center"))
        _l_(633233)
        _n_(633234, "player_rect", lambda: player_rect).centerx += -7
        _l_(633235)
        _n_(633236, "player_rect", lambda: player_rect).centery += -6
        _l_(633237)
        _c_(633243, _a_(633239, _n_(633238, "window", lambda: window), "blit"), _a_(633241, _n_(633240, "self", lambda: self), "ss1"),_n_(633242, "player_rect", lambda: player_rect))
        _l_(633244)

# Class Enemy
class enemy:
    _l_(633333)

    def __init__(self,x,y,width,height,color):
        _l_(633295)

        _n_(633247, "self", lambda: self).x = _n_(633248, "x", lambda: x)
        _l_(633249)
        _n_(633250, "self", lambda: self).y = _n_(633251, "y", lambda: y)
        _l_(633252)
        _n_(633253, "self", lambda: self).width = _n_(633254, "width", lambda: width)
        _l_(633255)
        _n_(633256, "self", lambda: self).height = _n_(633257, "height", lambda: height)
        _l_(633258)
        _n_(633259, "self", lambda: self).speed = 4
        _l_(633260)
        _n_(633261, "self", lambda: self).color = _n_(633262, "color", lambda: color)
        _l_(633263)
        _n_(633264, "self", lambda: self).rect = _c_(633271, _a_(633266, _n_(633265, "pygame", lambda: pygame), "Rect"), _n_(633267, "x", lambda: x),_n_(633268, "y", lambda: y),_n_(633269, "width", lambda: width),_n_(633270, "height", lambda: height))
        _l_(633272)
        _n_(633273, "self", lambda: self).ss1 = _c_(633277, _a_(633276, _a_(633275, _n_(633274, "pygame", lambda: pygame), "image"), "load"), "enemyplane1.png")
        _l_(633278)
        _n_(633279, "self", lambda: self).ss1 = _c_(633293, _a_(633282, _a_(633281, _n_(633280, "pygame", lambda: pygame), "transform"), "scale"), _a_(633284, _n_(633283, "self", lambda: self), "ss1"),(_c_(633288, _a_(633287, _a_(633286, _n_(633285, "self", lambda: self), "ss1"), "get_width"))//9,_c_(633292, _a_(633291, _a_(633290, _n_(633289, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(633294)
    def draw(self):
        _l_(633332)

        _a_(633297, _n_(633296, "self", lambda: self), "rect").topleft = (_a_(633299, _n_(633298, "self", lambda: self), "x"),_a_(633301, _n_(633300, "self", lambda: self), "y"))
        _l_(633302)
        _c_(633311, _a_(633305, _a_(633304, _n_(633303, "pygame", lambda: pygame), "draw"), "rect"), _n_(633306, "window", lambda: window),_a_(633308, _n_(633307, "self", lambda: self), "color"),_a_(633310, _n_(633309, "self", lambda: self), "rect"))
        _l_(633312)

        enemy_rect = _c_(633319, _a_(633315, _a_(633314, _n_(633313, "self", lambda: self), "ss1"), "get_rect"), center = _a_(633318, _a_(633317, _n_(633316, "self", lambda: self), "rect"), "center"))
        _l_(633320)
        _n_(633321, "enemy_rect", lambda: enemy_rect).centerx += -2
        _l_(633322)
        _n_(633323, "enemy_rect", lambda: enemy_rect).centery += -6
        _l_(633324)
        _c_(633330, _a_(633326, _n_(633325, "window", lambda: window), "blit"), _a_(633328, _n_(633327, "self", lambda: self), "ss1"),_n_(633329, "enemy_rect", lambda: enemy_rect))
        _l_(633331)


# Class Enemy2
class enemy2:
    _l_(633418)

    def __init__(self,x,y,width,height,color):
        _l_(633380)

        _n_(633334, "self", lambda: self).x = _n_(633335, "x", lambda: x)
        _l_(633336)
        _n_(633337, "self", lambda: self).y = _n_(633338, "y", lambda: y)
        _l_(633339)
        _n_(633340, "self", lambda: self).width = _n_(633341, "width", lambda: width)
        _l_(633342)
        _n_(633343, "self", lambda: self).height = _n_(633344, "height", lambda: height)
        _l_(633345)
        _n_(633346, "self", lambda: self).color = _n_(633347, "color", lambda: color)
        _l_(633348)
        _n_(633349, "self", lambda: self).rect = _c_(633356, _a_(633351, _n_(633350, "pygame", lambda: pygame), "Rect"), _n_(633352, "x", lambda: x),_n_(633353, "y", lambda: y),_n_(633354, "width", lambda: width),_n_(633355, "height", lambda: height))
        _l_(633357)
        _n_(633358, "self", lambda: self).ss1 = _c_(633362, _a_(633361, _a_(633360, _n_(633359, "pygame", lambda: pygame), "image"), "load"), "enemyplane2.png")
        _l_(633363)
        _n_(633364, "self", lambda: self).ss1 = _c_(633378, _a_(633367, _a_(633366, _n_(633365, "pygame", lambda: pygame), "transform"), "scale"), _a_(633369, _n_(633368, "self", lambda: self), "ss1"),(_c_(633373, _a_(633372, _a_(633371, _n_(633370, "self", lambda: self), "ss1"), "get_width"))//9,_c_(633377, _a_(633376, _a_(633375, _n_(633374, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(633379)
    def draw(self):
        _l_(633417)

        _a_(633382, _n_(633381, "self", lambda: self), "rect").topleft = (_a_(633384, _n_(633383, "self", lambda: self), "x"),_a_(633386, _n_(633385, "self", lambda: self), "y"))
        _l_(633387)
        _c_(633396, _a_(633390, _a_(633389, _n_(633388, "pygame", lambda: pygame), "draw"), "rect"), _n_(633391, "window", lambda: window),_a_(633393, _n_(633392, "self", lambda: self), "color"),_a_(633395, _n_(633394, "self", lambda: self), "rect"))
        _l_(633397)

        enemy2_rect = _c_(633404, _a_(633400, _a_(633399, _n_(633398, "self", lambda: self), "ss1"), "get_rect"), center = _a_(633403, _a_(633402, _n_(633401, "self", lambda: self), "rect"), "center"))
        _l_(633405)
        _n_(633406, "enemy2_rect", lambda: enemy2_rect).centerx += -4
        _l_(633407)
        _n_(633408, "enemy2_rect", lambda: enemy2_rect).centery += -6
        _l_(633409)
        _c_(633415, _a_(633411, _n_(633410, "window", lambda: window), "blit"), _a_(633413, _n_(633412, "self", lambda: self), "ss1"),_n_(633414, "enemy2_rect", lambda: enemy2_rect))
        _l_(633416)


# Class Enemy3
class enemy3:
    _l_(633503)

    def __init__(self,x,y,width,height,color):
        _l_(633465)

        _n_(633419, "self", lambda: self).x = _n_(633420, "x", lambda: x)
        _l_(633421)
        _n_(633422, "self", lambda: self).y = _n_(633423, "y", lambda: y)
        _l_(633424)
        _n_(633425, "self", lambda: self).width = _n_(633426, "width", lambda: width)
        _l_(633427)
        _n_(633428, "self", lambda: self).height = _n_(633429, "height", lambda: height)
        _l_(633430)
        _n_(633431, "self", lambda: self).color = _n_(633432, "color", lambda: color)
        _l_(633433)
        _n_(633434, "self", lambda: self).rect = _c_(633441, _a_(633436, _n_(633435, "pygame", lambda: pygame), "Rect"), _n_(633437, "x", lambda: x),_n_(633438, "y", lambda: y),_n_(633439, "width", lambda: width),_n_(633440, "height", lambda: height))
        _l_(633442)
        _n_(633443, "self", lambda: self).ss1 = _c_(633447, _a_(633446, _a_(633445, _n_(633444, "pygame", lambda: pygame), "image"), "load"), "enemyplane3.png")
        _l_(633448)
        _n_(633449, "self", lambda: self).ss1 = _c_(633463, _a_(633452, _a_(633451, _n_(633450, "pygame", lambda: pygame), "transform"), "scale"), _a_(633454, _n_(633453, "self", lambda: self), "ss1"),(_c_(633458, _a_(633457, _a_(633456, _n_(633455, "self", lambda: self), "ss1"), "get_width"))//9,_c_(633462, _a_(633461, _a_(633460, _n_(633459, "self", lambda: self), "ss1"), "get_height"))//9))
        _l_(633464)
    def draw(self):
        _l_(633502)

        _a_(633467, _n_(633466, "self", lambda: self), "rect").topleft = (_a_(633469, _n_(633468, "self", lambda: self), "x"),_a_(633471, _n_(633470, "self", lambda: self), "y"))
        _l_(633472)
        _c_(633481, _a_(633475, _a_(633474, _n_(633473, "pygame", lambda: pygame), "draw"), "rect"), _n_(633476, "window", lambda: window),_a_(633478, _n_(633477, "self", lambda: self), "color"),_a_(633480, _n_(633479, "self", lambda: self), "rect"))
        _l_(633482)

        enemy3_rect = _c_(633489, _a_(633485, _a_(633484, _n_(633483, "self", lambda: self), "ss1"), "get_rect"), center = _a_(633488, _a_(633487, _n_(633486, "self", lambda: self), "rect"), "center"))
        _l_(633490)
        _n_(633491, "enemy3_rect", lambda: enemy3_rect).centerx += -4
        _l_(633492)
        _n_(633493, "enemy3_rect", lambda: enemy3_rect).centery += -6
        _l_(633494)
        _c_(633500, _a_(633496, _n_(633495, "window", lambda: window), "blit"), _a_(633498, _n_(633497, "self", lambda: self), "ss1"),_n_(633499, "enemy3_rect", lambda: enemy3_rect))
        _l_(633501)



class projectile(_n_(633504, "object", lambda: object)):
    _l_(633551)

    def __init__(self, x, y,color):
        _l_(633535)

        _n_(633505, "self", lambda: self).x = _n_(633506, "x", lambda: x)
        _l_(633507)
        _n_(633508, "self", lambda: self).y = _n_(633509, "y", lambda: y)
        _l_(633510)
        _n_(633511, "self", lambda: self).slash = _c_(633515, _a_(633514, _a_(633513, _n_(633512, "pygame", lambda: pygame), "image"), "load"), "herogun1.png")
        _l_(633516)
        _n_(633517, "self", lambda: self).rect  = _c_(633521, _a_(633520, _a_(633519, _n_(633518, "self", lambda: self), "slash"), "get_rect"))
        _l_(633522)
        _a_(633524, _n_(633523, "self", lambda: self), "rect").topleft = ( _a_(633526, _n_(633525, "self", lambda: self), "x"), _a_(633528, _n_(633527, "self", lambda: self), "y") )
        _l_(633529)
        _n_(633530, "self", lambda: self).speed = 10
        _l_(633531)
        _n_(633532, "self", lambda: self).color = _n_(633533, "color", lambda: color)
        _l_(633534)

    def draw(self, window):
        _l_(633550)

        _a_(633537, _n_(633536, "self", lambda: self), "rect").topleft = ( _a_(633539, _n_(633538, "self", lambda: self), "x"),_a_(633541, _n_(633540, "self", lambda: self), "y") )
        _l_(633542)

        _c_(633548, _a_(633544, _n_(633543, "window", lambda: window), "blit"), _n_(633545, "slash", lambda: slash), _a_(633547, _n_(633546, "self", lambda: self), "rect"))
        _l_(633549)


class enemygun:
    _l_(633636)

    def __init__(self,x,y,width,height,color):
        _l_(633598)

        _n_(633552, "self", lambda: self).x = _n_(633553, "x", lambda: x)
        _l_(633554)
        _n_(633555, "self", lambda: self).y = _n_(633556, "y", lambda: y)
        _l_(633557)
        _n_(633558, "self", lambda: self).width = _n_(633559, "width", lambda: width)
        _l_(633560)
        _n_(633561, "self", lambda: self).height = _n_(633562, "height", lambda: height)
        _l_(633563)
        _n_(633564, "self", lambda: self).color = _n_(633565, "color", lambda: color)
        _l_(633566)
        _n_(633567, "self", lambda: self).rect = _c_(633574, _a_(633569, _n_(633568, "pygame", lambda: pygame), "Rect"), _n_(633570, "x", lambda: x),_n_(633571, "y", lambda: y),_n_(633572, "width", lambda: width),_n_(633573, "height", lambda: height))
        _l_(633575)
        _n_(633576, "self", lambda: self).ss1 = _c_(633580, _a_(633579, _a_(633578, _n_(633577, "pygame", lambda: pygame), "image"), "load"), "enemygun1.png")
        _l_(633581)
        _n_(633582, "self", lambda: self).ss1 = _c_(633596, _a_(633585, _a_(633584, _n_(633583, "pygame", lambda: pygame), "transform"), "scale"), _a_(633587, _n_(633586, "self", lambda: self), "ss1"),(_c_(633591, _a_(633590, _a_(633589, _n_(633588, "self", lambda: self), "ss1"), "get_width"))//11,_c_(633595, _a_(633594, _a_(633593, _n_(633592, "self", lambda: self), "ss1"), "get_height"))//11))
        _l_(633597)
    def draw(self):
        _l_(633635)

        _a_(633600, _n_(633599, "self", lambda: self), "rect").topleft = (_a_(633602, _n_(633601, "self", lambda: self), "x"),_a_(633604, _n_(633603, "self", lambda: self), "y"))
        _l_(633605)
        _c_(633614, _a_(633608, _a_(633607, _n_(633606, "pygame", lambda: pygame), "draw"), "rect"), _n_(633609, "window", lambda: window),_a_(633611, _n_(633610, "self", lambda: self), "color"),_a_(633613, _n_(633612, "self", lambda: self), "rect"))
        _l_(633615)

        enemy3_rect = _c_(633622, _a_(633618, _a_(633617, _n_(633616, "self", lambda: self), "ss1"), "get_rect"), center = _a_(633621, _a_(633620, _n_(633619, "self", lambda: self), "rect"), "center"))
        _l_(633623)
        _n_(633624, "enemy3_rect", lambda: enemy3_rect).centerx += -7
        _l_(633625)
        _n_(633626, "enemy3_rect", lambda: enemy3_rect).centery += -2
        _l_(633627)
        _c_(633633, _a_(633629, _n_(633628, "window", lambda: window), "blit"), _a_(633631, _n_(633630, "self", lambda: self), "ss1"),_n_(633632, "enemy3_rect", lambda: enemy3_rect))
        _l_(633634)
# Color
white = (255,255,255)
_l_(633637)

# Draw Player
playerman = _c_(633640, _n_(633638, "player", lambda: player), 5,250,90,40,_n_(633639, "white", lambda: white))
_l_(633641)

# For Enemy
enemy1 = _c_(633644, _n_(633642, "enemy", lambda: enemy), 400,100,90,40,_n_(633643, "white", lambda: white))
_l_(633645)
enemy4 = _c_(633648, _n_(633646, "enemy", lambda: enemy), 400,400,90,40,_n_(633647, "white", lambda: white))
_l_(633649)

# For Enemy2
enemy21 = _c_(633652, _n_(633650, "enemy2", lambda: enemy2), 400,300,90,40,_n_(633651, "white", lambda: white))
_l_(633653)

# For Enemy3
ememy31 = _c_(633656, _n_(633654, "enemy3", lambda: enemy3), 400,400,90,40,_n_(633655, "white", lambda: white))
_l_(633657)

egun1 = _c_(633660, _n_(633658, "enemygun", lambda: enemygun), 250,300,30,20,_n_(633659, "white", lambda: white))
_l_(633661)

enemys = [_n_(633662, "enemy1", lambda: enemy1),_n_(633663, "enemy4", lambda: enemy4)]
_l_(633664)


# enemys
enemyGroup = _c_(633668, _a_(633667, _a_(633666, _n_(633665, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(633669)
level1 = [
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",]
_l_(633670)


for iy, row in _c_(633673, _n_(633671, "enumerate", lambda: enumerate), _n_(633672, "level1", lambda: level1)):
    _l_(633690)

    for ix, col in _c_(633676, _n_(633674, "enumerate", lambda: enumerate), _n_(633675, "row", lambda: row)):
        _l_(633689)

        if _n_(633677, "col", lambda: col) == "1":
            _l_(633688)

            new_enemy = _c_(633681, _n_(633678, "enemy", lambda: enemy), _n_(633679, "ix", lambda: ix)*70,_n_(633680, "iy", lambda: iy)*70,90,40,(255,255,255))
            _l_(633682)
            _c_(633686, _a_(633684, _n_(633683, "enemys", lambda: enemys), "append"), _n_(633685, "new_enemy", lambda: new_enemy))
            _l_(633687)



# Redrawwinodw
def redrawwindow():
    _l_(633737)

    _c_(633693, _a_(633692, _n_(633691, "window", lambda: window), "fill"), (0,0,0))
    _l_(633694)

    bg_width = _c_(633697, _a_(633696, _n_(633695, "bg", lambda: bg), "get_width"))
    _l_(633698)
    bg_offset = _n_(633699, "bg_shift", lambda: bg_shift) % _n_(633700, "bg_width", lambda: bg_width) 
    _l_(633701) 
    
    _c_(633706, _a_(633703, _n_(633702, "window", lambda: window), "blit"), _n_(633704, "bg", lambda: bg), (-_n_(633705, "bg_offset", lambda: bg_offset), 0)) 
    _l_(633707) 
    _c_(633713, _a_(633709, _n_(633708, "window", lambda: window), "blit"), _n_(633710, "bg", lambda: bg), (_n_(633711, "bg_width", lambda: bg_width) - _n_(633712, "bg_offset", lambda: bg_offset), 0))
    _l_(633714)

    
    # Draw playerman
    _c_(633717, _a_(633716, _n_(633715, "playerman", lambda: playerman), "draw"))
    _l_(633718)

    # Draw enemy
    for enemy in _n_(633719, "enemys", lambda: enemys):
        _l_(633724)

        _c_(633722, _a_(633721, _n_(633720, "enemy", lambda: enemy), "draw"))
        _l_(633723)

    # Draw enemy2
    _c_(633727, _a_(633726, _n_(633725, "enemy21", lambda: enemy21), "draw"))
    _l_(633728)

    # Draw enemy3
    _c_(633731, _a_(633730, _n_(633729, "ememy31", lambda: ememy31), "draw"))
    _l_(633732)


    # Draw enemygun
    _c_(633735, _a_(633734, _n_(633733, "egun1", lambda: egun1), "draw"))
    _l_(633736)
 





# FPS Cnd Clock
fps = (30)
_l_(633738)
clock = _c_(633742, _a_(633741, _a_(633740, _n_(633739, "pygame", lambda: pygame), "time"), "Clock"))
_l_(633743)


bullets = []
_l_(633744)

# Main Loop
run = True
_l_(633745)
while _n_(633746, "run", lambda: run):
    _l_(633919)

    _c_(633750, _a_(633748, _n_(633747, "clock", lambda: clock), "tick"), _n_(633749, "fps", lambda: fps))
    _l_(633751)
    for event in _c_(633755, _a_(633754, _a_(633753, _n_(633752, "pygame", lambda: pygame), "event"), "get")):
        _l_(633762)

        if _a_(633757, _n_(633756, "event", lambda: event), "type") == _a_(633759, _n_(633758, "pygame", lambda: pygame), "QUIT"):
            _l_(633761)

            run = False
            _l_(633760)


    keys = _c_(633766, _a_(633765, _a_(633764, _n_(633763, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(633767)

    if _n_(633768, "keys", lambda: keys)[_a_(633770, _n_(633769, "pygame", lambda: pygame), "K_f")]:
        _l_(633811)

         
        for bullet in _n_(633771, "bullets", lambda: bullets):
            _l_(633788)

            if _a_(633773, _n_(633772, "bullet", lambda: bullet), "x") < 500 and _a_(633775, _n_(633774, "bullet", lambda: bullet), "x") > 0:
                _l_(633787)

                _n_(633776, "bullet", lambda: bullet).x += _n_(633777, "bullet", lambda: bullet).speed 
                _l_(633778) 
            else:
                _c_(633785, _a_(633780, _n_(633779, "bullets", lambda: bullets), "pop"), _c_(633784, _a_(633782, _n_(633781, "bullets", lambda: bullets), "index"), _n_(633783, "bullet", lambda: bullet)))
                _l_(633786)
        if _c_(633791, _n_(633789, "len", lambda: len), _n_(633790, "bullets", lambda: bullets)) < 2:
            _l_(633810)

            _c_(633808, _a_(633793, _n_(633792, "bullets", lambda: bullets), "append"), _c_(633807, _n_(633794, "projectile", lambda: projectile), _c_(633800, _n_(633795, "round", lambda: round), _a_(633797, _n_(633796, "playerman", lambda: playerman), "x")+_a_(633799, _n_(633798, "playerman", lambda: playerman), "width")//2),_c_(633806, _n_(633801, "round", lambda: round), _a_(633803, _n_(633802, "playerman", lambda: playerman), "y") + _a_(633805, _n_(633804, "playerman", lambda: playerman), "height")-54),(0,0,0)))
            _l_(633809)



    for enemy in _n_(633812, "enemys", lambda: enemys):
        _l_(633816)

        _n_(633813, "enemy", lambda: enemy).x -= _n_(633814, "enemy", lambda: enemy).speed
        _l_(633815)
    


    bg_shift += _c_(633818, _n_(633817, "round", lambda: round), 3/2)
    _l_(633819)


    # Keys For Playerman
    keys = _c_(633823, _a_(633822, _a_(633821, _n_(633820, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(633824)

    if _n_(633825, "keys", lambda: keys)[_a_(633827, _n_(633826, "pygame", lambda: pygame), "K_a")] and _a_(633829, _n_(633828, "playerman", lambda: playerman), "x") > _a_(633831, _n_(633830, "playerman", lambda: playerman), "speed"):
        _l_(633835)

        _n_(633832, "playerman", lambda: playerman).x -= _n_(633833, "playerman", lambda: playerman).speed
        _l_(633834)

    if _n_(633836, "keys", lambda: keys)[_a_(633838, _n_(633837, "pygame", lambda: pygame), "K_d")] and _a_(633840, _n_(633839, "playerman", lambda: playerman), "x") < 260 - _a_(633842, _n_(633841, "playerman", lambda: playerman), "width") - _a_(633844, _n_(633843, "playerman", lambda: playerman), "speed"):
        _l_(633848)

        _n_(633845, "playerman", lambda: playerman).x += _n_(633846, "playerman", lambda: playerman).speed
        _l_(633847)


    if _n_(633849, "keys", lambda: keys)[_a_(633851, _n_(633850, "pygame", lambda: pygame), "K_w")] and _a_(633853, _n_(633852, "playerman", lambda: playerman), "y") > _a_(633855, _n_(633854, "playerman", lambda: playerman), "speed"):
        _l_(633859)

        _n_(633856, "playerman", lambda: playerman).y -= _n_(633857, "playerman", lambda: playerman).speed
        _l_(633858)


    if _n_(633860, "keys", lambda: keys)[_a_(633862, _n_(633861, "pygame", lambda: pygame), "K_s")] and _a_(633864, _n_(633863, "playerman", lambda: playerman), "y") < 500 - _a_(633866, _n_(633865, "playerman", lambda: playerman), "height") - _a_(633868, _n_(633867, "playerman", lambda: playerman), "speed"):
        _l_(633872)

        _n_(633869, "playerman", lambda: playerman).y += _n_(633870, "playerman", lambda: playerman).speed
        _l_(633871)


    if _n_(633873, "keys", lambda: keys)[_a_(633875, _n_(633874, "pygame", lambda: pygame), "K_SPACE")]:
        _l_(633881)

        if _a_(633877, _n_(633876, "playerman", lambda: playerman), "left"):
            _l_(633880)

            facing = -1
            _l_(633878)
        else:
            facing = 1
            _l_(633879)

    if _c_(633884, _n_(633882, "len", lambda: len), _n_(633883, "bullets", lambda: bullets)) < 5:
        _l_(633904)

        _c_(633902, _a_(633886, _n_(633885, "bullets", lambda: bullets), "append"), _c_(633901, _n_(633887, "player", lambda: player), _c_(633893, _n_(633888, "round", lambda: round), _a_(633890, _n_(633889, "playerman", lambda: playerman), "x")+_a_(633892, _n_(633891, "playerman", lambda: playerman), "width")//2), _c_(633899, _n_(633894, "round", lambda: round), _a_(633896, _n_(633895, "playerman", lambda: playerman), "y") + _a_(633898, _n_(633897, "playerman", lambda: playerman), "height")//2), 6, (255,255,255), _n_(633900, "white", lambda: white))) 
        _l_(633903) 
# Update And Other Sutff    
    _c_(633906, _n_(633905, "redrawwindow", lambda: redrawwindow))
    _l_(633907)
    for bullet in _n_(633908, "bullets", lambda: bullets):
        _l_(633913)

        _c_(633911, _a_(633910, _n_(633909, "bullet", lambda: bullet), "draw"))
        _l_(633912)

    
    _c_(633917, _a_(633916, _a_(633915, _n_(633914, "pygame", lambda: pygame), "display"), "update"))
    _l_(633918)
_c_(633922, _a_(633921, _n_(633920, "pygame", lambda: pygame), "quit"))
_l_(633923)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71072210/space-invaders-game-strange-typeerror-int-object-is-not-subscriptable-error-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(636267)

except ImportError:
    pass
try:
    import random
    _l_(636269)

except ImportError:
    pass
try:
    import math
    _l_(636271)

except ImportError:
    pass
#pygame.time.Clock(30)

# Initialize the game
_c_(636274, _a_(636273, _n_(636272, "pygame", lambda: pygame), "init"))
_l_(636275)
# Screen
screen = _c_(636279, _a_(636278, _a_(636277, _n_(636276, "pygame", lambda: pygame), "display"), "set_mode"), (800, 600))
_l_(636280)
# background
background = _c_(636284, _a_(636283, _a_(636282, _n_(636281, "pygame", lambda: pygame), "image"), "load"), 'background.png')
_l_(636285)

# Title and icon
_c_(636289, _a_(636288, _a_(636287, _n_(636286, "pygame", lambda: pygame), "display"), "set_caption"), "Space Invaders")
_l_(636290)

# player
playerImg = _c_(636294, _a_(636293, _a_(636292, _n_(636291, "pygame", lambda: pygame), "image"), "load"), 'spaceship.png')
_l_(636295)
playerX = 370
_l_(636296)
playerY = 510
_l_(636297)
playerX_change = 0
_l_(636298)

# enemy
enemyImg = []
_l_(636299)
enemyX = []
_l_(636300)
enemyY = []
_l_(636301)
enemyX_change = []
_l_(636302)
enemyY_change = []
_l_(636303)
num_of_enemies = 6
_l_(636304)

for i in _c_(636307, _n_(636305, "range", lambda: range), _n_(636306, "num_of_enemies", lambda: num_of_enemies)):
    _l_(636338)

    _c_(636314, _a_(636309, _n_(636308, "enemyImg", lambda: enemyImg), "append"), _c_(636313, _a_(636312, _a_(636311, _n_(636310, "pygame", lambda: pygame), "image"), "load"), 'ufo.png'))
    _l_(636315)
    _c_(636321, _a_(636317, _n_(636316, "enemyX", lambda: enemyX), "append"), _c_(636320, _a_(636319, _n_(636318, "random", lambda: random), "randint"), 0, 735))
    _l_(636322)
    _c_(636328, _a_(636324, _n_(636323, "enemyY", lambda: enemyY), "append"), _c_(636327, _a_(636326, _n_(636325, "random", lambda: random), "randint"), 40, 100))
    _l_(636329)
    _c_(636332, _a_(636331, _n_(636330, "enemyX_change", lambda: enemyX_change), "append"), 2)
    _l_(636333)
    _c_(636336, _a_(636335, _n_(636334, "enemyY_change", lambda: enemyY_change), "append"), 40)
    _l_(636337)

# missile
missileImg = _c_(636342, _a_(636341, _a_(636340, _n_(636339, "pygame", lambda: pygame), "image"), "load"), 'missile.png')
_l_(636343)
missileX = _n_(636344, "playerX", lambda: playerX)
_l_(636345)
missileY = 483
_l_(636346)
missileY_change = 6
_l_(636347)
missile_state = "ready"
_l_(636348)

def player(x, y):
    _l_(636356)

    _c_(636354, _a_(636350, _n_(636349, "screen", lambda: screen), "blit"), _n_(636351, "playerImg", lambda: playerImg), (_n_(636352, "x", lambda: x), _n_(636353, "y", lambda: y)))
    _l_(636355)

def enemy(x, y, i):
    _l_(636365)

    _c_(636363, _a_(636358, _n_(636357, "screen", lambda: screen), "blit"), _n_(636359, "enemyImg", lambda: enemyImg)[_n_(636360, "i", lambda: i)], (_n_(636361, "x", lambda: x), _n_(636362, "y", lambda: y)))
    _l_(636364)

def fire_missile(x, y):
    _l_(636375)

    global missile_state
    _l_(636366)
    missile_state = "fire"
    _l_(636367)
    _c_(636373, _a_(636369, _n_(636368, "screen", lambda: screen), "blit"), _n_(636370, "missileImg", lambda: missileImg), (_n_(636371, "x", lambda: x) + 16, _n_(636372, "y", lambda: y) + 10))
    _l_(636374)

def is_collision(enemyX, enemyY, missileX, missileY):
    _l_(636394)

    distance = _c_(636388, _a_(636377, _n_(636376, "math", lambda: math), "sqrt"), _c_(636382, _a_(636379, _n_(636378, "math", lambda: math), "pow"), _n_(636380, "enemyX", lambda: enemyX) - _n_(636381, "missileX", lambda: missileX), 2) + _c_(636387, _a_(636384, _n_(636383, "math", lambda: math), "pow"), _n_(636385, "enemyY", lambda: enemyY) - _n_(636386, "missileY", lambda: missileY), 2))
    _l_(636389)
    if _n_(636390, "distance", lambda: distance) < 27:
        _l_(636393)

        aux = True
        _l_(636391)
        return aux
    else:
        aux = False
        _l_(636392)
        return aux

# Game loop
clock = _c_(636398, _a_(636397, _a_(636396, _n_(636395, "pygame", lambda: pygame), "time"), "Clock"))
_l_(636399)
running = True
_l_(636400)
while _n_(636401, "running", lambda: running):
    _l_(636600)

    _c_(636404, _a_(636403, _n_(636402, "clock", lambda: clock), "tick"), 60)
    _l_(636405)

    _c_(636408, _a_(636407, _n_(636406, "screen", lambda: screen), "fill"), (0, 0, 0))
    _l_(636409)
    # background image
    _c_(636413, _a_(636411, _n_(636410, "screen", lambda: screen), "blit"), _n_(636412, "background", lambda: background), (-100, 0))
    _l_(636414)

    for event in _c_(636418, _a_(636417, _a_(636416, _n_(636415, "pygame", lambda: pygame), "event"), "get")):
        _l_(636473)

        if _a_(636420, _n_(636419, "event", lambda: event), "type") == _a_(636422, _n_(636421, "pygame", lambda: pygame), "QUIT"):
            _l_(636424)

            running = False
            _l_(636423)
        # if keystroke is pressed check what key it is
        if _a_(636426, _n_(636425, "event", lambda: event), "type") == _a_(636428, _n_(636427, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(636457)

            if _a_(636430, _n_(636429, "event", lambda: event), "key") == _a_(636432, _n_(636431, "pygame", lambda: pygame), "K_a"):
                _l_(636434)

                playerX_change = -3
                _l_(636433)
            if _a_(636436, _n_(636435, "event", lambda: event), "key") == _a_(636438, _n_(636437, "pygame", lambda: pygame), "K_d"):
                _l_(636440)

                playerX_change = +3
                _l_(636439)
            if _a_(636442, _n_(636441, "event", lambda: event), "key") == _a_(636444, _n_(636443, "pygame", lambda: pygame), "K_SPACE"):
                _l_(636456)

                if _n_(636445, "missile_state", lambda: missile_state) == "ready":
                    _l_(636455)

                    missileX = _n_(636446, "playerX", lambda: playerX)
                    _l_(636447)
                    missileY = _n_(636448, "playerY", lambda: playerY) - 27
                    _l_(636449)
                    _c_(636453, _n_(636450, "fire_missile", lambda: fire_missile), _n_(636451, "missileX", lambda: missileX), _n_(636452, "missileY", lambda: missileY))
                    _l_(636454)
        if _a_(636459, _n_(636458, "event", lambda: event), "type") == _a_(636461, _n_(636460, "pygame", lambda: pygame), "KEYUP"):
            _l_(636472)

            if _a_(636463, _n_(636462, "event", lambda: event), "key") == _a_(636465, _n_(636464, "pygame", lambda: pygame), "K_a") or _a_(636467, _n_(636466, "event", lambda: event), "key") == _a_(636469, _n_(636468, "pygame", lambda: pygame), "K_d"):
                _l_(636471)

                playerX_change = 0
                _l_(636470)

    # spaceship boundary
    playerX += _n_(636474, "playerX_change", lambda: playerX_change)
    _l_(636475)
    if _n_(636476, "playerX", lambda: playerX) <= 0:
        _l_(636481)

        playerX = 0
        _l_(636477)
    elif _n_(636478, "playerX", lambda: playerX) >= 740:
        _l_(636480)

        playerX = 740
        _l_(636479)
    # enemy movement
    for i in _c_(636484, _n_(636482, "range", lambda: range), _n_(636483, "num_of_enemies", lambda: num_of_enemies)):
        _l_(636550)

        _n_(636485, "enemyX", lambda: enemyX)[_n_(636486, "i", lambda: i)] += _n_(636487, "enemyX_change", lambda: enemyX_change)[_n_(636488, "i", lambda: i)]
        _l_(636489)
        if _n_(636490, "enemyX", lambda: enemyX)[_n_(636491, "i", lambda: i)] <= 0:
            _l_(636511)

            _n_(636492, "enemyX_change", lambda: enemyX_change)[_n_(636493, "i", lambda: i)] = 2
            _l_(636494)
            _n_(636495, "enemyY", lambda: enemyY)[_n_(636496, "i", lambda: i)] += _n_(636497, "enemyY_change", lambda: enemyY_change)[_n_(636498, "i", lambda: i)]
            _l_(636499)
        elif _n_(636500, "enemyX", lambda: enemyX)[_n_(636501, "i", lambda: i)] >= 740:
            _l_(636510)

            _n_(636502, "enemyX_change", lambda: enemyX_change)[_n_(636503, "i", lambda: i)] = -2
            _l_(636504)
            _n_(636505, "enemyY", lambda: enemyY)[_n_(636506, "i", lambda: i)] += _n_(636507, "enemyY_change", lambda: enemyY_change)[_n_(636508, "i", lambda: i)]
            _l_(636509)

        collision = _c_(636519, _n_(636512, "is_collision", lambda: is_collision), _n_(636513, "enemyX", lambda: enemyX)[_n_(636514, "i", lambda: i)], _n_(636515, "enemyY", lambda: enemyY)[_n_(636516, "i", lambda: i)], _n_(636517, "missileX", lambda: missileX), _n_(636518, "missileY", lambda: missileY))
        _l_(636520)
        if _n_(636521, "collision", lambda: collision):
            _l_(636541)

            missileY = 483
            _l_(636522)
            missile_state = "ready"
            _l_(636523)
            score += 1
            _l_(636524)
            _c_(636527, _n_(636525, "print", lambda: print), _n_(636526, "score", lambda: score))
            _l_(636528)
            _n_(636529, "enemyX", lambda: enemyX)[_n_(636530, "i", lambda: i)] = _c_(636533, _a_(636532, _n_(636531, "random", lambda: random), "randint"), 0, 735)
            _l_(636534)
            _n_(636535, "enemyY", lambda: enemyY)[_n_(636536, "i", lambda: i)] = _c_(636539, _a_(636538, _n_(636537, "random", lambda: random), "randint"), 40, 100)
            _l_(636540)

        _c_(636548, _n_(636542, "enemy", lambda: enemy), _n_(636543, "enemyX", lambda: enemyX)[_n_(636544, "i", lambda: i)], _n_(636545, "enemyY", lambda: enemyY)[_n_(636546, "i", lambda: i)], _n_(636547, "i", lambda: i))
        _l_(636549)

    # missile movement
    if _n_(636551, "missileY", lambda: missileY) < -10:
        _l_(636554)

        missileY = 483
        _l_(636552)
        missile_state = "ready"
        _l_(636553)
    if _n_(636555, "missile_state", lambda: missile_state) is "fire":
        _l_(636563)

        _c_(636559, _n_(636556, "fire_missile", lambda: fire_missile), _n_(636557, "missileX", lambda: missileX), _n_(636558, "missileY", lambda: missileY))
        _l_(636560)
        missileY -= _n_(636561, "missileY_change", lambda: missileY_change)
        _l_(636562)
    
    collision = _c_(636571, _n_(636564, "is_collision", lambda: is_collision), _n_(636565, "enemyX", lambda: enemyX)[_n_(636566, "i", lambda: i)], _n_(636567, "enemyY", lambda: enemyY)[_n_(636568, "i", lambda: i)], _n_(636569, "missileX", lambda: missileX), _n_(636570, "missileY", lambda: missileY))
    _l_(636572)
    if _n_(636573, "collision", lambda: collision):
        _l_(636589)

        missileY = 483
        _l_(636574)
        missile_state = "ready"
        _l_(636575)
        score += 1
        _l_(636576)
        _c_(636579, _n_(636577, "print", lambda: print), _n_(636578, "score", lambda: score))
        _l_(636580)
        enemyX = _c_(636583, _a_(636582, _n_(636581, "random", lambda: random), "randint"), 0, 735)
        _l_(636584)
        enemyY = _c_(636587, _a_(636586, _n_(636585, "random", lambda: random), "randint"), 40, 100)
        _l_(636588)

    _c_(636593, _n_(636590, "player", lambda: player), _n_(636591, "playerX", lambda: playerX), _n_(636592, "playerY", lambda: playerY))
    _l_(636594)
    _c_(636598, _a_(636597, _a_(636596, _n_(636595, "pygame", lambda: pygame), "display"), "update"))
    _l_(636599)
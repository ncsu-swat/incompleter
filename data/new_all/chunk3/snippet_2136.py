# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62179706/pygame-error-typeerror-argument-1-must-be-pygame-surface-not-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(570985)

except ImportError:
    pass
try:
    import random
    _l_(570987)

except ImportError:
    pass
try:
    import pygame
    _l_(570989)

except ImportError:
    pass

_c_(570992, _a_(570991, _n_(570990, "pygame", lambda: pygame), "init"))
_l_(570993)
# Screen (Pixels by Pixels (X and Y (X = right and left Y = up and down)))
screen = _c_(570997, _a_(570996, _a_(570995, _n_(570994, "pygame", lambda: pygame), "display"), "set_mode"), (800, 600))
_l_(570998)
running = True
_l_(570999)
# Title and Icon
_c_(571003, _a_(571002, _a_(571001, _n_(571000, "pygame", lambda: pygame), "display"), "set_caption"), "Space Invaders")
_l_(571004)
icon = _c_(571008, _a_(571007, _a_(571006, _n_(571005, "pygame", lambda: pygame), "image"), "load"), 'Icon.png')
_l_(571009)
_c_(571014, _a_(571012, _a_(571011, _n_(571010, "pygame", lambda: pygame), "display"), "set_icon"), _n_(571013, "icon", lambda: icon))
_l_(571015)
# Player Icon/Image
playerimg = _c_(571019, _a_(571018, _a_(571017, _n_(571016, "pygame", lambda: pygame), "image"), "load"), 'Player.png')
_l_(571020)
playerX = 370
_l_(571021)
playerY = 480
_l_(571022)
playerX_change = 0
_l_(571023)


def player(x, y):
    _l_(571031)

    # Blit means Draw
    _c_(571029, _a_(571025, _n_(571024, "screen", lambda: screen), "blit"), _n_(571026, "playerimg", lambda: playerimg), (_n_(571027, "x", lambda: x), _n_(571028, "y", lambda: y)))
    _l_(571030)


def enemy(x, y):
    _l_(571039)

    # Blit means Draw
    _c_(571037, _a_(571033, _n_(571032, "screen", lambda: screen), "blit"), _n_(571034, "enemyImg", lambda: enemyImg), (_n_(571035, "x", lambda: x), _n_(571036, "y", lambda: y)))
    _l_(571038)


def fire_bullet(x, y):
    _l_(571049)

    global bullet_state
    _l_(571040)
    bullet_state = "fire"
    _l_(571041)
    _c_(571047, _a_(571043, _n_(571042, "screen", lambda: screen), "blit"), _n_(571044, "bulletimg", lambda: bulletimg), (_n_(571045, "x", lambda: x) + 16, _n_(571046, "y", lambda: y) + 10))
    _l_(571048)


def isCollision(enemyX, enemyY, bulletX, bulletY):
    _l_(571070)

    distance = _c_(571064, _a_(571051, _n_(571050, "math", lambda: math), "sqrt"), (_c_(571057, _a_(571053, _n_(571052, "math", lambda: math), "pow"), _n_(571054, "enemyX", lambda: enemyX)[_n_(571055, "i", lambda: i)] - _n_(571056, "bulletX", lambda: bulletX), 2) + _c_(571063, _a_(571059, _n_(571058, "math", lambda: math), "pow"), _n_(571060, "enemyY", lambda: enemyY)[_n_(571061, "i", lambda: i)] - _n_(571062, "bulletY", lambda: bulletY), 2)))
    _l_(571065)
    if _n_(571066, "distance", lambda: distance) < 27:
        _l_(571069)

        aux = True
        _l_(571067)
        return aux
    else:
        aux = False
        _l_(571068)
        return aux


background = _c_(571074, _a_(571073, _a_(571072, _n_(571071, "pygame", lambda: pygame), "image"), "load"), '247.jpg')
_l_(571075)

# Enemy
num_of_enemy = 6
_l_(571076)
enemyImg = []
_l_(571077)
enemyX = []
_l_(571078)
enemyY = []
_l_(571079)
enemyX_change = []
_l_(571080)
enemyY_change = []
_l_(571081)
for i in _c_(571084, _n_(571082, "range", lambda: range), _n_(571083, "num_of_enemy", lambda: num_of_enemy)):
    _l_(571115)

    _c_(571091, _a_(571086, _n_(571085, "enemyImg", lambda: enemyImg), "append"), _c_(571090, _a_(571089, _a_(571088, _n_(571087, "pygame", lambda: pygame), "image"), "load"), 'space-invaders.png'))
    _l_(571092)
    _c_(571098, _a_(571094, _n_(571093, "enemyX", lambda: enemyX), "append"), _c_(571097, _a_(571096, _n_(571095, "random", lambda: random), "randint"), 0, 735))
    _l_(571099)
    _c_(571105, _a_(571101, _n_(571100, "enemyY", lambda: enemyY), "append"), _c_(571104, _a_(571103, _n_(571102, "random", lambda: random), "randint"), 50, 150))
    _l_(571106)
    _c_(571109, _a_(571108, _n_(571107, "enemyX_change", lambda: enemyX_change), "append"), 4)
    _l_(571110)
    _c_(571113, _a_(571112, _n_(571111, "enemyY_change", lambda: enemyY_change), "append"), 40)
    _l_(571114)

bulletimg = _c_(571119, _a_(571118, _a_(571117, _n_(571116, "pygame", lambda: pygame), "image"), "load"), 'bullet.png')
_l_(571120)
bulletX = 0
_l_(571121)
bulletY = 450
_l_(571122)
bulletX_change = 480
_l_(571123)
bulletY_change = 10
_l_(571124)
bullet_state = "ready"
_l_(571125)

score = 0
_l_(571126)
# Game loop (Put most of code for game in this loop)
while _n_(571127, "running", lambda: running):
    _l_(571285)

    _c_(571130, _a_(571129, _n_(571128, "screen", lambda: screen), "fill"), (255, 0, 0))
    _l_(571131)
    # BAckground
    _c_(571135, _a_(571133, _n_(571132, "screen", lambda: screen), "blit"), _n_(571134, "background", lambda: background), (0, 0))
    _l_(571136)
    for event in _c_(571140, _a_(571139, _a_(571138, _n_(571137, "pygame", lambda: pygame), "event"), "get")):
        _l_(571193)

        if _a_(571142, _n_(571141, "event", lambda: event), "type") == _a_(571144, _n_(571143, "pygame", lambda: pygame), "QUIT"):
            _l_(571146)

            running = False
            _l_(571145)
        # if keystroke is pressed check whether is right or left
        if _a_(571148, _n_(571147, "event", lambda: event), "type") == _a_(571150, _n_(571149, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(571192)

            if _a_(571152, _n_(571151, "event", lambda: event), "key") == _a_(571154, _n_(571153, "pygame", lambda: pygame), "K_LEFT"):
                _l_(571156)

                playerX_change = -5
                _l_(571155)
            if _a_(571158, _n_(571157, "event", lambda: event), "key") == _a_(571160, _n_(571159, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(571162)

                playerX_change = 5
                _l_(571161)
            if _a_(571164, _n_(571163, "event", lambda: event), "key") == _a_(571166, _n_(571165, "pygame", lambda: pygame), "K_SPACE"):
                _l_(571176)

                if _n_(571167, "bullet_state", lambda: bullet_state) == "ready":
                    _l_(571175)

                    bulletX = _n_(571168, "playerX", lambda: playerX)
                    _l_(571169)
                    _c_(571173, _n_(571170, "fire_bullet", lambda: fire_bullet), _n_(571171, "playerX", lambda: playerX), _n_(571172, "bulletY", lambda: bulletY))
                    _l_(571174)



        elif _a_(571178, _n_(571177, "event", lambda: event), "type") == _a_(571180, _n_(571179, "pygame", lambda: pygame), "KEYUP"):
            _l_(571191)

            if _a_(571182, _n_(571181, "event", lambda: event), "key") == _a_(571184, _n_(571183, "pygame", lambda: pygame), "K_LEFT") or _a_(571186, _n_(571185, "event", lambda: event), "key") == _a_(571188, _n_(571187, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(571190)

                playerX_change = 0
                _l_(571189)

    # RGB (screen.fill) = red green blue
    # 5 = 5 + - 0.1 -> 5 = 5 - 0.1
    # making so nothing can go out of bounds
    for i in _c_(571196, _n_(571194, "range", lambda: range), _n_(571195, "num_of_enemy", lambda: num_of_enemy)):
        _l_(571224)

        _n_(571197, "enemyX", lambda: enemyX)[_n_(571198, "i", lambda: i)] += _n_(571199, "enemyX_change", lambda: enemyX_change)[_n_(571200, "i", lambda: i)]
        _l_(571201)
        if _n_(571202, "enemyX", lambda: enemyX)[_n_(571203, "i", lambda: i)] <= 0:
            _l_(571223)

            _n_(571204, "enemyX_change", lambda: enemyX_change)[_n_(571205, "i", lambda: i)] = 4
            _l_(571206)
            _n_(571207, "enemyY", lambda: enemyY)[_n_(571208, "i", lambda: i)] += _n_(571209, "enemyY_change", lambda: enemyY_change)[_n_(571210, "i", lambda: i)]
            _l_(571211)
        elif _n_(571212, "enemyX", lambda: enemyX)[_n_(571213, "i", lambda: i)] >= 736:
            _l_(571222)

            _n_(571214, "enemyX_change", lambda: enemyX_change)[_n_(571215, "i", lambda: i)] = -4
            _l_(571216)
            _n_(571217, "enemyY", lambda: enemyY)[_n_(571218, "i", lambda: i)] += _n_(571219, "enemyY_change", lambda: enemyY_change)[_n_(571220, "i", lambda: i)]
            _l_(571221)
    playerX += _n_(571225, "playerX_change", lambda: playerX_change)
    _l_(571226)
    if _n_(571227, "playerX", lambda: playerX) <= 0:
        _l_(571232)

        playerX = 0
        _l_(571228)
    elif _n_(571229, "playerX", lambda: playerX) >= 736:
        _l_(571231)

        playerX = 736
        _l_(571230)

    # Bullet movement
    if _n_(571233, "bulletY", lambda: bulletY) <= 0:
        _l_(571236)

        bulletY = 480
        _l_(571234)
        bullet_state = "ready"
        _l_(571235)

    if _n_(571237, "bullet_state", lambda: bullet_state) == "fire":
        _l_(571245)

        _c_(571241, _n_(571238, "fire_bullet", lambda: fire_bullet), _n_(571239, "bulletX", lambda: bulletX), _n_(571240, "bulletY", lambda: bulletY))
        _l_(571242)
        bulletY -= _n_(571243, "bulletY_change", lambda: bulletY_change)
        _l_(571244)

    # Collison
    collision = _c_(571251, _n_(571246, "isCollision", lambda: isCollision), _n_(571247, "enemyX", lambda: enemyX), _n_(571248, "enemyY", lambda: enemyY), _n_(571249, "bulletX", lambda: bulletX), _n_(571250, "bulletY", lambda: bulletY))
    _l_(571252)
    if _n_(571253, "collision", lambda: collision):
        _l_(571269)

        bulletY = 480
        _l_(571254)
        bullet_state = "ready"
        _l_(571255)
        score += 1
        _l_(571256)
        _c_(571259, _n_(571257, "print", lambda: print), _n_(571258, "score", lambda: score))
        _l_(571260)
        enemyX = _c_(571263, _a_(571262, _n_(571261, "random", lambda: random), "randint"), 0, 735)
        _l_(571264)
        enemyY = _c_(571267, _a_(571266, _n_(571265, "random", lambda: random), "randint"), 50, 150)
        _l_(571268)

    _c_(571273, _n_(571270, "player", lambda: player), _n_(571271, "playerX", lambda: playerX), _n_(571272, "playerY", lambda: playerY))
    _l_(571274)
    _c_(571278, _n_(571275, "enemy", lambda: enemy), _n_(571276, "enemyX", lambda: enemyX), _n_(571277, "enemyY", lambda: enemyY))
    _l_(571279)
    _c_(571283, _a_(571282, _a_(571281, _n_(571280, "pygame", lambda: pygame), "display"), "update"))
    _l_(571284)
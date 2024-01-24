# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54404044/typeerror-argument-1-must-be-pygame-surface-not-pygame-rect-in-my-python-game
# Imports--------------------------------------------------------------------------------------------------------------#

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(399176)

except ImportError:
    pass


# initialization-------------------------------------------------------------------------------------------------------#

_c_(399179, _a_(399178, _n_(399177, "pygame", lambda: pygame), "init"))
_l_(399180)

# Flags----------------------------------------------------------------------------------------------------------------#

gameExit = False
_l_(399181)

# Variables -----------------------------------------------------------------------------------------------------------#

display_height = 500
_l_(399182)
display_width = 500
_l_(399183)
bg = (0, 0, 0)
_l_(399184)
isJump = False
_l_(399185)
# Colors --------------------------------------------------------------------------------------------------------------#

FUCHSIA = (255, 0, 255)
_l_(399186)
PURPLE = (128, 0, 128)
_l_(399187)
TEAL = (0, 128, 128)
_l_(399188)
LIME = (0, 255, 0)
_l_(399189)
GREEN = (0, 128, 0)
_l_(399190)
OLIVE = (128, 128, 0)
_l_(399191)
YELLOW = (255, 255, 0)
_l_(399192)
ORANGE = (255, 165, 0)
_l_(399193)
RED = (255, 0, 0)
_l_(399194)
MAROON = (128, 0, 0)
_l_(399195)
SILVER = (192, 192, 192)
_l_(399196)
GRAY = (128, 128, 128)
_l_(399197)
BLUE = (0, 0, 255)
_l_(399198)
NAVY = (0, 0, 128)
_l_(399199)
AQUA = (0, 255, 255)
_l_(399200)
WHITE = (255, 255, 255)
_l_(399201)
BLACK = (0, 0, 0)
_l_(399202)

# Draw Screen----------------------------------------------------------------------------------------------------------#

win = _c_(399208, _a_(399205, _a_(399204, _n_(399203, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(399206, "display_width", lambda: display_width), _n_(399207, "display_height", lambda: display_height)))
_l_(399209)
_c_(399213, _a_(399212, _a_(399211, _n_(399210, "pygame", lambda: pygame), "display"), "set_caption"), "Airbender Training")
_l_(399214)
Clock = _c_(399218, _a_(399217, _a_(399216, _n_(399215, "pygame", lambda: pygame), "time"), "Clock"))
_l_(399219)

# Mobs ----------------------------------------------------------------------------------------------------------------#
class entity:
    _l_(399239)

    #Entities will be every mob in the game
    def __init__(self, width, height, velocity, x, y, sprite):
        _l_(399238)


        _n_(399220, "entity", lambda: entity).width = _n_(399221, "width", lambda: width)
        _l_(399222)
        _n_(399223, "entity", lambda: entity).height = _n_(399224, "height", lambda: height)
        _l_(399225)
        _n_(399226, "entity", lambda: entity).velocity = _n_(399227, "velocity", lambda: velocity)
        _l_(399228)
        _n_(399229, "entity", lambda: entity).x_position = _n_(399230, "x", lambda: x)
        _l_(399231)
        _n_(399232, "entity", lambda: entity).y_position = _n_(399233, "y", lambda: y)
        _l_(399234)
        _n_(399235, "entity", lambda: entity).sprite = _n_(399236, "sprite", lambda: sprite)
        _l_(399237)

player_width = 64
_l_(399240)
player_height = 64
_l_(399241)
player_velocity = 5
_l_(399242)
player_x_position = 5
_l_(399243)
player_y_position = 5
_l_(399244)
player_sprite = _c_(399254, _a_(399247, _a_(399246, _n_(399245, "pygame", lambda: pygame), "draw"), "rect"), _n_(399248, "win", lambda: win), _n_(399249, "RED", lambda: RED), (_n_(399250, "player_x_position", lambda: player_x_position), _n_(399251, "player_y_position", lambda: player_y_position), _n_(399252, "player_width", lambda: player_width), _n_(399253, "player_height", lambda: player_height)))
_l_(399255)
    # ^This makes a placeholder red square^
player = _c_(399263, _n_(399256, "entity", lambda: entity), _n_(399257, "player_width", lambda: player_width), _n_(399258, "player_height", lambda: player_height), _n_(399259, "player_velocity", lambda: player_velocity), _n_(399260, "player_x_position", lambda: player_x_position), _n_(399261, "player_y_position", lambda: player_y_position), _n_(399262, "player_sprite", lambda: player_sprite))
_l_(399264)

# Functions -----------------------------------------------------------------------------------------------------------#

def drawGameWindow():
    _l_(399288)


    _c_(399268, _a_(399266, _n_(399265, "win", lambda: win), "fill"), _n_(399267, "bg", lambda: bg))
    _l_(399269)
    _c_(399277, _a_(399271, _n_(399270, "win", lambda: win), "blit"), _n_(399272, "player_sprite", lambda: player_sprite), _a_(399274, _n_(399273, "player", lambda: player), "x_position"), _a_(399276, _n_(399275, "player", lambda: player), "y_position"))
    _l_(399278)
    _c_(399281, _a_(399280, _n_(399279, "Clock", lambda: Clock), "tick"), 60)
    _l_(399282)
    _c_(399286, _a_(399285, _a_(399284, _n_(399283, "pygame", lambda: pygame), "display"), "update"))
    _l_(399287)

def jump():
    _l_(399306)


    jumpCount = 1
    _l_(399289)
    while _n_(399290, "jumpCount", lambda: jumpCount) <= _a_(399292, _n_(399291, "entity", lambda: entity), "height") * 1.5:
        _l_(399297)

        _n_(399293, "entity", lambda: entity).y_position += _n_(399294, "jumpCount", lambda: jumpCount)
        _l_(399295)
        jumpCount += 1
        _l_(399296)
    while _n_(399298, "jumpCount", lambda: jumpCount) >= _a_(399300, _n_(399299, "entity", lambda: entity), "height") * 1.5:
        _l_(399305)

        _n_(399301, "entity", lambda: entity).y_position -= _n_(399302, "jumpCount", lambda: jumpCount)
        _l_(399303)
        jumpCount -= 1
        _l_(399304)

# Main Loop------------------------------------------------------------------------------------------------------------#

while not _n_(399307, "gameExit", lambda: gameExit):
    _l_(399358)


    for event in _c_(399311, _a_(399310, _a_(399309, _n_(399308, "pygame", lambda: pygame), "event"), "get")):
        _l_(399354)

        if _a_(399313, _n_(399312, "event", lambda: event), "type") == _a_(399315, _n_(399314, "pygame", lambda: pygame), "QUIT"):
            _l_(399317)

            gameExit = True
            _l_(399316)
        if _a_(399319, _n_(399318, "event", lambda: event), "type") == _a_(399321, _n_(399320, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(399353)

            if _n_(399322, "event", lambda: event) == _a_(399324, _n_(399323, "pygame", lambda: pygame), "k_RIGHT") or _n_(399325, "event", lambda: event) == _a_(399327, _n_(399326, "pygame", lambda: pygame), "k_D"):
                _l_(399330)

                _n_(399328, "player", lambda: player).x_position += 5
                _l_(399329)
            if _n_(399331, "event", lambda: event) == _a_(399333, _n_(399332, "pygame", lambda: pygame), "k_LEFT") or _n_(399334, "event", lambda: event) == _a_(399336, _n_(399335, "pygame", lambda: pygame), "k_A"):
                _l_(399339)

                _n_(399337, "player", lambda: player).x_position -= 5
                _l_(399338)
            while not _n_(399340, "isJump", lambda: isJump):
                _l_(399352)

                if _n_(399341, "event", lambda: event) == _a_(399343, _n_(399342, "pygame", lambda: pygame), "k_up") or _n_(399344, "event", lambda: event) == _a_(399346, _n_(399345, "pygame", lambda: pygame), "k_SPACE"):
                    _l_(399351)

                    _c_(399349, _n_(399347, "jump", lambda: jump), _n_(399348, "player", lambda: player))
                    _l_(399350)

    _c_(399356, _n_(399355, "drawGameWindow", lambda: drawGameWindow))
    _l_(399357)

_c_(399361, _a_(399360, _n_(399359, "pygame", lambda: pygame), "quit"))
_l_(399362)
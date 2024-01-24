# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58145276/typeerror-getting-too-many-positional-arguments-when-there-are-only-supposed-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(391152)

except ImportError:
    pass
try:
    import random
    _l_(391154)

except ImportError:
    pass
try:
    import math
    _l_(391156)

except ImportError:
    pass
try:
    import os
    _l_(391158)

except ImportError:
    pass
try:
    import time
    _l_(391160)

except ImportError:
    pass
try:
    import sys
    _l_(391162)

except ImportError:
    pass
try:
    from os import path
    _l_(391164)

except ImportError:
    pass
try:
    from newsettings import *
    _l_(391166)

except ImportError:
    pass
try:
    from spritesdata import *
    _l_(391168)

except ImportError:
    pass
class Game:
    _l_(391635)

    def __init__(self):
        _l_(391257)

        _c_(391171, _a_(391170, _n_(391169, "pygame", lambda: pygame), "init"))
        _l_(391172)
        _n_(391173, "self", lambda: self).clock = _c_(391177, _a_(391176, _a_(391175, _n_(391174, "pygame", lambda: pygame), "time"), "Clock"))
        _l_(391178)
        _n_(391179, "self", lambda: self).screen = _c_(391185, _a_(391182, _a_(391181, _n_(391180, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(391183, "WIDTH", lambda: WIDTH), _n_(391184, "HEIGHT", lambda: HEIGHT)))
        _l_(391186)
        _c_(391191, _a_(391189, _a_(391188, _n_(391187, "pygame", lambda: pygame), "display"), "set_caption"), _n_(391190, "TITLE", lambda: TITLE))
        _l_(391192)
        _n_(391193, "self", lambda: self).time = _c_(391197, _a_(391196, _a_(391195, _n_(391194, "pygame", lambda: pygame), "time"), "get_ticks"))
        _l_(391198)
        _c_(391202, _a_(391201, _a_(391200, _n_(391199, "pygame", lambda: pygame), "key"), "set_repeat"), 500, 100)
        _l_(391203)
        _n_(391204, "self", lambda: self).all_sprites = _c_(391208, _a_(391207, _a_(391206, _n_(391205, "pygame", lambda: pygame), "sprite"), "Group"))
        _l_(391209)
        _n_(391210, "self", lambda: self).console = _c_(391213, _n_(391211, "Console", lambda: Console), _n_(391212, "self", lambda: self), 0)
        _l_(391214)
        _n_(391215, "self", lambda: self).player = _c_(391218, _n_(391216, "Player", lambda: Player), _n_(391217, "self", lambda: self), 390, 595)
        _l_(391219)
        _n_(391220, "self", lambda: self).work = _c_(391223, _n_(391221, "Work", lambda: Work), _n_(391222, "self", lambda: self), 450, 250)
        _l_(391224)
        _n_(391225, "self", lambda: self).food_station = _c_(391228, _n_(391226, "Food_Station", lambda: Food_Station), _n_(391227, "self", lambda: self), 750, 200)
        _l_(391229)
        _n_(391230, "self", lambda: self).food = _c_(391233, _n_(391231, "Food", lambda: Food), _n_(391232, "self", lambda: self), 0, 10)
        _l_(391234)
        _n_(391235, "self", lambda: self).education = _c_(391238, _n_(391236, "Education", lambda: Education), _n_(391237, "self", lambda: self), 300, 10)
        _l_(391239)
        _n_(391240, "self", lambda: self).school = _c_(391243, _n_(391241, "School", lambda: School), _n_(391242, "self", lambda: self), 100, 200)
        _l_(391244)
        _n_(391245, "self", lambda: self).family = _c_(391248, _n_(391246, "Family", lambda: Family), _n_(391247, "self", lambda: self), 600, 10)
        _l_(391249)
        _n_(391250, "self", lambda: self).money = _c_(391253, _n_(391251, "Money", lambda: Money), _n_(391252, "self", lambda: self), 850, 15)
        _l_(391254)
        _n_(391255, "self", lambda: self).food_bar = 100
        _l_(391256)
    def run(self):
        _l_(391286)

        _n_(391258, "self", lambda: self).playing = True
        _l_(391259)
        while _a_(391261, _n_(391260, "self", lambda: self), "playing"):
            _l_(391285)

            _n_(391262, "self", lambda: self).dt = _c_(391267, _a_(391265, _a_(391264, _n_(391263, "self", lambda: self), "clock"), "tick"), _n_(391266, "FPS", lambda: FPS)) / 1000
            _l_(391268)
            _c_(391271, _a_(391270, _n_(391269, "self", lambda: self), "hunger"))
            _l_(391272)
            _c_(391275, _a_(391274, _n_(391273, "self", lambda: self), "events"))
            _l_(391276)
            _c_(391279, _a_(391278, _n_(391277, "self", lambda: self), "update"))
            _l_(391280)
            _c_(391283, _a_(391282, _n_(391281, "self", lambda: self), "draw"))
            _l_(391284)
    def hunger(self):
        _l_(391296)

        HUNGEREVENT = _a_(391288, _n_(391287, "pygame", lambda: pygame), "USEREVENT") + 1
        _l_(391289)
        _c_(391294, _a_(391292, _a_(391291, _n_(391290, "pygame", lambda: pygame), "time"), "set_timer"), _n_(391293, "HUNGEREVENT", lambda: HUNGEREVENT), 10000)
        _l_(391295)
    def food_food(self, x, y, cool):
        _l_(391337)

        if _n_(391297, "cool", lambda: cool) < 0:
            _l_(391299)

            cool = 0
            _l_(391298)
        BAR_LENGTH = 100
        _l_(391300)
        BAR_HEIGHT = 10
        _l_(391301)
        fill = (_n_(391302, "cool", lambda: cool) / 100) * _n_(391303, "BAR_LENGTH", lambda: BAR_LENGTH)
        _l_(391304)
        outline_rect = _c_(391311, _a_(391306, _n_(391305, "pygame", lambda: pygame), "Rect"), _n_(391307, "x", lambda: x), _n_(391308, "y", lambda: y), _n_(391309, "BAR_LENGTH", lambda: BAR_LENGTH), _n_(391310, "BAR_HEIGHT", lambda: BAR_HEIGHT))
        _l_(391312)
        fill_rect = _c_(391319, _a_(391314, _n_(391313, "pygame", lambda: pygame), "Rect"), _n_(391315, "x", lambda: x), _n_(391316, "y", lambda: y), _n_(391317, "fill", lambda: fill), _n_(391318, "BAR_HEIGHT", lambda: BAR_HEIGHT))
        _l_(391320)
        _c_(391327, _a_(391323, _a_(391322, _n_(391321, "pygame", lambda: pygame), "draw"), "rect"), _n_(391324, "self", lambda: self), _n_(391325, "GREEN", lambda: GREEN), _n_(391326, "fill_rect", lambda: fill_rect))
        _l_(391328)
        _c_(391335, _a_(391331, _a_(391330, _n_(391329, "pygame", lambda: pygame), "draw"), "rect"), _n_(391332, "self", lambda: self), _n_(391333, "WHITE", lambda: WHITE), _n_(391334, "outline_rect", lambda: outline_rect), 2)
        _l_(391336)
    def quit(self):
        _l_(391346)

        _c_(391340, _a_(391339, _n_(391338, "pygame", lambda: pygame), "quit"))
        _l_(391341)
        _c_(391344, _a_(391343, _n_(391342, "sys", lambda: sys), "exit"))
        _l_(391345)
    def update(self):
        _l_(391352)

        _c_(391350, _a_(391349, _a_(391348, _n_(391347, "self", lambda: self), "all_sprites"), "update"))
        _l_(391351)
    def draw(self):
        _l_(391458)

        _c_(391357, _a_(391355, _a_(391354, _n_(391353, "self", lambda: self), "screen"), "fill"), _n_(391356, "BGCOLOR", lambda: BGCOLOR))
        _l_(391358)
        _c_(391364, _a_(391361, _a_(391360, _n_(391359, "self", lambda: self), "all_sprites"), "draw"), _a_(391363, _n_(391362, "self", lambda: self), "screen"))
        _l_(391365)
        font = _c_(391369, _a_(391368, _a_(391367, _n_(391366, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 15, True, False)
        _l_(391370)
        _c_(391376, _a_(391372, _n_(391371, "self", lambda: self), "food_food"), _n_(391373, "screen", lambda: screen), 5, 5, _a_(391375, _n_(391374, "self", lambda: self), "food_bar"))
        _l_(391377)
        text = _c_(391381, _a_(391379, _n_(391378, "font", lambda: font), "render"), "Number of days:" , True, _n_(391380, "BLACK", lambda: BLACK))
        _l_(391382)
        _c_(391386, _a_(391384, _n_(391383, "screen", lambda: screen), "blit"), _n_(391385, "text", lambda: text), [0, 110])
        _l_(391387)
        font = _c_(391391, _a_(391390, _a_(391389, _n_(391388, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391392)
        text = _c_(391396, _a_(391394, _n_(391393, "font", lambda: font), "render"), "=" , True, _n_(391395, "BLACK", lambda: BLACK))
        _l_(391397)
        _c_(391401, _a_(391399, _n_(391398, "screen", lambda: screen), "blit"), _n_(391400, "text", lambda: text), [120, 40])
        _l_(391402)
        font = _c_(391406, _a_(391405, _a_(391404, _n_(391403, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391407)
        text = _c_(391411, _a_(391409, _n_(391408, "font", lambda: font), "render"), "=" , True, _n_(391410, "BLACK", lambda: BLACK))
        _l_(391412)
        _c_(391416, _a_(391414, _n_(391413, "screen", lambda: screen), "blit"), _n_(391415, "text", lambda: text), [400, 40])
        _l_(391417)
        font = _c_(391421, _a_(391420, _a_(391419, _n_(391418, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391422)
        text = _c_(391426, _a_(391424, _n_(391423, "font", lambda: font), "render"), "=" , True, _n_(391425, "BLACK", lambda: BLACK))
        _l_(391427)
        _c_(391431, _a_(391429, _n_(391428, "screen", lambda: screen), "blit"), _n_(391430, "text", lambda: text), [700, 40])
        _l_(391432)
        font = _c_(391436, _a_(391435, _a_(391434, _n_(391433, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391437)
        text = _c_(391441, _a_(391439, _n_(391438, "font", lambda: font), "render"), "=" , True, _n_(391440, "BLACK", lambda: BLACK))
        _l_(391442)
        _c_(391446, _a_(391444, _n_(391443, "screen", lambda: screen), "blit"), _n_(391445, "text", lambda: text), [950, 40])
        _l_(391447)
        _c_(391451, _a_(391450, _a_(391449, _n_(391448, "self", lambda: self), "all_sprites"), "update"))
        _l_(391452)
        _c_(391456, _a_(391455, _a_(391454, _n_(391453, "pygame", lambda: pygame), "display"), "flip"))
        _l_(391457)
    def events(self):
        _l_(391501)

        # catch all events here
        HUNGEREVENT = _a_(391460, _n_(391459, "pygame", lambda: pygame), "USEREVENT") + 1
        _l_(391461)
        _c_(391466, _a_(391464, _a_(391463, _n_(391462, "pygame", lambda: pygame), "time"), "set_timer"), _n_(391465, "HUNGEREVENT", lambda: HUNGEREVENT), 10000)
        _l_(391467)
        if _c_(391472, _a_(391470, _a_(391469, _n_(391468, "pygame", lambda: pygame), "event"), "get"), _n_(391471, "HUNGEREVENT", lambda: HUNGEREVENT)):
            _l_(391477)

            _n_(391473, "self", lambda: self).food_bar = _a_(391475, _n_(391474, "self", lambda: self), "food_bar") - 10
            _l_(391476)
        for event in _c_(391481, _a_(391480, _a_(391479, _n_(391478, "pygame", lambda: pygame), "event"), "get")):
            _l_(391500)

            if _a_(391483, _n_(391482, "event", lambda: event), "type") == _a_(391485, _n_(391484, "pygame", lambda: pygame), "QUIT"):
                _l_(391499)

                _c_(391488, _a_(391487, _n_(391486, "self", lambda: self), "quit"))
                _l_(391489)
                if _a_(391491, _n_(391490, "event", lambda: event), "key") == _a_(391493, _n_(391492, "pygame", lambda: pygame), "K_ESCAPE"):
                    _l_(391498)

                    _c_(391496, _a_(391495, _n_(391494, "self", lambda: self), "quit"))
                    _l_(391497)
    def end_screen(self):
        _l_(391634)

        _c_(391505, _a_(391503, _n_(391502, "screen", lambda: screen), "fill"), _n_(391504, "BLUE", lambda: BLUE))
        _l_(391506)
        font = _c_(391510, _a_(391509, _a_(391508, _n_(391507, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391511)
        text = _c_(391515, _a_(391513, _n_(391512, "font", lambda: font), "render"), "Life Simulator V2" , True, _n_(391514, "WHITE", lambda: WHITE))
        _l_(391516)
        _c_(391520, _a_(391518, _n_(391517, "screen", lambda: screen), "blit"), _n_(391519, "text", lambda: text), [400, 100])
        _l_(391521)
        font = _c_(391525, _a_(391524, _a_(391523, _n_(391522, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391526)
        text = _c_(391530, _a_(391528, _n_(391527, "font", lambda: font), "render"), "Controls: F for food, E for education, W for work", True, _n_(391529, "WHITE", lambda: WHITE))
        _l_(391531)
        _c_(391535, _a_(391533, _n_(391532, "screen", lambda: screen), "blit"), _n_(391534, "text", lambda: text), [175, 250])
        _l_(391536)
        font = _c_(391540, _a_(391539, _a_(391538, _n_(391537, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391541)
        text = _c_(391545, _a_(391543, _n_(391542, "font", lambda: font), "render"), "Hard mode: h    Easy mode: e    Normal mode: m", True, _n_(391544, "WHITE", lambda: WHITE))
        _l_(391546)
        _c_(391550, _a_(391548, _n_(391547, "screen", lambda: screen), "blit"), _n_(391549, "text", lambda: text), [175, 400])
        _l_(391551)
        font = _c_(391555, _a_(391554, _a_(391553, _n_(391552, "pygame", lambda: pygame), "font"), "SysFont"), 'Arial', 30, True, False)
        _l_(391556)
        text = _c_(391560, _a_(391558, _n_(391557, "font", lambda: font), "render"), "Start by pressing a key corresponding to that mode", True, _n_(391559, "WHITE", lambda: WHITE))
        _l_(391561)
        _c_(391565, _a_(391563, _n_(391562, "screen", lambda: screen), "blit"), _n_(391564, "text", lambda: text), [150, 600])
        _l_(391566)
        _c_(391570, _a_(391569, _a_(391568, _n_(391567, "pygame", lambda: pygame), "display"), "flip"))
        _l_(391571)
        waiting = True
        _l_(391572)
        while _n_(391573, "waiting", lambda: waiting):
            _l_(391633)

            _c_(391576, _a_(391575, _n_(391574, "pygame", lambda: pygame), "init"))
            _l_(391577)
            clock = _c_(391581, _a_(391580, _a_(391579, _n_(391578, "pygame", lambda: pygame), "time"), "Clock"))
            _l_(391582)
            _c_(391585, _a_(391584, _n_(391583, "clock", lambda: clock), "tick"), 60)
            _l_(391586)
            for event in _c_(391590, _a_(391589, _a_(391588, _n_(391587, "pygame", lambda: pygame), "event"), "get")):
                _l_(391632)

                if _a_(391592, _n_(391591, "event", lambda: event), "type") == _a_(391594, _n_(391593, "pygame", lambda: pygame), "QUIT"):
                    _l_(391599)

                    _c_(391597, _a_(391596, _n_(391595, "sys", lambda: sys), "exit"))
                    _l_(391598)
                if _a_(391601, _n_(391600, "event", lambda: event), "type") == _a_(391603, _n_(391602, "pygame", lambda: pygame), "KEYDOWN"):
                    _l_(391631)

                    if _a_(391605, _n_(391604, "event", lambda: event), "key") == _a_(391607, _n_(391606, "pygame", lambda: pygame), "K_h"):
                        _l_(391612)

                        waiting = False
                        _l_(391608)
                        initial_money = 50
                        _l_(391609)
                        _n_(391610, "self", lambda: self).food_bar = 100
                        _l_(391611)
                    if _a_(391614, _n_(391613, "event", lambda: event), "key") == _a_(391616, _n_(391615, "pygame", lambda: pygame), "K_m"):
                        _l_(391621)

                        waiting = False
                        _l_(391617)
                        initial_money = 100
                        _l_(391618)
                        _n_(391619, "self", lambda: self).food_bar = 100
                        _l_(391620)
                    if _a_(391623, _n_(391622, "event", lambda: event), "key") == _a_(391625, _n_(391624, "pygame", lambda: pygame), "K_e"):
                        _l_(391630)

                        waiting = False
                        _l_(391626)
                        initial_money = 200
                        _l_(391627)
                        _n_(391628, "self", lambda: self).food_bar = 100
                        _l_(391629)
g = _c_(391637, _n_(391636, "Game", lambda: Game))
_l_(391638)
_c_(391641, _a_(391640, _n_(391639, "g", lambda: g), "end_screen"))
_l_(391642)
_c_(391645, _a_(391644, _n_(391643, "g", lambda: g), "run"))
_l_(391646)
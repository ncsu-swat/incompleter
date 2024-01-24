# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77336211/typeerror-invalid-rect-assignment-with-vectors
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(601286)

except ImportError:
    pass
try:
    import os
    _l_(601288)

except ImportError:
    pass
try:
    import random
    _l_(601290)

except ImportError:
    pass

vec = _a_(601293, _a_(601292, _n_(601291, "pygame", lambda: pygame), "math"), "Vector2")
_l_(601294)

WIDTH, HEIGHT = 640, 480
_l_(601295)
WIN = _c_(601301, _a_(601298, _a_(601297, _n_(601296, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(601299, "WIDTH", lambda: WIDTH), _n_(601300, "HEIGHT", lambda: HEIGHT)))
_l_(601302)
_c_(601306, _a_(601305, _a_(601304, _n_(601303, "pygame", lambda: pygame), "display"), "set_caption"), "PongX")
_l_(601307)

WHITE = (255, 255, 255)
_l_(601308)
BLACK = (0, 0, 0)
_l_(601309)
RED = ()
_l_(601310)

FPS = 60
_l_(601311)
VEL = 5
_l_(601312)
ball_vel = 1
_l_(601313)

PONG_WIDTH, PONG_HEIGHT = 30, 10
_l_(601314)
LEFT_PONG_IMAGE = _c_(601322, _a_(601317, _a_(601316, _n_(601315, "pygame", lambda: pygame), "image"), "load"), _c_(601321, _a_(601320, _a_(601319, _n_(601318, "os", lambda: os), "path"), "join"), "Pong", "Pong.png"))
_l_(601323)
RIGHT_PONG_IMAGE = _c_(601331, _a_(601326, _a_(601325, _n_(601324, "pygame", lambda: pygame), "image"), "load"), _c_(601330, _a_(601329, _a_(601328, _n_(601327, "os", lambda: os), "path"), "join"), "Pong", "Pong.png"))
_l_(601332)
BALL_WIDTH, BALL_HEIGHT = 10, 10
_l_(601333)
PONG_BALL_IMAGE = _c_(601341, _a_(601336, _a_(601335, _n_(601334, "pygame", lambda: pygame), "image"), "load"), _c_(601340, _a_(601339, _a_(601338, _n_(601337, "os", lambda: os), "path"), "join"), "Pong", "Pong_Ball.png"))
_l_(601342)


UP_BORDER = _c_(601345, _a_(601344, _n_(601343, "pygame", lambda: pygame), "Rect"), 0, 640, -2, 2)
_l_(601346)
DOWN_BORDER = _c_(601349, _a_(601348, _n_(601347, "pygame", lambda: pygame), "Rect"), 0, 640, 478, 482)
_l_(601350)

def draw_window(left, right, ball):
    _l_(601404)

    _c_(601354, _a_(601352, _n_(601351, "WIN", lambda: WIN), "fill"), _n_(601353, "BLACK", lambda: BLACK))
    _l_(601355)
    _c_(601362, _a_(601358, _a_(601357, _n_(601356, "pygame", lambda: pygame), "draw"), "rect"), _n_(601359, "WIN", lambda: WIN), _n_(601360, "WHITE", lambda: WHITE), _n_(601361, "UP_BORDER", lambda: UP_BORDER))
    _l_(601363)
    _c_(601370, _a_(601366, _a_(601365, _n_(601364, "pygame", lambda: pygame), "draw"), "rect"), _n_(601367, "WIN", lambda: WIN), _n_(601368, "WHITE", lambda: WHITE), _n_(601369, "DOWN_BORDER", lambda: DOWN_BORDER))
    _l_(601371)
    _c_(601379, _a_(601373, _n_(601372, "WIN", lambda: WIN), "blit"), _n_(601374, "PONG_BALL_IMAGE", lambda: PONG_BALL_IMAGE), (_a_(601376, _n_(601375, "ball", lambda: ball), "x"), _a_(601378, _n_(601377, "ball", lambda: ball), "y")))
    _l_(601380)
    _c_(601388, _a_(601382, _n_(601381, "WIN", lambda: WIN), "blit"), _n_(601383, "LEFT_PONG_IMAGE", lambda: LEFT_PONG_IMAGE), (_a_(601385, _n_(601384, "left", lambda: left), "x"), _a_(601387, _n_(601386, "left", lambda: left), "y")))
    _l_(601389)
    _c_(601397, _a_(601391, _n_(601390, "WIN", lambda: WIN), "blit"), _n_(601392, "RIGHT_PONG_IMAGE", lambda: RIGHT_PONG_IMAGE), (_a_(601394, _n_(601393, "right", lambda: right), "x"), _a_(601396, _n_(601395, "right", lambda: right), "y")))
    _l_(601398)
    _c_(601402, _a_(601401, _a_(601400, _n_(601399, "pygame", lambda: pygame), "display"), "update"))
    _l_(601403)

def ball_handle_movement(ball):
    _l_(601431)

    if _a_(601406, _n_(601405, "ball", lambda: ball), "y") == 0 or 480:
        _l_(601417)

        _n_(601407, "ball", lambda: ball).y = _c_(601415, _n_(601408, "vec", lambda: vec), _c_(601411, _a_(601410, _n_(601409, "random", lambda: random), "randint"), 0, 480), _c_(601414, _a_(601413, _n_(601412, "random", lambda: random), "randint"), 0, 480))
        _l_(601416)
    if _a_(601419, _n_(601418, "ball", lambda: ball), "x") == 0 or 640:
        _l_(601430)

        _n_(601420, "ball", lambda: ball).x = _c_(601428, _n_(601421, "vec", lambda: vec), _c_(601424, _a_(601423, _n_(601422, "random", lambda: random), "randint"), 0, 640), _c_(601427, _a_(601426, _n_(601425, "random", lambda: random), "randint"), 0, 640))
        _l_(601429)


def left_handle_movement(keys_pressed, left):
    _l_(601455)

    if _n_(601432, "keys_pressed", lambda: keys_pressed)[_a_(601434, _n_(601433, "pygame", lambda: pygame), "K_w")] and _a_(601436, _n_(601435, "left", lambda: left), "y") - _n_(601437, "VEL", lambda: VEL) > 0:
        _l_(601441)

        _n_(601438, "left", lambda: left).y -= _n_(601439, "VEL", lambda: VEL)
        _l_(601440)
    if _n_(601442, "keys_pressed", lambda: keys_pressed)[_a_(601444, _n_(601443, "pygame", lambda: pygame), "K_s")] and _a_(601446, _n_(601445, "left", lambda: left), "y") + _n_(601447, "VEL", lambda: VEL) + _a_(601449, _n_(601448, "left", lambda: left), "height") < _n_(601450, "HEIGHT", lambda: HEIGHT) - 15:
        _l_(601454)

        _n_(601451, "left", lambda: left).y += _n_(601452, "VEL", lambda: VEL)
        _l_(601453)

def right_handle_movement(keys_pressed, right):
    _l_(601479)

    if _n_(601456, "keys_pressed", lambda: keys_pressed)[_a_(601458, _n_(601457, "pygame", lambda: pygame), "K_UP")] and _a_(601460, _n_(601459, "right", lambda: right), "y") - _n_(601461, "VEL", lambda: VEL) > 0:
        _l_(601465)

        _n_(601462, "right", lambda: right).y -= _n_(601463, "VEL", lambda: VEL)
        _l_(601464)
    if _n_(601466, "keys_pressed", lambda: keys_pressed)[_a_(601468, _n_(601467, "pygame", lambda: pygame), "K_DOWN")] and _a_(601470, _n_(601469, "right", lambda: right), "y") + _n_(601471, "VEL", lambda: VEL) + _a_(601473, _n_(601472, "right", lambda: right), "height") < _n_(601474, "HEIGHT", lambda: HEIGHT) - 15:
        _l_(601478)

        _n_(601475, "right", lambda: right).y += _n_(601476, "VEL", lambda: VEL)
        _l_(601477)

def main():
    _l_(601553)

    left = _c_(601484, _a_(601481, _n_(601480, "pygame", lambda: pygame), "Rect"), 30, 210, _n_(601482, "PONG_WIDTH", lambda: PONG_WIDTH), _n_(601483, "PONG_HEIGHT", lambda: PONG_HEIGHT))
    _l_(601485)
    right = _c_(601490, _a_(601487, _n_(601486, "pygame", lambda: pygame), "Rect"), 600, 210, _n_(601488, "PONG_WIDTH", lambda: PONG_WIDTH), _n_(601489, "PONG_HEIGHT", lambda: PONG_HEIGHT))
    _l_(601491)
    ball = _c_(601498, _a_(601493, _n_(601492, "pygame", lambda: pygame), "Rect"), _n_(601494, "WIDTH", lambda: WIDTH)/2, _n_(601495, "HEIGHT", lambda: HEIGHT)/2 ,_n_(601496, "BALL_WIDTH", lambda: BALL_WIDTH), _n_(601497, "BALL_HEIGHT", lambda: BALL_HEIGHT))
    _l_(601499)

    clock = _c_(601503, _a_(601502, _a_(601501, _n_(601500, "pygame", lambda: pygame), "time"), "Clock"))
    _l_(601504)
    run = True
    _l_(601505)
    while _n_(601506, "run", lambda: run):
        _l_(601548)

        _c_(601510, _a_(601508, _n_(601507, "clock", lambda: clock), "tick"), _n_(601509, "FPS", lambda: FPS))
        _l_(601511)
        for event in _c_(601515, _a_(601514, _a_(601513, _n_(601512, "pygame", lambda: pygame), "event"), "get")):
            _l_(601522)

            if _a_(601517, _n_(601516, "event", lambda: event), "type") == _a_(601519, _n_(601518, "pygame", lambda: pygame), "QUIT"):
                _l_(601521)

                run = False
                _l_(601520)



        keys_pressed = _c_(601526, _a_(601525, _a_(601524, _n_(601523, "pygame", lambda: pygame), "key"), "get_pressed"))
        _l_(601527)
        _c_(601530, _n_(601528, "ball_handle_movement", lambda: ball_handle_movement), _n_(601529, "ball", lambda: ball))
        _l_(601531)
        _c_(601535, _n_(601532, "left_handle_movement", lambda: left_handle_movement), _n_(601533, "keys_pressed", lambda: keys_pressed), _n_(601534, "left", lambda: left))
        _l_(601536)
        _c_(601540, _n_(601537, "right_handle_movement", lambda: right_handle_movement), _n_(601538, "keys_pressed", lambda: keys_pressed), _n_(601539, "right", lambda: right))
        _l_(601541)
        _c_(601546, _n_(601542, "draw_window", lambda: draw_window), _n_(601543, "left", lambda: left), _n_(601544, "right", lambda: right), _n_(601545, "ball", lambda: ball))
        _l_(601547)

    _c_(601551, _a_(601550, _n_(601549, "pygame", lambda: pygame), "quit"))
    _l_(601552)

if _n_(601554, "__name__", lambda: __name__) == "__main__":
    _l_(601558)

    _c_(601556, _n_(601555, "main", lambda: main))
    _l_(601557)
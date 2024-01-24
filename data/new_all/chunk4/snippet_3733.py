# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68992982/attributeerror-list-object-has-no-attribute-x-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pgzrun
    _l_(641364)

except ImportError:
    pass
try:
    import random
    _l_(641366)

except ImportError:
    pass

FONT_COLOR = (255, 255, 255) #màu RGB
_l_(641367) #màu RGB
WIDTH = 1300
_l_(641368)
HEIGHT = 700
_l_(641369)
CENTER_X = _n_(641370, "WIDTH", lambda: WIDTH) / 2
_l_(641371)
CENTER_Y = _n_(641372, "HEIGHT", lambda: HEIGHT) / 2
_l_(641373)
CENTER = (_n_(641374, "CENTER_X", lambda: CENTER_X), _n_(641375, "CENTER_Y", lambda: CENTER_Y))
_l_(641376)
START_SPEED = 10
_l_(641377)
COLORS = ["orange", "blue"]
_l_(641378)
current_level = 1
_l_(641379)
final_level = 5
_l_(641380)
game_over = False
_l_(641381)
game_complete = False
_l_(641382)
impostors = []
_l_(641383)
animation = []
_l_(641384)

def draw():
    _l_(641410)

    global impostors,current_level,game_over,game_complete
    _l_(641385)
    _c_(641388, _a_(641387, _n_(641386, "screen", lambda: screen), "clear"))
    _l_(641389)
    _c_(641392, _a_(641391, _n_(641390, "screen", lambda: screen), "blit"), "dark",(0,0))
    _l_(641393)
    if _n_(641394, "game_over", lambda: game_over):
        _l_(641409)

        _c_(641396, _n_(641395, "display_message", lambda: display_message), "Game Over", "Press Space to play again")
        _l_(641397)
    elif _n_(641398, "game_complete", lambda: game_complete):
        _l_(641408)

        _c_(641400, _n_(641399, "display_message", lambda: display_message), "You win", "Press Space to play again")
        _l_(641401)
    else:
        for im in _n_(641402, "impostors", lambda: impostors):
            _l_(641407)

            _c_(641405, _a_(641404, _n_(641403, "im", lambda: im), "draw"))
            _l_(641406)

def update():
    _l_(641429)

    global impostors,current_level,game_over,game_complete
    _l_(641411)
    if _c_(641414, _n_(641412, "len", lambda: len), _n_(641413, "impostors", lambda: impostors)) == 0:
        _l_(641419)

        impostors = _c_(641417, _n_(641415, "make_impostors", lambda: make_impostors), _n_(641416, "current_level", lambda: current_level))
        _l_(641418)
    if (_n_(641420, "game_over", lambda: game_over) or _n_(641421, "game_complete", lambda: game_complete)) and _a_(641423, _n_(641422, "keyboard", lambda: keyboard), "space"):
        _l_(641428)

        impostors = []
        _l_(641424)
        current_level = 1
        _l_(641425)
        game_complete = False
        _l_(641426)
        game_over = False
        _l_(641427)

def make_impostors(number_of_impostors):
    _l_(641448)

    colors_to_create = _c_(641432, _n_(641430, "get_colors_to_create", lambda: get_colors_to_create), _n_(641431, "number_of_impostors", lambda: number_of_impostors))
    _l_(641433)
    new_impostors = _c_(641436, _n_(641434, "create_impostors", lambda: create_impostors), _n_(641435, "colors_to_create", lambda: colors_to_create))
    _l_(641437)
    _c_(641440, _n_(641438, "layout_impostors", lambda: layout_impostors), _n_(641439, "new_impostors", lambda: new_impostors))
    _l_(641441)
    _c_(641444, _n_(641442, "animate_impostors", lambda: animate_impostors), _n_(641443, "new_impostors", lambda: new_impostors))
    _l_(641445)
    aux = _n_(641446, "new_impostors", lambda: new_impostors)
    _l_(641447)
    return aux

def get_colors_to_create(number_of_impostors):
    _l_(641466)

    colors_to_create = ["red"]
    _l_(641449)
    for i in _c_(641452, _n_(641450, "range", lambda: range), 0,_n_(641451, "number_of_impostors", lambda: number_of_impostors)):
        _l_(641463)

        random_color = _c_(641456, _a_(641454, _n_(641453, "random", lambda: random), "choice"), _n_(641455, "COLORS", lambda: COLORS))
        _l_(641457)
        _c_(641461, _a_(641459, _n_(641458, "colors_to_create", lambda: colors_to_create), "append"), _n_(641460, "random_color", lambda: random_color))
        _l_(641462)
    aux = _n_(641464, "colors_to_create", lambda: colors_to_create)
    _l_(641465)
    return aux

def create_impostors(colors_to_create):
    _l_(641481)

    new_impostors = []
    _l_(641467)
    for color in _n_(641468, "colors_to_create", lambda: colors_to_create):
        _l_(641478)

        impostor = _c_(641471, _n_(641469, "Actor", lambda: Actor), _n_(641470, "color", lambda: color) + "-im")
        _l_(641472)
        _c_(641476, _a_(641474, _n_(641473, "new_impostors", lambda: new_impostors), "append"), _n_(641475, "impostors", lambda: impostors))
        _l_(641477)
    aux = _n_(641479, "new_impostors", lambda: new_impostors)
    _l_(641480)
    return aux

def layout_impostors(impostors_to_layout):
    _l_(641504)

    number_of_gaps = _c_(641484, _n_(641482, "len", lambda: len), _n_(641483, "impostors_to_layout", lambda: impostors_to_layout)) + 1
    _l_(641485)
    gap_size = _n_(641486, "WIDTH", lambda: WIDTH)/_n_(641487, "number_of_gaps", lambda: number_of_gaps)
    _l_(641488)
    _c_(641492, _a_(641490, _n_(641489, "random", lambda: random), "shuffle"), _n_(641491, "impostors_to_layout", lambda: impostors_to_layout))
    _l_(641493)
    for index, impostor in _c_(641496, _n_(641494, "enumerate", lambda: enumerate), _n_(641495, "impostors_to_layout", lambda: impostors_to_layout)):
        _l_(641503)

        new_x_pos = (_n_(641497, "index", lambda: index) + 1)*_n_(641498, "gap_size", lambda: gap_size)
        _l_(641499)
        _n_(641500, "impostor", lambda: impostor).x = _n_(641501, "new_x_pos", lambda: new_x_pos)
        _l_(641502)

def animation_impostors(impostors_to_animate):
    _l_(641524)

    for impostors in _n_(641505, "impostors_to_animate", lambda: impostors_to_animate):
        _l_(641523)

        duration = _n_(641506, "START_SPEED", lambda: START_SPEED) - _n_(641507, "current_level", lambda: current_level)
        _l_(641508)
        _n_(641509, "impostors", lambda: impostors).anchor = ("center", "bottom")
        _l_(641510)
        animation = _c_(641516, _n_(641511, "animation", lambda: animation), _n_(641512, "impostors", lambda: impostors), duration = _n_(641513, "duration", lambda: duration), on_finished = _n_(641514, "handle_game_over", lambda: handle_game_over), y = _n_(641515, "HEIGHT", lambda: HEIGHT))
        _l_(641517)
        _c_(641521, _a_(641519, _n_(641518, "animations", lambda: animations), "append"), _n_(641520, "animation", lambda: animation))
        _l_(641522)

def handle_game_over():
    _l_(641527)

    global game_over
    _l_(641525)
    game_over = True
    _l_(641526)

def on_mouse_down(pos):
    _l_(641545)

    global impostors, current_level
    _l_(641528)
    for impostors in _n_(641529, "impostors", lambda: impostors):
        _l_(641544)

        if _c_(641533, _a_(641531, _n_(641530, "impostors", lambda: impostors), "collidepoint"), _n_(641532, "pos", lambda: pos)):
            _l_(641543)

            if "red" in _a_(641535, _n_(641534, "impostors", lambda: impostors), "image"):
                _l_(641542)

                _c_(641537, _n_(641536, "red_impostor_click", lambda: red_impostor_click))
                _l_(641538)
            else:
                _c_(641540, _n_(641539, "handle_game_over", lambda: handle_game_over))
                _l_(641541)

def red_impostor_click():
    _l_(641559)

    global current_level, impostors, animation, game_complete
    _l_(641546)
    _c_(641549, _n_(641547, "stop_animations", lambda: stop_animations), _n_(641548, "animations", lambda: animations))
    _l_(641550)
    if _n_(641551, "current_level", lambda: current_level) == _n_(641552, "final_level", lambda: final_level):
        _l_(641558)

        game_complete = True
        _l_(641553)
    else:
        current_level = _n_(641554, "current_level", lambda: current_level) + 1
        _l_(641555)
        impostors = []
        _l_(641556)
        animations = []
        _l_(641557)

def stop_animations(animations_to_stop):
    _l_(641569)

    for animation in _n_(641560, "animations_to_stop", lambda: animations_to_stop):
        _l_(641568)

        if _a_(641562, _n_(641561, "animation", lambda: animation), "running"):
            _l_(641567)

            _c_(641565, _a_(641564, _n_(641563, "animation", lambda: animation), "stop"))
            _l_(641566)

def display_message(heading_text, sub_heading_text):
    _l_(641587)

    _c_(641576, _a_(641572, _a_(641571, _n_(641570, "screen", lambda: screen), "draw"), "text"), _n_(641573, "heading_text", lambda: heading_text), fontsize = 60, center = _n_(641574, "CENTER", lambda: CENTER), color = _n_(641575, "FONT_COLOR", lambda: FONT_COLOR))
    _l_(641577)
    _c_(641585, _a_(641580, _a_(641579, _n_(641578, "screen", lambda: screen), "draw"), "text"), _n_(641581, "sub_heading_text", lambda: sub_heading_text),
    fontsize = 30,
    center = (_n_(641582, "CENTER_X", lambda: CENTER_X), _n_(641583, "CENTER_Y", lambda: CENTER_Y) + 30),
    color = _n_(641584, "FONT_COLOR", lambda: FONT_COLOR))
    _l_(641586)

_c_(641590, _a_(641589, _n_(641588, "pgzrun", lambda: pgzrun), "go"))
_l_(641591)
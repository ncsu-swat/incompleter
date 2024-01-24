# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68992982/attributeerror-list-object-has-no-attribute-x-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pgzrun
    _l_(586127)

except ImportError:
    pass
try:
    import random
    _l_(586129)

except ImportError:
    pass

FONT_COLOR = (255, 255, 255) #màu RGB
_l_(586130) #màu RGB
WIDTH = 1300
_l_(586131)
HEIGHT = 700
_l_(586132)
CENTER_X = _n_(586133, "WIDTH", lambda: WIDTH) / 2
_l_(586134)
CENTER_Y = _n_(586135, "HEIGHT", lambda: HEIGHT) / 2
_l_(586136)
CENTER = (_n_(586137, "CENTER_X", lambda: CENTER_X), _n_(586138, "CENTER_Y", lambda: CENTER_Y))
_l_(586139)
START_SPEED = 10
_l_(586140)
COLORS = ["orange", "blue"]
_l_(586141)
current_level = 1
_l_(586142)
final_level = 5
_l_(586143)
game_over = False
_l_(586144)
game_complete = False
_l_(586145)
impostors = []
_l_(586146)
animation = []
_l_(586147)

def draw():
    _l_(586173)

    global impostors,current_level,game_over,game_complete
    _l_(586148)
    _c_(586151, _a_(586150, _n_(586149, "screen", lambda: screen), "clear"))
    _l_(586152)
    _c_(586155, _a_(586154, _n_(586153, "screen", lambda: screen), "blit"), "dark",(0,0))
    _l_(586156)
    if _n_(586157, "game_over", lambda: game_over):
        _l_(586172)

        _c_(586159, _n_(586158, "display_message", lambda: display_message), "Game Over", "Press Space to play again")
        _l_(586160)
    elif _n_(586161, "game_complete", lambda: game_complete):
        _l_(586171)

        _c_(586163, _n_(586162, "display_message", lambda: display_message), "You win", "Press Space to play again")
        _l_(586164)
    else:
        for im in _n_(586165, "impostors", lambda: impostors):
            _l_(586170)

            _c_(586168, _a_(586167, _n_(586166, "im", lambda: im), "draw"))
            _l_(586169)

def update():
    _l_(586192)

    global impostors,current_level,game_over,game_complete
    _l_(586174)
    if _c_(586177, _n_(586175, "len", lambda: len), _n_(586176, "impostors", lambda: impostors)) == 0:
        _l_(586182)

        impostors = _c_(586180, _n_(586178, "make_impostors", lambda: make_impostors), _n_(586179, "current_level", lambda: current_level))
        _l_(586181)
    if (_n_(586183, "game_over", lambda: game_over) or _n_(586184, "game_complete", lambda: game_complete)) and _a_(586186, _n_(586185, "keyboard", lambda: keyboard), "space"):
        _l_(586191)

        impostors = []
        _l_(586187)
        current_level = 1
        _l_(586188)
        game_complete = False
        _l_(586189)
        game_over = False
        _l_(586190)

def make_impostors(number_of_impostors):
    _l_(586211)

    colors_to_create = _c_(586195, _n_(586193, "get_colors_to_create", lambda: get_colors_to_create), _n_(586194, "number_of_impostors", lambda: number_of_impostors))
    _l_(586196)
    new_impostors = _c_(586199, _n_(586197, "create_impostors", lambda: create_impostors), _n_(586198, "colors_to_create", lambda: colors_to_create))
    _l_(586200)
    _c_(586203, _n_(586201, "layout_impostors", lambda: layout_impostors), _n_(586202, "new_impostors", lambda: new_impostors))
    _l_(586204)
    _c_(586207, _n_(586205, "animate_impostors", lambda: animate_impostors), _n_(586206, "new_impostors", lambda: new_impostors))
    _l_(586208)
    aux = _n_(586209, "new_impostors", lambda: new_impostors)
    _l_(586210)
    return aux

def get_colors_to_create(number_of_impostors):
    _l_(586229)

    colors_to_create = ["red"]
    _l_(586212)
    for i in _c_(586215, _n_(586213, "range", lambda: range), 0,_n_(586214, "number_of_impostors", lambda: number_of_impostors)):
        _l_(586226)

        random_color = _c_(586219, _a_(586217, _n_(586216, "random", lambda: random), "choice"), _n_(586218, "COLORS", lambda: COLORS))
        _l_(586220)
        _c_(586224, _a_(586222, _n_(586221, "colors_to_create", lambda: colors_to_create), "append"), _n_(586223, "random_color", lambda: random_color))
        _l_(586225)
    aux = _n_(586227, "colors_to_create", lambda: colors_to_create)
    _l_(586228)
    return aux

def create_impostors(colors_to_create):
    _l_(586244)

    new_impostors = []
    _l_(586230)
    for color in _n_(586231, "colors_to_create", lambda: colors_to_create):
        _l_(586241)

        impostor = _c_(586234, _n_(586232, "Actor", lambda: Actor), _n_(586233, "color", lambda: color) + "-im")
        _l_(586235)
        _c_(586239, _a_(586237, _n_(586236, "new_impostors", lambda: new_impostors), "append"), _n_(586238, "impostors", lambda: impostors))
        _l_(586240)
    aux = _n_(586242, "new_impostors", lambda: new_impostors)
    _l_(586243)
    return aux

def layout_impostors(impostors_to_layout):
    _l_(586267)

    number_of_gaps = _c_(586247, _n_(586245, "len", lambda: len), _n_(586246, "impostors_to_layout", lambda: impostors_to_layout)) + 1
    _l_(586248)
    gap_size = _n_(586249, "WIDTH", lambda: WIDTH)/_n_(586250, "number_of_gaps", lambda: number_of_gaps)
    _l_(586251)
    _c_(586255, _a_(586253, _n_(586252, "random", lambda: random), "shuffle"), _n_(586254, "impostors_to_layout", lambda: impostors_to_layout))
    _l_(586256)
    for index, impostor in _c_(586259, _n_(586257, "enumerate", lambda: enumerate), _n_(586258, "impostors_to_layout", lambda: impostors_to_layout)):
        _l_(586266)

        new_x_pos = (_n_(586260, "index", lambda: index) + 1)*_n_(586261, "gap_size", lambda: gap_size)
        _l_(586262)
        _n_(586263, "impostor", lambda: impostor).x = _n_(586264, "new_x_pos", lambda: new_x_pos)
        _l_(586265)

def animation_impostors(impostors_to_animate):
    _l_(586287)

    for impostors in _n_(586268, "impostors_to_animate", lambda: impostors_to_animate):
        _l_(586286)

        duration = _n_(586269, "START_SPEED", lambda: START_SPEED) - _n_(586270, "current_level", lambda: current_level)
        _l_(586271)
        _n_(586272, "impostors", lambda: impostors).anchor = ("center", "bottom")
        _l_(586273)
        animation = _c_(586279, _n_(586274, "animation", lambda: animation), _n_(586275, "impostors", lambda: impostors), duration = _n_(586276, "duration", lambda: duration), on_finished = _n_(586277, "handle_game_over", lambda: handle_game_over), y = _n_(586278, "HEIGHT", lambda: HEIGHT))
        _l_(586280)
        _c_(586284, _a_(586282, _n_(586281, "animations", lambda: animations), "append"), _n_(586283, "animation", lambda: animation))
        _l_(586285)

def handle_game_over():
    _l_(586290)

    global game_over
    _l_(586288)
    game_over = True
    _l_(586289)

def on_mouse_down(pos):
    _l_(586308)

    global impostors, current_level
    _l_(586291)
    for impostors in _n_(586292, "impostors", lambda: impostors):
        _l_(586307)

        if _c_(586296, _a_(586294, _n_(586293, "impostors", lambda: impostors), "collidepoint"), _n_(586295, "pos", lambda: pos)):
            _l_(586306)

            if "red" in _a_(586298, _n_(586297, "impostors", lambda: impostors), "image"):
                _l_(586305)

                _c_(586300, _n_(586299, "red_impostor_click", lambda: red_impostor_click))
                _l_(586301)
            else:
                _c_(586303, _n_(586302, "handle_game_over", lambda: handle_game_over))
                _l_(586304)

def red_impostor_click():
    _l_(586322)

    global current_level, impostors, animation, game_complete
    _l_(586309)
    _c_(586312, _n_(586310, "stop_animations", lambda: stop_animations), _n_(586311, "animations", lambda: animations))
    _l_(586313)
    if _n_(586314, "current_level", lambda: current_level) == _n_(586315, "final_level", lambda: final_level):
        _l_(586321)

        game_complete = True
        _l_(586316)
    else:
        current_level = _n_(586317, "current_level", lambda: current_level) + 1
        _l_(586318)
        impostors = []
        _l_(586319)
        animations = []
        _l_(586320)

def stop_animations(animations_to_stop):
    _l_(586332)

    for animation in _n_(586323, "animations_to_stop", lambda: animations_to_stop):
        _l_(586331)

        if _a_(586325, _n_(586324, "animation", lambda: animation), "running"):
            _l_(586330)

            _c_(586328, _a_(586327, _n_(586326, "animation", lambda: animation), "stop"))
            _l_(586329)

def display_message(heading_text, sub_heading_text):
    _l_(586350)

    _c_(586339, _a_(586335, _a_(586334, _n_(586333, "screen", lambda: screen), "draw"), "text"), _n_(586336, "heading_text", lambda: heading_text), fontsize = 60, center = _n_(586337, "CENTER", lambda: CENTER), color = _n_(586338, "FONT_COLOR", lambda: FONT_COLOR))
    _l_(586340)
    _c_(586348, _a_(586343, _a_(586342, _n_(586341, "screen", lambda: screen), "draw"), "text"), _n_(586344, "sub_heading_text", lambda: sub_heading_text),
    fontsize = 30,
    center = (_n_(586345, "CENTER_X", lambda: CENTER_X), _n_(586346, "CENTER_Y", lambda: CENTER_Y) + 30),
    color = _n_(586347, "FONT_COLOR", lambda: FONT_COLOR))
    _l_(586349)

_c_(586353, _a_(586352, _n_(586351, "pgzrun", lambda: pgzrun), "go"))
_l_(586354)
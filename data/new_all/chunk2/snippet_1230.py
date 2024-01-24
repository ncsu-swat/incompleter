# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70369987/typeerror-changespeed-takes-2-positional-arguments-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(456178)

except ImportError:
    pass
try:
    import random
    _l_(456180)

except ImportError:
    pass

#-------------------------BUGS I NEED TO FIX-------------------------#
#CANNOT MOVE CHARACTER


# Define some colors
BLACK = (0, 0, 0)
_l_(456181)
WHITE = (255, 255, 255)
_l_(456182)
RED = (255, 0, 0)
_l_(456183)
YELLOW = (255,255,0)
_l_(456184)
score = 0
_l_(456185)
play = 0
_l_(456186)
progress = 0
_l_(456187)
errorkey = 0
_l_(456188)
helpme = 0
_l_(456189)
score1 = 0
_l_(456190)

#stop = 0

def levelsetup():
    _l_(456264)

    _a_(456192, _n_(456191, "testman", lambda: testman), "rect").x = 0
    _l_(456193)
    _a_(456195, _n_(456194, "one", lambda: one), "rect").x = 460
    _l_(456196)
    _a_(456198, _n_(456197, "two", lambda: two), "rect").x = 530
    _l_(456199)
    _a_(456201, _n_(456200, "three", lambda: three), "rect").x = 615
    _l_(456202)
    _a_(456204, _n_(456203, "four", lambda: four), "rect").x = 700
    _l_(456205)
    for crate in _n_(456206, "crate_list", lambda: crate_list):
        _l_(456211)

        _a_(456208, _n_(456207, "crate", lambda: crate), "rect").x -= _n_(456209, "rect_x_change", lambda: rect_x_change)
        _l_(456210)
    _c_(456215, _a_(456213, _n_(456212, "screen", lambda: screen), "blit"), _n_(456214, "user_interface", lambda: user_interface), [0,0])
    _l_(456216)
    _c_(456220, _a_(456218, _n_(456217, "lvlselect", lambda: lvlselect), "draw"), _n_(456219, "screen", lambda: screen))
    _l_(456221)
    font = _c_(456225, _a_(456224, _a_(456223, _n_(456222, "pygame", lambda: pygame), "font"), "SysFont"), 'comicsansms', 65, True, False)
    _l_(456226)
    playscore = _c_(456233, _a_(456228, _n_(456227, "font", lambda: font), "render"), _c_(456231, _n_(456229, "str", lambda: str), _n_(456230, "score1", lambda: score1)), True, _n_(456232, "BLACK", lambda: BLACK))
    _l_(456234)
    playhealth = _c_(456242, _a_(456236, _n_(456235, "font", lambda: font), "render"), _c_(456240, _n_(456237, "str", lambda: str), _a_(456239, _n_(456238, "testman", lambda: testman), "health")), True, _n_(456241, "BLACK", lambda: BLACK))
    _l_(456243)
    _c_(456247, _a_(456245, _n_(456244, "screen", lambda: screen), "blit"), _n_(456246, "playhealth", lambda: playhealth), [30,392])
    _l_(456248)
    _c_(456252, _a_(456250, _n_(456249, "screen", lambda: screen), "blit"), _n_(456251, "playscore", lambda: playscore), [205,392])
    _l_(456253)
    _c_(456257, _a_(456255, _n_(456254, "playersprite", lambda: playersprite), "draw"), _n_(456256, "screen", lambda: screen))
    _l_(456258)
    _c_(456262, _a_(456260, _n_(456259, "crate_list", lambda: crate_list), "draw"), _n_(456261, "screen", lambda: screen))
    _l_(456263)

class Sprite(_a_(456267, _a_(456266, _n_(456265, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(456301)

    def __init__(self,filename):
        _l_(456300)

        _c_(456270, _a_(456269, _n_(456268, "super", lambda: super)(), "__init__"))
        _l_(456271)
        _n_(456272, "self", lambda: self).image = _c_(456279, _a_(456278, _c_(456277, _a_(456275, _a_(456274, _n_(456273, "pygame", lambda: pygame), "image"), "load"), _n_(456276, "filename", lambda: filename)), "convert"))
        _l_(456280)
        _c_(456285, _a_(456283, _a_(456282, _n_(456281, "self", lambda: self), "image"), "set_colorkey"), _n_(456284, "BLACK", lambda: BLACK))
        _l_(456286)
        _n_(456287, "self", lambda: self).rect = _c_(456291, _a_(456290, _a_(456289, _n_(456288, "self", lambda: self), "image"), "get_rect"))
        _l_(456292)
        _n_(456293, "self", lambda: self).health = 100
        _l_(456294)
        _a_(456296, _n_(456295, "self", lambda: self), "rect").x = 0
        _l_(456297)
        _n_(456298, "self", lambda: self).change_x = 0
        _l_(456299)
class Player(_n_(456302, "Sprite", lambda: Sprite)):
    _l_(456335)

    def update(self):
        _l_(456330)

 
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = _c_(456306, _a_(456305, _a_(456304, _n_(456303, "pygame", lambda: pygame), "mouse"), "get_pos"))
        _l_(456307)
 
        # Now see how the mouse position is different from the current
        # player position. (How far did we move?)
        diff_x = _a_(456310, _a_(456309, _n_(456308, "self", lambda: self), "rect"), "x") - _n_(456311, "pos", lambda: pos)[0]
        _l_(456312)
        diff_y = _a_(456315, _a_(456314, _n_(456313, "self", lambda: self), "rect"), "y") - _n_(456316, "pos", lambda: pos)[1]
        _l_(456317)
 
        # Loop through each block that we are carrying and adjust
        # it by the amount we moved.
        _a_(456319, _n_(456318, "self", lambda: self), "rect").x += _n_(456320, "self", lambda: self).change_x
        _l_(456321)
        
        # Now wet the player object to the mouse location
        _a_(456323, _n_(456322, "self", lambda: self), "rect").x = _n_(456324, "pos", lambda: pos)[0]
        _l_(456325)
        _a_(456327, _n_(456326, "self", lambda: self), "rect").y = _n_(456328, "pos", lambda: pos)[1]
        _l_(456329)
    def changespeed(self, x):
        _l_(456334)

        _n_(456331, "self", lambda: self).change_x += _n_(456332, "x", lambda: x)
        _l_(456333)
 
class Block(_a_(456338, _a_(456337, _n_(456336, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(456363)


    def __init__(self, color, width, height):
        _l_(456362)


        # Call the parent class (Sprite) constructor
        _c_(456341, _a_(456340, _n_(456339, "super", lambda: super)(), "__init__"))
        _l_(456342)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        _n_(456343, "self", lambda: self).image = _c_(456348, _a_(456345, _n_(456344, "pygame", lambda: pygame), "Surface"), [_n_(456346, "width", lambda: width), _n_(456347, "height", lambda: height)])
        _l_(456349)
        _c_(456354, _a_(456352, _a_(456351, _n_(456350, "self", lambda: self), "image"), "fill"), _n_(456353, "color", lambda: color))
        _l_(456355)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        _n_(456356, "self", lambda: self).rect = _c_(456360, _a_(456359, _a_(456358, _n_(456357, "self", lambda: self), "image"), "get_rect"))
        _l_(456361)

_c_(456367, _a_(456366, _a_(456365, _n_(456364, "pygame", lambda: pygame), "mixer"), "pre_init"), 44100, -16, 1, 512)
_l_(456368)
# Initialize Pygame
_c_(456371, _a_(456370, _n_(456369, "pygame", lambda: pygame), "init"))
_l_(456372)

# Set the height and width of the screen
screen_width = 750
_l_(456373)
screen_height = 500
_l_(456374)

screen = _c_(456380, _a_(456377, _a_(456376, _n_(456375, "pygame", lambda: pygame), "display"), "set_mode"), [_n_(456378, "screen_width", lambda: screen_width), _n_(456379, "screen_height", lambda: screen_height)])
_l_(456381)

_c_(456385, _a_(456384, _a_(456383, _n_(456382, "pygame", lambda: pygame), "display"), "set_caption"), "LARP")
_l_(456386)

item_crate = _c_(456392, _a_(456391, _c_(456390, _a_(456389, _a_(456388, _n_(456387, "pygame", lambda: pygame), "image"), "load"), "crate.png"), "convert_alpha"))
_l_(456393)
crate_list = _c_(456397, _a_(456396, _a_(456395, _n_(456394, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456398)


def blit_text(surface, text, pos, font, color=_c_(456401, _a_(456400, _n_(456399, "pygame", lambda: pygame), "Color"), 'WHITE')):
    _l_(456454)

    words = [_c_(456404, _a_(456403, _n_(456402, "word", lambda: word), "split"), ' ') for word in _c_(456407, _a_(456406, _n_(456405, "text", lambda: text), "splitlines"))]  # 2D array where each row is a list of words.
    _l_(456408)  # 2D array where each row is a list of words.
    space = _c_(456411, _a_(456410, _n_(456409, "font", lambda: font), "size"), ' ')[0]  # The width of a space.
    _l_(456412)  # The width of a space.
    max_width, max_height = _c_(456415, _a_(456414, _n_(456413, "surface", lambda: surface), "get_size"))
    _l_(456416)
    x, y = _n_(456417, "pos", lambda: pos)
    _l_(456418)
    for line in _n_(456419, "words", lambda: words):
        _l_(456453)

        for word in _n_(456420, "line", lambda: line):
            _l_(456449)

            word_surface = _c_(456425, _a_(456422, _n_(456421, "font", lambda: font), "render"), _n_(456423, "word", lambda: word), 0, _n_(456424, "color", lambda: color))
            _l_(456426)
            word_width, word_height = _c_(456429, _a_(456428, _n_(456427, "word_surface", lambda: word_surface), "get_size"))
            _l_(456430)
            if _n_(456431, "x", lambda: x) + _n_(456432, "word_width", lambda: word_width) >= _n_(456433, "max_width", lambda: max_width):
                _l_(456438)

                x = _n_(456434, "pos", lambda: pos)[0]  # Reset the x.
                _l_(456435)  # Reset the x.
                y += _n_(456436, "word_height", lambda: word_height)  # Start on new row.
                _l_(456437)  # Start on new row.
            _c_(456444, _a_(456440, _n_(456439, "surface", lambda: surface), "blit"), _n_(456441, "word_surface", lambda: word_surface), (_n_(456442, "x", lambda: x), _n_(456443, "y", lambda: y)))
            _l_(456445)
            x += _n_(456446, "word_width", lambda: word_width) + _n_(456447, "space", lambda: space)
            _l_(456448)
        x = 83
        _l_(456450)
        #y = 80# Reset the x.
        y += _n_(456451, "word_height", lambda: word_height)  # Start on new row.
        _l_(456452)  # Start on new row.

text = "\n\n\nUnless you're a teacher I have no clue how you got this game.\nBut that doesn't matter. After your character received a\nmysterious LARP invitation in the forest he finds that the\ndevious Wendyl has turned the LARP group into an\nauthoritarian regime! It's your job to stop Wendyl and anyone\nin your way!"
_l_(456455)
text2 = "\n\n\n\n\n\n\n\n\nLEFT ARROW KEY - MOVE LEFT\nRIGHT ARROW KEY - MOVE RIGHT\nCLICK MOUSE - FIRE WEAPON/SELECT OPTION\nMOVE MOUSE - CURSOR/AIMING"
_l_(456456)

font = _c_(456460, _a_(456459, _a_(456458, _n_(456457, "pygame", lambda: pygame), "font"), "SysFont"), 'comicsansms', 20)
_l_(456461)
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = _c_(456465, _a_(456464, _a_(456463, _n_(456462, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456466)
#TITLE SCREEN
title_image = _c_(456472, _a_(456471, _c_(456470, _a_(456469, _a_(456468, _n_(456467, "pygame", lambda: pygame), "image"), "load"), "title.png"), "convert_alpha"))
_l_(456473)
quit_image = _c_(456479, _a_(456478, _c_(456477, _a_(456476, _a_(456475, _n_(456474, "pygame", lambda: pygame), "image"), "load"), "quit.png"), "convert_alpha"))
_l_(456480)
logo_image = _c_(456486, _a_(456485, _c_(456484, _a_(456483, _a_(456482, _n_(456481, "pygame", lambda: pygame), "image"), "load"), "logo.png"), "convert_alpha"))
_l_(456487)
background_image = _c_(456493, _a_(456492, _c_(456491, _a_(456490, _a_(456489, _n_(456488, "pygame", lambda: pygame), "image"), "load"), "title_screen.png"), "convert_alpha"))
_l_(456494)
map_image = _c_(456500, _a_(456499, _c_(456498, _a_(456497, _a_(456496, _n_(456495, "pygame", lambda: pygame), "image"), "load"), "map.png"), "convert_alpha"))
_l_(456501)
quit_block = _c_(456505, _a_(456504, _a_(456503, _n_(456502, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456506)
start_block = _c_(456510, _a_(456509, _a_(456508, _n_(456507, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456511)
Title = _c_(456515, _a_(456514, _a_(456513, _n_(456512, "pygame", lambda: pygame), "mixer"), "Sound"), "title_song.ogg")
_l_(456516)
Map = _c_(456520, _a_(456519, _a_(456518, _n_(456517, "pygame", lambda: pygame), "mixer"), "Sound"), "map_song.ogg")
_l_(456521)
help_image = _c_(456527, _a_(456526, _c_(456525, _a_(456524, _a_(456523, _n_(456522, "pygame", lambda: pygame), "image"), "load"), "help.png"), "convert_alpha"))
_l_(456528)
help_title = _c_(456532, _a_(456531, _a_(456530, _n_(456529, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456533)



#PLAYER
player_image = _c_(456539, _a_(456538, _c_(456537, _a_(456536, _a_(456535, _n_(456534, "pygame", lambda: pygame), "image"), "load"), "player.png"), "convert_alpha"))
_l_(456540)
#testman = pygame.image.load("testman.png").convert_alpha()
testman = _c_(456542, _n_(456541, "Sprite", lambda: Sprite), "testman.png")
_l_(456543)
playersprite = _c_(456547, _a_(456546, _a_(456545, _n_(456544, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456548)
_c_(456552, _a_(456550, _n_(456549, "playersprite", lambda: playersprite), "add"), _n_(456551, "testman", lambda: testman))
_l_(456553)
_a_(456555, _n_(456554, "testman", lambda: testman), "rect").y = 230
_l_(456556)


#CUTSCENES
cutscene_2 = _c_(456562, _a_(456561, _c_(456560, _a_(456559, _a_(456558, _n_(456557, "pygame", lambda: pygame), "image"), "load"), "cutscene_2.png"), "convert_alpha"))
_l_(456563)
cutscene_1 = _c_(456569, _a_(456568, _c_(456567, _a_(456566, _a_(456565, _n_(456564, "pygame", lambda: pygame), "image"), "load"), "cutscene_1.png"), "convert_alpha"))
_l_(456570)
continue_button = _c_(456576, _a_(456575, _c_(456574, _a_(456573, _a_(456572, _n_(456571, "pygame", lambda: pygame), "image"), "load"), "cont.png"), "convert_alpha"))
_l_(456577)
continue_list = _c_(456581, _a_(456580, _a_(456579, _n_(456578, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456582)

#NUMBERS
one = _c_(456584, _n_(456583, "Sprite", lambda: Sprite), "one.png")
_l_(456585)
two = _c_(456587, _n_(456586, "Sprite", lambda: Sprite), "two.png")
_l_(456588)
three = _c_(456590, _n_(456589, "Sprite", lambda: Sprite), "three.png")
_l_(456591)
four = _c_(456593, _n_(456592, "Sprite", lambda: Sprite), "four.png")
_l_(456594)
butt_one = _c_(456598, _a_(456597, _a_(456596, _n_(456595, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456599)
butt_two = _c_(456603, _a_(456602, _a_(456601, _n_(456600, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456604)
butt_three = _c_(456608, _a_(456607, _a_(456606, _n_(456605, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456609)
butt_four = _c_(456613, _a_(456612, _a_(456611, _n_(456610, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456614)
lvlselect = _c_(456618, _a_(456617, _a_(456616, _n_(456615, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456619)

#OTHER
back_button = _c_(456625, _a_(456624, _c_(456623, _a_(456622, _a_(456621, _n_(456620, "pygame", lambda: pygame), "image"), "load"), "back.png"), "convert_alpha"))
_l_(456626)
back_butt = _c_(456630, _a_(456629, _a_(456628, _n_(456627, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456631)
stage_error = _c_(456637, _a_(456636, _c_(456635, _a_(456634, _a_(456633, _n_(456632, "pygame", lambda: pygame), "image"), "load"), "stage_progess_error.png"), "convert_alpha"))
_l_(456638)
stage_error = _c_(456642, _a_(456641, _a_(456640, _n_(456639, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456643)
programIcon = _c_(456647, _a_(456646, _a_(456645, _n_(456644, "pygame", lambda: pygame), "image"), "load"), 'imggg.png')
_l_(456648)

map_screen = _c_(456652, _a_(456651, _a_(456650, _n_(456649, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456653)

#STAGES
stage_one = _c_(456659, _a_(456658, _c_(456657, _a_(456656, _a_(456655, _n_(456654, "pygame", lambda: pygame), "image"), "load"), "level_1.png"), "convert_alpha"))
_l_(456660)
stage_one_music = _c_(456664, _a_(456663, _a_(456662, _n_(456661, "pygame", lambda: pygame), "mixer"), "Sound"), "stage_1.ogg")
_l_(456665)

#USER INTERFACE
user_interface = _c_(456671, _a_(456670, _c_(456669, _a_(456668, _a_(456667, _n_(456666, "pygame", lambda: pygame), "image"), "load"), "ui.png"), "convert_alpha"))
_l_(456672)

# This is a list of every sprite.
# All blocks and the player block as well.
player_list = _c_(456676, _a_(456675, _a_(456674, _n_(456673, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456677)
all_sprites_list = _c_(456681, _a_(456680, _a_(456679, _n_(456678, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(456682)
 

#TITLE SCREEN
title = _c_(456684, _n_(456683, "Sprite", lambda: Sprite), "title.png")
_l_(456685)
_a_(456687, _n_(456686, "title", lambda: title), "rect").x = 340
_l_(456688)
_a_(456690, _n_(456689, "title", lambda: title), "rect").y = 220
_l_(456691)
_c_(456695, _a_(456693, _n_(456692, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(456694, "title", lambda: title))
_l_(456696)
_c_(456700, _a_(456698, _n_(456697, "start_block", lambda: start_block), "add"), _n_(456699, "title", lambda: title))
_l_(456701)
quitg = _c_(456703, _n_(456702, "Sprite", lambda: Sprite), "quit.png")
_l_(456704)
_a_(456706, _n_(456705, "quitg", lambda: quitg), "rect").x = 340
_l_(456707)
_a_(456709, _n_(456708, "quitg", lambda: quitg), "rect").y = 360
_l_(456710)
_c_(456714, _a_(456712, _n_(456711, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(456713, "quitg", lambda: quitg))
_l_(456715)
_c_(456719, _a_(456717, _n_(456716, "quit_block", lambda: quit_block), "add"), _n_(456718, "quitg", lambda: quitg))
_l_(456720)
logo = _c_(456722, _n_(456721, "Sprite", lambda: Sprite), "logo.png")
_l_(456723)
_a_(456725, _n_(456724, "logo", lambda: logo), "rect").y = 100
_l_(456726)
_a_(456728, _n_(456727, "logo", lambda: logo), "rect").x = 317
_l_(456729)
_c_(456733, _a_(456731, _n_(456730, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(456732, "logo", lambda: logo))
_l_(456734)
_c_(456738, _a_(456736, _n_(456735, "block_list", lambda: block_list), "add"), _n_(456737, "logo", lambda: logo))
_l_(456739)
help_image = _c_(456741, _n_(456740, "Sprite", lambda: Sprite), "help.png")
_l_(456742)
_a_(456744, _n_(456743, "help_image", lambda: help_image), "rect").x = 340
_l_(456745)
_a_(456747, _n_(456746, "help_image", lambda: help_image), "rect").y = 290
_l_(456748)
_c_(456752, _a_(456750, _n_(456749, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(456751, "help_image", lambda: help_image))
_l_(456753)
_c_(456757, _a_(456755, _n_(456754, "help_title", lambda: help_title), "add"), _n_(456756, "help_image", lambda: help_image))
_l_(456758)

#CUTSCENE
continues = _c_(456760, _n_(456759, "Sprite", lambda: Sprite), "cont.png")
_l_(456761)
_a_(456763, _n_(456762, "continues", lambda: continues), "rect").x = 608
_l_(456764)
_a_(456766, _n_(456765, "continues", lambda: continues), "rect").y = 466
_l_(456767)
_c_(456771, _a_(456769, _n_(456768, "continue_list", lambda: continue_list), "add"), _n_(456770, "continues", lambda: continues))
_l_(456772)

#NUMBERS
one = _c_(456774, _n_(456773, "Sprite", lambda: Sprite), "one.png")
_l_(456775)
_c_(456779, _a_(456777, _n_(456776, "butt_one", lambda: butt_one), "add"), _n_(456778, "one", lambda: one))
_l_(456780)
_c_(456784, _a_(456782, _n_(456781, "butt_two", lambda: butt_two), "add"), _n_(456783, "two", lambda: two))
_l_(456785)
_c_(456789, _a_(456787, _n_(456786, "butt_three", lambda: butt_three), "add"), _n_(456788, "three", lambda: three))
_l_(456790)
_c_(456794, _a_(456792, _n_(456791, "butt_four", lambda: butt_four), "add"), _n_(456793, "four", lambda: four))
_l_(456795)
_c_(456799, _a_(456797, _n_(456796, "lvlselect", lambda: lvlselect), "add"), _n_(456798, "one", lambda: one))
_l_(456800)
_c_(456804, _a_(456802, _n_(456801, "lvlselect", lambda: lvlselect), "add"), _n_(456803, "two", lambda: two))
_l_(456805)
_c_(456809, _a_(456807, _n_(456806, "lvlselect", lambda: lvlselect), "add"), _n_(456808, "three", lambda: three))
_l_(456810)
_c_(456814, _a_(456812, _n_(456811, "lvlselect", lambda: lvlselect), "add"), _n_(456813, "four", lambda: four))
_l_(456815)

#OTHER
back = _c_(456817, _n_(456816, "Sprite", lambda: Sprite), "back.png")
_l_(456818)
_a_(456820, _n_(456819, "back", lambda: back), "rect").x = 0
_l_(456821)
_a_(456823, _n_(456822, "back", lambda: back), "rect").y = 12
_l_(456824)
_c_(456828, _a_(456826, _n_(456825, "back_butt", lambda: back_butt), "add"), _n_(456827, "back", lambda: back))
_l_(456829)
error = _c_(456831, _n_(456830, "Sprite", lambda: Sprite), "stage_progess_error.png")
_l_(456832)
_a_(456834, _n_(456833, "error", lambda: error), "rect").x = 100
_l_(456835)
_a_(456837, _n_(456836, "error", lambda: error), "rect").y = 85
_l_(456838)
_c_(456842, _a_(456840, _n_(456839, "stage_error", lambda: stage_error), "add"), _n_(456841, "error", lambda: error))
_l_(456843)

map_image = _c_(456845, _n_(456844, "Sprite", lambda: Sprite), "map.png")
_l_(456846)
_c_(456850, _a_(456848, _n_(456847, "map_screen", lambda: map_screen), "add"), _n_(456849, "map_image", lambda: map_image))
_l_(456851)
_c_(456856, _a_(456854, _a_(456853, _n_(456852, "pygame", lambda: pygame), "display"), "set_icon"), _n_(456855, "programIcon", lambda: programIcon))
_l_(456857)

#PLAYER
player = _c_(456859, _n_(456858, "Player", lambda: Player), "player.png")
_l_(456860)
_c_(456864, _a_(456862, _n_(456861, "player_list", lambda: player_list), "add"), _n_(456863, "player", lambda: player))
_l_(456865)
_c_(456869, _a_(456867, _n_(456866, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(456868, "player", lambda: player))
_l_(456870)



rect_x = 0
_l_(456871)
rect_x_change = 1.65
_l_(456872)
for i in _c_(456874, _n_(456873, "range", lambda: range), 5):
    _l_(456903)

    crate = _c_(456876, _n_(456875, "Sprite", lambda: Sprite), "crate.png")
    _l_(456877)
    cratex = _c_(456880, _a_(456879, _n_(456878, "random", lambda: random), "randint"), 2000,18000)
    _l_(456881)
    _a_(456883, _n_(456882, "crate", lambda: crate), "rect").x = _n_(456884, "cratex", lambda: cratex)
    _l_(456885)
    _a_(456887, _n_(456886, "crate", lambda: crate), "rect").y = 245
    _l_(456888)
    _c_(456892, _a_(456890, _n_(456889, "crate_list", lambda: crate_list), "add"), _n_(456891, "crate", lambda: crate))
    _l_(456893)
    _c_(456901, _n_(456894, "print", lambda: print), _a_(456897, _a_(456896, _n_(456895, "crate", lambda: crate), "rect"), "x"), _a_(456900, _a_(456899, _n_(456898, "crate", lambda: crate), "rect"), "y"))
    _l_(456902)
 
# Loop until the user clicks the close button.
done = False
_l_(456904)
 
# Used to manage how fast the screen updates
clock = _c_(456908, _a_(456907, _a_(456906, _n_(456905, "pygame", lambda: pygame), "time"), "Clock"))
_l_(456909)
 
# Hide the mouse cursor
_c_(456913, _a_(456912, _a_(456911, _n_(456910, "pygame", lambda: pygame), "mouse"), "set_visible"), False)
_l_(456914)

 
# -------- Main Program Loop -----------
while not _n_(456915, "done", lambda: done):
    _l_(457353)

    for event in _c_(456919, _a_(456918, _a_(456917, _n_(456916, "pygame", lambda: pygame), "event"), "get")):
        _l_(457126)

        if _a_(456921, _n_(456920, "event", lambda: event), "type") == _a_(456923, _n_(456922, "pygame", lambda: pygame), "QUIT"):
            _l_(457125)

            done = True
            _l_(456924)
 
        elif _a_(456926, _n_(456925, "event", lambda: event), "type") == _a_(456928, _n_(456927, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
            _l_(457124)

            if _n_(456929, "play", lambda: play) == 0:
                _l_(457100)

                help_block_hit = _c_(456935, _a_(456932, _a_(456931, _n_(456930, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(456933, "player", lambda: player), _n_(456934, "help_title", lambda: help_title), False)
                _l_(456936)
                if _c_(456939, _n_(456937, "len", lambda: len), _n_(456938, "help_block_hit", lambda: help_block_hit)) >= 1:
                    _l_(456941)

                    helpme += 1
                    _l_(456940)
                
                start_block_hit = _c_(456947, _a_(456944, _a_(456943, _n_(456942, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(456945, "player", lambda: player), _n_(456946, "start_block", lambda: start_block), False)
                _l_(456948)
                if _c_(456951, _n_(456949, "len", lambda: len), _n_(456950, "start_block_hit", lambda: start_block_hit)) >= 1:
                    _l_(456953)

                    play += 1
                    _l_(456952)

                quit_block_hit = _c_(456959, _a_(456956, _a_(456955, _n_(456954, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(456957, "player", lambda: player), _n_(456958, "quit_block", lambda: quit_block), False)
                _l_(456960)
                if _c_(456963, _n_(456961, "len", lambda: len), _n_(456962, "quit_block_hit", lambda: quit_block_hit)) >= 1:
                    _l_(456965)

                    done = True
                    _l_(456964)
                if _n_(456966, "helpme", lambda: helpme) == 1:
                    _l_(456979)

                    back_butt_hit = _c_(456972, _a_(456969, _a_(456968, _n_(456967, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(456970, "player", lambda: player), _n_(456971, "back_butt", lambda: back_butt), False)
                    _l_(456973)
                    if _c_(456976, _n_(456974, "len", lambda: len), _n_(456975, "back_butt_hit", lambda: back_butt_hit)) >= 1:
                        _l_(456978)

                        helpme = 0
                        _l_(456977)
            elif _n_(456980, "play", lambda: play) == 1:
                _l_(457099)

                continue_block_hit = _c_(456986, _a_(456983, _a_(456982, _n_(456981, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(456984, "player", lambda: player), _n_(456985, "continue_list", lambda: continue_list), False)
                _l_(456987)
                if _c_(456990, _n_(456988, "len", lambda: len), _n_(456989, "continue_block_hit", lambda: continue_block_hit)) >= 1:
                    _l_(456992)

                    play += 1
                    _l_(456991)
            elif _n_(456993, "play", lambda: play) == 2:
                _l_(457098)

                if _c_(456996, _n_(456994, "len", lambda: len), _n_(456995, "continue_block_hit", lambda: continue_block_hit)) >= 1:
                    _l_(456998)

                    play += 1
                    _l_(456997)
            elif _n_(456999, "play", lambda: play) == 3:
                _l_(457097)

                back_butt_hit = _c_(457005, _a_(457002, _a_(457001, _n_(457000, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457003, "player", lambda: player), _n_(457004, "back_butt", lambda: back_butt), False)
                _l_(457006)
                if _c_(457009, _n_(457007, "len", lambda: len), _n_(457008, "back_butt_hit", lambda: back_butt_hit)) >= 1:
                    _l_(457011)

                    play = 0
                    _l_(457010)

                map_hit = _c_(457017, _a_(457014, _a_(457013, _n_(457012, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457015, "player", lambda: player), _n_(457016, "map_screen", lambda: map_screen), False)
                _l_(457018)
                if _c_(457021, _n_(457019, "len", lambda: len), _n_(457020, "map_hit", lambda: map_hit)) >= 1:
                    _l_(457023)

                    errorkey = 0
                    _l_(457022)

                one_butt_hit = _c_(457029, _a_(457026, _a_(457025, _n_(457024, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457027, "player", lambda: player), _n_(457028, "butt_one", lambda: butt_one), False)
                _l_(457030)
                if _c_(457033, _n_(457031, "len", lambda: len), _n_(457032, "one_butt_hit", lambda: one_butt_hit)) >= 1:
                    _l_(457035)

                    play = 4
                    _l_(457034)
                two_butt_hit = _c_(457041, _a_(457038, _a_(457037, _n_(457036, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457039, "player", lambda: player), _n_(457040, "butt_two", lambda: butt_two), False)
                _l_(457042)
                if _c_(457045, _n_(457043, "len", lambda: len), _n_(457044, "two_butt_hit", lambda: two_butt_hit)) >= 1:
                    _l_(457049)

                    if _n_(457046, "progress", lambda: progress) == 0:
                        _l_(457048)

                        errorkey = 1
                        _l_(457047)
                three_butt_hit = _c_(457055, _a_(457052, _a_(457051, _n_(457050, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457053, "player", lambda: player), _n_(457054, "butt_three", lambda: butt_three), False)
                _l_(457056)
                if _c_(457059, _n_(457057, "len", lambda: len), _n_(457058, "three_butt_hit", lambda: three_butt_hit)) >= 1:
                    _l_(457064)

                    if _n_(457060, "progress", lambda: progress) == 0 or _n_(457061, "progress", lambda: progress) == 1:
                        _l_(457063)

                        errorkey = 1
                        _l_(457062)
                four_butt_hit = _c_(457070, _a_(457067, _a_(457066, _n_(457065, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457068, "player", lambda: player), _n_(457069, "butt_four", lambda: butt_four), False)
                _l_(457071)
                if _c_(457074, _n_(457072, "len", lambda: len), _n_(457073, "four_butt_hit", lambda: four_butt_hit)) >= 1:
                    _l_(457080)

                    if _n_(457075, "progress", lambda: progress) == 0 or _n_(457076, "progress", lambda: progress) == 1 or _n_(457077, "progress", lambda: progress) == 2:
                        _l_(457079)

                        errorkey = 1
                        _l_(457078)
            elif _n_(457081, "play", lambda: play) == 4:
                _l_(457096)

                crate_hit = _c_(457087, _a_(457084, _a_(457083, _n_(457082, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(457085, "player", lambda: player), _n_(457086, "crate_list", lambda: crate_list), True)
                _l_(457088)
                if _c_(457091, _n_(457089, "len", lambda: len), _n_(457090, "crate_hit", lambda: crate_hit)) >= 1:
                    _l_(457095)

                    score1 += 100
                    _l_(457092)
                    _n_(457093, "testman", lambda: testman).health += 5
                    _l_(457094)
        elif _a_(457102, _n_(457101, "event", lambda: event), "type") == _a_(457104, _n_(457103, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(457123)

            if _a_(457106, _n_(457105, "event", lambda: event), "key") == _a_(457108, _n_(457107, "pygame", lambda: pygame), "K_LEFT"):
                _l_(457122)

                _c_(457111, _a_(457110, _n_(457109, "testman", lambda: testman), "changespeed"), -3, 0)
                _l_(457112)
            elif _a_(457114, _n_(457113, "event", lambda: event), "key") == _a_(457116, _n_(457115, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(457121)

                _c_(457119, _a_(457118, _n_(457117, "testman", lambda: testman), "change_x"), 3, 0)
                _l_(457120)

 
    _c_(457129, _a_(457128, _n_(457127, "all_sprites_list", lambda: all_sprites_list), "update"))
    _l_(457130)

   
    # Clear the screen
    _c_(457134, _a_(457132, _n_(457131, "screen", lambda: screen), "fill"), _n_(457133, "WHITE", lambda: WHITE))
    _l_(457135)
 
    # Draw all the spites
    if _n_(457136, "play", lambda: play) == 0:
        _l_(457332)

        _c_(457140, _a_(457138, _n_(457137, "screen", lambda: screen), "blit"), _n_(457139, "background_image", lambda: background_image), [0,0])
        _l_(457141)
        if _n_(457142, "helpme", lambda: helpme) == 0:
            _l_(457210)

            _c_(457146, _a_(457144, _n_(457143, "all_sprites_list", lambda: all_sprites_list), "draw"), _n_(457145, "screen", lambda: screen))
            _l_(457147)
            _c_(457150, _a_(457149, _n_(457148, "Map", lambda: Map), "stop"))
            _l_(457151)
            _c_(457154, _a_(457153, _n_(457152, "Title", lambda: Title), "play"))
            _l_(457155)
        elif _n_(457156, "helpme", lambda: helpme) == 1:
            _l_(457209)

            _a_(457158, _n_(457157, "back", lambda: back), "rect").x = 0
            _l_(457159)
            _a_(457161, _n_(457160, "back", lambda: back), "rect").y = 0
            _l_(457162)
            _c_(457168, _a_(457165, _a_(457164, _n_(457163, "pygame", lambda: pygame), "draw"), "rect"), _n_(457166, "screen", lambda: screen), _n_(457167, "BLACK", lambda: BLACK), [80,60,600,420])
            _l_(457169)
            _c_(457175, _a_(457172, _a_(457171, _n_(457170, "pygame", lambda: pygame), "draw"), "rect"), _n_(457173, "screen", lambda: screen), _n_(457174, "WHITE", lambda: WHITE), [80,280,600,10])
            _l_(457176)
            fontheader = _c_(457180, _a_(457179, _a_(457178, _n_(457177, "pygame", lambda: pygame), "font"), "SysFont"), 'comicsansms', 25, True, False)
            _l_(457181)
            textheader = _c_(457185, _a_(457183, _n_(457182, "fontheader", lambda: fontheader), "render"), "Welcome to LARP!", True, _n_(457184, "WHITE", lambda: WHITE))
            _l_(457186)
            _c_(457190, _a_(457188, _n_(457187, "screen", lambda: screen), "blit"), _n_(457189, "textheader", lambda: textheader), [255,60])
            _l_(457191)
            _c_(457195, _a_(457193, _n_(457192, "back_butt", lambda: back_butt), "draw"), _n_(457194, "screen", lambda: screen))
            _l_(457196)
            _c_(457201, _n_(457197, "blit_text", lambda: blit_text), _n_(457198, "screen", lambda: screen), _n_(457199, "text", lambda: text), (20, 20), _n_(457200, "font", lambda: font))
            _l_(457202)
            _c_(457207, _n_(457203, "blit_text", lambda: blit_text), _n_(457204, "screen", lambda: screen), _n_(457205, "text2", lambda: text2), (50,50), _n_(457206, "font", lambda: font))
            _l_(457208)
    elif _n_(457211, "play", lambda: play) == 1:
        _l_(457331)

        _c_(457215, _a_(457213, _n_(457212, "screen", lambda: screen), "blit"), _n_(457214, "cutscene_2", lambda: cutscene_2), [0,0])
        _l_(457216)
        _c_(457220, _a_(457218, _n_(457217, "continue_list", lambda: continue_list), "draw"), _n_(457219, "screen", lambda: screen))
        _l_(457221)
    elif _n_(457222, "play", lambda: play) == 2:
        _l_(457330)

        _c_(457226, _a_(457224, _n_(457223, "screen", lambda: screen), "blit"), _n_(457225, "cutscene_1", lambda: cutscene_1), [0,0])
        _l_(457227)
        _c_(457231, _a_(457229, _n_(457228, "continue_list", lambda: continue_list), "draw"), _n_(457230, "screen", lambda: screen))
        _l_(457232)
    elif _n_(457233, "play", lambda: play) == 3:
        _l_(457329)

        _a_(457235, _n_(457234, "back", lambda: back), "rect").x = 0
        _l_(457236)
        _a_(457238, _n_(457237, "back", lambda: back), "rect").y = 12
        _l_(457239)
        _a_(457241, _n_(457240, "one", lambda: one), "rect").x = 55
        _l_(457242)
        _a_(457244, _n_(457243, "one", lambda: one), "rect").y = 410
        _l_(457245)
        _a_(457247, _n_(457246, "two", lambda: two), "rect").x = 250
        _l_(457248)
        _a_(457250, _n_(457249, "two", lambda: two), "rect").y = 410
        _l_(457251)
        _a_(457253, _n_(457252, "three", lambda: three), "rect").x = 466
        _l_(457254)
        _a_(457256, _n_(457255, "three", lambda: three), "rect").y = 410
        _l_(457257)
        _a_(457259, _n_(457258, "four", lambda: four), "rect").x = 660
        _l_(457260)
        _a_(457262, _n_(457261, "four", lambda: four), "rect").y = 410
        _l_(457263)
        _c_(457267, _a_(457265, _n_(457264, "map_screen", lambda: map_screen), "draw"), _n_(457266, "screen", lambda: screen))
        _l_(457268)
        _c_(457272, _a_(457270, _n_(457269, "back_butt", lambda: back_butt), "draw"), _n_(457271, "screen", lambda: screen))
        _l_(457273)
        _c_(457277, _a_(457275, _n_(457274, "lvlselect", lambda: lvlselect), "draw"), _n_(457276, "screen", lambda: screen))
        _l_(457278)
        _c_(457281, _a_(457280, _n_(457279, "Title", lambda: Title), "stop"))
        _l_(457282)
        _c_(457285, _a_(457284, _n_(457283, "Map", lambda: Map), "play"))
        _l_(457286)
        if _n_(457287, "errorkey", lambda: errorkey) == 1:
            _l_(457293)

            _c_(457291, _a_(457289, _n_(457288, "stage_error", lambda: stage_error), "draw"), _n_(457290, "screen", lambda: screen))
            _l_(457292)
    #STAGE 1
    elif _n_(457294, "play", lambda: play) == 4:
        _l_(457328)

        _c_(457297, _a_(457296, _n_(457295, "Map", lambda: Map), "stop"))
        _l_(457298)
        _c_(457301, _a_(457300, _n_(457299, "Title", lambda: Title), "stop"))
        _l_(457302)
        _c_(457305, _a_(457304, _n_(457303, "stage_one_music", lambda: stage_one_music), "play"))
        _l_(457306)
        rect_x -= _n_(457307, "rect_x_change", lambda: rect_x_change)
        _l_(457308)
        _c_(457313, _a_(457310, _n_(457309, "screen", lambda: screen), "blit"), _n_(457311, "stage_one", lambda: stage_one), [_n_(457312, "rect_x", lambda: rect_x),-180])
        _l_(457314)
        _c_(457316, _n_(457315, "levelsetup", lambda: levelsetup))
        _l_(457317)
        if _a_(457319, _n_(457318, "testman", lambda: testman), "health") >= 100:
            _l_(457322)

            _n_(457320, "testman", lambda: testman).health = 100
            _l_(457321)
    elif _n_(457323, "play", lambda: play) == 5:
        _l_(457327)

        _c_(457325, _n_(457324, "levelsetup", lambda: levelsetup))
        _l_(457326)
    _c_(457342, _a_(457334, _n_(457333, "screen", lambda: screen), "blit"), _n_(457335, "player_image", lambda: player_image), [_a_(457338, _a_(457337, _n_(457336, "player", lambda: player), "rect"), "x"), _a_(457341, _a_(457340, _n_(457339, "player", lambda: player), "rect"), "y")])
    _l_(457343)
 
    # Limit to 60 frames per second
    _c_(457346, _a_(457345, _n_(457344, "clock", lambda: clock), "tick"), 60)
    _l_(457347)
 
    # Go ahead and update the screen with what we've drawn.
    _c_(457351, _a_(457350, _a_(457349, _n_(457348, "pygame", lambda: pygame), "display"), "flip"))
    _l_(457352)
 
_c_(457356, _a_(457355, _n_(457354, "pygame", lambda: pygame), "quit"))
_l_(457357)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64795214/why-am-i-getting-nameerror-wolf-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(464961)

except ImportError:
    pass
try:
    import random
    _l_(464963)

except ImportError:
    pass
try:
    import Colors
    _l_(464965)

except ImportError:
    pass
try:
    import Player
    _l_(464967)

except ImportError:
    pass
try:
    import Enemy
    _l_(464969)

except ImportError:
    pass
        
# Initialize Pygame
_c_(464972, _a_(464971, _n_(464970, "pygame", lambda: pygame), "init"))
_l_(464973)

# Set the height and width of the screen
screen_width  = 800
_l_(464974)
screen_height = 600
_l_(464975)
screen = _c_(464981, _a_(464978, _a_(464977, _n_(464976, "pygame", lambda: pygame), "display"), "set_mode"), [_n_(464979, "screen_width", lambda: screen_width), _n_(464980, "screen_height", lambda: screen_height)])
_l_(464982)

#SPRITE LIST CREATIONS
wolf_list = _c_(464986, _a_(464985, _a_(464984, _n_(464983, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(464987)
poison_wolf_list = _c_(464991, _a_(464990, _a_(464989, _n_(464988, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(464992)
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = _c_(464996, _a_(464995, _a_(464994, _n_(464993, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(464997)
 
for i in _c_(464999, _n_(464998, "range", lambda: range), 50):
    _l_(465029)

    # This represents a single block
    wolf = _c_(465003, _n_(465000, "Wolf", lambda: Wolf), _a_(465002, _n_(465001, "Colors", lambda: Colors), "GREEN"), 20, 15)
    _l_(465004)
    # Set a random location for the block
    _a_(465006, _n_(465005, "wolf", lambda: wolf), "rect").x = _c_(465010, _a_(465008, _n_(465007, "random", lambda: random), "randrange"), _n_(465009, "screen_width", lambda: screen_width))
    _l_(465011)
    _a_(465013, _n_(465012, "wolf", lambda: wolf), "rect").y = _c_(465017, _a_(465015, _n_(465014, "random", lambda: random), "randrange"), _n_(465016, "screen_height", lambda: screen_height))
    _l_(465018)
    # Add the block to the list of objects
    _c_(465022, _a_(465020, _n_(465019, "wolf_list", lambda: wolf_list), "add"), _n_(465021, "wolf", lambda: wolf))
    _l_(465023)
    _c_(465027, _a_(465025, _n_(465024, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(465026, "wolf", lambda: wolf))
    _l_(465028)
for i in _c_(465031, _n_(465030, "range", lambda: range), 50):
    _l_(465061)

    # This represents a single block
    wolf = _c_(465035, _n_(465032, "Wolf", lambda: Wolf), _a_(465034, _n_(465033, "Colors", lambda: Colors), "RED"), 20, 15)
    _l_(465036)
    # Set a random location for the block
    _a_(465038, _n_(465037, "wolf", lambda: wolf), "rect").x = _c_(465042, _a_(465040, _n_(465039, "random", lambda: random), "randrange"), _n_(465041, "screen_width", lambda: screen_width))
    _l_(465043)
    _a_(465045, _n_(465044, "wolf", lambda: wolf), "rect").y = _c_(465049, _a_(465047, _n_(465046, "random", lambda: random), "randrange"), _n_(465048, "screen_height", lambda: screen_height))
    _l_(465050)
    # Add the block to the list of objects
    _c_(465054, _a_(465052, _n_(465051, "poison_wolf_list", lambda: poison_wolf_list), "add"), _n_(465053, "wolf", lambda: wolf))
    _l_(465055)
    _c_(465059, _a_(465057, _n_(465056, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(465058, "wolf", lambda: wolf))
    _l_(465060)
 
# Create a RED player block
player = _c_(465064, _a_(465063, _n_(465062, "Player", lambda: Player), "Player"), 100, 100)
_l_(465065)
_c_(465069, _a_(465067, _n_(465066, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(465068, "player", lambda: player))
_l_(465070)
 
# Loop until the user clicks the close button.
done = False
_l_(465071)
 
# Used to manage how fast the screen updates
clock = _c_(465075, _a_(465074, _a_(465073, _n_(465072, "pygame", lambda: pygame), "time"), "Clock"))
_l_(465076)
 
score = 0
_l_(465077)
 
# -------- Main Program Loop -----------
while not _n_(465078, "done", lambda: done):
    _l_(465224)

    for event in _c_(465082, _a_(465081, _a_(465080, _n_(465079, "pygame", lambda: pygame), "event"), "get")):
        _l_(465171)

        if _a_(465084, _n_(465083, "event", lambda: event), "type") == _a_(465086, _n_(465085, "pygame", lambda: pygame), "QUIT"):
            _l_(465170)

            done = True
            _l_(465087)

        # Set the speed based on the key pressed
        elif _a_(465089, _n_(465088, "event", lambda: event), "type") == _a_(465091, _n_(465090, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(465169)

            if _a_(465093, _n_(465092, "event", lambda: event), "key") == _a_(465095, _n_(465094, "pygame", lambda: pygame), "K_a"):
                _l_(465127)

                _c_(465098, _a_(465097, _n_(465096, "player", lambda: player), "changespeed"), -3, 0)
                _l_(465099)
            elif _a_(465101, _n_(465100, "event", lambda: event), "key") == _a_(465103, _n_(465102, "pygame", lambda: pygame), "K_d"):
                _l_(465126)

                _c_(465106, _a_(465105, _n_(465104, "player", lambda: player), "changespeed"), 3, 0)
                _l_(465107)
            elif _a_(465109, _n_(465108, "event", lambda: event), "key") == _a_(465111, _n_(465110, "pygame", lambda: pygame), "K_w"):
                _l_(465125)

                _c_(465114, _a_(465113, _n_(465112, "player", lambda: player), "changespeed"), 0, -3)
                _l_(465115)
            elif _a_(465117, _n_(465116, "event", lambda: event), "key") == _a_(465119, _n_(465118, "pygame", lambda: pygame), "K_s"):
                _l_(465124)

                _c_(465122, _a_(465121, _n_(465120, "player", lambda: player), "changespeed"), 0, 3)
                _l_(465123)
 
        # Reset speed when key goes up
        elif _a_(465129, _n_(465128, "event", lambda: event), "type") == _a_(465131, _n_(465130, "pygame", lambda: pygame), "KEYUP"):
            _l_(465168)

            if _a_(465133, _n_(465132, "event", lambda: event), "key") == _a_(465135, _n_(465134, "pygame", lambda: pygame), "K_a"):
                _l_(465167)

                _c_(465138, _a_(465137, _n_(465136, "player", lambda: player), "changespeed"), 3, 0)
                _l_(465139)
            elif _a_(465141, _n_(465140, "event", lambda: event), "key") == _a_(465143, _n_(465142, "pygame", lambda: pygame), "K_d"):
                _l_(465166)

                _c_(465146, _a_(465145, _n_(465144, "player", lambda: player), "changespeed"), -3, 0)
                _l_(465147)
            elif _a_(465149, _n_(465148, "event", lambda: event), "key") == _a_(465151, _n_(465150, "pygame", lambda: pygame), "K_w"):
                _l_(465165)

                _c_(465154, _a_(465153, _n_(465152, "player", lambda: player), "changespeed"), 0, 3)
                _l_(465155)
            elif _a_(465157, _n_(465156, "event", lambda: event), "key") == _a_(465159, _n_(465158, "pygame", lambda: pygame), "K_s"):
                _l_(465164)

                _c_(465162, _a_(465161, _n_(465160, "player", lambda: player), "changespeed"), 0, -3)
                _l_(465163)

    # Clear the screen
    _c_(465176, _a_(465173, _n_(465172, "screen", lambda: screen), "fill"), _a_(465175, _n_(465174, "Colors", lambda: Colors), "WHITE"))
    _l_(465177)
 
    # Game Logic
    _c_(465180, _a_(465179, _n_(465178, "all_sprites_list", lambda: all_sprites_list), "update"))
    _l_(465181)

 
    # See if the player block has collided with anything.
    wolf_list = _c_(465187, _a_(465184, _a_(465183, _n_(465182, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(465185, "player", lambda: player), _n_(465186, "wolf_list", lambda: wolf_list), True)
    _l_(465188)
    poison_wolf_list = _c_(465194, _a_(465191, _a_(465190, _n_(465189, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(465192, "player", lambda: player), _n_(465193, "poison_wolf_list", lambda: poison_wolf_list), True)
    _l_(465195)
    # Check the list of collisions.
    for block in _n_(465196, "wolf_list", lambda: wolf_list):
        _l_(465202)

        score += 1
        _l_(465197)
        _c_(465200, _n_(465198, "print", lambda: print), _n_(465199, "score", lambda: score))
        _l_(465201)
    for block in _n_(465203, "poison_wolf_list", lambda: poison_wolf_list):
        _l_(465209)

        score -= 1
        _l_(465204)
        _c_(465207, _n_(465205, "print", lambda: print), _n_(465206, "score", lambda: score)) 
        _l_(465208) 
    # Draw all the spites
    _c_(465213, _a_(465211, _n_(465210, "all_sprites_list", lambda: all_sprites_list), "draw"), _n_(465212, "screen", lambda: screen))
    _l_(465214)
 
    # Go ahead and update the screen with what we've drawn.
    _c_(465218, _a_(465217, _a_(465216, _n_(465215, "pygame", lambda: pygame), "display"), "flip"))
    _l_(465219)
 
    # Limit to 60 frames per second
    _c_(465222, _a_(465221, _n_(465220, "clock", lambda: clock), "tick"), 60)
    _l_(465223)
 
_c_(465227, _a_(465226, _n_(465225, "pygame", lambda: pygame), "quit"))
_l_(465228)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame.font
    _l_(703409)

except ImportError:
    pass
try:
    from pygame.sprite import Group
    _l_(703411)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(703413)

except ImportError:
    pass

class Scoreboard():
    _l_(703645)

    """A class to report scoring information."""
    
    def __init__(self, ai_settings, screen, stats):
        _l_(703451)

        """Initialize scorekeeping attributes."""
        _n_(703414, "self", lambda: self).screen = _n_(703415, "screen", lambda: screen)
        _l_(703416)
        _n_(703417, "self", lambda: self).screen_rect = _c_(703420, _a_(703419, _n_(703418, "screen", lambda: screen), "get_rect"))
        _l_(703421)
        _n_(703422, "self", lambda: self).ai_settings = _n_(703423, "ai_settings", lambda: ai_settings)
        _l_(703424)
        _n_(703425, "self", lambda: self).stats = _n_(703426, "stats", lambda: stats)
        _l_(703427)
        
        # Font settings for scoring information.
        _n_(703428, "self", lambda: self).text_color = (30, 30, 30)
        _l_(703429)
        _n_(703430, "self", lambda: self).font = _c_(703433, _a_(703432, _a_(703431, pygame, "font"), "SysFont"), None, 48)
        _l_(703434)
        
        # Prepare the initial score images.
        _c_(703437, _a_(703436, _n_(703435, "self", lambda: self), "prep_score"))
        _l_(703438)
        _c_(703441, _a_(703440, _n_(703439, "self", lambda: self), "prep_high_score"))
        _l_(703442)
        _c_(703445, _a_(703444, _n_(703443, "self", lambda: self), "prep_level"))
        _l_(703446)
        _c_(703449, _a_(703448, _n_(703447, "self", lambda: self), "prep_ships"))
        _l_(703450)
    def prep_score(self):
        _l_(703497)

        """Turn the score into a rendered image."""
        rounded_score = _c_(703458, _n_(703452, "int", lambda: int), _c_(703457, _n_(703453, "round", lambda: round), _a_(703456, _a_(703455, _n_(703454, "self", lambda: self), "stats"), "score"), -1))
        _l_(703459)
        score_str = _c_(703462, _a_(703460, "{:,}", "format"), _n_(703461, "rounded_score", lambda: rounded_score))
        _l_(703463)
        score_str = _c_(703468, _n_(703464, "str", lambda: str), _a_(703467, _a_(703466, _n_(703465, "self", lambda: self), "stats"), "score"))
        _l_(703469)
        _n_(703470, "self", lambda: self).score_image = _c_(703480, _a_(703473, _a_(703472, _n_(703471, "self", lambda: self), "font"), "render"), _n_(703474, "score_str", lambda: score_str), True, _a_(703476, _n_(703475, "self", lambda: self), "text_color"), _a_(703479, _a_(703478, _n_(703477, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(703481)
        
        # Display the score at the top right of the screen.
        _n_(703482, "self", lambda: self).score_rect = _c_(703486, _a_(703485, _a_(703484, _n_(703483, "self", lambda: self), "score_image"), "get_rect"))
        _l_(703487)
        _a_(703489, _n_(703488, "self", lambda: self), "score_rect").right = _a_(703492, _a_(703491, _n_(703490, "self", lambda: self), "screen_rect"), "right") - 20
        _l_(703493)
        _a_(703495, _n_(703494, "self", lambda: self), "score_rect").top = 20
        _l_(703496)
    def prep_high_score(self):
        _l_(703540)

        """Turn the high score into a rendered image."""
        high_score = _c_(703504, _n_(703498, "int", lambda: int), _c_(703503, _n_(703499, "round", lambda: round), _a_(703502, _a_(703501, _n_(703500, "self", lambda: self), "stats"), "high_score"), -1))
        _l_(703505)
        high_score_str = _c_(703508, _a_(703506, "{:,}", "format"), _n_(703507, "high_score", lambda: high_score))
        _l_(703509)
        _n_(703510, "self", lambda: self).high_score_image = _c_(703520, _a_(703513, _a_(703512, _n_(703511, "self", lambda: self), "font"), "render"), _n_(703514, "high_score_str", lambda: high_score_str), True, _a_(703516, _n_(703515, "self", lambda: self), "text_color"), _a_(703519, _a_(703518, _n_(703517, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(703521)
        
        # Center the high score at the top of the screen.
        _n_(703522, "self", lambda: self).high_score_rect = _c_(703526, _a_(703525, _a_(703524, _n_(703523, "self", lambda: self), "high_score_image"), "get_rect"))
        _l_(703527)
        _a_(703529, _n_(703528, "self", lambda: self), "high_score_rect").centerx = _a_(703532, _a_(703531, _n_(703530, "self", lambda: self), "screen_rect"), "centerx")
        _l_(703533)
        _a_(703535, _n_(703534, "self", lambda: self), "high_score_rect").top = _a_(703538, _a_(703537, _n_(703536, "self", lambda: self), "score_rect"), "top")
        _l_(703539)
    def prep_level(self):
        _l_(703575)

        """Turn the level into a rendered image."""
        _n_(703541, "self", lambda: self).level_image = _c_(703555, _a_(703544, _a_(703543, _n_(703542, "self", lambda: self), "font"), "render"), _c_(703549, _n_(703545, "str", lambda: str), _a_(703548, _a_(703547, _n_(703546, "self", lambda: self), "stats"), "level")), True, _a_(703551, _n_(703550, "self", lambda: self), "text_color"), _a_(703554, _a_(703553, _n_(703552, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(703556)
        
        # Position the level below the score.
        _n_(703557, "self", lambda: self).level_rect = _c_(703561, _a_(703560, _a_(703559, _n_(703558, "self", lambda: self), "level_image"), "get_rect"))
        _l_(703562)
        _a_(703564, _n_(703563, "self", lambda: self), "level_rect").right = _a_(703567, _a_(703566, _n_(703565, "self", lambda: self), "score_rect"), "right")
        _l_(703568)
        _a_(703570, _n_(703569, "self", lambda: self), "level_rect").top = _a_(703573, _a_(703572, _n_(703571, "self", lambda: self), "score_rect"), "bottom") + 10
        _l_(703574)
    def prep_ships(self):
        _l_(703609)

        """Show how many ships are left."""
        _n_(703576, "self", lambda: self).ships = _c_(703578, _n_(703577, "Group", lambda: Group))
        _l_(703579)
        for ship_number in _c_(703584, _n_(703580, "range", lambda: range), _a_(703583, _a_(703582, _n_(703581, "self", lambda: self), "stats"), "ships_left")):
            _l_(703608)

            ship = _c_(703590, _n_(703585, "Ship", lambda: Ship), _a_(703587, _n_(703586, "self", lambda: self), "ai_settings"), _a_(703589, _n_(703588, "self", lambda: self), "screen"))
            _l_(703591)
            _a_(703593, _n_(703592, "ship", lambda: ship), "rect").x = 10 + _n_(703594, "ship_number", lambda: ship_number) * _a_(703597, _a_(703596, _n_(703595, "ship", lambda: ship), "rect"), "width")
            _l_(703598)
            _a_(703600, _n_(703599, "ship", lambda: ship), "rect").y = 10
            _l_(703601)
            _c_(703606, _a_(703604, _a_(703603, _n_(703602, "self", lambda: self), "ships"), "add"), _n_(703605, "ship", lambda: ship))
            _l_(703607)
    def show_score(self):
        _l_(703644)

        """Draw scores and ships to the screen."""
        _c_(703617, _a_(703612, _a_(703611, _n_(703610, "self", lambda: self), "screen"), "blit"), _a_(703614, _n_(703613, "self", lambda: self), "score_image"), _a_(703616, _n_(703615, "self", lambda: self), "score_rect"))
        _l_(703618)
        _c_(703626, _a_(703621, _a_(703620, _n_(703619, "self", lambda: self), "screen"), "blit"), _a_(703623, _n_(703622, "self", lambda: self), "high_score_image"), _a_(703625, _n_(703624, "self", lambda: self), "high_score_rect"))
        _l_(703627)
        _c_(703635, _a_(703630, _a_(703629, _n_(703628, "self", lambda: self), "screen"), "blit"), _a_(703632, _n_(703631, "self", lambda: self), "level_image"), _a_(703634, _n_(703633, "self", lambda: self), "level_rect"))
        _l_(703636)
        # Draw ships.
        _c_(703642, _a_(703639, _a_(703638, _n_(703637, "self", lambda: self), "ships"), "draw"), _a_(703641, _n_(703640, "self", lambda: self), "screen"))
        _l_(703643)
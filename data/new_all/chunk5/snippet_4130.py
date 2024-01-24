# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame.font
    _l_(654581)

except ImportError:
    pass
try:
    from pygame.sprite import Group
    _l_(654583)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(654585)

except ImportError:
    pass

class Scoreboard():
    _l_(654817)

    """A class to report scoring information."""
    
    def __init__(self, ai_settings, screen, stats):
        _l_(654623)

        """Initialize scorekeeping attributes."""
        _n_(654586, "self", lambda: self).screen = _n_(654587, "screen", lambda: screen)
        _l_(654588)
        _n_(654589, "self", lambda: self).screen_rect = _c_(654592, _a_(654591, _n_(654590, "screen", lambda: screen), "get_rect"))
        _l_(654593)
        _n_(654594, "self", lambda: self).ai_settings = _n_(654595, "ai_settings", lambda: ai_settings)
        _l_(654596)
        _n_(654597, "self", lambda: self).stats = _n_(654598, "stats", lambda: stats)
        _l_(654599)
        
        # Font settings for scoring information.
        _n_(654600, "self", lambda: self).text_color = (30, 30, 30)
        _l_(654601)
        _n_(654602, "self", lambda: self).font = _c_(654605, _a_(654604, _a_(654603, pygame, "font"), "SysFont"), None, 48)
        _l_(654606)
        
        # Prepare the initial score images.
        _c_(654609, _a_(654608, _n_(654607, "self", lambda: self), "prep_score"))
        _l_(654610)
        _c_(654613, _a_(654612, _n_(654611, "self", lambda: self), "prep_high_score"))
        _l_(654614)
        _c_(654617, _a_(654616, _n_(654615, "self", lambda: self), "prep_level"))
        _l_(654618)
        _c_(654621, _a_(654620, _n_(654619, "self", lambda: self), "prep_ships"))
        _l_(654622)
    def prep_score(self):
        _l_(654669)

        """Turn the score into a rendered image."""
        rounded_score = _c_(654630, _n_(654624, "int", lambda: int), _c_(654629, _n_(654625, "round", lambda: round), _a_(654628, _a_(654627, _n_(654626, "self", lambda: self), "stats"), "score"), -1))
        _l_(654631)
        score_str = _c_(654634, _a_(654632, "{:,}", "format"), _n_(654633, "rounded_score", lambda: rounded_score))
        _l_(654635)
        score_str = _c_(654640, _n_(654636, "str", lambda: str), _a_(654639, _a_(654638, _n_(654637, "self", lambda: self), "stats"), "score"))
        _l_(654641)
        _n_(654642, "self", lambda: self).score_image = _c_(654652, _a_(654645, _a_(654644, _n_(654643, "self", lambda: self), "font"), "render"), _n_(654646, "score_str", lambda: score_str), True, _a_(654648, _n_(654647, "self", lambda: self), "text_color"), _a_(654651, _a_(654650, _n_(654649, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(654653)
        
        # Display the score at the top right of the screen.
        _n_(654654, "self", lambda: self).score_rect = _c_(654658, _a_(654657, _a_(654656, _n_(654655, "self", lambda: self), "score_image"), "get_rect"))
        _l_(654659)
        _a_(654661, _n_(654660, "self", lambda: self), "score_rect").right = _a_(654664, _a_(654663, _n_(654662, "self", lambda: self), "screen_rect"), "right") - 20
        _l_(654665)
        _a_(654667, _n_(654666, "self", lambda: self), "score_rect").top = 20
        _l_(654668)
    def prep_high_score(self):
        _l_(654712)

        """Turn the high score into a rendered image."""
        high_score = _c_(654676, _n_(654670, "int", lambda: int), _c_(654675, _n_(654671, "round", lambda: round), _a_(654674, _a_(654673, _n_(654672, "self", lambda: self), "stats"), "high_score"), -1))
        _l_(654677)
        high_score_str = _c_(654680, _a_(654678, "{:,}", "format"), _n_(654679, "high_score", lambda: high_score))
        _l_(654681)
        _n_(654682, "self", lambda: self).high_score_image = _c_(654692, _a_(654685, _a_(654684, _n_(654683, "self", lambda: self), "font"), "render"), _n_(654686, "high_score_str", lambda: high_score_str), True, _a_(654688, _n_(654687, "self", lambda: self), "text_color"), _a_(654691, _a_(654690, _n_(654689, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(654693)
        
        # Center the high score at the top of the screen.
        _n_(654694, "self", lambda: self).high_score_rect = _c_(654698, _a_(654697, _a_(654696, _n_(654695, "self", lambda: self), "high_score_image"), "get_rect"))
        _l_(654699)
        _a_(654701, _n_(654700, "self", lambda: self), "high_score_rect").centerx = _a_(654704, _a_(654703, _n_(654702, "self", lambda: self), "screen_rect"), "centerx")
        _l_(654705)
        _a_(654707, _n_(654706, "self", lambda: self), "high_score_rect").top = _a_(654710, _a_(654709, _n_(654708, "self", lambda: self), "score_rect"), "top")
        _l_(654711)
    def prep_level(self):
        _l_(654747)

        """Turn the level into a rendered image."""
        _n_(654713, "self", lambda: self).level_image = _c_(654727, _a_(654716, _a_(654715, _n_(654714, "self", lambda: self), "font"), "render"), _c_(654721, _n_(654717, "str", lambda: str), _a_(654720, _a_(654719, _n_(654718, "self", lambda: self), "stats"), "level")), True, _a_(654723, _n_(654722, "self", lambda: self), "text_color"), _a_(654726, _a_(654725, _n_(654724, "self", lambda: self), "ai_settings"), "bg_color"))
        _l_(654728)
        
        # Position the level below the score.
        _n_(654729, "self", lambda: self).level_rect = _c_(654733, _a_(654732, _a_(654731, _n_(654730, "self", lambda: self), "level_image"), "get_rect"))
        _l_(654734)
        _a_(654736, _n_(654735, "self", lambda: self), "level_rect").right = _a_(654739, _a_(654738, _n_(654737, "self", lambda: self), "score_rect"), "right")
        _l_(654740)
        _a_(654742, _n_(654741, "self", lambda: self), "level_rect").top = _a_(654745, _a_(654744, _n_(654743, "self", lambda: self), "score_rect"), "bottom") + 10
        _l_(654746)
    def prep_ships(self):
        _l_(654781)

        """Show how many ships are left."""
        _n_(654748, "self", lambda: self).ships = _c_(654750, _n_(654749, "Group", lambda: Group))
        _l_(654751)
        for ship_number in _c_(654756, _n_(654752, "range", lambda: range), _a_(654755, _a_(654754, _n_(654753, "self", lambda: self), "stats"), "ships_left")):
            _l_(654780)

            ship = _c_(654762, _n_(654757, "Ship", lambda: Ship), _a_(654759, _n_(654758, "self", lambda: self), "ai_settings"), _a_(654761, _n_(654760, "self", lambda: self), "screen"))
            _l_(654763)
            _a_(654765, _n_(654764, "ship", lambda: ship), "rect").x = 10 + _n_(654766, "ship_number", lambda: ship_number) * _a_(654769, _a_(654768, _n_(654767, "ship", lambda: ship), "rect"), "width")
            _l_(654770)
            _a_(654772, _n_(654771, "ship", lambda: ship), "rect").y = 10
            _l_(654773)
            _c_(654778, _a_(654776, _a_(654775, _n_(654774, "self", lambda: self), "ships"), "add"), _n_(654777, "ship", lambda: ship))
            _l_(654779)
    def show_score(self):
        _l_(654816)

        """Draw scores and ships to the screen."""
        _c_(654789, _a_(654784, _a_(654783, _n_(654782, "self", lambda: self), "screen"), "blit"), _a_(654786, _n_(654785, "self", lambda: self), "score_image"), _a_(654788, _n_(654787, "self", lambda: self), "score_rect"))
        _l_(654790)
        _c_(654798, _a_(654793, _a_(654792, _n_(654791, "self", lambda: self), "screen"), "blit"), _a_(654795, _n_(654794, "self", lambda: self), "high_score_image"), _a_(654797, _n_(654796, "self", lambda: self), "high_score_rect"))
        _l_(654799)
        _c_(654807, _a_(654802, _a_(654801, _n_(654800, "self", lambda: self), "screen"), "blit"), _a_(654804, _n_(654803, "self", lambda: self), "level_image"), _a_(654806, _n_(654805, "self", lambda: self), "level_rect"))
        _l_(654808)
        # Draw ships.
        _c_(654814, _a_(654811, _a_(654810, _n_(654809, "self", lambda: self), "ships"), "draw"), _a_(654813, _n_(654812, "self", lambda: self), "screen"))
        _l_(654815)
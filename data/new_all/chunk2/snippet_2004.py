# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70735803/why-am-i-getting-an-attributeerror-alien-object-has-no-attribute-draw-bullet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(432486)

except ImportError:
    pass
try:
    from pygame.sprite import Group
    _l_(432488)

except ImportError:
    pass
try:
    from settings import Settings
    _l_(432490)

except ImportError:
    pass
try:
    from game_stats import GameStats
    _l_(432492)

except ImportError:
    pass
try:
    from button import Button
    _l_(432494)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(432496)

except ImportError:
    pass
try:
    from alien import Alien
    _l_(432498)

except ImportError:
    pass
try:
    import game_functions as gf
    _l_(432500)

except ImportError:
    pass

def run_game():
    _l_(432598)

    # Initialize pygame, settings, and screen object.
    _c_(432503, _a_(432502, _n_(432501, "pygame", lambda: pygame), "init"))
    _l_(432504)
    ai_settings = _c_(432506, _n_(432505, "Settings", lambda: Settings))
    _l_(432507)
    screen = _c_(432515, _a_(432510, _a_(432509, _n_(432508, "pygame", lambda: pygame), "display"), "set_mode"), (_a_(432512, _n_(432511, "ai_settings", lambda: ai_settings), "screen_width"), _a_(432514, _n_(432513, "ai_settings", lambda: ai_settings), "screen_height")))
    _l_(432516)
    _c_(432520, _a_(432519, _a_(432518, _n_(432517, "pygame", lambda: pygame), "display"), "set_caption"), "Alien Invasion")
    _l_(432521)
    
    # Make the Play Button.
    play_button = _c_(432525, _n_(432522, "Button", lambda: Button), _n_(432523, "ai_settings", lambda: ai_settings), _n_(432524, "screen", lambda: screen), "Play")
    _l_(432526)
    
    #Create an instance to store game statistics.
    stats = _c_(432529, _n_(432527, "GameStats", lambda: GameStats), _n_(432528, "ai_settings", lambda: ai_settings))
    _l_(432530)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = _c_(432534, _n_(432531, "Ship", lambda: Ship), _n_(432532, "ai_settings", lambda: ai_settings), _n_(432533, "screen", lambda: screen))
    _l_(432535)
    bullets = _c_(432537, _n_(432536, "Group", lambda: Group))
    _l_(432538)
    aliens = _c_(432540, _n_(432539, "Group", lambda: Group))
    _l_(432541)
    
    # Create the fleet of aliens.
    _c_(432548, _a_(432543, _n_(432542, "gf", lambda: gf), "create_fleet"), _n_(432544, "ai_settings", lambda: ai_settings), _n_(432545, "screen", lambda: screen), _n_(432546, "ship", lambda: ship), _n_(432547, "bullets", lambda: bullets))
    _l_(432549)
    
    # Start the main loop for the game.
    while True:
        _l_(432597)

        _c_(432558, _a_(432551, _n_(432550, "gf", lambda: gf), "check_events"), _n_(432552, "ai_settings", lambda: ai_settings), _n_(432553, "screen", lambda: screen), _n_(432554, "stats", lambda: stats), _n_(432555, "play_button", lambda: play_button), _n_(432556, "ship", lambda: ship), _n_(432557, "bullets", lambda: bullets))
        _l_(432559)
        
        if _a_(432561, _n_(432560, "stats", lambda: stats), "game_active"):
            _l_(432585)

            _c_(432564, _a_(432563, _n_(432562, "ship", lambda: ship), "update"))
            _l_(432565)
            _c_(432573, _a_(432567, _n_(432566, "gf", lambda: gf), "update_bullets"), _n_(432568, "ai_settings", lambda: ai_settings), _n_(432569, "screen", lambda: screen), _n_(432570, "ship", lambda: ship), _n_(432571, "aliens", lambda: aliens), _n_(432572, "bullets", lambda: bullets))
            _l_(432574)
            _c_(432583, _a_(432576, _n_(432575, "gf", lambda: gf), "update_aliens"), _n_(432577, "ai_settings", lambda: ai_settings), _n_(432578, "stats", lambda: stats), _n_(432579, "screen", lambda: screen), _n_(432580, "ship", lambda: ship), _n_(432581, "aliens", lambda: aliens), _n_(432582, "bullets", lambda: bullets))
            _l_(432584)
        _c_(432595, _a_(432587, _n_(432586, "gf", lambda: gf), "update_screen"), _n_(432588, "ai_settings", lambda: ai_settings), _n_(432589, "screen", lambda: screen), _n_(432590, "stats", lambda: stats), _n_(432591, "ship", lambda: ship), _n_(432592, "aliens", lambda: aliens), _n_(432593, "bullets", lambda: bullets), _n_(432594, "play_button", lambda: play_button))
        _l_(432596)
_c_(432600, _n_(432599, "run_game", lambda: run_game))
_l_(432601)
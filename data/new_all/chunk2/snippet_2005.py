# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70735803/why-am-i-getting-an-attributeerror-alien-object-has-no-attribute-draw-bullet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(420420)

except ImportError:
    pass
try:
    from time import sleep
    _l_(420422)

except ImportError:
    pass
try:
    import pygame
    _l_(420424)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(420426)

except ImportError:
    pass
try:
    from alien import Alien
    _l_(420428)

except ImportError:
    pass

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    _l_(420464)

    """Respond to keypresses."""
    if _a_(420430, _n_(420429, "event", lambda: event), "key") == _a_(420432, _n_(420431, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(420463)

        _n_(420433, "ship", lambda: ship).moving_right = True
        _l_(420434)
    elif _a_(420436, _n_(420435, "event", lambda: event), "key") == _a_(420438, _n_(420437, "pygame", lambda: pygame), "K_LEFT"):
        _l_(420462)

        _n_(420439, "ship", lambda: ship).moving_left = True
        _l_(420440)
    elif _a_(420442, _n_(420441, "event", lambda: event), "key") == _a_(420444, _n_(420443, "pygame", lambda: pygame), "K_SPACE"):
        _l_(420461)

        _c_(420450, _n_(420445, "fire_bullet", lambda: fire_bullet), _n_(420446, "ai_settings", lambda: ai_settings), _n_(420447, "screen", lambda: screen), _n_(420448, "ship", lambda: ship), _n_(420449, "bullets", lambda: bullets))
        _l_(420451)
    elif _a_(420453, _n_(420452, "event", lambda: event), "key") == _a_(420455, _n_(420454, "pygame", lambda: pygame), "K_q"):
        _l_(420460)

        _c_(420458, _a_(420457, _n_(420456, "sys", lambda: sys), "exit"))
        _l_(420459)
def fire_bullet(ai_settings, screen, ship, bullets):
    _l_(420482)

    """Fire a bullet if limit is not reached."""
    # Create a new bullet and add it to the bullets group.
    if _c_(420467, _n_(420465, "len", lambda: len), _n_(420466, "bullets", lambda: bullets)) < _a_(420469, _n_(420468, "ai_settings", lambda: ai_settings), "bullets_allowed"):
        _l_(420481)

        new_bullet = _c_(420474, _n_(420470, "Bullet", lambda: Bullet), _n_(420471, "ai_settings", lambda: ai_settings), _n_(420472, "screen", lambda: screen), _n_(420473, "ship", lambda: ship))
        _l_(420475)
        _c_(420479, _a_(420477, _n_(420476, "bullets", lambda: bullets), "add"), _n_(420478, "new_bullet", lambda: new_bullet))
        _l_(420480)

def check_keyup_events(event, ship):
    _l_(420497)

    if _a_(420484, _n_(420483, "event", lambda: event), "key") == _a_(420486, _n_(420485, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(420496)

        _n_(420487, "ship", lambda: ship).moving_right = False
        _l_(420488)
    elif _a_(420490, _n_(420489, "event", lambda: event), "key") == _a_(420492, _n_(420491, "pygame", lambda: pygame), "K_LEFT"):
        _l_(420495)

        _n_(420493, "ship", lambda: ship).moving_left = False
        _l_(420494)

def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    _l_(420552)

    """Respond to keypresses and mouse events."""
    for event in _c_(420501, _a_(420500, _a_(420499, _n_(420498, "pygame", lambda: pygame), "event"), "get")):
        _l_(420551)

        if _a_(420503, _n_(420502, "event", lambda: event), "type") == _a_(420505, _n_(420504, "pygame", lambda: pygame), "QUIT"):
            _l_(420550)

            _c_(420508, _a_(420507, _n_(420506, "sys", lambda: sys), "exit"))
            _l_(420509)
        elif _a_(420511, _n_(420510, "event", lambda: event), "type") == _a_(420513, _n_(420512, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(420549)

            _c_(420520, _n_(420514, "check_keydown_events", lambda: check_keydown_events), _n_(420515, "event", lambda: event), _n_(420516, "ai_settings", lambda: ai_settings), _n_(420517, "screen", lambda: screen), _n_(420518, "ship", lambda: ship), _n_(420519, "bullets", lambda: bullets))                 
            _l_(420521)                 
        elif _a_(420523, _n_(420522, "event", lambda: event), "type") == _a_(420525, _n_(420524, "pygame", lambda: pygame), "KEYUP"):
            _l_(420548)

            _c_(420529, _n_(420526, "check_keyup_events", lambda: check_keyup_events), _n_(420527, "event", lambda: event), _n_(420528, "ship", lambda: ship))
            _l_(420530)
        elif _a_(420532, _n_(420531, "event", lambda: event), "type") == _a_(420534, _n_(420533, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
            _l_(420547)

            mouse_x, mouse_y = _c_(420538, _a_(420537, _a_(420536, _n_(420535, "pygame", lambda: pygame), "mouse"), "get_pos"))
            _l_(420539)
            _c_(420545, _n_(420540, "check_play_button", lambda: check_play_button), _n_(420541, "stats", lambda: stats), _n_(420542, "play_button", lambda: play_button), _n_(420543, "mouse_x", lambda: mouse_x), _n_(420544, "mouse_y", lambda: mouse_y))
            _l_(420546)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    _l_(420562)

    """Start a new game when the player clicks Play."""
    if _c_(420558, _a_(420555, _a_(420554, _n_(420553, "play_button", lambda: play_button), "rect"), "collidepoint"), _n_(420556, "mouse_x", lambda: mouse_x), _n_(420557, "mouse_y", lambda: mouse_y)):
        _l_(420561)

        _n_(420559, "stats", lambda: stats).game_active = True
        _l_(420560)
def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    _l_(420598)

    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    _c_(420567, _a_(420564, _n_(420563, "screen", lambda: screen), "fill"), _a_(420566, _n_(420565, "ai_settings", lambda: ai_settings), "bg_color"))
    _l_(420568)
    # Redraw all bullets behind ship and aliens.
    for bullet in _c_(420571, _a_(420570, _n_(420569, "bullets", lambda: bullets), "sprites")):
        _l_(420576)

        _c_(420574, _a_(420573, _n_(420572, "bullet", lambda: bullet), "draw_bullet"))
        _l_(420575)
    _c_(420579, _a_(420578, _n_(420577, "ship", lambda: ship), "blitme"))
    _l_(420580)
    _c_(420584, _a_(420582, _n_(420581, "aliens", lambda: aliens), "draw"), _n_(420583, "screen", lambda: screen))
    _l_(420585)
    
    # Draw the play button if the game is inactive.
    if not _a_(420587, _n_(420586, "stats", lambda: stats), "game_active"):
        _l_(420592)

        _c_(420590, _a_(420589, _n_(420588, "play_button", lambda: play_button), "draw_button"))
        _l_(420591)
    # Make the most recently drawn screen visible.
    _c_(420596, _a_(420595, _a_(420594, _n_(420593, "pygame", lambda: pygame), "display"), "flip"))
    _l_(420597)

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    _l_(420624)

    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    _c_(420601, _a_(420600, _n_(420599, "bullets", lambda: bullets), "update"))
    _l_(420602)
    
    # Get rid of bullets that have disappeared.
    for bullet in _c_(420605, _a_(420604, _n_(420603, "bullets", lambda: bullets), "copy")):
        _l_(420615)

        if _a_(420608, _a_(420607, _n_(420606, "bullet", lambda: bullet), "rect"), "bottom") <= 0:
            _l_(420614)

            _c_(420612, _a_(420610, _n_(420609, "bullets", lambda: bullets), "remove"), _n_(420611, "bullet", lambda: bullet))
            _l_(420613)
    
    _c_(420622, _n_(420616, "check_bullet_alien_collisions", lambda: check_bullet_alien_collisions), _n_(420617, "ai_settings", lambda: ai_settings), _n_(420618, "screen", lambda: screen), _n_(420619, "ship", lambda: ship), _n_(420620, "aliens", lambda: aliens), _n_(420621, "bullets", lambda: bullets))
    _l_(420623)
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    _l_(420647)

    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = _c_(420630, _a_(420627, _a_(420626, _n_(420625, "pygame", lambda: pygame), "sprite"), "groupcollide"), _n_(420628, "bullets", lambda: bullets), _n_(420629, "aliens", lambda: aliens), True, True)        
    _l_(420631)        
    if _c_(420634, _n_(420632, "len", lambda: len), _n_(420633, "aliens", lambda: aliens)) ==0:
        _l_(420646)

        #Destroy existing bullets and create new fleet.
        _c_(420637, _a_(420636, _n_(420635, "bullets", lambda: bullets), "empty"))
        _l_(420638)
        _c_(420644, _n_(420639, "create_fleet", lambda: create_fleet), _n_(420640, "ai_settings", lambda: ai_settings), _n_(420641, "screen", lambda: screen), _n_(420642, "ship", lambda: ship), _n_(420643, "aliens", lambda: aliens))
        _l_(420645)
def get_number_aliens_x(ai_settings, alien_width):
    _l_(420659)

    """Determine the number of aliens that fit in a row."""
    available_space_x = _a_(420649, _n_(420648, "ai_settings", lambda: ai_settings), "screen_width") - 2 * _n_(420650, "alien_width", lambda: alien_width)
    _l_(420651)
    number_aliens_x = _c_(420655, _n_(420652, "int", lambda: int), _n_(420653, "available_space_x", lambda: available_space_x) / (2 * _n_(420654, "alien_width", lambda: alien_width)))
    _l_(420656)
    aux = _n_(420657, "number_aliens_x", lambda: number_aliens_x)
    _l_(420658)
    return aux

def get_number_rows(ai_settings, ship_height, alien_height):
    _l_(420672)

    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (_a_(420661, _n_(420660, "ai_settings", lambda: ai_settings), "screen_height") - (3 * _n_(420662, "alien_height", lambda: alien_height)) - _n_(420663, "ship_height", lambda: ship_height))
    _l_(420664)
    number_rows = _c_(420668, _n_(420665, "int", lambda: int), _n_(420666, "available_space_y", lambda: available_space_y) / (2 * _n_(420667, "alien_height", lambda: alien_height)))
    _l_(420669)
    aux = _n_(420670, "number_rows", lambda: number_rows)
    _l_(420671)
    return aux
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    _l_(420707)

    """Create an alien and place it in the row."""
    alien = _c_(420676, _n_(420673, "Alien", lambda: Alien), _n_(420674, "ai_settings", lambda: ai_settings), _n_(420675, "screen", lambda: screen))
    _l_(420677)
    alien_width = _a_(420680, _a_(420679, _n_(420678, "alien", lambda: alien), "rect"), "width")
    _l_(420681)
    _n_(420682, "alien", lambda: alien).x = _n_(420683, "alien_width", lambda: alien_width) + 2 * _n_(420684, "alien_width", lambda: alien_width) * _n_(420685, "alien_number", lambda: alien_number)
    _l_(420686)
    _a_(420688, _n_(420687, "alien", lambda: alien), "rect").x = _a_(420690, _n_(420689, "alien", lambda: alien), "x")
    _l_(420691)
    _a_(420693, _n_(420692, "alien", lambda: alien), "rect").y = _a_(420696, _a_(420695, _n_(420694, "alien", lambda: alien), "rect"), "height") + 2 * _a_(420699, _a_(420698, _n_(420697, "alien", lambda: alien), "rect"), "height") * _n_(420700, "row_number", lambda: row_number)
    _l_(420701)
    _c_(420705, _a_(420703, _n_(420702, "aliens", lambda: aliens), "add"), _n_(420704, "alien", lambda: alien))
    _l_(420706)
def create_fleet(ai_settings, screen, ship, aliens):
    _l_(420746)

    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = _c_(420711, _n_(420708, "Alien", lambda: Alien), _n_(420709, "ai_settings", lambda: ai_settings), _n_(420710, "screen", lambda: screen))
    _l_(420712)
    number_aliens_x = _c_(420718, _n_(420713, "get_number_aliens_x", lambda: get_number_aliens_x), _n_(420714, "ai_settings", lambda: ai_settings), _a_(420717, _a_(420716, _n_(420715, "alien", lambda: alien), "rect"), "width"))    
    _l_(420719)    
    number_rows = _c_(420728, _n_(420720, "get_number_rows", lambda: get_number_rows), _n_(420721, "ai_settings", lambda: ai_settings), _a_(420724, _a_(420723, _n_(420722, "ship", lambda: ship), "rect"), "height"), _a_(420727, _a_(420726, _n_(420725, "alien", lambda: alien), "rect"), "height"))
    _l_(420729)
    
    # Create the first row of aliens.
    for row_number in _c_(420732, _n_(420730, "range", lambda: range), _n_(420731, "number_rows", lambda: number_rows)):
        _l_(420745)

        for alien_number in _c_(420735, _n_(420733, "range", lambda: range), _n_(420734, "number_aliens_x", lambda: number_aliens_x)):
            _l_(420744)

            _c_(420742, _n_(420736, "create_alien", lambda: create_alien), _n_(420737, "ai_settings", lambda: ai_settings), _n_(420738, "screen", lambda: screen), _n_(420739, "aliens", lambda: aliens), _n_(420740, "alien_number", lambda: alien_number), _n_(420741, "row_number", lambda: row_number))
            _l_(420743)
def check_fleet_edges(ai_settings, aliens):
    _l_(420761)

    """Respond appropriately if any aliens have reached an edge."""
    for alien in _c_(420749, _a_(420748, _n_(420747, "aliens", lambda: aliens), "sprites")):
        _l_(420760)

        if _c_(420752, _a_(420751, _n_(420750, "alien", lambda: alien), "check_edges")):
            _l_(420759)

            _c_(420756, _n_(420753, "change_fleet_direction", lambda: change_fleet_direction), _n_(420754, "ai_settings", lambda: ai_settings), _n_(420755, "aliens", lambda: aliens))
            _l_(420757)
            break
            _l_(420758)
def change_fleet_direction(ai_settings, aliens):
    _l_(420772)

    """Drop the entire fleet and change the fleet's direction."""
    for alien in _c_(420764, _a_(420763, _n_(420762, "aliens", lambda: aliens), "sprites")):
        _l_(420769)

        _a_(420766, _n_(420765, "alien", lambda: alien), "rect").y += _n_(420767, "ai_settings", lambda: ai_settings).fleet_drop_speed
        _l_(420768)
    _n_(420770, "ai_settings", lambda: ai_settings).fleet_direction *= -1
    _l_(420771)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    _l_(420802)

    """Respond to ship being hit by alien."""
    if _a_(420774, _n_(420773, "stats", lambda: stats), "ships_left") > 0:
        _l_(420779)

        # Decrement ships_left.
        _n_(420775, "stats", lambda: stats).ships_left -= 1
        _l_(420776)
    
    else:
        _n_(420777, "stats", lambda: stats).game_active = False
        _l_(420778)
    
    # Empty the list o faliens and bullets.
    _c_(420782, _a_(420781, _n_(420780, "aliens", lambda: aliens), "empty"))
    _l_(420783)
    _c_(420786, _a_(420785, _n_(420784, "bullets", lambda: bullets), "empty"))
    _l_(420787)
    
    # Create a new fleet and center the ship.
    _c_(420793, _n_(420788, "create_fleet", lambda: create_fleet), _n_(420789, "ai_settings", lambda: ai_settings), _n_(420790, "screen", lambda: screen), _n_(420791, "ship", lambda: ship), _n_(420792, "aliens", lambda: aliens))
    _l_(420794)
    _c_(420797, _a_(420796, _n_(420795, "ship", lambda: ship), "center_ship"))
    _l_(420798)
    
    # Pause.
    _c_(420800, _n_(420799, "sleep", lambda: sleep), 0.5)
    _l_(420801)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    _l_(420827)

    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = _c_(420805, _a_(420804, _n_(420803, "screen", lambda: screen), "get_rect"))
    _l_(420806)
    for alien in _c_(420809, _a_(420808, _n_(420807, "aliens", lambda: aliens), "sprites")):
        _l_(420826)

        if _a_(420812, _a_(420811, _n_(420810, "alien", lambda: alien), "rect"), "bottom") >= _a_(420814, _n_(420813, "screen_rect", lambda: screen_rect), "bottom"):
            _l_(420825)

            # Treat this the same as if ship gets hit.
            _c_(420822, _n_(420815, "ship_hit", lambda: ship_hit), _n_(420816, "ai_settings", lambda: ai_settings), _n_(420817, "stats", lambda: stats), _n_(420818, "screen", lambda: screen), _n_(420819, "ship", lambda: ship), _n_(420820, "aliens", lambda: aliens), _n_(420821, "bullets", lambda: bullets))
            _l_(420823)
            break
            _l_(420824)
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    _l_(420865)

    """Check if the fleet is at an edge, and update positions of all aliens in fleet."""
    _c_(420831, _n_(420828, "check_fleet_edges", lambda: check_fleet_edges), _n_(420829, "ai_settings", lambda: ai_settings), _n_(420830, "aliens", lambda: aliens))
    _l_(420832)
    _c_(420835, _a_(420834, _n_(420833, "aliens", lambda: aliens), "update"))
    _l_(420836)
    
    # Look for alien-ship collisions.
    if _c_(420842, _a_(420839, _a_(420838, _n_(420837, "pygame", lambda: pygame), "sprite"), "spritecollideany"), _n_(420840, "ship", lambda: ship), _n_(420841, "aliens", lambda: aliens)):
        _l_(420855)

        _c_(420850, _n_(420843, "ship_hit", lambda: ship_hit), _n_(420844, "ai_settings", lambda: ai_settings), _n_(420845, "stats", lambda: stats), _n_(420846, "screen", lambda: screen), _n_(420847, "ship", lambda: ship), _n_(420848, "aliens", lambda: aliens), _n_(420849, "bullets", lambda: bullets))
        _l_(420851)
        _c_(420853, _n_(420852, "print", lambda: print), "Ship hit!!!")
        _l_(420854)

    # Look for aliens hitting the bottom of the screen.
    _c_(420863, _n_(420856, "check_aliens_bottom", lambda: check_aliens_bottom), _n_(420857, "ai_settings", lambda: ai_settings), _n_(420858, "stats", lambda: stats), _n_(420859, "screen", lambda: screen), _n_(420860, "ship", lambda: ship), _n_(420861, "aliens", lambda: aliens), _n_(420862, "bullets", lambda: bullets))
    _l_(420864)
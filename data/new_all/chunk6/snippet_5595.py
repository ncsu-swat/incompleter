# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67491264/typeerror-exceptions-must-derive-from-baseexception-im-trying-to-pause-my-ga
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, sys, random
    _l_(338570)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(338572)

except ImportError:
    pass
try:
    from pygame.math import Vector2
    _l_(338574)

except ImportError:
    pass
try:
    from pathlib import *
    _l_(338576)

except ImportError:
    pass

cell_size = 40
_l_(338577)
cell_number = 19
_l_(338578)
screen_color = (175, 215, 70)
_l_(338579)
snake_color = (183, 111, 122)
_l_(338580)
food_color = (70, 70, 214)
_l_(338581)
score_color = (56, 76, 11)
_l_(338582)
score_bg_color = (167, 211, 65)
_l_(338583)

_c_(338586, _a_(338585, _n_(338584, "pygame", lambda: pygame), "init"))
_l_(338587)
screen = _c_(338595, _a_(338590, _a_(338589, _n_(338588, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(338591, "cell_number", lambda: cell_number) * _n_(338592, "cell_size", lambda: cell_size), _n_(338593, "cell_number", lambda: cell_number) * _n_(338594, "cell_size", lambda: cell_size)))
_l_(338596)
base_directory = _c_(338602, _a_(338601, _a_(338600, _c_(338599, _n_(338597, "Path", lambda: Path), _n_(338598, "__file__", lambda: __file__)), "parent"), "absolute"))
_l_(338603)
apple_path = 'snake2_resources/images/apple.png'
_l_(338604)
apple = _c_(338612, _a_(338611, _c_(338610, _a_(338607, _a_(338606, _n_(338605, "pygame", lambda: pygame), "image"), "load"), _n_(338608, "base_directory", lambda: base_directory) / _n_(338609, "apple_path", lambda: apple_path)), "convert_alpha"))
_l_(338613)
font_path = _n_(338614, "base_directory", lambda: base_directory) / 'snake2_resources/font/poetsen_one_regular.ttf'
_l_(338615)
game_font = _c_(338620, _a_(338618, _a_(338617, _n_(338616, "pygame", lambda: pygame), "font"), "Font"), _n_(338619, "font_path", lambda: font_path), 24)
_l_(338621)
clock = _c_(338625, _a_(338624, _a_(338623, _n_(338622, "pygame", lambda: pygame), "time"), "Clock"))
_l_(338626)

class Snake:
    _l_(339044)

    def __init__(self):
        _l_(338769)

        _n_(338627, "self", lambda: self).snake_body = [_c_(338629, _n_(338628, "Vector2", lambda: Vector2), 5, 10),_c_(338631, _n_(338630, "Vector2", lambda: Vector2), 4, 10),_c_(338633, _n_(338632, "Vector2", lambda: Vector2), 3, 10)]
        _l_(338634)
        _n_(338635, "self", lambda: self).direction = _c_(338637, _n_(338636, "Vector2", lambda: Vector2), 0, 0)
        _l_(338638)
        _n_(338639, "self", lambda: self).new_body = False
        _l_(338640)
        snake_path = _n_(338641, "base_directory", lambda: base_directory) / 'snake2_resources/images/snake'
        _l_(338642)

        _n_(338643, "self", lambda: self).head_up = _c_(338650, _a_(338649, _c_(338648, _a_(338646, _a_(338645, _n_(338644, "pygame", lambda: pygame), "image"), "load"), _n_(338647, "snake_path", lambda: snake_path) / 'head_up.png'), "convert_alpha"))
        _l_(338651)
        _n_(338652, "self", lambda: self).head_down = _c_(338659, _a_(338658, _c_(338657, _a_(338655, _a_(338654, _n_(338653, "pygame", lambda: pygame), "image"), "load"), _n_(338656, "snake_path", lambda: snake_path) / 'head_down.png'), "convert_alpha"))
        _l_(338660)
        _n_(338661, "self", lambda: self).head_right = _c_(338668, _a_(338667, _c_(338666, _a_(338664, _a_(338663, _n_(338662, "pygame", lambda: pygame), "image"), "load"), _n_(338665, "snake_path", lambda: snake_path) / 'head_right.png'), "convert_alpha"))
        _l_(338669)
        _n_(338670, "self", lambda: self).head_left = _c_(338677, _a_(338676, _c_(338675, _a_(338673, _a_(338672, _n_(338671, "pygame", lambda: pygame), "image"), "load"), _n_(338674, "snake_path", lambda: snake_path) / 'head_left.png'), "convert_alpha"))
        _l_(338678)
        
        _n_(338679, "self", lambda: self).tail_up = _c_(338686, _a_(338685, _c_(338684, _a_(338682, _a_(338681, _n_(338680, "pygame", lambda: pygame), "image"), "load"), _n_(338683, "snake_path", lambda: snake_path) / 'tail_up.png'), "convert_alpha"))
        _l_(338687)
        _n_(338688, "self", lambda: self).tail_down = _c_(338695, _a_(338694, _c_(338693, _a_(338691, _a_(338690, _n_(338689, "pygame", lambda: pygame), "image"), "load"), _n_(338692, "snake_path", lambda: snake_path) / 'tail_down.png'), "convert_alpha"))
        _l_(338696)
        _n_(338697, "self", lambda: self).tail_right = _c_(338704, _a_(338703, _c_(338702, _a_(338700, _a_(338699, _n_(338698, "pygame", lambda: pygame), "image"), "load"), _n_(338701, "snake_path", lambda: snake_path) / 'tail_right.png'), "convert_alpha"))
        _l_(338705)
        _n_(338706, "self", lambda: self).tail_left = _c_(338713, _a_(338712, _c_(338711, _a_(338709, _a_(338708, _n_(338707, "pygame", lambda: pygame), "image"), "load"), _n_(338710, "snake_path", lambda: snake_path) / 'tail_left.png'), "convert_alpha"))
        _l_(338714)
        
        _n_(338715, "self", lambda: self).body_vertical = _c_(338722, _a_(338721, _c_(338720, _a_(338718, _a_(338717, _n_(338716, "pygame", lambda: pygame), "image"), "load"), _n_(338719, "snake_path", lambda: snake_path) / 'body_vertical.png'), "convert_alpha"))
        _l_(338723)
        _n_(338724, "self", lambda: self).body_horizontal = _c_(338731, _a_(338730, _c_(338729, _a_(338727, _a_(338726, _n_(338725, "pygame", lambda: pygame), "image"), "load"), _n_(338728, "snake_path", lambda: snake_path) / 'body_horizontal.png'), "convert_alpha"))
        _l_(338732)
        
        _n_(338733, "self", lambda: self).body_tr = _c_(338740, _a_(338739, _c_(338738, _a_(338736, _a_(338735, _n_(338734, "pygame", lambda: pygame), "image"), "load"), _n_(338737, "snake_path", lambda: snake_path) / 'body_tr.png'), "convert_alpha"))
        _l_(338741)
        _n_(338742, "self", lambda: self).body_tl = _c_(338749, _a_(338748, _c_(338747, _a_(338745, _a_(338744, _n_(338743, "pygame", lambda: pygame), "image"), "load"), _n_(338746, "snake_path", lambda: snake_path) / 'body_tl.png'), "convert_alpha"))
        _l_(338750)
        _n_(338751, "self", lambda: self).body_br = _c_(338758, _a_(338757, _c_(338756, _a_(338754, _a_(338753, _n_(338752, "pygame", lambda: pygame), "image"), "load"), _n_(338755, "snake_path", lambda: snake_path) / 'body_br.png'), "convert_alpha"))
        _l_(338759)
        _n_(338760, "self", lambda: self).body_bl = _c_(338767, _a_(338766, _c_(338765, _a_(338763, _a_(338762, _n_(338761, "pygame", lambda: pygame), "image"), "load"), _n_(338764, "snake_path", lambda: snake_path) / 'body_bl.png'), "convert_alpha"))
        _l_(338768)

    def update_snake_head(self):
        _l_(338807)

        head_direction = _a_(338771, _n_(338770, "self", lambda: self), "snake_body")[1] - _a_(338773, _n_(338772, "self", lambda: self), "snake_body")[0]
        _l_(338774)

        if _n_(338775, "head_direction", lambda: head_direction) == _c_(338777, _n_(338776, "Vector2", lambda: Vector2), 1, 0):
            _l_(338806)

            _n_(338778, "self", lambda: self).head = _a_(338780, _n_(338779, "self", lambda: self), "head_left")
            _l_(338781)
        elif _n_(338782, "head_direction", lambda: head_direction) == _c_(338784, _n_(338783, "Vector2", lambda: Vector2), -1, 0):
            _l_(338805)

            _n_(338785, "self", lambda: self).head = _a_(338787, _n_(338786, "self", lambda: self), "head_right")
            _l_(338788)
        elif _n_(338789, "head_direction", lambda: head_direction) == _c_(338791, _n_(338790, "Vector2", lambda: Vector2), 0, 1):
            _l_(338804)

            _n_(338792, "self", lambda: self).head = _a_(338794, _n_(338793, "self", lambda: self), "head_up")
            _l_(338795)
        elif _n_(338796, "head_direction", lambda: head_direction) == _c_(338798, _n_(338797, "Vector2", lambda: Vector2), 0, -1):
            _l_(338803)

            _n_(338799, "self", lambda: self).head = _a_(338801, _n_(338800, "self", lambda: self), "head_down")
            _l_(338802)

    def update_snake_tail(self):
        _l_(338845)

        tail_direction = _a_(338809, _n_(338808, "self", lambda: self), "snake_body")[-2] - _a_(338811, _n_(338810, "self", lambda: self), "snake_body")[-1]
        _l_(338812)

        if _n_(338813, "tail_direction", lambda: tail_direction) == _c_(338815, _n_(338814, "Vector2", lambda: Vector2), 1, 0):
            _l_(338844)

            _n_(338816, "self", lambda: self).tail = _a_(338818, _n_(338817, "self", lambda: self), "tail_left")
            _l_(338819)
        elif _n_(338820, "tail_direction", lambda: tail_direction) == _c_(338822, _n_(338821, "Vector2", lambda: Vector2), -1, 0):
            _l_(338843)

            _n_(338823, "self", lambda: self).tail = _a_(338825, _n_(338824, "self", lambda: self), "tail_right")
            _l_(338826)
        elif _n_(338827, "tail_direction", lambda: tail_direction) == _c_(338829, _n_(338828, "Vector2", lambda: Vector2), 0, 1):
            _l_(338842)

            _n_(338830, "self", lambda: self).tail = _a_(338832, _n_(338831, "self", lambda: self), "tail_up")
            _l_(338833)
        elif _n_(338834, "tail_direction", lambda: tail_direction) == _c_(338836, _n_(338835, "Vector2", lambda: Vector2), 0, -1):
            _l_(338841)

            _n_(338837, "self", lambda: self).tail = _a_(338839, _n_(338838, "self", lambda: self), "tail_down")
            _l_(338840)
    
    def draw_snake(self):
        _l_(338995)

        _c_(338848, _a_(338847, _n_(338846, "self", lambda: self), "update_snake_head"))
        _l_(338849)
        _c_(338852, _a_(338851, _n_(338850, "self", lambda: self), "update_snake_tail"))
        _l_(338853)

        for index, body_part in _c_(338857, _n_(338854, "enumerate", lambda: enumerate), _a_(338856, _n_(338855, "self", lambda: self), "snake_body")):
            _l_(338994)

            body_part_x = _a_(338859, _n_(338858, "body_part", lambda: body_part), "x") * _n_(338860, "cell_size", lambda: cell_size)
            _l_(338861)
            body_part_y = _a_(338863, _n_(338862, "body_part", lambda: body_part), "y") * _n_(338864, "cell_size", lambda: cell_size)
            _l_(338865)
            body_part_surface = _c_(338872, _a_(338867, _n_(338866, "pygame", lambda: pygame), "Rect"), _n_(338868, "body_part_x", lambda: body_part_x), _n_(338869, "body_part_y", lambda: body_part_y), _n_(338870, "cell_size", lambda: cell_size), _n_(338871, "cell_size", lambda: cell_size))
            _l_(338873)
            
            if _n_(338874, "index", lambda: index) == 0:
                _l_(338993)

                _c_(338880, _a_(338876, _n_(338875, "screen", lambda: screen), "blit"), _a_(338878, _n_(338877, "self", lambda: self), "head"), _n_(338879, "body_part_surface", lambda: body_part_surface))
                _l_(338881)

            elif _n_(338882, "index", lambda: index) == _c_(338886, _n_(338883, "len", lambda: len), _a_(338885, _n_(338884, "self", lambda: self), "snake_body")) - 1:
                _l_(338992)

                _c_(338892, _a_(338888, _n_(338887, "screen", lambda: screen), "blit"), _a_(338890, _n_(338889, "self", lambda: self), "tail"), _n_(338891, "body_part_surface", lambda: body_part_surface))
                _l_(338893)

            else:
                previous_body_part = _a_(338895, _n_(338894, "self", lambda: self), "snake_body")[_n_(338896, "index", lambda: index) + 1] - _n_(338897, "body_part", lambda: body_part)
                _l_(338898)
                next_body_part = _a_(338900, _n_(338899, "self", lambda: self), "snake_body")[_n_(338901, "index", lambda: index) - 1] - _n_(338902, "body_part", lambda: body_part)
                _l_(338903)

                if _a_(338905, _n_(338904, "previous_body_part", lambda: previous_body_part), "x") == _a_(338907, _n_(338906, "next_body_part", lambda: next_body_part), "x"):
                    _l_(338991)

                    _c_(338913, _a_(338909, _n_(338908, "screen", lambda: screen), "blit"), _a_(338911, _n_(338910, "self", lambda: self), "body_vertical"), _n_(338912, "body_part_surface", lambda: body_part_surface))
                    _l_(338914)

                elif _a_(338916, _n_(338915, "previous_body_part", lambda: previous_body_part), "y") == _a_(338918, _n_(338917, "next_body_part", lambda: next_body_part), "y"):
                    _l_(338990)

                    _c_(338924, _a_(338920, _n_(338919, "screen", lambda: screen), "blit"), _a_(338922, _n_(338921, "self", lambda: self), "body_horizontal"), _n_(338923, "body_part_surface", lambda: body_part_surface))
                    _l_(338925)

                else:
                    if _a_(338927, _n_(338926, "previous_body_part", lambda: previous_body_part), "x") == -1 and _a_(338929, _n_(338928, "next_body_part", lambda: next_body_part), "y") == -1 or _a_(338931, _n_(338930, "previous_body_part", lambda: previous_body_part), "y") == -1 and _a_(338933, _n_(338932, "next_body_part", lambda: next_body_part), "x") == -1:
                        _l_(338989)

                        _c_(338939, _a_(338935, _n_(338934, "screen", lambda: screen), "blit"), _a_(338937, _n_(338936, "self", lambda: self), "body_tl"), _n_(338938, "body_part_surface", lambda: body_part_surface))
                        _l_(338940)

                    elif _a_(338942, _n_(338941, "previous_body_part", lambda: previous_body_part), "x") == -1 and _a_(338944, _n_(338943, "next_body_part", lambda: next_body_part), "y") == 1 or _a_(338946, _n_(338945, "previous_body_part", lambda: previous_body_part), "y") == 1 and _a_(338948, _n_(338947, "next_body_part", lambda: next_body_part), "x") == -1:
                        _l_(338988)

                        _c_(338954, _a_(338950, _n_(338949, "screen", lambda: screen), "blit"), _a_(338952, _n_(338951, "self", lambda: self), "body_bl"), _n_(338953, "body_part_surface", lambda: body_part_surface))
                        _l_(338955)

                    elif _a_(338957, _n_(338956, "previous_body_part", lambda: previous_body_part), "x") == 1 and _a_(338959, _n_(338958, "next_body_part", lambda: next_body_part), "y") == -1 or _a_(338961, _n_(338960, "previous_body_part", lambda: previous_body_part), "y") == -1 and _a_(338963, _n_(338962, "next_body_part", lambda: next_body_part), "x") == 1:
                        _l_(338987)

                        _c_(338969, _a_(338965, _n_(338964, "screen", lambda: screen), "blit"), _a_(338967, _n_(338966, "self", lambda: self), "body_tr"), _n_(338968, "body_part_surface", lambda: body_part_surface))
                        _l_(338970)
                    
                    elif _a_(338972, _n_(338971, "previous_body_part", lambda: previous_body_part), "x") == 1 and _a_(338974, _n_(338973, "next_body_part", lambda: next_body_part), "y") == 1 or _a_(338976, _n_(338975, "previous_body_part", lambda: previous_body_part), "y") == 1 and _a_(338978, _n_(338977, "next_body_part", lambda: next_body_part), "x") == 1:
                        _l_(338986)

                        _c_(338984, _a_(338980, _n_(338979, "screen", lambda: screen), "blit"), _a_(338982, _n_(338981, "self", lambda: self), "body_br"), _n_(338983, "body_part_surface", lambda: body_part_surface))
                        _l_(338985)

    def add_body(self):
        _l_(338998)

        _n_(338996, "self", lambda: self).new_body = True
        _l_(338997)
    
    def move_snake(self):
        _l_(339030)

        if _a_(339000, _n_(338999, "self", lambda: self), "new_body") == True:
            _l_(339029)

            snake_body_copy = _a_(339002, _n_(339001, "self", lambda: self), "snake_body")[:]
            _l_(339003)
            _c_(339009, _a_(339005, _n_(339004, "snake_body_copy", lambda: snake_body_copy), "insert"), 0, _n_(339006, "snake_body_copy", lambda: snake_body_copy)[0] + _a_(339008, _n_(339007, "self", lambda: self), "direction"))
            _l_(339010)
            _n_(339011, "self", lambda: self).snake_body = _n_(339012, "snake_body_copy", lambda: snake_body_copy)[:]
            _l_(339013)
            _n_(339014, "self", lambda: self).new_body = False
            _l_(339015)
    
        else:
            snake_body_copy = _a_(339017, _n_(339016, "self", lambda: self), "snake_body")[: -1]
            _l_(339018)
            _c_(339024, _a_(339020, _n_(339019, "snake_body_copy", lambda: snake_body_copy), "insert"), 0, _n_(339021, "snake_body_copy", lambda: snake_body_copy)[0] + _a_(339023, _n_(339022, "self", lambda: self), "direction"))
            _l_(339025)
            _n_(339026, "self", lambda: self).snake_body = _n_(339027, "snake_body_copy", lambda: snake_body_copy)[:]
            _l_(339028)

    def reset(self):
        _l_(339043)

        _n_(339031, "self", lambda: self).snake_body = [_c_(339033, _n_(339032, "Vector2", lambda: Vector2), 5, 10), _c_(339035, _n_(339034, "Vector2", lambda: Vector2), 4, 10), _c_(339037, _n_(339036, "Vector2", lambda: Vector2), 3, 10)]
        _l_(339038)
        _n_(339039, "self", lambda: self).direction = _c_(339041, _n_(339040, "Vector2", lambda: Vector2), 0, 0)
        _l_(339042)

class Food:
    _l_(339092)

    def __init__(self):
        _l_(339049)

        _c_(339047, _a_(339046, _n_(339045, "self", lambda: self), "randomize"))
        _l_(339048)

    def draw_food(self):
        _l_(339070)

        food_surface = _c_(339062, _a_(339051, _n_(339050, "pygame", lambda: pygame), "Rect"), _a_(339054, _a_(339053, _n_(339052, "self", lambda: self), "position"), "x") * _n_(339055, "cell_size", lambda: cell_size), _a_(339058, _a_(339057, _n_(339056, "self", lambda: self), "position"), "y") * _n_(339059, "cell_size", lambda: cell_size), _n_(339060, "cell_size", lambda: cell_size), _n_(339061, "cell_size", lambda: cell_size))
        _l_(339063)
        _c_(339068, _a_(339065, _n_(339064, "screen", lambda: screen), "blit"), _n_(339066, "apple", lambda: apple), _n_(339067, "food_surface", lambda: food_surface))
        _l_(339069)

    def randomize(self):
        _l_(339091)

        _n_(339071, "self", lambda: self).food_x = _c_(339075, _a_(339073, _n_(339072, "random", lambda: random), "randint"), 0, _n_(339074, "cell_number", lambda: cell_number) - 1)
        _l_(339076)
        _n_(339077, "self", lambda: self).food_y = _c_(339081, _a_(339079, _n_(339078, "random", lambda: random), "randint"), 0, _n_(339080, "cell_number", lambda: cell_number) - 1)
        _l_(339082)
        _n_(339083, "self", lambda: self).position = _c_(339089, _n_(339084, "Vector2", lambda: Vector2), _a_(339086, _n_(339085, "self", lambda: self), "food_x"), _a_(339088, _n_(339087, "self", lambda: self), "food_y"))
        _l_(339090)

class Game_Snake2:
    _l_(339518)

    def __init__(self):
        _l_(339114)

        _n_(339093, "self", lambda: self).screen_update = _a_(339095, _n_(339094, "pygame", lambda: pygame), "USEREVENT")
        _l_(339096)
        _c_(339102, _a_(339099, _a_(339098, _n_(339097, "pygame", lambda: pygame), "time"), "set_timer"), _a_(339101, _n_(339100, "self", lambda: self), "screen_update"), 156)
        _l_(339103)
        _n_(339104, "self", lambda: self).snake = _c_(339106, _n_(339105, "Snake", lambda: Snake))
        _l_(339107)
        _n_(339108, "self", lambda: self).food = _c_(339110, _n_(339109, "Food", lambda: Food))
        _l_(339111)
        _n_(339112, "self", lambda: self).pause = False
        _l_(339113)

    def draw_grass(self):
        _l_(339170)

        grass_color = (167, 209, 61)
        _l_(339115)
        
        for row in _c_(339118, _n_(339116, "range", lambda: range), _n_(339117, "cell_number", lambda: cell_number)):
            _l_(339169)

            if _n_(339119, "row", lambda: row) % 2 == 0:
                _l_(339168)

                for column in _c_(339122, _n_(339120, "range", lambda: range), _n_(339121, "cell_number", lambda: cell_number)):
                    _l_(339143)

                    if _n_(339123, "column", lambda: column) % 2 == 0:
                        _l_(339142)

                        grass_surface = _c_(339132, _a_(339125, _n_(339124, "pygame", lambda: pygame), "Rect"), _n_(339126, "column", lambda: column) * _n_(339127, "cell_size", lambda: cell_size), _n_(339128, "row", lambda: row) * _n_(339129, "cell_size", lambda: cell_size), _n_(339130, "cell_size", lambda: cell_size), _n_(339131, "cell_size", lambda: cell_size))
                        _l_(339133)
                        _c_(339140, _a_(339136, _a_(339135, _n_(339134, "pygame", lambda: pygame), "draw"), "rect"), _n_(339137, "screen", lambda: screen), _n_(339138, "grass_color", lambda: grass_color), _n_(339139, "grass_surface", lambda: grass_surface))
                        _l_(339141)

            else:
                for column in _c_(339146, _n_(339144, "range", lambda: range), _n_(339145, "cell_number", lambda: cell_number)):
                    _l_(339167)

                    if _n_(339147, "column", lambda: column) % 2 != 0:
                        _l_(339166)

                        grass_surface = _c_(339156, _a_(339149, _n_(339148, "pygame", lambda: pygame), "Rect"), _n_(339150, "column", lambda: column) * _n_(339151, "cell_size", lambda: cell_size), _n_(339152, "row", lambda: row) * _n_(339153, "cell_size", lambda: cell_size), _n_(339154, "cell_size", lambda: cell_size), _n_(339155, "cell_size", lambda: cell_size))
                        _l_(339157)
                        _c_(339164, _a_(339160, _a_(339159, _n_(339158, "pygame", lambda: pygame), "draw"), "rect"), _n_(339161, "screen", lambda: screen), _n_(339162, "grass_color", lambda: grass_color), _n_(339163, "grass_surface", lambda: grass_surface))
                        _l_(339165)
    
    def display_score(self):
        _l_(339247)

        score = _c_(339177, _n_(339171, "str", lambda: str), _c_(339176, _n_(339172, "len", lambda: len), _a_(339175, _a_(339174, _n_(339173, "self", lambda: self), "snake"), "snake_body")) - 3)
        _l_(339178)
        score_surface = _c_(339183, _a_(339180, _n_(339179, "game_font", lambda: game_font), "render"), _n_(339181, "score", lambda: score), True, _n_(339182, "score_color", lambda: score_color))
        _l_(339184)
        score_x = _n_(339185, "cell_size", lambda: cell_size) * _n_(339186, "cell_number", lambda: cell_number) - 60
        _l_(339187)
        score_y = _n_(339188, "cell_size", lambda: cell_size) * _n_(339189, "cell_number", lambda: cell_number) - 40
        _l_(339190)
        score_shape = _c_(339195, _a_(339192, _n_(339191, "score_surface", lambda: score_surface), "get_rect"), center=(_n_(339193, "score_x", lambda: score_x), _n_(339194, "score_y", lambda: score_y)))
        _l_(339196)
        score_apple = _c_(339203, _a_(339198, _n_(339197, "apple", lambda: apple), "get_rect"), midright = (_a_(339200, _n_(339199, "score_shape", lambda: score_shape), "left"), _a_(339202, _n_(339201, "score_shape", lambda: score_shape), "centery")))
        _l_(339204)
        score_background = _c_(339217, _a_(339206, _n_(339205, "pygame", lambda: pygame), "Rect"), _a_(339208, _n_(339207, "score_apple", lambda: score_apple), "left"), _a_(339210, _n_(339209, "score_apple", lambda: score_apple), "top"), _a_(339212, _n_(339211, "score_apple", lambda: score_apple), "width") + _a_(339214, _n_(339213, "score_shape", lambda: score_shape), "width") + 6, _a_(339216, _n_(339215, "score_apple", lambda: score_apple), "height"))
        _l_(339218)
        
        _c_(339225, _a_(339221, _a_(339220, _n_(339219, "pygame", lambda: pygame), "draw"), "rect"), _n_(339222, "screen", lambda: screen), _n_(339223, "score_bg_color", lambda: score_bg_color), _n_(339224, "score_background", lambda: score_background))
        _l_(339226)
        _c_(339231, _a_(339228, _n_(339227, "screen", lambda: screen), "blit"), _n_(339229, "score_surface", lambda: score_surface), _n_(339230, "score_shape", lambda: score_shape))
        _l_(339232)
        _c_(339237, _a_(339234, _n_(339233, "screen", lambda: screen), "blit"), _n_(339235, "apple", lambda: apple), _n_(339236, "score_apple", lambda: score_apple))
        _l_(339238)
        _c_(339245, _a_(339241, _a_(339240, _n_(339239, "pygame", lambda: pygame), "draw"), "rect"), _n_(339242, "screen", lambda: screen), _n_(339243, "score_color", lambda: score_color), _n_(339244, "score_background", lambda: score_background), 2)
        _l_(339246)
    
    def draw_elements(self):
        _l_(339266)

        _c_(339250, _a_(339249, _n_(339248, "self", lambda: self), "draw_grass"))
        _l_(339251)
        _c_(339255, _a_(339254, _a_(339253, _n_(339252, "self", lambda: self), "snake"), "draw_snake"))
        _l_(339256)
        _c_(339260, _a_(339259, _a_(339258, _n_(339257, "self", lambda: self), "food"), "draw_food"))
        _l_(339261)
        _c_(339264, _a_(339263, _n_(339262, "self", lambda: self), "display_score"))
        _l_(339265)
    
    def play_sound(self, sound_name):
        _l_(339280)

        sound_path = _n_(339267, "base_directory", lambda: base_directory) / f'snake2_resources/sounds/{_n_(339268, "sound_name", lambda: sound_name)}.mp3'
        _l_(339269)
        sound = _c_(339274, _a_(339272, _a_(339271, _n_(339270, 'pygame', lambda: pygame), 'mixer'), 'Sound'), _n_(339273, 'sound_path', lambda: sound_path))
        _l_(339275)
        _c_(339278, _a_(339277, _n_(339276, 'sound', lambda: sound), 'play'))
        _l_(339279)
    
    def is_hit(self):
        _l_(339316)

        if _a_(339283, _a_(339282, _n_(339281, 'self', lambda: self), 'food'), 'position') == _a_(339286, _a_(339285, _n_(339284, 'self', lambda: self), 'snake'), 'snake_body')[0]:
            _l_(339301)

            _c_(339290, _a_(339289, _a_(339288, _n_(339287, 'self', lambda: self), 'food'), 'randomize'))
            _l_(339291)
            _c_(339295, _a_(339294, _a_(339293, _n_(339292, 'self', lambda: self), 'snake'), 'add_body'))
            _l_(339296)
            _c_(339299, _a_(339298, _n_(339297, 'self', lambda: self), 'play_sound'), 'ding')
            _l_(339300)

        for body_part in _a_(339304, _a_(339303, _n_(339302, 'self', lambda: self), 'snake'), 'snake_body')[1:]:
            _l_(339315)

            if _n_(339305, 'body_part', lambda: body_part) == _a_(339308, _a_(339307, _n_(339306, 'self', lambda: self), 'food'), 'position'):
                _l_(339314)

                _c_(339312, _a_(339311, _a_(339310, _n_(339309, 'self', lambda: self), 'food'), 'randomize'))
                _l_(339313)

    def game_over(self):
        _l_(339343)

        if not 0 <= _a_(339320, _a_(339319, _a_(339318, _n_(339317, 'self', lambda: self), 'snake'), 'snake_body')[0], 'x') < _n_(339321, 'cell_number', lambda: cell_number) or not 0 <= _a_(339325, _a_(339324, _a_(339323, _n_(339322, 'self', lambda: self), 'snake'), 'snake_body')[0], 'y') < _n_(339326, 'cell_number', lambda: cell_number):
            _l_(339332)

            _c_(339329, _a_(339328, _n_(339327, 'self', lambda: self), 'play_sound'), 'crash')
            _l_(339330)
            raise 'Game Over!'
            _l_(339331)

        for tail in _a_(339335, _a_(339334, _n_(339333, 'self', lambda: self), 'snake'), 'snake_body')[1:]:
            _l_(339342)

            if _n_(339336, 'tail', lambda: tail) == _a_(339339, _a_(339338, _n_(339337, 'self', lambda: self), 'snake'), 'snake_body')[0]:
                _l_(339341)

                raise 'Game Over!'
                _l_(339340)

    def update_screen(self):
        _l_(339357)

        _c_(339347, _a_(339346, _a_(339345, _n_(339344, 'self', lambda: self), 'snake'), 'move_snake'))
        _l_(339348)
        _c_(339351, _a_(339350, _n_(339349, 'self', lambda: self), 'is_hit'))
        _l_(339352)
        _c_(339355, _a_(339354, _n_(339353, 'self', lambda: self), 'game_over'))
        _l_(339356)
    
    def run(self):
        _l_(339517)

        running = True
        _l_(339358)
        
        while _n_(339359, 'running', lambda: running):
            _l_(339516)

            for event in _c_(339363, _a_(339362, _a_(339361, _n_(339360, 'pygame', lambda: pygame), 'event'), 'get')):
                _l_(339497)

                if _a_(339365, _n_(339364, 'event', lambda: event), 'type') == _a_(339367, _n_(339366, 'pygame', lambda: pygame), 'KEYDOWN'):
                    _l_(339476)

                    if _a_(339369, _n_(339368, 'event', lambda: event), 'key') == _n_(339370, 'K_ESCAPE', lambda: K_ESCAPE):
                        _l_(339379)

                        _c_(339373, _a_(339372, _n_(339371, 'pygame', lambda: pygame), 'quit'))
                        _l_(339374)
                        _c_(339377, _a_(339376, _n_(339375, 'sys', lambda: sys), 'exit'))
                        _l_(339378)
                    
                    if _a_(339381, _n_(339380, 'event', lambda: event), 'key') == _n_(339382, 'K_RETURN', lambda: K_RETURN):
                        _l_(339390)

                        # pygame.mixer.music.unpause()
                        _n_(339383, 'self', lambda: self).pause = False
                        _l_(339384)
                        _c_(339388, _a_(339387, _a_(339386, _n_(339385, 'self', lambda: self), 'snake'), 'reset'))
                        _l_(339389)
                    
                    if not _a_(339392, _n_(339391, 'self', lambda: self), 'pause'):
                        _l_(339453)

                        if _a_(339394, _n_(339393, 'event', lambda: event), 'key') == _a_(339396, _n_(339395, 'pygame', lambda: pygame), 'K_UP'):
                            _l_(339407)

                            if _a_(339400, _a_(339399, _a_(339398, _n_(339397, 'game', lambda: game), 'snake'), 'direction'), 'y') != 1:
                                _l_(339406)

                                _a_(339402, _n_(339401, 'game', lambda: game), 'snake').direction = _c_(339404, _n_(339403, 'Vector2', lambda: Vector2), 0, -1)
                                _l_(339405)

                        if _a_(339409, _n_(339408, 'event', lambda: event), 'key') == _a_(339411, _n_(339410, 'pygame', lambda: pygame), 'K_DOWN'):
                            _l_(339422)

                            if _a_(339415, _a_(339414, _a_(339413, _n_(339412, 'game', lambda: game), 'snake'), 'direction'), 'y') != -1:
                                _l_(339421)

                                _a_(339417, _n_(339416, 'game', lambda: game), 'snake').direction = _c_(339419, _n_(339418, 'Vector2', lambda: Vector2), 0, 1)
                                _l_(339420)

                        if _a_(339424, _n_(339423, 'event', lambda: event), 'key') == _a_(339426, _n_(339425, 'pygame', lambda: pygame), 'K_LEFT'):
                            _l_(339437)

                            if _a_(339430, _a_(339429, _a_(339428, _n_(339427, 'game', lambda: game), 'snake'), 'direction'), 'x') != 1:
                                _l_(339436)

                                _a_(339432, _n_(339431, 'game', lambda: game), 'snake').direction = _c_(339434, _n_(339433, 'Vector2', lambda: Vector2), -1, 0)
                                _l_(339435)

                        if _a_(339439, _n_(339438, 'event', lambda: event), 'key') == _a_(339441, _n_(339440, 'pygame', lambda: pygame), 'K_RIGHT'):
                            _l_(339452)

                            if _a_(339445, _a_(339444, _a_(339443, _n_(339442, 'game', lambda: game), 'snake'), 'direction'), 'x') != -1:
                                _l_(339451)

                                _a_(339447, _n_(339446, 'game', lambda: game), 'snake').direction = _c_(339449, _n_(339448, 'Vector2', lambda: Vector2), 1, 0)
                                _l_(339450)
            
                elif _a_(339455, _n_(339454, 'event', lambda: event), 'type') == _a_(339457, _n_(339456, 'self', lambda: self), 'screen_update'):
                    _l_(339475)

                    _c_(339460, _a_(339459, _n_(339458, 'self', lambda: self), 'update_screen'))
                    _l_(339461)
                
                elif _a_(339463, _n_(339462, 'event', lambda: event), 'type') == _a_(339465, _n_(339464, 'pygame', lambda: pygame), 'QUIT'):
                    _l_(339474)

                    _c_(339468, _a_(339467, _n_(339466, 'pygame', lambda: pygame), 'quit'))
                    _l_(339469)
                    _c_(339472, _a_(339471, _n_(339470, 'sys', lambda: sys), 'exit'))
                    _l_(339473)

                try:
                    _l_(339496)

                    if not _a_(339478, _n_(339477, 'self', lambda: self), 'pause') and _a_(339480, _n_(339479, 'event', lambda: event), 'type') == _a_(339482, _n_(339481, 'self', lambda: self), 'screen_update'):
                        _l_(339487)

                        _c_(339485, _a_(339484, _n_(339483, 'self', lambda: self), 'update_screen'))
                        _l_(339486)

                except _n_(339488, 'Exception', lambda: Exception):
                    _l_(339495)

                    _c_(339491, _a_(339490, _n_(339489, 'self', lambda: self), 'display_score'))
                    _l_(339492)
                    _n_(339493, 'self', lambda: self).pause = True
                    _l_(339494)

            _c_(339501, _a_(339499, _n_(339498, 'screen', lambda: screen), 'fill'), _n_(339500, 'screen_color', lambda: screen_color))
            _l_(339502)
            _c_(339505, _a_(339504, _n_(339503, 'self', lambda: self), 'draw_elements'))
            _l_(339506)
            _c_(339510, _a_(339509, _a_(339508, _n_(339507, 'pygame', lambda: pygame), 'display'), 'update'))
            _l_(339511)
            _c_(339514, _a_(339513, _n_(339512, 'clock', lambda: clock), 'tick'), 60)
            _l_(339515)

if _n_(339519, '__name__', lambda: __name__) == '__main__':
    _l_(339527)

    game = _c_(339521, _n_(339520, 'Game_Snake2', lambda: Game_Snake2))
    _l_(339522)
    _c_(339525, _a_(339524, _n_(339523, 'game', lambda: game), 'run'))
    _l_(339526)
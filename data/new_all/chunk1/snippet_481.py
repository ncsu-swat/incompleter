# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62823806/random-brick-color-typeerror-pygame-color-object-is-not-callable
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
Created on Thu Jul  2 09:33:50 2020

@author: 
"""
try:
        import pygame, sys, random
        _l_(403627)

except ImportError:
        pass
try:
        from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, K_ESCAPE
        _l_(403629)

except ImportError:
        pass
try:
        from pygame import display
        _l_(403631)

except ImportError:
        pass



#Functions

def draw_bricks():
        _l_(403640)

        for b in _n_(403632, "bricks", lambda: bricks):
                _l_(403639)

                _c_(403637, _a_(403634, _n_(403633, "windowSurfaceObj", lambda: windowSurfaceObj), "blit"), _n_(403635, "brick", lambda: brick)[0], _n_(403636, "b", lambda: b)) # makes a copy of brick image acording to coordinates, where stuff is drawn!
                _l_(403638) # makes a copy of brick image acording to coordinates, where stuff is drawn!
def draw_bat():
        _l_(403647)

        _c_(403645, _a_(403642, _n_(403641, "windowSurfaceObj", lambda: windowSurfaceObj), "blit"), _n_(403643, "bat", lambda: bat), _n_(403644, "batRect", lambda: batRect))
        _l_(403646)
      
def draw_ball():
        _l_(403654)

        _c_(403652, _a_(403649, _n_(403648, "windowSurfaceObj", lambda: windowSurfaceObj), "blit"), _n_(403650, "ball", lambda: ball), _n_(403651, "ballRect", lambda: ballRect))
        _l_(403653)


def brick_color():
        _l_(403685)

        color_var = _c_(403657, _a_(403656, _n_(403655, "random", lambda: random), "randint"), 0,3)
        _l_(403658)
        
        if _n_(403659, "color_var", lambda: color_var) == 0:
                _l_(403682)

                brick_color = _c_(403662, _a_(403661, _n_(403660, "pygame", lambda: pygame), "Color"), 198,44,58)
                _l_(403663)
        elif _n_(403664, "color_var", lambda: color_var) == 1:
                _l_(403681)

                brick_color = _c_(403667, _a_(403666, _n_(403665, "pygame", lambda: pygame), "Color"), 1,128,181)
                _l_(403668)
        elif _n_(403669, "color_var", lambda: color_var) == 2:
                _l_(403680)

                brick_color = _c_(403672, _a_(403671, _n_(403670, "pygame", lambda: pygame), "Color"), 255,211,92)
                _l_(403673)
        elif _n_(403674, "color_var", lambda: color_var) == 3:
                _l_(403679)

                brick_color = _c_(403677, _a_(403676, _n_(403675, "pygame", lambda: pygame), "Color"), 0,157,103)
                _l_(403678)
        aux = _n_(403683, "brick_color", lambda: brick_color)
        _l_(403684)
        return aux









_c_(403688, _a_(403687, _n_(403686, "pygame", lambda: pygame), "init"))
_l_(403689)
fpsClock = _c_(403693, _a_(403692, _a_(403691, _n_(403690, "pygame", lambda: pygame), "time"), "Clock"))
_l_(403694)


# new and improved:
# create surface object aka. the main window
inf = _c_(403697, _a_(403696, _n_(403695, "display", lambda: display), "Info"))
_l_(403698)
screen_width = _a_(403700, _n_(403699, "inf", lambda: inf), "current_w") - 200 # make window sizea little bit smaller than actual screen
_l_(403701) # make window sizea little bit smaller than actual screen
screen_height = _a_(403703, _n_(403702, "inf", lambda: inf), "current_h") - 200
_l_(403704)
# windowSurfaceObj = display.set_mode(size=(screen_width, screen_height), flags=pygame.FULLSCREEN) # initialize window
windowSurfaceObj = _c_(403709, _a_(403706, _n_(403705, "display", lambda: display), "set_mode"), size=(_n_(403707, "screen_width", lambda: screen_width), _n_(403708, "screen_height", lambda: screen_height))) # initialize window
_l_(403710) # initialize window

_c_(403713, _a_(403712, _n_(403711, "display", lambda: display), "set_caption"), 'New and improved Bricks'); # set window title
_l_(403714)# set window title

# brick layout

brick_width = 50
_l_(403715)
brick_height = 20
_l_(403716)
num_bricks_in_row = 7
_l_(403717)
num_brick_rows = 5
_l_(403718)
brick_row_height = 2 * _n_(403719, "brick_height", lambda: brick_height)
_l_(403720)
brick_offset_y = 100
_l_(403721)
brick_column_width = 2 * _n_(403722, "brick_width", lambda: brick_width)
_l_(403723)
brick_offset_x = _c_(403728, _n_(403724, "int", lambda: int), _n_(403725, "screen_width", lambda: screen_width)/2 - _n_(403726, "brick_column_width", lambda: brick_column_width)*_n_(403727, "num_bricks_in_row", lambda: num_bricks_in_row)/2) # place it in the middle of the screen
_l_(403729) # place it in the middle of the screen
brick_color = _c_(403731, _n_(403730, "brick_color", lambda: brick_color))
_l_(403732)

# ball related stuff

ball_radius = _c_(403735, _n_(403733, "int", lambda: int), _n_(403734, "screen_height", lambda: screen_height)/200)
_l_(403736)

# more game constants!

fps = 60 # desired frames per second
_l_(403737) # desired frames per second
background_colour = _c_(403740, _a_(403739, _n_(403738, "pygame", lambda: pygame), "Color"), 0, 0, 0) # background is black
_l_(403741) # background is black

# used variables for bat dimensions
bat_width = 100
_l_(403742)
bat_height = 10
_l_(403743)

# ball related stuff
ball_start_x = 24 # somehwere near the left of the window
_l_(403744) # somehwere near the left of the window
ball_start_y = 200 # initial ball position when new ball is released
_l_(403745) # initial ball position when new ball is released
ball_speed = _c_(403748, _n_(403746, "int", lambda: int), _n_(403747, "fps", lambda: fps)*0.15) # speed of ball in pixel per frame! use fps var. here to make real ball speed independent of frame rate
_l_(403749) # speed of ball in pixel per frame! use fps var. here to make real ball speed independent of frame rate


# bat init

# replace bat with crude hand drawn one

batcolor = _c_(403752, _a_(403751, _n_(403750, "pygame", lambda: pygame), "Color"), 0, 0, 255) # bat color: blue!
_l_(403753) # bat color: blue!
bat = _c_(403758, _a_(403755, _n_(403754, "pygame", lambda: pygame), "Surface"), [_n_(403756, "bat_width", lambda: bat_width), _n_(403757, "bat_height", lambda: bat_height)]) # this Surface is for drawing the bat upon
_l_(403759) # this Surface is for drawing the bat upon
_c_(403767, _a_(403762, _a_(403761, _n_(403760, "pygame", lambda: pygame), "draw"), "rect"), _n_(403763, "bat", lambda: bat), _n_(403764, "batcolor", lambda: batcolor), [0, 0, _n_(403765, "bat_width", lambda: bat_width), _n_(403766, "bat_height", lambda: bat_height)]) # draw bat. It's a simple rectangle.
_l_(403768) # draw bat. It's a simple rectangle.
bat = _c_(403771, _a_(403770, _n_(403769, "bat", lambda: bat), "convert_alpha")) # deal with transparency
_l_(403772) # deal with transparency

# place the bat somewhere near the bottom of the screen/window
player_start_x = 0 # initial position is on left
_l_(403773) # initial position is on left
player_start_y = _n_(403774, "screen_height", lambda: screen_height) - 6 * _n_(403775, "bat_height", lambda: bat_height) # this is used as Y coordinate for bat, near the bottom of the screen
_l_(403776) # this is used as Y coordinate for bat, near the bottom of the screen

batRect = _c_(403779, _a_(403778, _n_(403777, "bat", lambda: bat), "get_rect")) # rectangle around bat, used to move it around later
_l_(403780) # rectangle around bat, used to move it around later
mousex = _n_(403781, "player_start_x", lambda: player_start_x)
_l_(403782)
mousey = _n_(403783, "player_start_y", lambda: player_start_y) # mousex and mousey later used for moving the bat around, not actual mouse coordinates at this point
_l_(403784) # mousex and mousey later used for moving the bat around, not actual mouse coordinates at this point

# ball init

ball_color = _c_(403787, _a_(403786, _n_(403785, "pygame", lambda: pygame), "Color"), 255, 255, 255) # white
_l_(403788) # white
ball = _c_(403793, _a_(403790, _n_(403789, "pygame", lambda: pygame), "Surface"), [_n_(403791, "ball_radius", lambda: ball_radius)*2, _n_(403792, "ball_radius", lambda: ball_radius)*2]) # Surface for drawing the ball upon
_l_(403794) # Surface for drawing the ball upon
_c_(403803, _a_(403797, _a_(403796, _n_(403795, "pygame", lambda: pygame), "draw"), "circle"), _n_(403798, "ball", lambda: ball), _n_(403799, "ball_color", lambda: ball_color), (_n_(403800, "ball_radius", lambda: ball_radius), _n_(403801, "ball_radius", lambda: ball_radius)), _n_(403802, "ball_radius", lambda: ball_radius)) # draw circle on ball surface
_l_(403804) # draw circle on ball surface

ballRect = _c_(403807, _a_(403806, _n_(403805, "ball", lambda: ball), "get_rect")) # rectangle around ball, use to move it around later
_l_(403808) # rectangle around ball, use to move it around later
ballServed = False
_l_(403809)
bx = _n_(403810, "ball_start_x", lambda: ball_start_x) # bx is actual ball postion
_l_(403811) # bx is actual ball postion
by = _n_(403812, "ball_start_y", lambda: ball_start_y) # by is actual (current) ball position
_l_(403813) # by is actual (current) ball position
sx = _n_(403814, "ball_speed", lambda: ball_speed) # current ball speed in horizontal direction
_l_(403815) # current ball speed in horizontal direction
sy = _n_(403816, "ball_speed", lambda: ball_speed) # current ball speed vertical
_l_(403817) # current ball speed vertical
_n_(403818, "ballRect", lambda: ballRect).topleft = (_n_(403819, "bx", lambda: bx), _n_(403820, "by", lambda: by)) # move ball rectangle to initial position
_l_(403821) # move ball rectangle to initial position

# brick init
brick = _c_(403826, _a_(403823, _n_(403822, "pygame", lambda: pygame), "Surface"), [_n_(403824, "brick_width", lambda: brick_width), _n_(403825, "brick_height", lambda: brick_height)]),_n_(403827, "brick_color", lambda: brick_color) # surface for a single brick
_l_(403828) # surface for a single brick
_c_(403836, _a_(403831, _a_(403830, _n_(403829, "pygame", lambda: pygame), "draw"), "rect"), _n_(403832, "brick", lambda: brick)[0], _n_(403833, "brick", lambda: brick)[1], [0, 0, _n_(403834, "brick_width", lambda: brick_width), _n_(403835, "brick_height", lambda: brick_height)])
_l_(403837)



bricks = [] # list of *coordinates* of the bricks
_l_(403838) # list of *coordinates* of the bricks

# initialize coordinates of bricks

for y in _c_(403841, _n_(403839, "range", lambda: range), _n_(403840, "num_brick_rows", lambda: num_brick_rows)):
        _l_(403864)

        brickY = (_n_(403842, "y", lambda: y) * _n_(403843, "brick_row_height", lambda: brick_row_height)) + _n_(403844, "brick_offset_y", lambda: brick_offset_y)    
        _l_(403845)    
        for x in _c_(403848, _n_(403846, "range", lambda: range), _n_(403847, "num_bricks_in_row", lambda: num_bricks_in_row)):
                _l_(403863)

                brickX = (_n_(403849, "x", lambda: x) * _n_(403850, "brick_column_width", lambda: brick_column_width)) + _n_(403851, "brick_offset_x", lambda: brick_offset_x)
                _l_(403852)
                color_of_brick = _c_(403854, _n_(403853, "brick_color", lambda: brick_color))
                _l_(403855)
                _c_(403861, _a_(403857, _n_(403856, "bricks", lambda: bricks), "append"), (_n_(403858, "brickX", lambda: brickX), _n_(403859, "brickY", lambda: brickY)),_n_(403860, "color_of_brick", lambda: color_of_brick)) # coordinates are in fact tuples (x,y)
                _l_(403862) # coordinates are in fact tuples (x,y)

while True:
        _l_(404044)

        
        _c_(403868, _a_(403866, _n_(403865, "windowSurfaceObj", lambda: windowSurfaceObj), "fill"), _n_(403867, "background_colour", lambda: background_colour)) # clear the screen
        _l_(403869) # clear the screen

        # brick draw
        # for b in bricks: # remember: bricks is a list of brick coordinates, not surfaces
        #     windowSurfaceObj.blit(brick, b) # make copy of brick image and place it on screen, b = brick coordinates
        _c_(403871, _n_(403870, "draw_bricks", lambda: draw_bricks))
        _l_(403872)
        
        # bat and ball draw, rectangles around bat and ball are used for positioning
        # windowSurfaceObj.blit(bat, batRect) # copy surface with image of bat to screen
        # windowSurfaceObj.blit(ball, ballRect) # same for ball
        _c_(403874, _n_(403873, "draw_bat", lambda: draw_bat))
        _l_(403875)
        _c_(403877, _n_(403876, "draw_ball", lambda: draw_ball))
        _l_(403878)
        
        # main event loop
        # process user interaction
        for event in _c_(403882, _a_(403881, _a_(403880, _n_(403879, "pygame", lambda: pygame), "event"), "get")):
                _l_(403932)

                # quit the game if window is closed or escape key is pressed
                if _a_(403884, _n_(403883, "event", lambda: event), "type") == _n_(403885, "QUIT", lambda: QUIT) or (_a_(403887, _n_(403886, "event", lambda: event), "type") == _n_(403888, "KEYDOWN", lambda: KEYDOWN) and _a_(403890, _n_(403889, "event", lambda: event), "key") == _n_(403891, "K_ESCAPE", lambda: K_ESCAPE)):
                        _l_(403931)

                        _c_(403894, _a_(403893, _n_(403892, "pygame", lambda: pygame), "quit"))
                        _l_(403895)
                        _c_(403898, _a_(403897, _n_(403896, "sys", lambda: sys), "exit"))
                        _l_(403899)
                elif _a_(403901, _n_(403900, "event", lambda: event), "type") == _n_(403902, "MOUSEBUTTONUP", lambda: MOUSEBUTTONUP) and not _n_(403903, "ballServed", lambda: ballServed):
                        _l_(403930)

                        ballServed = True # start game, when mouse is clicked
                        _l_(403904) # start game, when mouse is clicked
                elif _a_(403906, _n_(403905, "event", lambda: event), "type") == _n_(403907, "MOUSEMOTION", lambda: MOUSEMOTION):
                        _l_(403929)

                        mousex, mousey = _a_(403909, _n_(403908, "event", lambda: event), "pos") # set mouse coordinate variables to actual mouse coordinates
                        _l_(403910) # set mouse coordinate variables to actual mouse coordinates
                        if _n_(403911, "mousex", lambda: mousex) < _n_(403912, "screen_width", lambda: screen_width) - _n_(403913, "bat_width", lambda: bat_width):
                                _l_(403928)

                                if _n_(403914, "mousex", lambda: mousex) < 0:
                                        _l_(403922)

                                        _n_(403915, "batRect", lambda: batRect).topleft = (0, _n_(403916, "player_start_y", lambda: player_start_y))
                                        _l_(403917)
                                else:
                                    _n_(403918, "batRect", lambda: batRect).topleft = (_n_(403919, "mousex", lambda: mousex), _n_(403920, "player_start_y", lambda: player_start_y))
                                    _l_(403921)
                        else:
                            _n_(403923, "batRect", lambda: batRect).topleft = (_n_(403924, "screen_width", lambda: screen_width) - _n_(403925, "bat_width", lambda: bat_width), _n_(403926, "player_start_y", lambda: player_start_y))
                            _l_(403927)
        
        # main game logic 
        if _n_(403933, "ballServed", lambda: ballServed):
                _l_(403942)

                _n_(403934, "ballRect", lambda: ballRect).topleft = (_n_(403935, "bx", lambda: bx), _n_(403936, "by", lambda: by)) # position the ball using its rectangle
                _l_(403937) # position the ball using its rectangle
                bx += _n_(403938, "sx", lambda: sx) # sx = speed of the ball in X direction
                _l_(403939) # sx = speed of the ball in X direction
                by += _n_(403940, "sy", lambda: sy) # sy = speed of the ball in Y direction
                _l_(403941) # sy = speed of the ball in Y direction
        
        if (_n_(403943, "by", lambda: by) >= _n_(403944, "screen_height", lambda: screen_height)):
                _l_(403953)

                ballServed = False # game not in progess, ball lost!
                _l_(403945) # game not in progess, ball lost!
                bx, by = (_n_(403946, "ball_start_x", lambda: ball_start_x), _n_(403947, "ball_start_y", lambda: ball_start_y)) # ball is reset to start position
                _l_(403948) # ball is reset to start position
                _n_(403949, "ballRect", lambda: ballRect).topleft = (_n_(403950, "bx", lambda: bx), _n_(403951, "by", lambda: by)) # move the rectangle around ball to correct position
                _l_(403952) # move the rectangle around ball to correct position
        if _n_(403954, "by", lambda: by) <= 0:
                _l_(403957)

                by = 0
                _l_(403955)
                sy *= -1 # reflect
                _l_(403956) # reflect
        if _n_(403958, "bx", lambda: bx) <= 0:
                _l_(403961)

                bx = 0
                _l_(403959)
                sx *= -1 # reflect
                _l_(403960) # reflect
        if _n_(403962, "bx", lambda: bx) >= _n_(403963, "screen_width", lambda: screen_width) - _n_(403964, "ball_radius", lambda: ball_radius)*2:
                _l_(403969)

                bx = _n_(403965, "screen_width", lambda: screen_width) - _n_(403966, "ball_radius", lambda: ball_radius)*2
                _l_(403967)
                sx *= -1 # reflection
                _l_(403968) # reflection
        
        # collision detection
        brickForRemoval = None
        _l_(403970)
            
        for b in _n_(403971, "bricks", lambda: bricks):
                _l_(404013)

                briX, briY = _n_(403972, "b", lambda: b) # tuple unwrapping: x and y coordinates of top left of brick
                _l_(403973) # tuple unwrapping: x and y coordinates of top left of brick
                if _n_(403974, "bx", lambda: bx) + _n_(403975, "ball_radius", lambda: ball_radius)*2 >= _n_(403976, "briX", lambda: briX) and _n_(403977, "bx", lambda: bx) <= _n_(403978, "briX", lambda: briX) + _n_(403979, "brick_width", lambda: brick_width):
                        _l_(404012)

                        if (_n_(403980, "by", lambda: by) + _n_(403981, "ball_radius", lambda: ball_radius)*2 >= _n_(403982, "briY", lambda: briY) and _n_(403983, "by", lambda: by) <= _n_(403984, "briY", lambda: briY) + _n_(403985, "brick_height", lambda: brick_height)):
                                _l_(404011)

                                brickForRemoval = _n_(403986, "b", lambda: b) # brick was hit and is scheduled for removal
                                _l_(403987) # brick was hit and is scheduled for removal
                                if _n_(403988, "bx", lambda: bx) <= _n_(403989, "briX", lambda: briX) + _n_(403990, "ball_radius", lambda: ball_radius)*2:
                                        _l_(403998)

                                        sx *= -1 # reflect
                                        _l_(403991) # reflect
                                elif _n_(403992, "bx", lambda: bx) >= _n_(403993, "briX", lambda: briX) + _n_(403994, "brick_width", lambda: brick_width) - _n_(403995, "ball_radius", lambda: ball_radius)*2:
                                        _l_(403997)

                                        sx *= -1 # reflect
                                        _l_(403996) # reflect
                                if _n_(403999, "by", lambda: by) <= _n_(404000, "briY", lambda: briY) + _n_(404001, "ball_radius", lambda: ball_radius) * 2:
                                        _l_(404009)

                                        sy *= -1 # reflect
                                        _l_(404002) # reflect
                                elif _n_(404003, "by", lambda: by) >= _n_(404004, "briY", lambda: briY) + _n_(404005, "brick_height", lambda: brick_height) - _n_(404006, "ball_radius", lambda: ball_radius)*2:
                                        _l_(404008)

                                        sy *= -1 # reflect
                                        _l_(404007) # reflect
                                break # ball hit a brick and cannot hit another one at the same time
                                _l_(404010) # ball hit a brick and cannot hit another one at the same time
        if _n_(404014, "brickForRemoval", lambda: brickForRemoval) != None:
                _l_(404020)

                _c_(404018, _a_(404016, _n_(404015, "bricks", lambda: bricks), "remove"), _n_(404017, "brickForRemoval", lambda: brickForRemoval)) # … remove it!
                _l_(404019) # … remove it!
        # collision check: does bat hit ball?
        if (_n_(404021, "bx", lambda: bx) >= _n_(404022, "mousex", lambda: mousex) and _n_(404023, "bx", lambda: bx) <= _n_(404024, "mousex", lambda: mousex) + _n_(404025, "bat_width", lambda: bat_width)):
                _l_(404033)

                if(_n_(404026, "by", lambda: by) >= _n_(404027, "player_start_y", lambda: player_start_y) - _n_(404028, "bat_height", lambda: bat_height) and _n_(404029, "by", lambda: by) <= _n_(404030, "player_start_y", lambda: player_start_y)):
                        _l_(404032)

                        sy *= -1 # reflect
                        _l_(404031) # reflect
        _c_(404037, _a_(404036, _a_(404035, _n_(404034, "pygame", lambda: pygame), "display"), "update")) # show updated screen
        _l_(404038) # show updated screen
        _c_(404042, _a_(404040, _n_(404039, "fpsClock", lambda: fpsClock), "tick"), _n_(404041, "fps", lambda: fps)) # limit fps
        _l_(404043) # limit fps
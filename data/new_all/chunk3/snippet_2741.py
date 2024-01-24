# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64728441/python-crash-course-alien-invasion-attributeerror-bullet-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import sys
 _l_(536263)

except ImportError:
 pass
try:
 import game_functions as gf
 _l_(536265)

except ImportError:
 pass
try:
 import pygame
 _l_(536267)

except ImportError:
 pass
try:
 from settings import Settings
 _l_(536269)

except ImportError:
 pass
try:
 from ship import Ship
 _l_(536271)

except ImportError:
 pass
try:
 from pygame.sprite import Group
 _l_(536273)

except ImportError:
 pass

def run_game():
 _l_(536281)

# Initialize pygame, settings, and screen object.
 _c_(536276, _a_(536275, _n_(536274, "pygame", lambda: pygame), "init"))
 _l_(536277)
 ai_settings = _c_(536279, _n_(536278, "Settings", lambda: Settings))
 _l_(536280)



screen = _c_(536289, _a_(536284, _a_(536283, _n_(536282, "pygame", lambda: pygame), "display"), "set_mode"), (_a_(536286, _n_(536285, "ai_settings", lambda: ai_settings), "screen_width"), _a_(536288, _n_(536287, "ai_settings", lambda: ai_settings), "screen_height")))
_l_(536290)
_c_(536294, _a_(536293, _a_(536292, _n_(536291, "pygame", lambda: pygame), "display"), "set_caption"), "Alien Invasion")
_l_(536295)

_c_(536300, _a_(536297, _n_(536296, "screen", lambda: screen), "fill"), _a_(536299, _n_(536298, "ai_settings", lambda: ai_settings), "bg_color"))
_l_(536301)
# Make a ship.
ship = _c_(536305, _n_(536302, "Ship", lambda: Ship), _n_(536303, "screen", lambda: screen), _n_(536304, "ai_settings", lambda: ai_settings))
_l_(536306)
bullets = _c_(536308, _n_(536307, "Group", lambda: Group))
_l_(536309)

# Background color
bg_color = (230, 230, 230)
_l_(536310)


while True:
 _l_(536373)


 _c_(536317, _a_(536312, _n_(536311, "gf", lambda: gf), "check_events"), _n_(536313, "ai_settings", lambda: ai_settings), _n_(536314, "screen", lambda: screen), _n_(536315, "ship", lambda: ship), _n_(536316, "bullets", lambda: bullets))
 _l_(536318)
 _c_(536325, _a_(536320, _n_(536319, "gf", lambda: gf), "update_screen"), _n_(536321, "ai_settings", lambda: ai_settings), _n_(536322, "bullets", lambda: bullets), _n_(536323, "screen", lambda: screen), _n_(536324, "ship", lambda: ship))
 _l_(536326)

 _c_(536333, _a_(536328, _n_(536327, "gf", lambda: gf), "check_events"), _n_(536329, "ship", lambda: ship), _n_(536330, "screen", lambda: screen), _n_(536331, "ship", lambda: ship), _n_(536332, "bullets", lambda: bullets))
 _l_(536334)
 _c_(536338, _a_(536336, _n_(536335, "ship", lambda: ship), "update"), _n_(536337, "ai_settings", lambda: ai_settings))
 _l_(536339)
 _c_(536342, _a_(536341, _n_(536340, "bullets", lambda: bullets), "update"))
 _l_(536343)


 for event in _c_(536347, _a_(536346, _a_(536345, _n_(536344, "pygame", lambda: pygame), "event"), "get")):
  _l_(536357)

  if _a_(536349, _n_(536348, "event", lambda: event), "type") == _a_(536351, _n_(536350, "pygame", lambda: pygame), "QUIT"):
   _l_(536356)

   _c_(536354, _a_(536353, _n_(536352, "sys", lambda: sys), "exit"))
   _l_(536355)

 _c_(536362, _a_(536359, _n_(536358, "screen", lambda: screen), "fill"), _a_(536361, _n_(536360, "ai_settings", lambda: ai_settings), "bg_color"))
 _l_(536363)

 _c_(536366, _a_(536365, _n_(536364, "ship", lambda: ship), "blitme"))
 _l_(536367)
 _c_(536371, _a_(536370, _a_(536369, _n_(536368, "pygame", lambda: pygame), "display"), "flip"))
 _l_(536372)

_c_(536375, _n_(536374, "run_game", lambda: run_game))
_l_(536376)
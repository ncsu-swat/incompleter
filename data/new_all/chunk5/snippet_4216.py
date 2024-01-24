# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61480481/python-class-attribute-error-although-the-attribute-is-present
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Enemy(_n_(647523, "Character", lambda: Character)):
     _l_(647550)

     def __int__(self,char_name,char_desc):
          _l_(647536)

          _c_(647528, _a_(647525, _n_(647524, "super", lambda: super)(), "__int__"), _n_(647526, "char_name", lambda: char_name),_n_(647527, "char_desc", lambda: char_desc))
          _l_(647529)
          _n_(647530, "self", lambda: self).hit_points = 0
          _l_(647531)
          _n_(647532, "self", lambda: self).melee_strengths = {
              'Normal damage': None,
              'Piercing damage': None,
              'Bludgoning damage': None}
          _l_(647533)
          _n_(647534, "self", lambda: self).special_strengths = {
              'Acid damage': None,
              'Cold damage': None,
              'Heat damage': None,
              'Holy damage': None,
              'Undead damage': None}
          _l_(647535)
     def set_melee_strength(self, norm_str, pierce_str, bludge_str):
          _l_(647549)

          _a_(647538, _n_(647537, "self", lambda: self), "melee_strengths")['Normal damage'] = _n_(647539, "norm_str", lambda: norm_str)
          _l_(647540)
          _a_(647542, _n_(647541, "self", lambda: self), "melee_strengths")['Piercing damage'] = _n_(647543, "pierce_str", lambda: pierce_str)
          _l_(647544)
          _a_(647546, _n_(647545, "self", lambda: self), "melee_strengths")['Bludgoning damage'] = _n_(647547, "bludge_str", lambda: bludge_str)
          _l_(647548)
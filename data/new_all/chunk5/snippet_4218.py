# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61480481/python-class-attribute-error-although-the-attribute-is-present
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Enemy(_n_(663657, "Character", lambda: Character)):
     _l_(663684)

     def __int__(self,char_name,char_desc):
          _l_(663670)

          _c_(663662, _a_(663659, _n_(663658, "super", lambda: super)(), "__int__"), _n_(663660, "char_name", lambda: char_name),_n_(663661, "char_desc", lambda: char_desc))
          _l_(663663)
          _n_(663664, "self", lambda: self).hit_points = 0
          _l_(663665)
          _n_(663666, "self", lambda: self).melee_strengths = {
              'Normal damage': None,
              'Piercing damage': None,
              'Bludgoning damage': None}
          _l_(663667)
          _n_(663668, "self", lambda: self).special_strengths = {
              'Acid damage': None,
              'Cold damage': None,
              'Heat damage': None,
              'Holy damage': None,
              'Undead damage': None}
          _l_(663669)
     def set_melee_strength(self, norm_str, pierce_str, bludge_str):
          _l_(663683)

          _a_(663672, _n_(663671, "self", lambda: self), "melee_strengths")['Normal damage'] = _n_(663673, "norm_str", lambda: norm_str)
          _l_(663674)
          _a_(663676, _n_(663675, "self", lambda: self), "melee_strengths")['Piercing damage'] = _n_(663677, "pierce_str", lambda: pierce_str)
          _l_(663678)
          _a_(663680, _n_(663679, "self", lambda: self), "melee_strengths")['Bludgoning damage'] = _n_(663681, "bludge_str", lambda: bludge_str)
          _l_(663682)
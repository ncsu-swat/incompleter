# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52359991/python-3-6-nameerror-name-a-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def NuclearBindingEnergy(A,Z):
  _l_(669681)

  a_V=15.67
  _l_(669653)
  a_S=17.23
  _l_(669654)
  a_C=0.75
  _l_(669655)
  a_A=93.2
  _l_(669656)
  a_P=0
  _l_(669657)

  if _n_(669658, "A", lambda: A)%2==1:
    _l_(669664)

    a_P=0
    _l_(669659)
  else:
    if _n_(669660, "Z", lambda: Z)%2==0:
      _l_(669663)

      a_P=12.0
      _l_(669661)
    else:
      a_P=-12.0
      _l_(669662)

  B = _n_(669665, "a_V", lambda: (a_V))*_n_(669666, "A", lambda: A) - (_n_(669667, "a_S", lambda: (a_S))*(_n_(669668, "A", lambda: A)**(2/3))) - _n_(669669, "a_C", lambda: (a_C))*(_n_(669670, "Z", lambda: Z)**2/(_n_(669671, "A", lambda: A)**(1/3))) - (_n_(669672, "a_A", lambda: (a_A))*(((_n_(669673, "A", lambda: A)-(2*_n_(669674, "Z", lambda: Z)))**2)/_n_(669675, "A", lambda: A))) + (_n_(669676, "a_P", lambda: (a_P))/_n_(669677, "A", lambda: A)**(1/2))
  _l_(669678)
  aux = _n_(669679, "B", lambda: B)
  _l_(669680)

  return aux

def NuclearBindingEnergyPerNucleon(A,Z):
  _l_(669688)

  aux = _c_(669685, _n_(669682, "NuclearBindingEnergy", lambda: NuclearBindingEnergy), _n_(669683, "A", lambda: A),_n_(669684, "Z", lambda: Z))/_n_(669686, "A", lambda: A)
  _l_(669687)
  return aux

_c_(669694, _n_(669689, "print", lambda: print), _c_(669693, _n_(669690, "NuclearBindingEnergy", lambda: NuclearBindingEnergy), _n_(669691, "A", lambda: A),_n_(669692, "Z", lambda: Z)))
_l_(669695)
_c_(669702, _n_(669696, "print", lambda: print), _c_(669700, _n_(669697, "NuclearBindingEnergy", lambda: NuclearBindingEnergy), _n_(669698, "A", lambda: A),_n_(669699, "Z", lambda: Z))/_n_(669701, "A", lambda: A))
_l_(669703)
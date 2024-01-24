# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57717370/typeerror-int-object-is-not-callable-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class reflex_vacuum():
  _l_(365027)


  global count
  _l_(364941)


  def count(pos, l, r):
    _l_(364988)

    global count
    _l_(364942)
    global p 
    _l_(364943) 
    global left
    _l_(364944)
    global right
    _l_(364945)
    p = _n_(364946, "pos", lambda: pos)
    _l_(364947)
    left = _n_(364948, "l", lambda: l) 
    _l_(364949) 
    right = _n_(364950, "r", lambda: r) 
    _l_(364951) 


    count = 0 
    _l_(364952) 

    def clean(pos, l, r):
      _l_(364972)

      global p 
      _l_(364953) 
      global left
      _l_(364954)
      global right
      _l_(364955)

      if _n_(364956, "pos", lambda: pos) == 'left':
        _l_(364965)

        if _n_(364957, "l", lambda: l) == 1:
          _l_(364959)

          l=0
          _l_(364958)
        pos = 'right'
        _l_(364960)

      else:
        if _n_(364961, "r", lambda: r) == 1:
          _l_(364963)

          r=0
          _l_(364962)
        pos = 'left'
        _l_(364964)
      p = _n_(364966, "pos", lambda: pos)
      _l_(364967)
      left = _n_(364968, "l", lambda: l) 
      _l_(364969) 
      right = _n_(364970, "r", lambda: r)  
      _l_(364971)  

    while _n_(364973, "left", lambda: left)==1 or _n_(364974, "right", lambda: right)==1:
      _l_(364983)

      _c_(364979, _n_(364975, "clean", lambda: clean), _n_(364976, "p", lambda: p), _n_(364977, "left", lambda: left), _n_(364978, "right", lambda: right))
      _l_(364980)
      count=_n_(364981, "count", lambda: count)+1 
      _l_(364982) 
    _c_(364986, _n_(364984, "print", lambda: print), _n_(364985, "count", lambda: count))
    _l_(364987)

  def scale(sum):
    _l_(364999)

    global count
    _l_(364989)
    s = 10 - (_n_(364990, "count", lambda: count)/_n_(364991, "sum", lambda: sum))
    _l_(364992)
    _c_(364997, _n_(364993, "print", lambda: print), 'The score is ' + _c_(364996, _n_(364994, "str", lambda: str), _n_(364995, "s", lambda: s)) + ' out of 10.')
    _l_(364998)


  _c_(365001, _n_(365000, "print", lambda: print), 'This program checks the efficiency of the vacuum depending on the vacuum position and dirt placement. The scale is 10 points. each move deducts a point. If move was made with dirt on both sides (thus move was necessary) then the move count is divided by two. \n')    
  _l_(365002)    
  _c_(365004, _n_(365003, "print", lambda: print), 'Starting left with no dirt')
  _l_(365005)
  _c_(365007, _n_(365006, "count", lambda: count), 'left', 0, 0)
  _l_(365008)
  _c_(365009, scale, 2)
  _l_(365010)

  _c_(365012, _n_(365011, "print", lambda: print), '\nStarting right with no dirt')
  _l_(365013)
  _c_(365015, _n_(365014, "count", lambda: count), 'right', 0, 0)
  _l_(365016)
  _c_(365017, scale, 1)
  _l_(365018)

  _c_(365020, _n_(365019, "print", lambda: print), '\nStarting left with dirt left')
  _l_(365021)
  _c_(365023, _n_(365022, "count", lambda: count), 'left', 1, 0)
  _l_(365024)
  _c_(365025, scale, 1)
  _l_(365026)
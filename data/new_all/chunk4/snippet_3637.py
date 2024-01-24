# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70298185/str-object-has-no-attribute-append-attribute-error-when-i-try-append-to-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import glob
 _l_(628700)

except ImportError:
 pass
try:
 import os
 _l_(628702)

except ImportError:
 pass

def main():
 _l_(628761)


 direct = r"C:\Users\Inzaghi\Desktop\Ondra_origin"
 _l_(628703)

 main_dict={}
 _l_(628704)

 for filename in _c_(628712, _a_(628706, _n_(628705, "glob", lambda: glob), "glob"), _c_(628711, _a_(628709, _a_(628708, _n_(628707, "os", lambda: os), "path"), "join"), _n_(628710, "direct", lambda: direct), '*.spe')):
  _l_(628760)

  
  with _c_(628715, _n_(628713, "open", lambda: open), _n_(628714, "filename", lambda: filename),'r') as file:
   _l_(628759)

   _c_(628718, _n_(628716, "print", lambda: print), 'file read: ' + _n_(628717, "filename", lambda: filename))
   _l_(628719)
   lst=[]
   _l_(628720)
   for line in _n_(628721, "file", lambda: file):
    _l_(628741)

    line = _c_(628724, _a_(628723, _n_(628722, "line", lambda: line), "replace"), '# ','')
    _l_(628725)
    if _c_(628728, _n_(628726, "len", lambda: len), _n_(628727, "line", lambda: line)) == 14:
     _l_(628740)

     line = _c_(628733, _a_(628732, _c_(628731, _a_(628730, _n_(628729, "line", lambda: line), "rstrip")), "split"))
     _l_(628734)
     _c_(628738, _a_(628736, _n_(628735, "lst", lambda: lst), "append"), _n_(628737, "line", lambda: line)[1])
     _l_(628739)
      
   for count, n in _c_(628744, _n_(628742, "enumerate", lambda: enumerate), _n_(628743, "lst", lambda: lst)[:-4]):
    _l_(628758)

    if _n_(628745, "count", lambda: count) in _n_(628746, "main_dict", lambda: main_dict):
     _l_(628757)

     _c_(628751, _a_(628749, _n_(628747, "main_dict", lambda: main_dict)[_n_(628748, "count", lambda: count)], "append"), _n_(628750, "n", lambda: n))
     _l_(628752)
    else:
         _n_(628753, "main_dict", lambda: main_dict)[_n_(628754, "count", lambda: count)]=_n_(628755, "n", lambda: n)
         _l_(628756)
         
with _c_(628764, _n_(628762, "open", lambda: open), _n_(628763, "direct", lambda: direct)+'\celkovy_file.txt','a') as f:
 _l_(628777)

 for i in _c_(628769, _n_(628765, "range", lambda: range), 0,_c_(628768, _n_(628766, "len", lambda: len), _n_(628767, "main_dict", lambda: main_dict))):
  _l_(628776)

  _c_(628774, _a_(628771, _n_(628770, "f", lambda: f), "write"), _n_(628772, "main_dict", lambda: main_dict)[_n_(628773, "i", lambda: i)] + '\n')
  _l_(628775)
_c_(628779, _n_(628778, "print", lambda: print), 'Done')
_l_(628780)

if _n_(628781, "__name__", lambda: __name__)=='__main__':
 _l_(628785)

 _c_(628783, _n_(628782, "main", lambda: main)) 
 _l_(628784) 
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71717884/how-to-overcome-type-error-with-subprocess-call-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import subprocess
   _l_(534796)

except ImportError:
   pass
try:
   import socket
   _l_(534798)

except ImportError:
   pass
threshold = 10
_l_(534799)
hst_name = _c_(534802, _a_(534801, _n_(534800, "socket", lambda: socket), "gethostname"))
_l_(534803)

def fs_function(usage):
   _l_(534820)

   return_val = None
   _l_(534804)
   try:
      _l_(534817)

      return_val = _c_(534810, _a_(534806, _n_(534805, "subprocess", lambda: subprocess), "Popen"), ['df', '-Ph', _n_(534807, "usage", lambda: usage)], stdout=_a_(534809, _n_(534808, "subprocess", lambda: subprocess), "PIPE"))
      _l_(534811)
   except _n_(534812, "IndexError", lambda: IndexError):
      _l_(534816)

      _c_(534814, _n_(534813, "print", lambda: print), "Mount point not found.")
      _l_(534815)
   aux = _n_(534818, "return_val", lambda: return_val)
   _l_(534819)
   return aux


def show_result(output, mount_name):
   _l_(534849)

   if _c_(534823, _n_(534821, "len", lambda: len), _n_(534822, "output", lambda: output)) > 0:
      _l_(534848)

      for x in _n_(534824, "output", lambda: output)[1:]:
         _l_(534847)

         perc = _c_(534829, _n_(534825, "int", lambda: int), _c_(534828, _a_(534827, _n_(534826, "x", lambda: x), "split"))[-2][:-1])
         _l_(534830)
         if _n_(534831, "perc", lambda: perc) >= _n_(534832, "threshold", lambda: threshold):
            _l_(534846)

            _c_(534839, _n_(534833, "print", lambda: print), "Service Status:  Filesystem For " + _n_(534834, "mount_name", lambda: mount_name) + " is not normal and " + _c_(534837, _n_(534835, "str", lambda: str), _n_(534836, "perc", lambda: perc)) + "% used on the host",_n_(534838, "hst_name", lambda: hst_name))
            _l_(534840)
         else:
           _c_(534844, _n_(534841, "print", lambda: print), "Service Status:  Filesystem For " + _n_(534842, "mount_name", lambda: mount_name) + " is normal on the host",_n_(534843, "hst_name", lambda: hst_name))
           _l_(534845)
def fs_main():
   _l_(534895)

   rootfs = _c_(534851, _n_(534850, "fs_function", lambda: fs_function), "/")
   _l_(534852)
   varfs  = _c_(534854, _n_(534853, "fs_function", lambda: fs_function), "/var")
   _l_(534855)
   tmPfs = _c_(534857, _n_(534856, "fs_function", lambda: fs_function), "/tmp")
   _l_(534858)

   output = _c_(534865, _a_(534864, _c_(534863, _a_(534862, _c_(534861, _a_(534860, _n_(534859, "rootfs", lambda: rootfs), "communicate"))[0], "strip")), "split"), "\n")
   _l_(534866)
   _c_(534869, _n_(534867, "show_result", lambda: show_result), _n_(534868, "output", lambda: output), "root (/)")
   _l_(534870)

   output = _c_(534877, _a_(534876, _c_(534875, _a_(534874, _c_(534873, _a_(534872, _n_(534871, "varfs", lambda: varfs), "communicate"))[0], "strip")), "split"), "\n")
   _l_(534878)
   _c_(534881, _n_(534879, "show_result", lambda: show_result), _n_(534880, "output", lambda: output), "Var (/var)")
   _l_(534882)

   output = _c_(534889, _a_(534888, _c_(534887, _a_(534886, _c_(534885, _a_(534884, _n_(534883, "tmPfs", lambda: tmPfs), "communicate"))[0], "strip")), "split"), "\n")
   _l_(534890)
   _c_(534893, _n_(534891, "show_result", lambda: show_result), _n_(534892, "output", lambda: output), "tmp (/tmp)")
   _l_(534894)
_c_(534897, _n_(534896, "fs_main", lambda: fs_main))
_l_(534898)
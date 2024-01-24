# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43924260/filenotfound-error-when-trying-to-move-files-with-the-shutil-python-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import shutil, os
   _l_(387419)

except ImportError:
   pass

gifext = ['.gif', 'gifv']
_l_(387420)
picext = ['.png', '.jpg']
_l_(387421)

for file in _n_(387422, "files", lambda: files):
   _l_(387473)

   if _c_(387428, _a_(387424, _n_(387423, "file", lambda: file), "endswith"), _c_(387427, _n_(387425, "tuple", lambda: tuple), _n_(387426, "gifext", lambda: gifext))):
      _l_(387472)

      if not _c_(387433, _a_(387431, _a_(387430, _n_(387429, "os", lambda: os), "path"), "exists"), _n_(387432, "cdir", lambda: cdir)+'\Gifs'):
         _l_(387439)

         _c_(387437, _a_(387435, _n_(387434, "os", lambda: os), "makedirs"), _n_(387436, "cdir", lambda: cdir) + '\Gifs')
         _l_(387438)
      _c_(387445, _a_(387441, _n_(387440, "shutil", lambda: shutil), "move"), _n_(387442, "cdir", lambda: cdir) + _n_(387443, "file", lambda: file), _n_(387444, "cdir", lambda: cdir) + '\Gifs')
      _l_(387446)

   elif _c_(387452, _a_(387448, _n_(387447, "file", lambda: file), "endswith"), _c_(387451, _n_(387449, "tuple", lambda: tuple), _n_(387450, "picext", lambda: picext))):
      _l_(387471)

      if not _c_(387457, _a_(387455, _a_(387454, _n_(387453, "os", lambda: os), "path"), "exists"), _n_(387456, "cdir", lambda: cdir)+'\Images'):
         _l_(387463)

         _c_(387461, _a_(387459, _n_(387458, "os", lambda: os), "makedirs"), _n_(387460, "cdir", lambda: cdir) + '\Images')
         _l_(387462)
      _c_(387469, _a_(387465, _n_(387464, "shutil", lambda: shutil), "move"), _n_(387466, "cdir", lambda: cdir) + _n_(387467, "file", lambda: file), _n_(387468, "cdir", lambda: cdir) + '\Images')
      _l_(387470)
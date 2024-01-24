# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73933775/attributeerror-enter-when-using-with-taglib-filepath
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import os
   _l_(631098)

except ImportError:
   pass
try:
   import subprocess
   _l_(631100)

except ImportError:
   pass
try:
   import taglib
   _l_(631102)

except ImportError:
   pass
try:
   import sys
   _l_(631104)

except ImportError:
   pass

def set_song_metadata_by_path(path, inviter, duetpartner):
   _l_(631123)

   #with taglib.File(path, save_on_exit=True) as song:
   with _c_(631108, _a_(631106, _n_(631105, "taglib", lambda: taglib), "File"), _n_(631107, "path", lambda: path)) as song:
      _l_(631122)

      _a_(631110, _n_(631109, "song", lambda: song), "tags")["ALBUM"] = _n_(631111, "inviter", lambda: inviter)
      _l_(631112)
      _a_(631114, _n_(631113, "song", lambda: song), "tags")["ARTIST"] = _n_(631115, "inviter", lambda: inviter) + _n_(631116, "duetpartner", lambda: duetpartner)
      _l_(631117)
      _c_(631120, _a_(631119, _n_(631118, "song", lambda: song), "save"))
      _l_(631121)

# wipe metadata
def wipe_metadata(filetowipemetadata, output):
   _l_(631136)

   if _c_(631128, _a_(631125, _n_(631124, "subprocess", lambda: subprocess), "call"), 'ffmpeg -y -i "%s" -map_metadata -1 -c:v copy -c:a copy "%s"' % (_n_(631126, "filetowipemetadata", lambda: filetowipemetadata), _n_(631127, "output", lambda: output)), shell=True):
      _l_(631135)

      _c_(631133, _a_(631131, _a_(631130, _n_(631129, "sys", lambda: sys), "stderr"), "write"), "Error remuxing '%s', skipping." % _n_(631132, "filetowipemetadata", lambda: (filetowipemetadata)))
      _l_(631134)
# here was continue, but no loop hence this

_c_(631138, _n_(631137, "wipe_metadata", lambda: wipe_metadata), 'bored.m4a', 'bored2.m4a')
_l_(631139)
_c_(631141, _n_(631140, "set_song_metadata_by_path", lambda: set_song_metadata_by_path), './bored2.m4a', 'test1', 'test2')
_l_(631142)
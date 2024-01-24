# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64218176/attributeerror-line2d-object-has-no-property-xlabel
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import pandas as pd
  _l_(413103)

except ImportError:
  pass
try:
  import matplotlib.pyplot as plt
  _l_(413105)

except ImportError:
  pass
try:
  from flask import Flask, send_file, make_response, render_template
  _l_(413107)

except ImportError:
  pass
try:
  import io
  _l_(413109)

except ImportError:
  pass

app = _c_(413112, _n_(413110, "Flask", lambda: Flask), _n_(413111, "__name__", lambda: __name__))
_l_(413113)
#run_with_ngrok(app) 

@_c_(413116, _a_(413115, _n_(413114, "app", lambda: app), "route"), "/")
def home():
  _l_(413171)

  dates = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17']
  _l_(413117)
  steps = [9000, 9500.756, 9800.859, 10000.262, 9800.972, 10500.058, 11300.703]
  _l_(413118)
  df= _c_(413123, _a_(413120, _n_(413119, "pd", lambda: pd), "DataFrame"), {'date': _n_(413121, "dates", lambda: dates), 'steps': _n_(413122, "steps", lambda: steps)})
  _l_(413124)
  fig, axes = _c_(413127, _a_(413126, _n_(413125, "plt", lambda: plt), "subplots"), nrows=1, ncols=1)
  _l_(413128)
  major_xtick=[2,3,4,5,6,7]
  _l_(413129)
  major_xticklabel=['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17']
  _l_(413130)
  color=['blue','green','blue']
  _l_(413131)
  ax=_c_(413136, _a_(413133, _n_(413132, "df", lambda: df), "plot"), ax=_n_(413134, "axes", lambda: axes),figsize=(10,8),linewidth=2,marker='o',xlabel="Year" \
          ,ylabel="steps" \
          ,title="2dline plot" \
          ,xlim=(0,8),ylim=(2000,15000) \
          , color=_n_(413135, "color", lambda: color))
  _l_(413137)
  _c_(413141, _a_(413139, _n_(413138, "ax", lambda: ax), "set_xticks"), _n_(413140, "major_xtick", lambda: major_xtick))
  _l_(413142)
  _c_(413146, _a_(413144, _n_(413143, "ax", lambda: ax), "set_xticklabels"), _n_(413145, "major_xticklabel", lambda: major_xticklabel))
  _l_(413147)
  _c_(413150, _a_(413149, _n_(413148, "ax", lambda: ax), "legend"))
  _l_(413151)
  bytes_image = _c_(413154, _a_(413153, _n_(413152, "io", lambda: io), "BytesIO"))
  _l_(413155)
  _c_(413159, _a_(413157, _n_(413156, "plt", lambda: plt), "savefig"), _n_(413158, "bytes_image", lambda: bytes_image), format='png')
  _l_(413160)
  _c_(413163, _a_(413162, _n_(413161, "bytes_image", lambda: bytes_image), "seek"), 0)
  _l_(413164)
  bytes_obj = _n_(413165, "bytes_image", lambda: bytes_image) #do_plot()
  _l_(413166) #do_plot()
  aux = _c_(413169, _n_(413167, "send_file", lambda: send_file), _n_(413168, "bytes_obj", lambda: bytes_obj),
                     attachment_filename='plot.png',
                     mimetype='image/png')
  _l_(413170)
    
  # return render_template('create_plot.html', pfile='abc')
  # return "<h3>  {{ pfile }} is successfully created</h3>"
  return aux
#    app.run()
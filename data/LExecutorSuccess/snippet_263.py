# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def display_all(df):
   _l_(1541647)

   with _c_(1541637, _a_(1541636, _n_(1541635, "pd", lambda: pd), "option_context"), 'display.max_rows',1000):
      _l_(1541646)

      with _c_(1541640, _a_(1541639, _n_(1541638, "pd", lambda: pd), "option_context"), 'display.max_columns',1000):
         _l_(1541645)

         _c_(1541643, _n_(1541641, "display", lambda: display), _n_(1541642, "df", lambda: df))
         _l_(1541644)


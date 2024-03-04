# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_row = _a_(65225, _n_(65224, "df", lambda: df), "shape")[0]  # Gives number of rows
_l_(65226)  # Gives number of rows
count_col = _a_(65228, _n_(65227, "df", lambda: df), "shape")[1]  # Gives number of columns
_l_(65229)  # Gives number of columns

r, c = _a_(65231, _n_(65230, "df", lambda: df), "shape")
_l_(65232)


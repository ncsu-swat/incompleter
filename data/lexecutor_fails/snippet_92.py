# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_row = _a_(1548740, _n_(1548739, "df", lambda: df), "shape")[0]  # Gives number of rows
_l_(1548741)  # Gives number of rows
count_col = _a_(1548743, _n_(1548742, "df", lambda: df), "shape")[1]  # Gives number of columns
_l_(1548744)  # Gives number of columns

r, c = _a_(1548746, _n_(1548745, "df", lambda: df), "shape")
_l_(1548747)


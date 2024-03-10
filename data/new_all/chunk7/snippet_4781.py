# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77232147/filenotfounderror-errno-2-no-such-file-or-directory-c-users-sardo-downl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df=_c_(685193, _a_(685192, _n_(685191, "pd", lambda: pd), "read_csv"), r'C:\Users\sardo\Downloads\ChicagoCensusData.csv')
_l_(685194)
_c_(685198, _a_(685196, _n_(685195, "df", lambda: df), "to_sql"), "CENSUS_DATA", _n_(685197, "con", lambda: con), if_exists='replace', index=False, method='mutli')
_l_(685199)
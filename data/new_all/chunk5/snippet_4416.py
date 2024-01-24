# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58116673/fuzzy-string-matching-with-pandas-and-fuzzywuzzy-data-matching-typeerror-canno
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(664426)

except ImportError:
    pass


names_array=[]
_l_(664427)
ratio_array=[]
_l_(664428)
def match_names(wrong_names,correct_names):
    _l_(664450)

    for row in _n_(664429, "wrong_names", lambda: wrong_names):
        _l_(664446)

        x=_c_(664434, _a_(664431, _n_(664430, "process", lambda: process), "extractOne"), _n_(664432, "row", lambda: row), _n_(664433, "correct_names", lambda: correct_names))
        _l_(664435)
        _c_(664439, _a_(664437, _n_(664436, "names_array", lambda: names_array), "append"), _n_(664438, "x", lambda: x)[0])
        _l_(664440)
        _c_(664444, _a_(664442, _n_(664441, "ratio_array", lambda: ratio_array), "append"), _n_(664443, "x", lambda: x)[1])
        _l_(664445)
    aux = _n_(664447, "names_array", lambda: names_array),_n_(664448, "ratio_array", lambda: ratio_array)
    _l_(664449)
    return aux

fields = ['name']
_l_(664451)
#Wrong country names dataset
df=_c_(664455, _a_(664453, _n_(664452, "pd", lambda: pd), "read_csv"), "wrong-country-names.csv",encoding="ISO-8859-1",sep=';', skipinitialspace=True, usecols= _n_(664454, "fields", lambda: fields) )
_l_(664456)
_c_(664460, _n_(664457, "print", lambda: print), _a_(664459, _n_(664458, "df", lambda: df), "dtypes"))
_l_(664461)


wrong_names=_a_(664465, _c_(664464, _a_(664463, _n_(664462, "df", lambda: df), "dropna")), "values")
_l_(664466)


#Correct country names dataset
choices_df=_c_(664469, _a_(664468, _n_(664467, "pd", lambda: pd), "read_csv"), "country-names.csv",encoding="ISO-8859-1",sep='\t', skipinitialspace=True)
_l_(664470)
correct_names=_a_(664472, _n_(664471, "choices_df", lambda: choices_df), "values")
_l_(664473)

name_match,ratio_match=_c_(664477, _n_(664474, "match_names", lambda: match_names), _n_(664475, "wrong_names", lambda: wrong_names),_n_(664476, "correct_names", lambda: correct_names))
_l_(664478)

_n_(664479, "df", lambda: df)['correct_country_name']=_c_(664483, _a_(664481, _n_(664480, "pd", lambda: pd), "Series"), _n_(664482, "name_match", lambda: name_match))
_l_(664484)
_n_(664485, "df", lambda: df)['country_names_ratio']=_c_(664489, _a_(664487, _n_(664486, "pd", lambda: pd), "Series"), _n_(664488, "ratio_match", lambda: ratio_match))
_l_(664490)

_c_(664493, _a_(664492, _n_(664491, "df", lambda: df), "to_csv"), "string_matched_country_names.csv")
_l_(664494)

_c_(664499, _n_(664495, "print", lambda: print), _c_(664498, _a_(664497, _n_(664496, "df", lambda: df)[['name','correct_country_name','country_names_ratio']], "head"), 10))
_l_(664500)
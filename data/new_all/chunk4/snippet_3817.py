# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67273012/how-to-fix-attributeerror-int-object-has-no-attribute-strip-while-loading-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
local_path= '../../data/RetailStore.xlsx'
_l_(581507)
out_path= '../../out/hyperstore.csv'
_l_(581508)

def load_retail_data(local_path,sheet_name):
    _l_(581515)

    aux = _c_(581513, _a_(581510, _n_(581509, "pd", lambda: pd), "read_excel"), _n_(581511, "local_path", lambda: local_path),
        header=4,
        sheet_name=_n_(581512, "sheet_name", lambda: sheet_name),
        parse_dates=True
    )
    _l_(581514)
    return aux

def clean_headers(data_frame:_a_(581517, _n_(581516, "pd", lambda: pd), "DataFrame")) -> _a_(581519, _n_(581518, "pd", lambda: pd), "DataFrame"):
    _l_(581550)

    data_frame=_c_(581525, _a_(581521, _n_(581520, "data_frame", lambda: data_frame), "rename"), columns=lambda x:_c_(581524, _a_(581523, _n_(581522, "x", lambda: x), "strip")))
    _l_(581526)
    data_frame=_c_(581532, _a_(581528, _n_(581527, "data_frame", lambda: data_frame), "rename"), columns=lambda x:_c_(581531, _a_(581530, _n_(581529, "x", lambda: x), "replace"), '\n',' '))
    _l_(581533)
    data_frame=_c_(581539, _a_(581535, _n_(581534, "data_frame", lambda: data_frame), "rename"), columns=lambda x:_c_(581538, _a_(581537, _n_(581536, "x", lambda: x), "replace"), "'",' '))
    _l_(581540)
    data_frame=_c_(581546, _a_(581542, _n_(581541, "data_frame", lambda: data_frame), "rename"), columns=lambda x:_c_(581545, _a_(581544, _n_(581543, "x", lambda: x), "replace"), '  ',' '))
    _l_(581547)
    aux = _n_(581548, "data_frame", lambda: data_frame)
    _l_(581549)
    return aux

def filter_ship_mode(df):
    _l_(581559)

    aux = _n_(581551, "df", lambda: df)[(_n_(581552, "df", lambda: df)[_a_(581554, _n_(581553, "ColumnsStore", lambda: ColumnsStore), "ship_mode")]!= 'Standard Class') & (_n_(581555, "df", lambda: df)[_a_(581557, _n_(581556, "ColumnsStore", lambda: ColumnsStore), "ship_mode")]!='Second Class')]
    _l_(581558)
    return aux


def calc_retail_data(local_path,sheet_name):
    _l_(581575)

    retail_data=_c_(581563, _n_(581560, "load_retail_data", lambda: load_retail_data), _n_(581561, "local_path", lambda: local_path),_n_(581562, "sheet_name", lambda: sheet_name))
    _l_(581564)
    retail_clean_headers=_c_(581567, _n_(581565, "clean_headers", lambda: clean_headers), _n_(581566, "retail_data", lambda: retail_data))
    _l_(581568)
    retail_filtered=_c_(581571, _n_(581569, "filter_ship_mode", lambda: filter_ship_mode), _n_(581570, "retail_clean_headers", lambda: retail_clean_headers))
    _l_(581572)
    aux = _n_(581573, "retail_filtered", lambda: retail_filtered)
    _l_(581574)
    return aux


if _n_(581576, "__name__", lambda: __name__)=="__main__":
    _l_(581586)

    df_retail_data=_c_(581579, _n_(581577, "calc_retail_data", lambda: calc_retail_data), _n_(581578, "local_path", lambda: local_path),'Orders')
    _l_(581580)
    _c_(581584, _a_(581582, _n_(581581, "df_retail_data", lambda: df_retail_data), "to_csv"), _n_(581583, "out_path", lambda: out_path),index=False)
    _l_(581585)
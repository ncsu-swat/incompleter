# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57291797/dask-attributeerror-dataframe-object-has-no-attribute-getitem-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import boto3
        _l_(399753)

except ImportError:
        pass
try:
        import dask.dataframe as dd
        _l_(399755)

except ImportError:
        pass

def import_df(key):
        _l_(399767)

        s3 = _c_(399758, _a_(399757, _n_(399756, "boto3", lambda: boto3), "client"), 's3')
        _l_(399759)
        df = _c_(399763, _a_(399761, _n_(399760, "dd", lambda: dd), "read_csv"), 's3://.../' + _n_(399762, "key", lambda: key) ,encoding='latin1')
        _l_(399764)
        aux = _n_(399765, "df", lambda: df)
        _l_(399766)
        return aux

key = 'Churn/CLEANED_data/file.csv'
_l_(399768)
train = _c_(399771, _n_(399769, "import_df", lambda: import_df), _n_(399770, "key", lambda: key))
_l_(399772)
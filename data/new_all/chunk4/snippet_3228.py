# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77079339/getting-attributeerror-when-using-pickle-on-a-python-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
udf_bytes = _c_(593172, _a_(593171, _c_(593170, _a_(593169, _n_(593168, "s3_client", lambda: s3_client), "get_object"), Bucket="Bucket_name", Key="key")["Body"], "read"))
_l_(593173)

downloaded_func = _c_(593177, _a_(593175, _n_(593174, "pickle", lambda: pickle), "loads"), _n_(593176, "udf_bytes", lambda: udf_bytes))
_l_(593178)
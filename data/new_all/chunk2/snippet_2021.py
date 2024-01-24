# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69054414/why-am-i-getting-a-filenotfounderror-when-trying-to-create-a-sparkcontext
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(425429)

except ImportError:
    pass
try:
    from pyspark import SparkContext, SparkConf
    _l_(425431)

except ImportError:
    pass
try:
    from pyspark.streaming import StreamingContext
    _l_(425433)

except ImportError:
    pass
try:
    from pyspark.streaming.kafka import KafkaUtils
    _l_(425435)

except ImportError:
    pass

if _n_(425436, "__name__", lambda: __name__) == "__main__":
    _l_(425440)

    sc = _c_(425438, _n_(425437, "SparkContext", lambda: SparkContext), appName="PythonStreamingReceiverKafkaWordCount")
    _l_(425439)
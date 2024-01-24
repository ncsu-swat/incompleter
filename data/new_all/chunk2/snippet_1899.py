# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41553652/type-error-when-using-sparkit-learns-sparkcountvectorizer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from splearn.rdd import ArrayRDD
    _l_(448464)

except ImportError:
    pass
try:
    from splearn.feature_extraction.text import SparkCountVectorizer
    _l_(448466)

except ImportError:
    pass

jdbcDF = _c_(448476, _a_(448475, _c_(448474, _a_(448473, _c_(448472, _a_(448471, _c_(448470, _a_(448469, _a_(448468, _n_(448467, "spark", lambda: spark), "read"), "format"), 'jdbc'), "option"), 'url', 'jdbc:sqlserver://XXX:1433;database=XXX;user=XXX;password=XXX;'), "option"), 'dbtable', 'XXX.XXX'), "load"))
_l_(448477)

my_rdd = _a_(448483, _c_(448482, _a_(448479, _n_(448478, "jdbcDF", lambda: jdbcDF), "select"), _a_(448481, _n_(448480, "jdbcDF", lambda: jdbcDF), "columnoftexts")), "rdd")
_l_(448484)
_c_(448487, _a_(448486, _n_(448485, "my_rdd", lambda: my_rdd), "take"), 2)
_l_(448488)
# [Row(columnoftexts='some perfectly reasonable string'), Row(columnoftexts='another perfectly reasonable string')]

array_rdd = _c_(448491, _n_(448489, "ArrayRDD", lambda: ArrayRDD), _n_(448490, "my_rdd", lambda: my_rdd))
_l_(448492)
counter = _c_(448494, _n_(448493, "SparkCountVectorizer", lambda: SparkCountVectorizer))
_l_(448495)
tf = _c_(448499, _a_(448497, _n_(448496, "counter", lambda: counter), "fit_transform"), _n_(448498, "array_rdd", lambda: array_rdd))
_l_(448500)

# 17/01/09 15:07:50 WARN BlockManager: Putting block rdd_5_0 failed
# 17/01/09 15:07:50 ERROR Executor: Exception in task 0.0 in stage 1.0 (TID 1)
# org.apache.spark.api.python.PythonException: Traceback (most recent call last):
# File "/home/cgu.local/thiagovm/spark-2.0.0-bin-hadoop2.7/python/lib/pyspark.zip/pyspark/worker.py", line 172, in main
# process()
# File "/home/cgu.local/thiagovm/spark-2.0.0-bin-hadoop2.7/python/lib/pyspark.zip/pyspark/worker.py", line 167, in process
# serializer.dump_stream(func(split_index, iterator), outfile)
# File "/home/cgu.local/thiagovm/spark-2.0.0-bin-hadoop2.7/python/lib/pyspark.zip/pyspark/serializers.py", line 263, in dump_stream
# vs = list(itertools.islice(iterator, batch))
# File "/usr/local/lib/python3.5/site-packages/splearn/feature_extraction/text.py", line 289, in <lambda>
# A = Z.transform(lambda X: list(map(analyze, X)), column='X').persist()
# File "/usr/local/lib/python3.5/site-packages/sklearn/feature_extraction/text.py", line 238, in <lambda>
# tokenize(preprocess(self.decode(doc))), stop_words)
# File "/usr/local/lib/python3.5/site-packages/sklearn/feature_extraction/text.py", line 204, in <lambda>
# return lambda x: strip_accents(x.lower())
# AttributeError: 'numpy.ndarray' object has no attribute 'lower'

#     at org.apache.spark.api.python.PythonRunner$$anon$1.read(PythonRDD.scala:193)
#     at org.apache.spark.api.python.PythonRunner$$anon$1.<init>(PythonRDD.scala:234)
#     at org.apache.spark.api.python.PythonRunner.compute(PythonRDD.scala:152)
#     at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:63)
#     at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:319)
#     at org.apache.spark.rdd.RDD$$anonfun$8.apply(RDD.scala:332)
#     at org.apache.spark.rdd.RDD$$anonfun$8.apply(RDD.scala:330)
#     at org.apache.spark.storage.BlockManager$$anonfun$doPutIterator$1.apply(BlockManager.scala:935)
#     at org.apache.spark.storage.BlockManager$$anonfun$doPutIterator$1.apply(BlockManager.scala:910)
#     at org.apache.spark.storage.BlockManager.doPut(BlockManager.scala:866)
#     at org.apache.spark.storage.BlockManager.doPutIterator(BlockManager.scala:910)
#     at org.apache.spark.storage.BlockManager.getOrElseUpdate(BlockManager.scala:668)
#     at org.apache.spark.rdd.RDD.getOrCompute(RDD.scala:330)
#     at org.apache.spark.rdd.RDD.iterator(RDD.scala:281)
#     at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:63)
#     at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:319)
#     at org.apache.spark.rdd.RDD.iterator(RDD.scala:283)
#     at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:70)
#     at org.apache.spark.scheduler.Task.run(Task.scala:85)
#     at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:274)
#     at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
#     at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
#     at java.lang.Thread.run(Thread.java:745)
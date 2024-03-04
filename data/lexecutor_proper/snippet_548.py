# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1316767/how-can-i-explicitly-free-memory-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dask import delayed
    _l_(63617)

except ImportError:
    pass
def f(storage, index, chunk_size):
    _l_(63620)

    aux = _n_(63618, "storage", lambda: storage)
    _l_(63619)
    # read the chunk of size chunk_size starting at index in the file
    # process it using data in storage if needed
    # append data needed for further computations  to storage 
    return aux

partial_result = _c_(63622, _n_(63621, "delayed", lambda: delayed), [])  # put into the delayed() the constructor for your data structure
_l_(63623)  # put into the delayed() the constructor for your data structure
# I personally use "delayed(nx.Graph())" since I am creating a networkx Graph
chunk_size = 100  # ideally you want this as big as possible while still enabling the computations to fit in memory
_l_(63624)  # ideally you want this as big as possible while still enabling the computations to fit in memory
for index in _c_(63630, _n_(63625, "range", lambda: range), 0, _c_(63628, _n_(63626, "len", lambda: len), _n_(63627, "file", lambda: file)), _n_(63629, "chunk_size", lambda: chunk_size)):
    _l_(63639)

    # we indicates to dask that we will want to apply f to the parameters partial_result, index, chunk_size
    partial_result = _c_(63637, _c_(63633, _n_(63631, "delayed", lambda: delayed), _n_(63632, "f", lambda: f)), _n_(63634, "partial_result", lambda: partial_result), _n_(63635, "index", lambda: index), _n_(63636, "chunk_size", lambda: chunk_size))
    _l_(63638)

# this launches all the computations
result = _c_(63642, _a_(63641, _n_(63640, "partial_result", lambda: partial_result), "compute"))
_l_(63643)

# one thread is spawned for each "delayed" one at a time to compute its result
# dask then closes the tread, which solves the memory freeing issue
# the strange performance issue with gc.collect() is also avoided


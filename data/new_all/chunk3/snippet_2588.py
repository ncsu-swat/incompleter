# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70425953/attributeerror-tuple-object-has-no-attribute-lower-when-returning-specific
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
read_data = [] # stores Weather1, Weather2 etc. as we read that
_l_(572392) # stores Weather1, Weather2 etc. as we read that
final_array = [] # stores final arrays
_l_(572393) # stores final arrays

# stores data for weather1, then clears it out and
# then stores data for weather2, and so on...
sub_array = [] 
_l_(572394) 

# read each item of array
for x in _n_(572395, "array", lambda: array):
    _l_(572429)


    # e.g. for first row, is Weather1 already read?
    # No, it's not read
    if _c_(572398, _a_(572397, _n_(572396, "x", lambda: x)[0], "lower")) not in _n_(572399, "read_data", lambda: read_data):
        _l_(572428)


        # when you reach weather 2 and hit this statement,
        # sub_array will have data from weather1. So, if you find
        # sub_array with data, it is time to add it to the final_array
        # and start fresh with the sub_array
        if _c_(572402, _n_(572400, "len", lambda: len), _n_(572401, "sub_array", lambda: sub_array)) > 0:
            _l_(572415)

            _c_(572406, _a_(572404, _n_(572403, "final_array", lambda: final_array), "append"), _n_(572405, "sub_array", lambda: sub_array))
            _l_(572407)
            sub_array = [_n_(572408, "x", lambda: x)[2]]
            _l_(572409)
        # if sub_array is empty, just add data to it
        else:
            _c_(572413, _a_(572411, _n_(572410, "sub_array", lambda: sub_array), "append"), _n_(572412, "x", lambda: x)[2])
            _l_(572414)
        
        # make sure that read_data contains the item you read
        _c_(572421, _a_(572417, _n_(572416, "read_data", lambda: read_data), "append"), _c_(572420, _a_(572419, _n_(572418, "x", lambda: x)[0], "lower")))
        _l_(572422)

    # if weather1 has been read already, just add item to sub_array
    else:
        _c_(572426, _a_(572424, _n_(572423, "sub_array", lambda: sub_array), "append"), _n_(572425, "x", lambda: x)[2])
        _l_(572427)

# After you are done reading all the lines, sub_array may have data in it
# if so, add to the final alrray
if _c_(572432, _n_(572430, "len", lambda: len), _n_(572431, "sub_array", lambda: sub_array)) > 0:
    _l_(572438)

    _c_(572436, _a_(572434, _n_(572433, "final_array", lambda: final_array), "append"), _n_(572435, "sub_array", lambda: sub_array))
    _l_(572437)
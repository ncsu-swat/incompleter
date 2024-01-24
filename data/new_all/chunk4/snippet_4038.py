# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
from __future__ import division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(612215)
try:
    import sys
    _l_(612217)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(612219)

except ImportError:
    pass
try:
    import numpy as np
    _l_(612221)

except ImportError:
    pass
try:
    import pylab
    _l_(612223)

except ImportError:
    pass
try:
    import pdb
    _l_(612225)

except ImportError:
    pass
try:
    import time
    _l_(612227)

except ImportError:
    pass

def pad10star1(M, n):
    _l_(612316)

    """Pad M with the pad10*1 padding rule to reach a length multiple of r bits
    M: message pair (length in bits, string of hex characters ('9AFC...')
    n: length in bits (must be a multiple of 8)
    Example: pad10star1([60, 'BA594E0FB9EBBD30'],8) returns 'BA594E0FB9EBBD93'
    """

    [my_string_length, my_string]=_n_(612228, "M", lambda: M)
    _l_(612229)

    # Check the parameter n
    if _n_(612230, "n", lambda: n)%8!=0:
        _l_(612235)

        raise _c_(612233, _a_(612232, _n_(612231, "KeccakError", lambda: KeccakError), "KeccakError"), "n must be a multiple of 8")
        _l_(612234)

    # Check the length of the provided string
    if _c_(612238, _n_(612236, "len", lambda: len), _n_(612237, "my_string", lambda: my_string))%2!=0:
        _l_(612241)

        #Pad with one '0' to reach correct length (don't know test
        #vectors coding)
        my_string=_n_(612239, "my_string", lambda: my_string)+'0'
        _l_(612240)
    if _n_(612242, "my_string_length", lambda: my_string_length)>(_c_(612245, _n_(612243, "len", lambda: len), _n_(612244, "my_string", lambda: my_string))//2*8):
        _l_(612250)

        raise _c_(612248, _a_(612247, _n_(612246, "KeccakError", lambda: KeccakError), "KeccakError"), "the string is too short to contain the number of bits announced")
        _l_(612249)

    nr_bytes_filled=_n_(612251, "my_string_length", lambda: my_string_length)//8
    _l_(612252)
    nbr_bits_filled=_n_(612253, "my_string_length", lambda: my_string_length)%8
    _l_(612254)
    l = _n_(612255, "my_string_length", lambda: my_string_length) % _n_(612256, "n", lambda: n)
    _l_(612257)
    if ((_n_(612258, "n", lambda: n)-8) <= _n_(612259, "l", lambda: l) <= (_n_(612260, "n", lambda: n)-2)):
        _l_(612313)

        if (_n_(612261, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(612269)

            my_byte = 0
            _l_(612262)
        else:
            my_byte=_c_(612267, _n_(612263, "int", lambda: int), _n_(612264, "my_string", lambda: my_string)[_n_(612265, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(612266, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(612268)
        my_byte=(_n_(612270, "my_byte", lambda: my_byte)>>(8-_n_(612271, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(612272)
        my_byte=_n_(612273, "my_byte", lambda: my_byte)+2**_n_(612274, "nbr_bits_filled", lambda: (nbr_bits_filled))+2**7
        _l_(612275)
        my_byte="%02X" % _n_(612276, "my_byte", lambda: my_byte)
        _l_(612277)
        my_string=_n_(612278, "my_string", lambda: my_string)[0:_n_(612279, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(612280, "my_byte", lambda: my_byte)
        _l_(612281)
    else:
        if (_n_(612282, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(612290)

            my_byte = 0
            _l_(612283)
        else:
            my_byte=_c_(612288, _n_(612284, "int", lambda: int), _n_(612285, "my_string", lambda: my_string)[_n_(612286, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(612287, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(612289)
        my_byte=(_n_(612291, "my_byte", lambda: my_byte)>>(8-_n_(612292, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(612293)
        my_byte=_n_(612294, "my_byte", lambda: my_byte)+2**_n_(612295, "nbr_bits_filled", lambda: (nbr_bits_filled))
        _l_(612296)
        my_byte="%02X" % _n_(612297, "my_byte", lambda: my_byte)
        _l_(612298)
        my_string=_n_(612299, "my_string", lambda: my_string)[0:_n_(612300, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(612301, "my_byte", lambda: my_byte)
        _l_(612302)
        while((8*_c_(612305, _n_(612303, "len", lambda: len), _n_(612304, "my_string", lambda: my_string))//2)%_n_(612306, "n", lambda: n) < (_n_(612307, "n", lambda: n)-8)):
            _l_(612310)

            my_string=_n_(612308, "my_string", lambda: my_string)+'00'
            _l_(612309)
        my_string = _n_(612311, "my_string", lambda: my_string)+'80'
        _l_(612312)
    aux = _n_(612314, "my_string", lambda: my_string)
    _l_(612315)

    return aux

def KeccakF(to_hash, iterations, curr_iter, program, context, queue):
    _l_(612515)




    WORDLENGTH = 64
    _l_(612317)
    inputnum = _c_(612321, _n_(612318, "int", lambda: int), _a_(612320, _n_(612319, "to_hash", lambda: to_hash), "shape")[0]/5)
    _l_(612322)
    #Set up Round constants
    RC=[0x0000000000000001,
        0x0000000000008082,
        0x800000000000808A,
        0x8000000080008000,
        0x000000000000808B,
        0x0000000080000001,
        0x8000000080008081,
        0x8000000000008009,
        0x000000000000008A,
        0x0000000000000088,
        0x0000000080008009,
        0x000000008000000A,
        0x000000008000808B,
        0x800000000000008B,
        0x8000000000008089,
        0x8000000000008003,
        0x8000000000008002,
        0x8000000000000080,
        0x000000000000800A,
        0x800000008000000A,
        0x8000000080008081,
        0x8000000000008080,
        0x0000000080000001,
        0x8000000080008008]
    _l_(612323)

    round_constants = _c_(612331, _a_(612325, _n_(612324, "np", lambda: np), "array"), [_c_(612329, _a_(612327, _n_(612326, "np", lambda: np), "uint64"), _n_(612328, "x", lambda: x)) for x in _n_(612330, "RC", lambda: RC)])
    _l_(612332)
    round_constants_gpu = _c_(612342, _a_(612334, _n_(612333, "cl", lambda: cl), "Buffer"), _n_(612335, "context", lambda: context), _a_(612338, _a_(612337, _n_(612336, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(612341, _n_(612339, "len", lambda: len), _n_(612340, "round_constants", lambda: round_constants)))   #Why * 8???
    _l_(612343)   #Why * 8???
    _c_(612349, _a_(612345, _n_(612344, "cl", lambda: cl), "enqueue_copy"), _n_(612346, "queue", lambda: queue), _n_(612347, "round_constants_gpu", lambda: round_constants_gpu), _n_(612348, "round_constants", lambda: round_constants), is_blocking=False)
    _l_(612350)

    #Set up rotation offsets
    rotation_offsets = _c_(612353, _a_(612352, _n_(612351, "np", lambda: np), "array"), [0, 36, 3, 41, 18, \
                                1 ,44 ,10 ,45 ,2,   \
                                62, 6 ,43 ,15 ,61,  \
                                28, 55, 25, 21, 56, \
                                27, 20, 39, 8 ,14])
    _l_(612354)

    rotation_offsets = _c_(612362, _a_(612356, _n_(612355, "np", lambda: np), "array"), [_c_(612360, _a_(612358, _n_(612357, "np", lambda: np), "uint64"), _n_(612359, "x", lambda: x)) for x in _n_(612361, "rotation_offsets", lambda: rotation_offsets)])
    _l_(612363)
    rotation_gpu_buffer = _c_(612373, _a_(612365, _n_(612364, "cl", lambda: cl), "Buffer"), _n_(612366, "context", lambda: context), _a_(612369, _a_(612368, _n_(612367, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(612372, _n_(612370, "len", lambda: len), _n_(612371, "rotation_offsets", lambda: rotation_offsets)))
    _l_(612374)
    _c_(612380, _a_(612376, _n_(612375, "cl", lambda: cl), "enqueue_copy"), _n_(612377, "queue", lambda: queue), _n_(612378, "rotation_gpu_buffer", lambda: rotation_gpu_buffer), _n_(612379, "rotation_offsets", lambda: rotation_offsets), is_blocking=False)
    _l_(612381)




    stuff_to_hash = _c_(612390, _a_(612383, _n_(612382, "cl", lambda: cl), "Buffer"), _n_(612384, "context", lambda: context), _a_(612387, _a_(612386, _n_(612385, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _a_(612389, _n_(612388, "to_hash", lambda: to_hash), "size") * 8)
    _l_(612391)
    _c_(612397, _a_(612393, _n_(612392, "cl", lambda: cl), "enqueue_copy"), _n_(612394, "queue", lambda: queue), _n_(612395, "stuff_to_hash", lambda: stuff_to_hash), _n_(612396, "to_hash", lambda: to_hash), is_blocking=False)#is_block=True means wait for completion
    _l_(612398)#is_block=True means wait for completion

    #Buffer for GPU to write final hash
    gpu_final_hash = _c_(612407, _a_(612400, _n_(612399, "cl", lambda: cl), "Buffer"), _n_(612401, "context", lambda: context), _a_(612404, _a_(612403, _n_(612402, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), _a_(612406, _n_(612405, "to_hash", lambda: to_hash), "size") * 8)
    _l_(612408)
    
    #control the number of iterations of each hash in Keccak
    gpu_iterations = _c_(612418, _a_(612410, _n_(612409, "cl", lambda: cl), "Buffer"), _n_(612411, "context", lambda: context), _a_(612414, _a_(612413, _n_(612412, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _c_(612417, _n_(612415, "len", lambda: len), _n_(612416, "iterations", lambda: iterations))*8)
    _l_(612419)
    _c_(612428, _a_(612421, _n_(612420, "cl", lambda: cl), "enqueue_copy"), _n_(612422, "queue", lambda: queue), _n_(612423, "gpu_iterations", lambda: gpu_iterations), _c_(612427, _a_(612425, _n_(612424, "np", lambda: np), "array"), _n_(612426, "iterations", lambda: iterations)), is_blocking=False)#is_block=True means wait for completion
    _l_(612429)#is_block=True means wait for completion

    gpu_curr_iter = _c_(612436, _a_(612431, _n_(612430, "cl", lambda: cl), "Buffer"), _n_(612432, "context", lambda: context), _a_(612435, _a_(612434, _n_(612433, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8)
    _l_(612437)
    _c_(612446, _a_(612439, _n_(612438, "cl", lambda: cl), "enqueue_copy"), _n_(612440, "queue", lambda: queue), _n_(612441, "gpu_curr_iter", lambda: gpu_curr_iter), _c_(612445, _a_(612443, _n_(612442, "np", lambda: np), "array"), _n_(612444, "curr_iter", lambda: curr_iter)), is_blocking=False)#is_block=True means wait for completion
    _l_(612447)#is_block=True means wait for completion


    #Create 5x5 workgroup, local buffer
    local_size, global_size = (5, 5) , (5,5*_n_(612448, "inputnum", lambda: inputnum))
    _l_(612449)
    local_buf_w,local_buf_h = _c_(612452, _a_(612451, _n_(612450, "np", lambda: np), "uint64"), 5),_c_(612455, _a_(612454, _n_(612453, "np", lambda: np), "uint64"), 5)
    _l_(612456)
    A = _c_(612459, _a_(612458, _n_(612457, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(612460)
    B = _c_(612463, _a_(612462, _n_(612461, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(612464)
    C = _c_(612467, _a_(612466, _n_(612465, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(612468)
    D = _c_(612471, _a_(612470, _n_(612469, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(612472)

    #Hash input
    final_hash = _c_(612476, _a_(612474, _n_(612473, "np", lambda: np), "zeros"), (5*_n_(612475, "inputnum", lambda: inputnum),5))
    _l_(612477)
    final_hash = _c_(612485, _a_(612479, _n_(612478, "np", lambda: np), "array"), [_c_(612483, _a_(612481, _n_(612480, "np", lambda: np), "uint64"), _n_(612482, "x", lambda: x)) for x in _n_(612484, "final_hash", lambda: final_hash)])    
    _l_(612486)    
    hash_event = _c_(612504, _a_(612488, _n_(612487, "program", lambda: program), "sha_3_hash"), _n_(612489, "queue", lambda: queue), _n_(612490, "global_size", lambda: global_size), _n_(612491, "local_size", lambda: local_size),
                              _n_(612492, "stuff_to_hash", lambda: stuff_to_hash), _n_(612493, "gpu_final_hash", lambda: gpu_final_hash),_n_(612494, "rotation_gpu_buffer", lambda: rotation_gpu_buffer),_n_(612495, "round_constants_gpu", lambda: round_constants_gpu), _n_(612496, "gpu_iterations", lambda: gpu_iterations), _n_(612497, "gpu_curr_iter", lambda: gpu_curr_iter),
                              _n_(612498, "B", lambda: B),_n_(612499, "A", lambda: A), _n_(612500, "C", lambda: C), _n_(612501, "D", lambda: D), _n_(612502, "local_buf_w", lambda: local_buf_w),_n_(612503, "local_buf_h", lambda: local_buf_h))
    _l_(612505)

    
    
    _c_(612511, _a_(612507, _n_(612506, "cl", lambda: cl), "enqueue_copy"), _n_(612508, "queue", lambda: queue), _n_(612509, "final_hash", lambda: final_hash), _n_(612510, "gpu_final_hash", lambda: gpu_final_hash), is_blocking=True)
    _l_(612512)
    aux = _n_(612513, "final_hash", lambda: final_hash)
    _l_(612514)

    return aux


def Keccak(inputlist, n,r,c, program, context, queue):
    _l_(612786)




    inputnum = _c_(612518, _n_(612516, "len", lambda: len), _n_(612517, "inputlist", lambda: inputlist))
    _l_(612519)
    input_str = _n_(612520, "inputlist", lambda: inputlist)[0]
    _l_(612521)

    #P is a storage for the padded inputs
    P = []
    _l_(612522)

    #Z is a storage for the output hashes
    Z = []
    _l_(612523)

    iterations = []
    _l_(612524)

    #start = time.time()
    ### Padding Phase
    for i in _c_(612527, _n_(612525, "range", lambda: range), _n_(612526, "inputnum", lambda: inputnum)):
        _l_(612555)

        tmpstr = _c_(612536, _n_(612528, "pad10star1", lambda: pad10star1), [_c_(612532, _n_(612529, "len", lambda: len), _n_(612530, "inputlist", lambda: inputlist)[_n_(612531, "i", lambda: i)])*4, _n_(612533, "inputlist", lambda: inputlist)[_n_(612534, "i", lambda: i)]],_n_(612535, "r", lambda: r)) 
        _l_(612537) 
        _c_(612541, _a_(612539, _n_(612538, "P", lambda: P), "append"), _n_(612540, "tmpstr", lambda: tmpstr))
        _l_(612542)
        _c_(612545, _a_(612544, _n_(612543, "Z", lambda: Z), "append"), "")
        _l_(612546)
        _c_(612553, _a_(612548, _n_(612547, "iterations", lambda: iterations), "append"), (_c_(612551, _n_(612549, "len", lambda: len), _n_(612550, "tmpstr", lambda: tmpstr))*8//2)//_n_(612552, "r", lambda: r))
        _l_(612554)

    #print ("Time to run padding: " + str(time.time() - start))

    # Initialisation of state
    S = _c_(612559, _a_(612557, _n_(612556, "np", lambda: np), "zeros"), (5*_n_(612558, "inputnum", lambda: inputnum),5))
    _l_(612560)


    #Testing
    S = _c_(612568, _a_(612562, _n_(612561, "np", lambda: np), "array"), [_c_(612566, _a_(612564, _n_(612563, "np", lambda: np), "uint64"), _n_(612565, "x", lambda: x)) for x in _n_(612567, "S", lambda: S)])
    _l_(612569)

    #Initialize workgroup sizes for the gpu
    local_size, global_size = (5, 5) , (5,5*_n_(612570, "inputnum", lambda: inputnum))
    _l_(612571)

    for i in _c_(612576, _n_(612572, "range", lambda: range), _c_(612575, _n_(612573, "max", lambda: max), _n_(612574, "iterations", lambda: iterations))):
        _l_(612705)


        host_string = ""
        _l_(612577)
        Pi = _c_(612581, _a_(612579, _n_(612578, "np", lambda: np), "zeros"), (5*_n_(612580, "inputnum", lambda: inputnum),5))
        _l_(612582)
        Pi = _c_(612590, _a_(612584, _n_(612583, "np", lambda: np), "array"), [_c_(612588, _a_(612586, _n_(612585, "np", lambda: np), "uint64"), _n_(612587, "x", lambda: x)) for x in _n_(612589, "Pi", lambda: Pi)])
        _l_(612591)

        for j in _c_(612594, _n_(612592, "range", lambda: range), _n_(612593, "inputnum", lambda: inputnum)):
            _l_(612612)


            if (_n_(612595, "iterations", lambda: iterations)[_n_(612596, "j", lambda: j)] > _n_(612597, "i", lambda: i)):
                _l_(612611)

                #Absorbing Phase
                host_string = _n_(612598, "host_string", lambda: host_string) + _c_(612607, _n_(612599, "str", lambda: str), _n_(612600, "P", lambda: P)[_n_(612601, "j", lambda: j)][_n_(612602, "i", lambda: i)*(2*_n_(612603, "r", lambda: r)//8):(_n_(612604, "i", lambda: i)+1)*(2*_n_(612605, "r", lambda: r)//8)]+'00'*(_n_(612606, "c", lambda: c)//8))
                _l_(612608)
            else:
                #Dummy variables. Won't be used.
                host_string = _n_(612609, "host_string", lambda: host_string) + "0"*400
                _l_(612610)

        gpu_string = _c_(612623, _a_(612614, _n_(612613, "cl", lambda: cl), "Buffer"), _n_(612615, "context", lambda: context), _a_(612618, _a_(612617, _n_(612616, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(612621, _a_(612620, _n_(612619, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(612622, "host_string", lambda: host_string))
        _l_(612624)
        gpu_table = _c_(612632, _a_(612626, _n_(612625, "cl", lambda: cl), "Buffer"), _n_(612627, "context", lambda: context), _a_(612630, _a_(612629, _n_(612628, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 25*8 * _n_(612631, "inputnum", lambda: inputnum))
        _l_(612633)
        part_of_string = _c_(612636, _a_(612635, _n_(612634, "cl", lambda: cl), "LocalMemory"), 1*16)
        _l_(612637)
        _c_(612655, _a_(612639, _n_(612638, "program", lambda: program), "convert_str_to_table"), _n_(612640, "queue", lambda: queue),_n_(612641, "global_size", lambda: global_size),_n_(612642, "local_size", lambda: local_size), _n_(612643, "gpu_string", lambda: gpu_string), _n_(612644, "gpu_table", lambda: gpu_table), _n_(612645, "part_of_string", lambda: part_of_string), _c_(612648, _a_(612647, _n_(612646, "np", lambda: np), "uint64"), 5),_c_(612651, _a_(612650, _n_(612649, "np", lambda: np), "uint64"), 5),_c_(612654, _a_(612653, _n_(612652, "np", lambda: np), "uint64"), 64))
        _l_(612656)
        _c_(612662, _a_(612658, _n_(612657, "cl", lambda: cl), "enqueue_copy"), _n_(612659, "queue", lambda: queue), _n_(612660, "Pi", lambda: Pi), _n_(612661, "gpu_table", lambda: gpu_table), is_blocking=True)
        _l_(612663)




        for x in _c_(612666, _n_(612664, "range", lambda: range), 5*_n_(612665, "inputnum", lambda: inputnum)):
            _l_(612686)

            for y in _c_(612668, _n_(612667, "range", lambda: range), 5):
                _l_(612685)

                #print 'type S:',type(S[x][y]),'type P:',type(Pi[x][y])

                if (_n_(612669, "iterations", lambda: iterations)[_c_(612672, _n_(612670, "int", lambda: int), _n_(612671, "x", lambda: x)/5)] > _n_(612673, "i", lambda: i)):
                    _l_(612684)

                    _n_(612674, "S", lambda: S)[_n_(612675, "x", lambda: x)][_n_(612676, "y", lambda: y)] = _n_(612677, "S", lambda: S)[_n_(612678, "x", lambda: x)][_n_(612679, "y", lambda: y)]^_n_(612680, "Pi", lambda: Pi)[_n_(612681, "x", lambda: x)][_n_(612682, "y", lambda: y)]
                    _l_(612683)



        S = _c_(612694, _a_(612688, _n_(612687, "np", lambda: np), "array"), [_c_(612692, _a_(612690, _n_(612689, "np", lambda: np), "uint64"), _n_(612691, "x", lambda: x)) for x in _n_(612693, "S", lambda: S)])
        _l_(612695)
        #start = time.time()
        S = _c_(612703, _n_(612696, "KeccakF", lambda: KeccakF), _n_(612697, "S", lambda: S), _n_(612698, "iterations", lambda: iterations), _n_(612699, "i", lambda: i),  _n_(612700, "program", lambda: program), _n_(612701, "context", lambda: context), _n_(612702, "queue", lambda: queue))
        _l_(612704)

    #Squeezing phase

    outputstring = _c_(612709, _a_(612707, _n_(612706, "np", lambda: np), "chararray"), 400 * _n_(612708, "inputnum", lambda: inputnum))
    _l_(612710)
    gpu_table = _c_(612721, _a_(612712, _n_(612711, "cl", lambda: cl), "Buffer"), _n_(612713, "context", lambda: context), _a_(612716, _a_(612715, _n_(612714, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(612719, _a_(612718, _n_(612717, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(612720, "S", lambda: S))
    _l_(612722)
    gpu_string = _c_(612730, _a_(612724, _n_(612723, "cl", lambda: cl), "Buffer"), _n_(612725, "context", lambda: context), _a_(612728, _a_(612727, _n_(612726, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 144*8 * _n_(612729, "inputnum", lambda: inputnum))
    _l_(612731)
    _c_(612748, _a_(612733, _n_(612732, "program", lambda: program), "convert_table_to_str"), _n_(612734, "queue", lambda: queue),_n_(612735, "global_size", lambda: global_size),_n_(612736, "local_size", lambda: local_size),_n_(612737, "gpu_table", lambda: gpu_table), _n_(612738, "gpu_string", lambda: gpu_string),_c_(612741, _a_(612740, _n_(612739, "np", lambda: np), "uint64"), 5),_c_(612744, _a_(612743, _n_(612742, "np", lambda: np), "uint64"), 5),_c_(612747, _a_(612746, _n_(612745, "np", lambda: np), "uint64"), 64))
    _l_(612749)
    _c_(612755, _a_(612751, _n_(612750, "cl", lambda: cl), "enqueue_copy"), _n_(612752, "queue", lambda: queue), _n_(612753, "outputstring", lambda: outputstring), _n_(612754, "gpu_string", lambda: gpu_string), is_blocking=True)
    _l_(612756)

    string = _c_(612759, _a_(612757, '', "join"), _n_(612758, "outputstring", lambda: outputstring))
    _l_(612760)

    for x in _c_(612763, _n_(612761, "range", lambda: range), _n_(612762, "inputnum", lambda: inputnum)):
        _l_(612773)

        _n_(612764, "Z", lambda: Z)[_n_(612765, "x", lambda: x)] = _n_(612766, "Z", lambda: Z)[_n_(612767, "x", lambda: x)] + _n_(612768, "string", lambda: string)[400 * _n_(612769, "x", lambda: x): 400 * _n_(612770, "x", lambda: x) + _n_(612771, "r", lambda: r)*2//8]
        _l_(612772)


    for x in _c_(612776, _n_(612774, "range", lambda: range), _n_(612775, "inputnum", lambda: inputnum)):
        _l_(612783)

        _n_(612777, "Z", lambda: Z)[_n_(612778, "x", lambda: x)] = _n_(612779, "Z", lambda: Z)[_n_(612780, "x", lambda: x)][0:2*_n_(612781, "n", lambda: n)//8]
        _l_(612782)
    aux = _n_(612784, "Z", lambda: Z)
    _l_(612785)

    #output the pre-set number of bits
    return aux

if _n_(612787, "__name__", lambda: __name__) == '__main__':
    _l_(612876)



    # List our platforms
    platforms = _c_(612790, _a_(612789, _n_(612788, "cl", lambda: cl), "get_platforms"))
    _l_(612791)

    # Create a context with all the devices
    devices = _c_(612794, _a_(612793, _n_(612792, "platforms", lambda: platforms)[0], "get_devices"))
    _l_(612795)
    context = _c_(612799, _a_(612797, _n_(612796, "cl", lambda: cl), "Context"), _n_(612798, "devices", lambda: devices)[:2])
    _l_(612800)
    #print ('This context is associated with ', len(context.devices), 'devices')

    # Create a queue for transferring data and launching computations.
    # Turn on profiling to allow us to check event times.
    queue = _c_(612809, _a_(612802, _n_(612801, "cl", lambda: cl), "CommandQueue"), _n_(612803, "context", lambda: context), _a_(612805, _n_(612804, "context", lambda: context), "devices")[0],
                            properties=_a_(612808, _a_(612807, _n_(612806, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
    _l_(612810)
    #print ('The queue is using the device:', queue.device.name)

    
    program = _c_(612820, _a_(612819, _c_(612818, _a_(612812, _n_(612811, "cl", lambda: cl), "Program"), _n_(612813, "context", lambda: context), _c_(612817, _a_(612816, _c_(612815, _n_(612814, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
    _l_(612821)


    #PARAMETERS for SHA 512
    r = 576
    _l_(612822)
    c = 1024
    _l_(612823)
    n = 512
    _l_(612824)

    inputlist = []
    _l_(612825)
    _c_(612828, _a_(612827, _n_(612826, "inputlist", lambda: inputlist), "append"), "")
    _l_(612829)
    _c_(612832, _a_(612831, _n_(612830, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(612833)
    _c_(612836, _a_(612835, _n_(612834, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(612837)
    _c_(612840, _a_(612839, _n_(612838, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(612841)
    _c_(612844, _a_(612843, _n_(612842, "inputlist", lambda: inputlist), "append"), "a" * 1000)
    _l_(612845)

    start = _c_(612848, _a_(612847, _n_(612846, "time", lambda: time), "time"))
    _l_(612849)
    result = _c_(612858, _n_(612850, "Keccak", lambda: Keccak), _n_(612851, "inputlist", lambda: inputlist), _n_(612852, "n", lambda: n), _n_(612853, "r", lambda: r),_n_(612854, "c", lambda: c), _n_(612855, "program", lambda: program), _n_(612856, "context", lambda: context), _n_(612857, "queue", lambda: queue))
    _l_(612859)
    _c_(612861, _n_(612860, "print", lambda: print), "Hashing Result is")
    _l_(612862)
    _c_(612865, _n_(612863, "print", lambda: print), _n_(612864, "result", lambda: result))
    _l_(612866)
    _c_(612874, _n_(612867, "print", lambda: print), "Time taken is: " + _c_(612873, _n_(612868, "str", lambda: str), _c_(612871, _a_(612870, _n_(612869, "time", lambda: time), "time")) - _n_(612872, "start", lambda: start)))
    _l_(612875)
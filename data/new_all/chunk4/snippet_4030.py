# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
from __future__ import division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(584463)
try:
    import sys
    _l_(584465)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(584467)

except ImportError:
    pass
try:
    import numpy as np
    _l_(584469)

except ImportError:
    pass
try:
    import pylab
    _l_(584471)

except ImportError:
    pass
try:
    import pdb
    _l_(584473)

except ImportError:
    pass
try:
    import time
    _l_(584475)

except ImportError:
    pass

def pad10star1(M, n):
    _l_(584564)

    """Pad M with the pad10*1 padding rule to reach a length multiple of r bits
    M: message pair (length in bits, string of hex characters ('9AFC...')
    n: length in bits (must be a multiple of 8)
    Example: pad10star1([60, 'BA594E0FB9EBBD30'],8) returns 'BA594E0FB9EBBD93'
    """

    [my_string_length, my_string]=_n_(584476, "M", lambda: M)
    _l_(584477)

    # Check the parameter n
    if _n_(584478, "n", lambda: n)%8!=0:
        _l_(584483)

        raise _c_(584481, _a_(584480, _n_(584479, "KeccakError", lambda: KeccakError), "KeccakError"), "n must be a multiple of 8")
        _l_(584482)

    # Check the length of the provided string
    if _c_(584486, _n_(584484, "len", lambda: len), _n_(584485, "my_string", lambda: my_string))%2!=0:
        _l_(584489)

        #Pad with one '0' to reach correct length (don't know test
        #vectors coding)
        my_string=_n_(584487, "my_string", lambda: my_string)+'0'
        _l_(584488)
    if _n_(584490, "my_string_length", lambda: my_string_length)>(_c_(584493, _n_(584491, "len", lambda: len), _n_(584492, "my_string", lambda: my_string))//2*8):
        _l_(584498)

        raise _c_(584496, _a_(584495, _n_(584494, "KeccakError", lambda: KeccakError), "KeccakError"), "the string is too short to contain the number of bits announced")
        _l_(584497)

    nr_bytes_filled=_n_(584499, "my_string_length", lambda: my_string_length)//8
    _l_(584500)
    nbr_bits_filled=_n_(584501, "my_string_length", lambda: my_string_length)%8
    _l_(584502)
    l = _n_(584503, "my_string_length", lambda: my_string_length) % _n_(584504, "n", lambda: n)
    _l_(584505)
    if ((_n_(584506, "n", lambda: n)-8) <= _n_(584507, "l", lambda: l) <= (_n_(584508, "n", lambda: n)-2)):
        _l_(584561)

        if (_n_(584509, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(584517)

            my_byte = 0
            _l_(584510)
        else:
            my_byte=_c_(584515, _n_(584511, "int", lambda: int), _n_(584512, "my_string", lambda: my_string)[_n_(584513, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(584514, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(584516)
        my_byte=(_n_(584518, "my_byte", lambda: my_byte)>>(8-_n_(584519, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(584520)
        my_byte=_n_(584521, "my_byte", lambda: my_byte)+2**_n_(584522, "nbr_bits_filled", lambda: (nbr_bits_filled))+2**7
        _l_(584523)
        my_byte="%02X" % _n_(584524, "my_byte", lambda: my_byte)
        _l_(584525)
        my_string=_n_(584526, "my_string", lambda: my_string)[0:_n_(584527, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(584528, "my_byte", lambda: my_byte)
        _l_(584529)
    else:
        if (_n_(584530, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(584538)

            my_byte = 0
            _l_(584531)
        else:
            my_byte=_c_(584536, _n_(584532, "int", lambda: int), _n_(584533, "my_string", lambda: my_string)[_n_(584534, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(584535, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(584537)
        my_byte=(_n_(584539, "my_byte", lambda: my_byte)>>(8-_n_(584540, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(584541)
        my_byte=_n_(584542, "my_byte", lambda: my_byte)+2**_n_(584543, "nbr_bits_filled", lambda: (nbr_bits_filled))
        _l_(584544)
        my_byte="%02X" % _n_(584545, "my_byte", lambda: my_byte)
        _l_(584546)
        my_string=_n_(584547, "my_string", lambda: my_string)[0:_n_(584548, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(584549, "my_byte", lambda: my_byte)
        _l_(584550)
        while((8*_c_(584553, _n_(584551, "len", lambda: len), _n_(584552, "my_string", lambda: my_string))//2)%_n_(584554, "n", lambda: n) < (_n_(584555, "n", lambda: n)-8)):
            _l_(584558)

            my_string=_n_(584556, "my_string", lambda: my_string)+'00'
            _l_(584557)
        my_string = _n_(584559, "my_string", lambda: my_string)+'80'
        _l_(584560)
    aux = _n_(584562, "my_string", lambda: my_string)
    _l_(584563)

    return aux

def KeccakF(to_hash, iterations, curr_iter, program, context, queue):
    _l_(584763)




    WORDLENGTH = 64
    _l_(584565)
    inputnum = _c_(584569, _n_(584566, "int", lambda: int), _a_(584568, _n_(584567, "to_hash", lambda: to_hash), "shape")[0]/5)
    _l_(584570)
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
    _l_(584571)

    round_constants = _c_(584579, _a_(584573, _n_(584572, "np", lambda: np), "array"), [_c_(584577, _a_(584575, _n_(584574, "np", lambda: np), "uint64"), _n_(584576, "x", lambda: x)) for x in _n_(584578, "RC", lambda: RC)])
    _l_(584580)
    round_constants_gpu = _c_(584590, _a_(584582, _n_(584581, "cl", lambda: cl), "Buffer"), _n_(584583, "context", lambda: context), _a_(584586, _a_(584585, _n_(584584, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(584589, _n_(584587, "len", lambda: len), _n_(584588, "round_constants", lambda: round_constants)))   #Why * 8???
    _l_(584591)   #Why * 8???
    _c_(584597, _a_(584593, _n_(584592, "cl", lambda: cl), "enqueue_copy"), _n_(584594, "queue", lambda: queue), _n_(584595, "round_constants_gpu", lambda: round_constants_gpu), _n_(584596, "round_constants", lambda: round_constants), is_blocking=False)
    _l_(584598)

    #Set up rotation offsets
    rotation_offsets = _c_(584601, _a_(584600, _n_(584599, "np", lambda: np), "array"), [0, 36, 3, 41, 18, \
                                1 ,44 ,10 ,45 ,2,   \
                                62, 6 ,43 ,15 ,61,  \
                                28, 55, 25, 21, 56, \
                                27, 20, 39, 8 ,14])
    _l_(584602)

    rotation_offsets = _c_(584610, _a_(584604, _n_(584603, "np", lambda: np), "array"), [_c_(584608, _a_(584606, _n_(584605, "np", lambda: np), "uint64"), _n_(584607, "x", lambda: x)) for x in _n_(584609, "rotation_offsets", lambda: rotation_offsets)])
    _l_(584611)
    rotation_gpu_buffer = _c_(584621, _a_(584613, _n_(584612, "cl", lambda: cl), "Buffer"), _n_(584614, "context", lambda: context), _a_(584617, _a_(584616, _n_(584615, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(584620, _n_(584618, "len", lambda: len), _n_(584619, "rotation_offsets", lambda: rotation_offsets)))
    _l_(584622)
    _c_(584628, _a_(584624, _n_(584623, "cl", lambda: cl), "enqueue_copy"), _n_(584625, "queue", lambda: queue), _n_(584626, "rotation_gpu_buffer", lambda: rotation_gpu_buffer), _n_(584627, "rotation_offsets", lambda: rotation_offsets), is_blocking=False)
    _l_(584629)




    stuff_to_hash = _c_(584638, _a_(584631, _n_(584630, "cl", lambda: cl), "Buffer"), _n_(584632, "context", lambda: context), _a_(584635, _a_(584634, _n_(584633, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _a_(584637, _n_(584636, "to_hash", lambda: to_hash), "size") * 8)
    _l_(584639)
    _c_(584645, _a_(584641, _n_(584640, "cl", lambda: cl), "enqueue_copy"), _n_(584642, "queue", lambda: queue), _n_(584643, "stuff_to_hash", lambda: stuff_to_hash), _n_(584644, "to_hash", lambda: to_hash), is_blocking=False)#is_block=True means wait for completion
    _l_(584646)#is_block=True means wait for completion

    #Buffer for GPU to write final hash
    gpu_final_hash = _c_(584655, _a_(584648, _n_(584647, "cl", lambda: cl), "Buffer"), _n_(584649, "context", lambda: context), _a_(584652, _a_(584651, _n_(584650, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), _a_(584654, _n_(584653, "to_hash", lambda: to_hash), "size") * 8)
    _l_(584656)
    
    #control the number of iterations of each hash in Keccak
    gpu_iterations = _c_(584666, _a_(584658, _n_(584657, "cl", lambda: cl), "Buffer"), _n_(584659, "context", lambda: context), _a_(584662, _a_(584661, _n_(584660, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _c_(584665, _n_(584663, "len", lambda: len), _n_(584664, "iterations", lambda: iterations))*8)
    _l_(584667)
    _c_(584676, _a_(584669, _n_(584668, "cl", lambda: cl), "enqueue_copy"), _n_(584670, "queue", lambda: queue), _n_(584671, "gpu_iterations", lambda: gpu_iterations), _c_(584675, _a_(584673, _n_(584672, "np", lambda: np), "array"), _n_(584674, "iterations", lambda: iterations)), is_blocking=False)#is_block=True means wait for completion
    _l_(584677)#is_block=True means wait for completion

    gpu_curr_iter = _c_(584684, _a_(584679, _n_(584678, "cl", lambda: cl), "Buffer"), _n_(584680, "context", lambda: context), _a_(584683, _a_(584682, _n_(584681, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8)
    _l_(584685)
    _c_(584694, _a_(584687, _n_(584686, "cl", lambda: cl), "enqueue_copy"), _n_(584688, "queue", lambda: queue), _n_(584689, "gpu_curr_iter", lambda: gpu_curr_iter), _c_(584693, _a_(584691, _n_(584690, "np", lambda: np), "array"), _n_(584692, "curr_iter", lambda: curr_iter)), is_blocking=False)#is_block=True means wait for completion
    _l_(584695)#is_block=True means wait for completion


    #Create 5x5 workgroup, local buffer
    local_size, global_size = (5, 5) , (5,5*_n_(584696, "inputnum", lambda: inputnum))
    _l_(584697)
    local_buf_w,local_buf_h = _c_(584700, _a_(584699, _n_(584698, "np", lambda: np), "uint64"), 5),_c_(584703, _a_(584702, _n_(584701, "np", lambda: np), "uint64"), 5)
    _l_(584704)
    A = _c_(584707, _a_(584706, _n_(584705, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(584708)
    B = _c_(584711, _a_(584710, _n_(584709, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(584712)
    C = _c_(584715, _a_(584714, _n_(584713, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(584716)
    D = _c_(584719, _a_(584718, _n_(584717, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(584720)

    #Hash input
    final_hash = _c_(584724, _a_(584722, _n_(584721, "np", lambda: np), "zeros"), (5*_n_(584723, "inputnum", lambda: inputnum),5))
    _l_(584725)
    final_hash = _c_(584733, _a_(584727, _n_(584726, "np", lambda: np), "array"), [_c_(584731, _a_(584729, _n_(584728, "np", lambda: np), "uint64"), _n_(584730, "x", lambda: x)) for x in _n_(584732, "final_hash", lambda: final_hash)])    
    _l_(584734)    
    hash_event = _c_(584752, _a_(584736, _n_(584735, "program", lambda: program), "sha_3_hash"), _n_(584737, "queue", lambda: queue), _n_(584738, "global_size", lambda: global_size), _n_(584739, "local_size", lambda: local_size),
                              _n_(584740, "stuff_to_hash", lambda: stuff_to_hash), _n_(584741, "gpu_final_hash", lambda: gpu_final_hash),_n_(584742, "rotation_gpu_buffer", lambda: rotation_gpu_buffer),_n_(584743, "round_constants_gpu", lambda: round_constants_gpu), _n_(584744, "gpu_iterations", lambda: gpu_iterations), _n_(584745, "gpu_curr_iter", lambda: gpu_curr_iter),
                              _n_(584746, "B", lambda: B),_n_(584747, "A", lambda: A), _n_(584748, "C", lambda: C), _n_(584749, "D", lambda: D), _n_(584750, "local_buf_w", lambda: local_buf_w),_n_(584751, "local_buf_h", lambda: local_buf_h))
    _l_(584753)

    
    
    _c_(584759, _a_(584755, _n_(584754, "cl", lambda: cl), "enqueue_copy"), _n_(584756, "queue", lambda: queue), _n_(584757, "final_hash", lambda: final_hash), _n_(584758, "gpu_final_hash", lambda: gpu_final_hash), is_blocking=True)
    _l_(584760)
    aux = _n_(584761, "final_hash", lambda: final_hash)
    _l_(584762)

    return aux


def Keccak(inputlist, n,r,c, program, context, queue):
    _l_(585034)




    inputnum = _c_(584766, _n_(584764, "len", lambda: len), _n_(584765, "inputlist", lambda: inputlist))
    _l_(584767)
    input_str = _n_(584768, "inputlist", lambda: inputlist)[0]
    _l_(584769)

    #P is a storage for the padded inputs
    P = []
    _l_(584770)

    #Z is a storage for the output hashes
    Z = []
    _l_(584771)

    iterations = []
    _l_(584772)

    #start = time.time()
    ### Padding Phase
    for i in _c_(584775, _n_(584773, "range", lambda: range), _n_(584774, "inputnum", lambda: inputnum)):
        _l_(584803)

        tmpstr = _c_(584784, _n_(584776, "pad10star1", lambda: pad10star1), [_c_(584780, _n_(584777, "len", lambda: len), _n_(584778, "inputlist", lambda: inputlist)[_n_(584779, "i", lambda: i)])*4, _n_(584781, "inputlist", lambda: inputlist)[_n_(584782, "i", lambda: i)]],_n_(584783, "r", lambda: r)) 
        _l_(584785) 
        _c_(584789, _a_(584787, _n_(584786, "P", lambda: P), "append"), _n_(584788, "tmpstr", lambda: tmpstr))
        _l_(584790)
        _c_(584793, _a_(584792, _n_(584791, "Z", lambda: Z), "append"), "")
        _l_(584794)
        _c_(584801, _a_(584796, _n_(584795, "iterations", lambda: iterations), "append"), (_c_(584799, _n_(584797, "len", lambda: len), _n_(584798, "tmpstr", lambda: tmpstr))*8//2)//_n_(584800, "r", lambda: r))
        _l_(584802)

    #print ("Time to run padding: " + str(time.time() - start))

    # Initialisation of state
    S = _c_(584807, _a_(584805, _n_(584804, "np", lambda: np), "zeros"), (5*_n_(584806, "inputnum", lambda: inputnum),5))
    _l_(584808)


    #Testing
    S = _c_(584816, _a_(584810, _n_(584809, "np", lambda: np), "array"), [_c_(584814, _a_(584812, _n_(584811, "np", lambda: np), "uint64"), _n_(584813, "x", lambda: x)) for x in _n_(584815, "S", lambda: S)])
    _l_(584817)

    #Initialize workgroup sizes for the gpu
    local_size, global_size = (5, 5) , (5,5*_n_(584818, "inputnum", lambda: inputnum))
    _l_(584819)

    for i in _c_(584824, _n_(584820, "range", lambda: range), _c_(584823, _n_(584821, "max", lambda: max), _n_(584822, "iterations", lambda: iterations))):
        _l_(584953)


        host_string = ""
        _l_(584825)
        Pi = _c_(584829, _a_(584827, _n_(584826, "np", lambda: np), "zeros"), (5*_n_(584828, "inputnum", lambda: inputnum),5))
        _l_(584830)
        Pi = _c_(584838, _a_(584832, _n_(584831, "np", lambda: np), "array"), [_c_(584836, _a_(584834, _n_(584833, "np", lambda: np), "uint64"), _n_(584835, "x", lambda: x)) for x in _n_(584837, "Pi", lambda: Pi)])
        _l_(584839)

        for j in _c_(584842, _n_(584840, "range", lambda: range), _n_(584841, "inputnum", lambda: inputnum)):
            _l_(584860)


            if (_n_(584843, "iterations", lambda: iterations)[_n_(584844, "j", lambda: j)] > _n_(584845, "i", lambda: i)):
                _l_(584859)

                #Absorbing Phase
                host_string = _n_(584846, "host_string", lambda: host_string) + _c_(584855, _n_(584847, "str", lambda: str), _n_(584848, "P", lambda: P)[_n_(584849, "j", lambda: j)][_n_(584850, "i", lambda: i)*(2*_n_(584851, "r", lambda: r)//8):(_n_(584852, "i", lambda: i)+1)*(2*_n_(584853, "r", lambda: r)//8)]+'00'*(_n_(584854, "c", lambda: c)//8))
                _l_(584856)
            else:
                #Dummy variables. Won't be used.
                host_string = _n_(584857, "host_string", lambda: host_string) + "0"*400
                _l_(584858)

        gpu_string = _c_(584871, _a_(584862, _n_(584861, "cl", lambda: cl), "Buffer"), _n_(584863, "context", lambda: context), _a_(584866, _a_(584865, _n_(584864, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(584869, _a_(584868, _n_(584867, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(584870, "host_string", lambda: host_string))
        _l_(584872)
        gpu_table = _c_(584880, _a_(584874, _n_(584873, "cl", lambda: cl), "Buffer"), _n_(584875, "context", lambda: context), _a_(584878, _a_(584877, _n_(584876, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 25*8 * _n_(584879, "inputnum", lambda: inputnum))
        _l_(584881)
        part_of_string = _c_(584884, _a_(584883, _n_(584882, "cl", lambda: cl), "LocalMemory"), 1*16)
        _l_(584885)
        _c_(584903, _a_(584887, _n_(584886, "program", lambda: program), "convert_str_to_table"), _n_(584888, "queue", lambda: queue),_n_(584889, "global_size", lambda: global_size),_n_(584890, "local_size", lambda: local_size), _n_(584891, "gpu_string", lambda: gpu_string), _n_(584892, "gpu_table", lambda: gpu_table), _n_(584893, "part_of_string", lambda: part_of_string), _c_(584896, _a_(584895, _n_(584894, "np", lambda: np), "uint64"), 5),_c_(584899, _a_(584898, _n_(584897, "np", lambda: np), "uint64"), 5),_c_(584902, _a_(584901, _n_(584900, "np", lambda: np), "uint64"), 64))
        _l_(584904)
        _c_(584910, _a_(584906, _n_(584905, "cl", lambda: cl), "enqueue_copy"), _n_(584907, "queue", lambda: queue), _n_(584908, "Pi", lambda: Pi), _n_(584909, "gpu_table", lambda: gpu_table), is_blocking=True)
        _l_(584911)




        for x in _c_(584914, _n_(584912, "range", lambda: range), 5*_n_(584913, "inputnum", lambda: inputnum)):
            _l_(584934)

            for y in _c_(584916, _n_(584915, "range", lambda: range), 5):
                _l_(584933)

                #print 'type S:',type(S[x][y]),'type P:',type(Pi[x][y])

                if (_n_(584917, "iterations", lambda: iterations)[_c_(584920, _n_(584918, "int", lambda: int), _n_(584919, "x", lambda: x)/5)] > _n_(584921, "i", lambda: i)):
                    _l_(584932)

                    _n_(584922, "S", lambda: S)[_n_(584923, "x", lambda: x)][_n_(584924, "y", lambda: y)] = _n_(584925, "S", lambda: S)[_n_(584926, "x", lambda: x)][_n_(584927, "y", lambda: y)]^_n_(584928, "Pi", lambda: Pi)[_n_(584929, "x", lambda: x)][_n_(584930, "y", lambda: y)]
                    _l_(584931)



        S = _c_(584942, _a_(584936, _n_(584935, "np", lambda: np), "array"), [_c_(584940, _a_(584938, _n_(584937, "np", lambda: np), "uint64"), _n_(584939, "x", lambda: x)) for x in _n_(584941, "S", lambda: S)])
        _l_(584943)
        #start = time.time()
        S = _c_(584951, _n_(584944, "KeccakF", lambda: KeccakF), _n_(584945, "S", lambda: S), _n_(584946, "iterations", lambda: iterations), _n_(584947, "i", lambda: i),  _n_(584948, "program", lambda: program), _n_(584949, "context", lambda: context), _n_(584950, "queue", lambda: queue))
        _l_(584952)

    #Squeezing phase

    outputstring = _c_(584957, _a_(584955, _n_(584954, "np", lambda: np), "chararray"), 400 * _n_(584956, "inputnum", lambda: inputnum))
    _l_(584958)
    gpu_table = _c_(584969, _a_(584960, _n_(584959, "cl", lambda: cl), "Buffer"), _n_(584961, "context", lambda: context), _a_(584964, _a_(584963, _n_(584962, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(584967, _a_(584966, _n_(584965, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(584968, "S", lambda: S))
    _l_(584970)
    gpu_string = _c_(584978, _a_(584972, _n_(584971, "cl", lambda: cl), "Buffer"), _n_(584973, "context", lambda: context), _a_(584976, _a_(584975, _n_(584974, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 144*8 * _n_(584977, "inputnum", lambda: inputnum))
    _l_(584979)
    _c_(584996, _a_(584981, _n_(584980, "program", lambda: program), "convert_table_to_str"), _n_(584982, "queue", lambda: queue),_n_(584983, "global_size", lambda: global_size),_n_(584984, "local_size", lambda: local_size),_n_(584985, "gpu_table", lambda: gpu_table), _n_(584986, "gpu_string", lambda: gpu_string),_c_(584989, _a_(584988, _n_(584987, "np", lambda: np), "uint64"), 5),_c_(584992, _a_(584991, _n_(584990, "np", lambda: np), "uint64"), 5),_c_(584995, _a_(584994, _n_(584993, "np", lambda: np), "uint64"), 64))
    _l_(584997)
    _c_(585003, _a_(584999, _n_(584998, "cl", lambda: cl), "enqueue_copy"), _n_(585000, "queue", lambda: queue), _n_(585001, "outputstring", lambda: outputstring), _n_(585002, "gpu_string", lambda: gpu_string), is_blocking=True)
    _l_(585004)

    string = _c_(585007, _a_(585005, '', "join"), _n_(585006, "outputstring", lambda: outputstring))
    _l_(585008)

    for x in _c_(585011, _n_(585009, "range", lambda: range), _n_(585010, "inputnum", lambda: inputnum)):
        _l_(585021)

        _n_(585012, "Z", lambda: Z)[_n_(585013, "x", lambda: x)] = _n_(585014, "Z", lambda: Z)[_n_(585015, "x", lambda: x)] + _n_(585016, "string", lambda: string)[400 * _n_(585017, "x", lambda: x): 400 * _n_(585018, "x", lambda: x) + _n_(585019, "r", lambda: r)*2//8]
        _l_(585020)


    for x in _c_(585024, _n_(585022, "range", lambda: range), _n_(585023, "inputnum", lambda: inputnum)):
        _l_(585031)

        _n_(585025, "Z", lambda: Z)[_n_(585026, "x", lambda: x)] = _n_(585027, "Z", lambda: Z)[_n_(585028, "x", lambda: x)][0:2*_n_(585029, "n", lambda: n)//8]
        _l_(585030)
    aux = _n_(585032, "Z", lambda: Z)
    _l_(585033)

    #output the pre-set number of bits
    return aux

if _n_(585035, "__name__", lambda: __name__) == '__main__':
    _l_(585124)



    # List our platforms
    platforms = _c_(585038, _a_(585037, _n_(585036, "cl", lambda: cl), "get_platforms"))
    _l_(585039)

    # Create a context with all the devices
    devices = _c_(585042, _a_(585041, _n_(585040, "platforms", lambda: platforms)[0], "get_devices"))
    _l_(585043)
    context = _c_(585047, _a_(585045, _n_(585044, "cl", lambda: cl), "Context"), _n_(585046, "devices", lambda: devices)[:2])
    _l_(585048)
    #print ('This context is associated with ', len(context.devices), 'devices')

    # Create a queue for transferring data and launching computations.
    # Turn on profiling to allow us to check event times.
    queue = _c_(585057, _a_(585050, _n_(585049, "cl", lambda: cl), "CommandQueue"), _n_(585051, "context", lambda: context), _a_(585053, _n_(585052, "context", lambda: context), "devices")[0],
                            properties=_a_(585056, _a_(585055, _n_(585054, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
    _l_(585058)
    #print ('The queue is using the device:', queue.device.name)

    
    program = _c_(585068, _a_(585067, _c_(585066, _a_(585060, _n_(585059, "cl", lambda: cl), "Program"), _n_(585061, "context", lambda: context), _c_(585065, _a_(585064, _c_(585063, _n_(585062, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
    _l_(585069)


    #PARAMETERS for SHA 512
    r = 576
    _l_(585070)
    c = 1024
    _l_(585071)
    n = 512
    _l_(585072)

    inputlist = []
    _l_(585073)
    _c_(585076, _a_(585075, _n_(585074, "inputlist", lambda: inputlist), "append"), "")
    _l_(585077)
    _c_(585080, _a_(585079, _n_(585078, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(585081)
    _c_(585084, _a_(585083, _n_(585082, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(585085)
    _c_(585088, _a_(585087, _n_(585086, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(585089)
    _c_(585092, _a_(585091, _n_(585090, "inputlist", lambda: inputlist), "append"), "a" * 1000)
    _l_(585093)

    start = _c_(585096, _a_(585095, _n_(585094, "time", lambda: time), "time"))
    _l_(585097)
    result = _c_(585106, _n_(585098, "Keccak", lambda: Keccak), _n_(585099, "inputlist", lambda: inputlist), _n_(585100, "n", lambda: n), _n_(585101, "r", lambda: r),_n_(585102, "c", lambda: c), _n_(585103, "program", lambda: program), _n_(585104, "context", lambda: context), _n_(585105, "queue", lambda: queue))
    _l_(585107)
    _c_(585109, _n_(585108, "print", lambda: print), "Hashing Result is")
    _l_(585110)
    _c_(585113, _n_(585111, "print", lambda: print), _n_(585112, "result", lambda: result))
    _l_(585114)
    _c_(585122, _n_(585115, "print", lambda: print), "Time taken is: " + _c_(585121, _n_(585116, "str", lambda: str), _c_(585119, _a_(585118, _n_(585117, "time", lambda: time), "time")) - _n_(585120, "start", lambda: start)))
    _l_(585123)
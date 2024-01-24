# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
from __future__ import division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(640021)
try:
    import sys
    _l_(640023)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(640025)

except ImportError:
    pass
try:
    import numpy as np
    _l_(640027)

except ImportError:
    pass
try:
    import pylab
    _l_(640029)

except ImportError:
    pass
try:
    import pdb
    _l_(640031)

except ImportError:
    pass
try:
    import time
    _l_(640033)

except ImportError:
    pass

def pad10star1(M, n):
    _l_(640122)

    """Pad M with the pad10*1 padding rule to reach a length multiple of r bits
    M: message pair (length in bits, string of hex characters ('9AFC...')
    n: length in bits (must be a multiple of 8)
    Example: pad10star1([60, 'BA594E0FB9EBBD30'],8) returns 'BA594E0FB9EBBD93'
    """

    [my_string_length, my_string]=_n_(640034, "M", lambda: M)
    _l_(640035)

    # Check the parameter n
    if _n_(640036, "n", lambda: n)%8!=0:
        _l_(640041)

        raise _c_(640039, _a_(640038, _n_(640037, "KeccakError", lambda: KeccakError), "KeccakError"), "n must be a multiple of 8")
        _l_(640040)

    # Check the length of the provided string
    if _c_(640044, _n_(640042, "len", lambda: len), _n_(640043, "my_string", lambda: my_string))%2!=0:
        _l_(640047)

        #Pad with one '0' to reach correct length (don't know test
        #vectors coding)
        my_string=_n_(640045, "my_string", lambda: my_string)+'0'
        _l_(640046)
    if _n_(640048, "my_string_length", lambda: my_string_length)>(_c_(640051, _n_(640049, "len", lambda: len), _n_(640050, "my_string", lambda: my_string))//2*8):
        _l_(640056)

        raise _c_(640054, _a_(640053, _n_(640052, "KeccakError", lambda: KeccakError), "KeccakError"), "the string is too short to contain the number of bits announced")
        _l_(640055)

    nr_bytes_filled=_n_(640057, "my_string_length", lambda: my_string_length)//8
    _l_(640058)
    nbr_bits_filled=_n_(640059, "my_string_length", lambda: my_string_length)%8
    _l_(640060)
    l = _n_(640061, "my_string_length", lambda: my_string_length) % _n_(640062, "n", lambda: n)
    _l_(640063)
    if ((_n_(640064, "n", lambda: n)-8) <= _n_(640065, "l", lambda: l) <= (_n_(640066, "n", lambda: n)-2)):
        _l_(640119)

        if (_n_(640067, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(640075)

            my_byte = 0
            _l_(640068)
        else:
            my_byte=_c_(640073, _n_(640069, "int", lambda: int), _n_(640070, "my_string", lambda: my_string)[_n_(640071, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(640072, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(640074)
        my_byte=(_n_(640076, "my_byte", lambda: my_byte)>>(8-_n_(640077, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(640078)
        my_byte=_n_(640079, "my_byte", lambda: my_byte)+2**_n_(640080, "nbr_bits_filled", lambda: (nbr_bits_filled))+2**7
        _l_(640081)
        my_byte="%02X" % _n_(640082, "my_byte", lambda: my_byte)
        _l_(640083)
        my_string=_n_(640084, "my_string", lambda: my_string)[0:_n_(640085, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(640086, "my_byte", lambda: my_byte)
        _l_(640087)
    else:
        if (_n_(640088, "nbr_bits_filled", lambda: nbr_bits_filled) == 0):
            _l_(640096)

            my_byte = 0
            _l_(640089)
        else:
            my_byte=_c_(640094, _n_(640090, "int", lambda: int), _n_(640091, "my_string", lambda: my_string)[_n_(640092, "nr_bytes_filled", lambda: nr_bytes_filled)*2:_n_(640093, "nr_bytes_filled", lambda: nr_bytes_filled)*2+2],16)
            _l_(640095)
        my_byte=(_n_(640097, "my_byte", lambda: my_byte)>>(8-_n_(640098, "nbr_bits_filled", lambda: nbr_bits_filled)))
        _l_(640099)
        my_byte=_n_(640100, "my_byte", lambda: my_byte)+2**_n_(640101, "nbr_bits_filled", lambda: (nbr_bits_filled))
        _l_(640102)
        my_byte="%02X" % _n_(640103, "my_byte", lambda: my_byte)
        _l_(640104)
        my_string=_n_(640105, "my_string", lambda: my_string)[0:_n_(640106, "nr_bytes_filled", lambda: nr_bytes_filled)*2]+_n_(640107, "my_byte", lambda: my_byte)
        _l_(640108)
        while((8*_c_(640111, _n_(640109, "len", lambda: len), _n_(640110, "my_string", lambda: my_string))//2)%_n_(640112, "n", lambda: n) < (_n_(640113, "n", lambda: n)-8)):
            _l_(640116)

            my_string=_n_(640114, "my_string", lambda: my_string)+'00'
            _l_(640115)
        my_string = _n_(640117, "my_string", lambda: my_string)+'80'
        _l_(640118)
    aux = _n_(640120, "my_string", lambda: my_string)
    _l_(640121)

    return aux

def KeccakF(to_hash, iterations, curr_iter, program, context, queue):
    _l_(640321)




    WORDLENGTH = 64
    _l_(640123)
    inputnum = _c_(640127, _n_(640124, "int", lambda: int), _a_(640126, _n_(640125, "to_hash", lambda: to_hash), "shape")[0]/5)
    _l_(640128)
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
    _l_(640129)

    round_constants = _c_(640137, _a_(640131, _n_(640130, "np", lambda: np), "array"), [_c_(640135, _a_(640133, _n_(640132, "np", lambda: np), "uint64"), _n_(640134, "x", lambda: x)) for x in _n_(640136, "RC", lambda: RC)])
    _l_(640138)
    round_constants_gpu = _c_(640148, _a_(640140, _n_(640139, "cl", lambda: cl), "Buffer"), _n_(640141, "context", lambda: context), _a_(640144, _a_(640143, _n_(640142, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(640147, _n_(640145, "len", lambda: len), _n_(640146, "round_constants", lambda: round_constants)))   #Why * 8???
    _l_(640149)   #Why * 8???
    _c_(640155, _a_(640151, _n_(640150, "cl", lambda: cl), "enqueue_copy"), _n_(640152, "queue", lambda: queue), _n_(640153, "round_constants_gpu", lambda: round_constants_gpu), _n_(640154, "round_constants", lambda: round_constants), is_blocking=False)
    _l_(640156)

    #Set up rotation offsets
    rotation_offsets = _c_(640159, _a_(640158, _n_(640157, "np", lambda: np), "array"), [0, 36, 3, 41, 18, \
                                1 ,44 ,10 ,45 ,2,   \
                                62, 6 ,43 ,15 ,61,  \
                                28, 55, 25, 21, 56, \
                                27, 20, 39, 8 ,14])
    _l_(640160)

    rotation_offsets = _c_(640168, _a_(640162, _n_(640161, "np", lambda: np), "array"), [_c_(640166, _a_(640164, _n_(640163, "np", lambda: np), "uint64"), _n_(640165, "x", lambda: x)) for x in _n_(640167, "rotation_offsets", lambda: rotation_offsets)])
    _l_(640169)
    rotation_gpu_buffer = _c_(640179, _a_(640171, _n_(640170, "cl", lambda: cl), "Buffer"), _n_(640172, "context", lambda: context), _a_(640175, _a_(640174, _n_(640173, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8 * _c_(640178, _n_(640176, "len", lambda: len), _n_(640177, "rotation_offsets", lambda: rotation_offsets)))
    _l_(640180)
    _c_(640186, _a_(640182, _n_(640181, "cl", lambda: cl), "enqueue_copy"), _n_(640183, "queue", lambda: queue), _n_(640184, "rotation_gpu_buffer", lambda: rotation_gpu_buffer), _n_(640185, "rotation_offsets", lambda: rotation_offsets), is_blocking=False)
    _l_(640187)




    stuff_to_hash = _c_(640196, _a_(640189, _n_(640188, "cl", lambda: cl), "Buffer"), _n_(640190, "context", lambda: context), _a_(640193, _a_(640192, _n_(640191, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _a_(640195, _n_(640194, "to_hash", lambda: to_hash), "size") * 8)
    _l_(640197)
    _c_(640203, _a_(640199, _n_(640198, "cl", lambda: cl), "enqueue_copy"), _n_(640200, "queue", lambda: queue), _n_(640201, "stuff_to_hash", lambda: stuff_to_hash), _n_(640202, "to_hash", lambda: to_hash), is_blocking=False)#is_block=True means wait for completion
    _l_(640204)#is_block=True means wait for completion

    #Buffer for GPU to write final hash
    gpu_final_hash = _c_(640213, _a_(640206, _n_(640205, "cl", lambda: cl), "Buffer"), _n_(640207, "context", lambda: context), _a_(640210, _a_(640209, _n_(640208, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), _a_(640212, _n_(640211, "to_hash", lambda: to_hash), "size") * 8)
    _l_(640214)
    
    #control the number of iterations of each hash in Keccak
    gpu_iterations = _c_(640224, _a_(640216, _n_(640215, "cl", lambda: cl), "Buffer"), _n_(640217, "context", lambda: context), _a_(640220, _a_(640219, _n_(640218, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), _c_(640223, _n_(640221, "len", lambda: len), _n_(640222, "iterations", lambda: iterations))*8)
    _l_(640225)
    _c_(640234, _a_(640227, _n_(640226, "cl", lambda: cl), "enqueue_copy"), _n_(640228, "queue", lambda: queue), _n_(640229, "gpu_iterations", lambda: gpu_iterations), _c_(640233, _a_(640231, _n_(640230, "np", lambda: np), "array"), _n_(640232, "iterations", lambda: iterations)), is_blocking=False)#is_block=True means wait for completion
    _l_(640235)#is_block=True means wait for completion

    gpu_curr_iter = _c_(640242, _a_(640237, _n_(640236, "cl", lambda: cl), "Buffer"), _n_(640238, "context", lambda: context), _a_(640241, _a_(640240, _n_(640239, "cl", lambda: cl), "mem_flags"), "READ_ONLY"), 8)
    _l_(640243)
    _c_(640252, _a_(640245, _n_(640244, "cl", lambda: cl), "enqueue_copy"), _n_(640246, "queue", lambda: queue), _n_(640247, "gpu_curr_iter", lambda: gpu_curr_iter), _c_(640251, _a_(640249, _n_(640248, "np", lambda: np), "array"), _n_(640250, "curr_iter", lambda: curr_iter)), is_blocking=False)#is_block=True means wait for completion
    _l_(640253)#is_block=True means wait for completion


    #Create 5x5 workgroup, local buffer
    local_size, global_size = (5, 5) , (5,5*_n_(640254, "inputnum", lambda: inputnum))
    _l_(640255)
    local_buf_w,local_buf_h = _c_(640258, _a_(640257, _n_(640256, "np", lambda: np), "uint64"), 5),_c_(640261, _a_(640260, _n_(640259, "np", lambda: np), "uint64"), 5)
    _l_(640262)
    A = _c_(640265, _a_(640264, _n_(640263, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(640266)
    B = _c_(640269, _a_(640268, _n_(640267, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(640270)
    C = _c_(640273, _a_(640272, _n_(640271, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(640274)
    D = _c_(640277, _a_(640276, _n_(640275, "cl", lambda: cl), "LocalMemory"), 8*25)
    _l_(640278)

    #Hash input
    final_hash = _c_(640282, _a_(640280, _n_(640279, "np", lambda: np), "zeros"), (5*_n_(640281, "inputnum", lambda: inputnum),5))
    _l_(640283)
    final_hash = _c_(640291, _a_(640285, _n_(640284, "np", lambda: np), "array"), [_c_(640289, _a_(640287, _n_(640286, "np", lambda: np), "uint64"), _n_(640288, "x", lambda: x)) for x in _n_(640290, "final_hash", lambda: final_hash)])    
    _l_(640292)    
    hash_event = _c_(640310, _a_(640294, _n_(640293, "program", lambda: program), "sha_3_hash"), _n_(640295, "queue", lambda: queue), _n_(640296, "global_size", lambda: global_size), _n_(640297, "local_size", lambda: local_size),
                              _n_(640298, "stuff_to_hash", lambda: stuff_to_hash), _n_(640299, "gpu_final_hash", lambda: gpu_final_hash),_n_(640300, "rotation_gpu_buffer", lambda: rotation_gpu_buffer),_n_(640301, "round_constants_gpu", lambda: round_constants_gpu), _n_(640302, "gpu_iterations", lambda: gpu_iterations), _n_(640303, "gpu_curr_iter", lambda: gpu_curr_iter),
                              _n_(640304, "B", lambda: B),_n_(640305, "A", lambda: A), _n_(640306, "C", lambda: C), _n_(640307, "D", lambda: D), _n_(640308, "local_buf_w", lambda: local_buf_w),_n_(640309, "local_buf_h", lambda: local_buf_h))
    _l_(640311)

    
    
    _c_(640317, _a_(640313, _n_(640312, "cl", lambda: cl), "enqueue_copy"), _n_(640314, "queue", lambda: queue), _n_(640315, "final_hash", lambda: final_hash), _n_(640316, "gpu_final_hash", lambda: gpu_final_hash), is_blocking=True)
    _l_(640318)
    aux = _n_(640319, "final_hash", lambda: final_hash)
    _l_(640320)

    return aux


def Keccak(inputlist, n,r,c, program, context, queue):
    _l_(640592)




    inputnum = _c_(640324, _n_(640322, "len", lambda: len), _n_(640323, "inputlist", lambda: inputlist))
    _l_(640325)
    input_str = _n_(640326, "inputlist", lambda: inputlist)[0]
    _l_(640327)

    #P is a storage for the padded inputs
    P = []
    _l_(640328)

    #Z is a storage for the output hashes
    Z = []
    _l_(640329)

    iterations = []
    _l_(640330)

    #start = time.time()
    ### Padding Phase
    for i in _c_(640333, _n_(640331, "range", lambda: range), _n_(640332, "inputnum", lambda: inputnum)):
        _l_(640361)

        tmpstr = _c_(640342, _n_(640334, "pad10star1", lambda: pad10star1), [_c_(640338, _n_(640335, "len", lambda: len), _n_(640336, "inputlist", lambda: inputlist)[_n_(640337, "i", lambda: i)])*4, _n_(640339, "inputlist", lambda: inputlist)[_n_(640340, "i", lambda: i)]],_n_(640341, "r", lambda: r)) 
        _l_(640343) 
        _c_(640347, _a_(640345, _n_(640344, "P", lambda: P), "append"), _n_(640346, "tmpstr", lambda: tmpstr))
        _l_(640348)
        _c_(640351, _a_(640350, _n_(640349, "Z", lambda: Z), "append"), "")
        _l_(640352)
        _c_(640359, _a_(640354, _n_(640353, "iterations", lambda: iterations), "append"), (_c_(640357, _n_(640355, "len", lambda: len), _n_(640356, "tmpstr", lambda: tmpstr))*8//2)//_n_(640358, "r", lambda: r))
        _l_(640360)

    #print ("Time to run padding: " + str(time.time() - start))

    # Initialisation of state
    S = _c_(640365, _a_(640363, _n_(640362, "np", lambda: np), "zeros"), (5*_n_(640364, "inputnum", lambda: inputnum),5))
    _l_(640366)


    #Testing
    S = _c_(640374, _a_(640368, _n_(640367, "np", lambda: np), "array"), [_c_(640372, _a_(640370, _n_(640369, "np", lambda: np), "uint64"), _n_(640371, "x", lambda: x)) for x in _n_(640373, "S", lambda: S)])
    _l_(640375)

    #Initialize workgroup sizes for the gpu
    local_size, global_size = (5, 5) , (5,5*_n_(640376, "inputnum", lambda: inputnum))
    _l_(640377)

    for i in _c_(640382, _n_(640378, "range", lambda: range), _c_(640381, _n_(640379, "max", lambda: max), _n_(640380, "iterations", lambda: iterations))):
        _l_(640511)


        host_string = ""
        _l_(640383)
        Pi = _c_(640387, _a_(640385, _n_(640384, "np", lambda: np), "zeros"), (5*_n_(640386, "inputnum", lambda: inputnum),5))
        _l_(640388)
        Pi = _c_(640396, _a_(640390, _n_(640389, "np", lambda: np), "array"), [_c_(640394, _a_(640392, _n_(640391, "np", lambda: np), "uint64"), _n_(640393, "x", lambda: x)) for x in _n_(640395, "Pi", lambda: Pi)])
        _l_(640397)

        for j in _c_(640400, _n_(640398, "range", lambda: range), _n_(640399, "inputnum", lambda: inputnum)):
            _l_(640418)


            if (_n_(640401, "iterations", lambda: iterations)[_n_(640402, "j", lambda: j)] > _n_(640403, "i", lambda: i)):
                _l_(640417)

                #Absorbing Phase
                host_string = _n_(640404, "host_string", lambda: host_string) + _c_(640413, _n_(640405, "str", lambda: str), _n_(640406, "P", lambda: P)[_n_(640407, "j", lambda: j)][_n_(640408, "i", lambda: i)*(2*_n_(640409, "r", lambda: r)//8):(_n_(640410, "i", lambda: i)+1)*(2*_n_(640411, "r", lambda: r)//8)]+'00'*(_n_(640412, "c", lambda: c)//8))
                _l_(640414)
            else:
                #Dummy variables. Won't be used.
                host_string = _n_(640415, "host_string", lambda: host_string) + "0"*400
                _l_(640416)

        gpu_string = _c_(640429, _a_(640420, _n_(640419, "cl", lambda: cl), "Buffer"), _n_(640421, "context", lambda: context), _a_(640424, _a_(640423, _n_(640422, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(640427, _a_(640426, _n_(640425, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(640428, "host_string", lambda: host_string))
        _l_(640430)
        gpu_table = _c_(640438, _a_(640432, _n_(640431, "cl", lambda: cl), "Buffer"), _n_(640433, "context", lambda: context), _a_(640436, _a_(640435, _n_(640434, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 25*8 * _n_(640437, "inputnum", lambda: inputnum))
        _l_(640439)
        part_of_string = _c_(640442, _a_(640441, _n_(640440, "cl", lambda: cl), "LocalMemory"), 1*16)
        _l_(640443)
        _c_(640461, _a_(640445, _n_(640444, "program", lambda: program), "convert_str_to_table"), _n_(640446, "queue", lambda: queue),_n_(640447, "global_size", lambda: global_size),_n_(640448, "local_size", lambda: local_size), _n_(640449, "gpu_string", lambda: gpu_string), _n_(640450, "gpu_table", lambda: gpu_table), _n_(640451, "part_of_string", lambda: part_of_string), _c_(640454, _a_(640453, _n_(640452, "np", lambda: np), "uint64"), 5),_c_(640457, _a_(640456, _n_(640455, "np", lambda: np), "uint64"), 5),_c_(640460, _a_(640459, _n_(640458, "np", lambda: np), "uint64"), 64))
        _l_(640462)
        _c_(640468, _a_(640464, _n_(640463, "cl", lambda: cl), "enqueue_copy"), _n_(640465, "queue", lambda: queue), _n_(640466, "Pi", lambda: Pi), _n_(640467, "gpu_table", lambda: gpu_table), is_blocking=True)
        _l_(640469)




        for x in _c_(640472, _n_(640470, "range", lambda: range), 5*_n_(640471, "inputnum", lambda: inputnum)):
            _l_(640492)

            for y in _c_(640474, _n_(640473, "range", lambda: range), 5):
                _l_(640491)

                #print 'type S:',type(S[x][y]),'type P:',type(Pi[x][y])

                if (_n_(640475, "iterations", lambda: iterations)[_c_(640478, _n_(640476, "int", lambda: int), _n_(640477, "x", lambda: x)/5)] > _n_(640479, "i", lambda: i)):
                    _l_(640490)

                    _n_(640480, "S", lambda: S)[_n_(640481, "x", lambda: x)][_n_(640482, "y", lambda: y)] = _n_(640483, "S", lambda: S)[_n_(640484, "x", lambda: x)][_n_(640485, "y", lambda: y)]^_n_(640486, "Pi", lambda: Pi)[_n_(640487, "x", lambda: x)][_n_(640488, "y", lambda: y)]
                    _l_(640489)



        S = _c_(640500, _a_(640494, _n_(640493, "np", lambda: np), "array"), [_c_(640498, _a_(640496, _n_(640495, "np", lambda: np), "uint64"), _n_(640497, "x", lambda: x)) for x in _n_(640499, "S", lambda: S)])
        _l_(640501)
        #start = time.time()
        S = _c_(640509, _n_(640502, "KeccakF", lambda: KeccakF), _n_(640503, "S", lambda: S), _n_(640504, "iterations", lambda: iterations), _n_(640505, "i", lambda: i),  _n_(640506, "program", lambda: program), _n_(640507, "context", lambda: context), _n_(640508, "queue", lambda: queue))
        _l_(640510)

    #Squeezing phase

    outputstring = _c_(640515, _a_(640513, _n_(640512, "np", lambda: np), "chararray"), 400 * _n_(640514, "inputnum", lambda: inputnum))
    _l_(640516)
    gpu_table = _c_(640527, _a_(640518, _n_(640517, "cl", lambda: cl), "Buffer"), _n_(640519, "context", lambda: context), _a_(640522, _a_(640521, _n_(640520, "cl", lambda: cl), "mem_flags"), "READ_ONLY") | _a_(640525, _a_(640524, _n_(640523, "cl", lambda: cl), "mem_flags"), "COPY_HOST_PTR"), hostbuf=_n_(640526, "S", lambda: S))
    _l_(640528)
    gpu_string = _c_(640536, _a_(640530, _n_(640529, "cl", lambda: cl), "Buffer"), _n_(640531, "context", lambda: context), _a_(640534, _a_(640533, _n_(640532, "cl", lambda: cl), "mem_flags"), "READ_WRITE"), 144*8 * _n_(640535, "inputnum", lambda: inputnum))
    _l_(640537)
    _c_(640554, _a_(640539, _n_(640538, "program", lambda: program), "convert_table_to_str"), _n_(640540, "queue", lambda: queue),_n_(640541, "global_size", lambda: global_size),_n_(640542, "local_size", lambda: local_size),_n_(640543, "gpu_table", lambda: gpu_table), _n_(640544, "gpu_string", lambda: gpu_string),_c_(640547, _a_(640546, _n_(640545, "np", lambda: np), "uint64"), 5),_c_(640550, _a_(640549, _n_(640548, "np", lambda: np), "uint64"), 5),_c_(640553, _a_(640552, _n_(640551, "np", lambda: np), "uint64"), 64))
    _l_(640555)
    _c_(640561, _a_(640557, _n_(640556, "cl", lambda: cl), "enqueue_copy"), _n_(640558, "queue", lambda: queue), _n_(640559, "outputstring", lambda: outputstring), _n_(640560, "gpu_string", lambda: gpu_string), is_blocking=True)
    _l_(640562)

    string = _c_(640565, _a_(640563, '', "join"), _n_(640564, "outputstring", lambda: outputstring))
    _l_(640566)

    for x in _c_(640569, _n_(640567, "range", lambda: range), _n_(640568, "inputnum", lambda: inputnum)):
        _l_(640579)

        _n_(640570, "Z", lambda: Z)[_n_(640571, "x", lambda: x)] = _n_(640572, "Z", lambda: Z)[_n_(640573, "x", lambda: x)] + _n_(640574, "string", lambda: string)[400 * _n_(640575, "x", lambda: x): 400 * _n_(640576, "x", lambda: x) + _n_(640577, "r", lambda: r)*2//8]
        _l_(640578)


    for x in _c_(640582, _n_(640580, "range", lambda: range), _n_(640581, "inputnum", lambda: inputnum)):
        _l_(640589)

        _n_(640583, "Z", lambda: Z)[_n_(640584, "x", lambda: x)] = _n_(640585, "Z", lambda: Z)[_n_(640586, "x", lambda: x)][0:2*_n_(640587, "n", lambda: n)//8]
        _l_(640588)
    aux = _n_(640590, "Z", lambda: Z)
    _l_(640591)

    #output the pre-set number of bits
    return aux

if _n_(640593, "__name__", lambda: __name__) == '__main__':
    _l_(640682)



    # List our platforms
    platforms = _c_(640596, _a_(640595, _n_(640594, "cl", lambda: cl), "get_platforms"))
    _l_(640597)

    # Create a context with all the devices
    devices = _c_(640600, _a_(640599, _n_(640598, "platforms", lambda: platforms)[0], "get_devices"))
    _l_(640601)
    context = _c_(640605, _a_(640603, _n_(640602, "cl", lambda: cl), "Context"), _n_(640604, "devices", lambda: devices)[:2])
    _l_(640606)
    #print ('This context is associated with ', len(context.devices), 'devices')

    # Create a queue for transferring data and launching computations.
    # Turn on profiling to allow us to check event times.
    queue = _c_(640615, _a_(640608, _n_(640607, "cl", lambda: cl), "CommandQueue"), _n_(640609, "context", lambda: context), _a_(640611, _n_(640610, "context", lambda: context), "devices")[0],
                            properties=_a_(640614, _a_(640613, _n_(640612, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
    _l_(640616)
    #print ('The queue is using the device:', queue.device.name)

    
    program = _c_(640626, _a_(640625, _c_(640624, _a_(640618, _n_(640617, "cl", lambda: cl), "Program"), _n_(640619, "context", lambda: context), _c_(640623, _a_(640622, _c_(640621, _n_(640620, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
    _l_(640627)


    #PARAMETERS for SHA 512
    r = 576
    _l_(640628)
    c = 1024
    _l_(640629)
    n = 512
    _l_(640630)

    inputlist = []
    _l_(640631)
    _c_(640634, _a_(640633, _n_(640632, "inputlist", lambda: inputlist), "append"), "")
    _l_(640635)
    _c_(640638, _a_(640637, _n_(640636, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(640639)
    _c_(640642, _a_(640641, _n_(640640, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(640643)
    _c_(640646, _a_(640645, _n_(640644, "inputlist", lambda: inputlist), "append"), "abcd")
    _l_(640647)
    _c_(640650, _a_(640649, _n_(640648, "inputlist", lambda: inputlist), "append"), "a" * 1000)
    _l_(640651)

    start = _c_(640654, _a_(640653, _n_(640652, "time", lambda: time), "time"))
    _l_(640655)
    result = _c_(640664, _n_(640656, "Keccak", lambda: Keccak), _n_(640657, "inputlist", lambda: inputlist), _n_(640658, "n", lambda: n), _n_(640659, "r", lambda: r),_n_(640660, "c", lambda: c), _n_(640661, "program", lambda: program), _n_(640662, "context", lambda: context), _n_(640663, "queue", lambda: queue))
    _l_(640665)
    _c_(640667, _n_(640666, "print", lambda: print), "Hashing Result is")
    _l_(640668)
    _c_(640671, _n_(640669, "print", lambda: print), _n_(640670, "result", lambda: result))
    _l_(640672)
    _c_(640680, _n_(640673, "print", lambda: print), "Time taken is: " + _c_(640679, _n_(640674, "str", lambda: str), _c_(640677, _a_(640676, _n_(640675, "time", lambda: time), "time")) - _n_(640678, "start", lambda: start)))
    _l_(640681)
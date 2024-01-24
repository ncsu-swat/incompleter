# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64477938/typeerror-while-creating-custom-layer-with-tensorflow-map-fn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(629712)

except ImportError:
    pass
_c_(629716, _n_(629713, "print", lambda: print), _a_(629715, _n_(629714, "tf", lambda: tf), "__version__"))
_l_(629717)
try:
    from tensorflow import math as m
    _l_(629719)

except ImportError:
    pass
try:
    from tensorflow.keras import layers
    _l_(629721)

except ImportError:
    pass

class Kinematics_Physics(_a_(629723, _n_(629722, "layers", lambda: layers), "Layer")):
    _l_(630222)


    def __init__(self,):
        _l_(629844)

        _c_(629728, _a_(629727, _n_(629724, "super", lambda: super)(_n_(629725, "Kinematics_Physics", lambda: Kinematics_Physics), _n_(629726, "self", lambda: self)), "__init__"))
        _l_(629729)
        # define initial variables
        _n_(629730, "self", lambda: self).TF_PI = _c_(629735, _a_(629732, _n_(629731, "tf", lambda: tf), "constant"), 3.1415926535897932, dtype =_a_(629734, _n_(629733, "tf", lambda: tf), "float32"))
        _l_(629736)
        _n_(629737, "self", lambda: self).TF_180 = _c_(629742, _a_(629739, _n_(629738, "tf", lambda: tf), "constant"), 180.0, dtype =_a_(629741, _n_(629740, "tf", lambda: tf), "float32"))
        _l_(629743)
        _n_(629744, "self", lambda: self).TINY_VALUE = _c_(629749, _a_(629746, _n_(629745, "tf", lambda: tf), "constant"), 1e-6, dtype =_a_(629748, _n_(629747, "tf", lambda: tf), "float32"))
        _l_(629750)
        _n_(629751, "self", lambda: self).out_Pose=_c_(629756, _a_(629753, _n_(629752, "tf", lambda: tf), "Variable"), [0,0,0,0,0,0],  dtype =_a_(629755, _n_(629754, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629757)
        _n_(629758, "self", lambda: self).A_Deg = _c_(629763, _a_(629760, _n_(629759, "tf", lambda: tf), "Variable"), 0,dtype = _a_(629762, _n_(629761, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629764)
        _n_(629765, "self", lambda: self).B_Deg = _c_(629770, _a_(629767, _n_(629766, "tf", lambda: tf), "Variable"), 0,dtype = _a_(629769, _n_(629768, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629771)
        _n_(629772, "self", lambda: self).C_Deg = _c_(629777, _a_(629774, _n_(629773, "tf", lambda: tf), "Variable"), 0,dtype = _a_(629776, _n_(629775, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629778)
        _n_(629779, "self", lambda: self).sA = _c_(629784, _a_(629781, _n_(629780, "tf", lambda: tf), "Variable"), 0,dtype = _a_(629783, _n_(629782, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629785)
        _n_(629786, "self", lambda: self).cA = _c_(629791, _a_(629788, _n_(629787, "tf", lambda: tf), "Variable"), 0,dtype = _a_(629790, _n_(629789, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629792)
        _n_(629793, "self", lambda: self).b = _c_(629803, _a_(629795, _n_(629794, "tf", lambda: tf), "Variable"), _c_(629800, _a_(629797, _n_(629796, "tf", lambda: tf), "zeros"), (4,4),dtype = _a_(629799, _n_(629798, "tf", lambda: tf), "float32")),dtype = _a_(629802, _n_(629801, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629804)
        
        # initial dh parameters: 6 x 4 parameters for a robotic arm with 6 joints.
        dh = _c_(629809, _a_(629806, _n_(629805, "tf", lambda: tf), "constant"), [  [0 ,    180.,   -650.,  0.],
                            [270.,   90.,      0.,  0.],
                            [800.,    0.,      0.,  0.],
                            [140.,   90.,   -908.,  0.],
                            [0.,    -96.,      0.,  0.],
                            [0.,    -65.,   260.,   0.]] ,dtype = _a_(629808, _n_(629807, "tf", lambda: tf), "float32"))
        _l_(629810)
        
        # convert to trainable weights?? for further optimization 
        _n_(629811, "self", lambda: self).dh = _c_(629815, _a_(629813, _n_(629812, "tf", lambda: tf), "Variable"), initial_value=_n_(629814, "dh", lambda: dh), trainable=True)
        _l_(629816)

        # initialize a buffer to calculate the the modified angles
        _n_(629817, "self", lambda: self).dh_processed = _c_(629830, _a_(629819, _n_(629818, "tf", lambda: tf), "Variable"), _c_(629827, _a_(629821, _n_(629820, "tf", lambda: tf), "zeros"), _a_(629824, _a_(629823, _n_(629822, "self", lambda: self), "dh"), "shape"),dtype = _a_(629826, _n_(629825, "tf", lambda: tf), "float32")),dtype = _a_(629829, _n_(629828, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629831)
        # buffer for transformation matrix
        _n_(629832, "self", lambda: self).trans_matrix = _c_(629842, _a_(629834, _n_(629833, "tf", lambda: tf), "Variable"), _c_(629839, _a_(629836, _n_(629835, "tf", lambda: tf), "zeros"), (4,4),dtype = _a_(629838, _n_(629837, "tf", lambda: tf), "float32")),  dtype =_a_(629841, _n_(629840, "tf", lambda: tf), "float32"), trainable = False)
        _l_(629843)


    @_a_(629846, _n_(629845, "tf", lambda: tf), "function")
    def radians(self,a):
        _l_(629859)

        aux = _c_(629857, _a_(629848, _n_(629847, "m", lambda: m), "multiply"), _n_(629849, "a", lambda: a),_c_(629856, _a_(629851, _n_(629850, "tf", lambda: tf), "divide"), _a_(629853, _n_(629852, "self", lambda: self), "TF_PI"), _a_(629855, _n_(629854, "self", lambda: self), "TF_180") ))
        _l_(629858)
        return aux
    
    @_a_(629861, _n_(629860, "tf", lambda: tf), "function")
    def degrees(self,a):
        _l_(629874)

        aux = _c_(629872, _a_(629863, _n_(629862, "m", lambda: m), "multiply"), _n_(629864, "a", lambda: a),_c_(629871, _a_(629866, _n_(629865, "tf", lambda: tf), "divide"), _a_(629868, _n_(629867, "self", lambda: self), "TF_180") , _a_(629870, _n_(629869, "self", lambda: self), "TF_PI")))
        _l_(629873)
        return aux
    
    @_a_(629876, _n_(629875, "tf", lambda: tf), "function")
    def joint_transform(self,input_values):
        _l_(629977)

        '''input: format --> 1D array = [a, α, d, θ]'''
        _l_(629877)
    
        a = _n_(629878, "input_values", lambda: input_values)[0] # a
        _l_(629879) # a
        alpha = _c_(629883, _a_(629881, _n_(629880, "self", lambda: self), "radians"), _n_(629882, "input_values", lambda: input_values)[1]) #convert degrees to radians
        _l_(629884) #convert degrees to radians
        d = _n_(629885, "input_values", lambda: input_values)[2] # d
        _l_(629886) # d
        theta = _c_(629890, _a_(629888, _n_(629887, "self", lambda: self), "radians"), _n_(629889, "input_values", lambda: input_values)[3]) #convert degrees to radians θ
        _l_(629891) #convert degrees to radians θ
        
        _c_(629972, _a_(629894, _a_(629893, _n_(629892, "self", lambda: self), "trans_matrix"), "assign"), [[      _c_(629898, _a_(629896, _n_(629895, "m", lambda: m), "cos"), _n_(629897, "theta", lambda: theta)),             -_c_(629902, _a_(629900, _n_(629899, "m", lambda: m), "sin"), _n_(629901, "theta", lambda: theta)),              0,                _n_(629903, "a", lambda: a)],
                                [_c_(629914, _a_(629905, _n_(629904, "m", lambda: m), "multiply"), _c_(629909, _a_(629907, _n_(629906, "m", lambda: m), "sin"), _n_(629908, "theta", lambda: theta)),_c_(629913, _a_(629911, _n_(629910, "m", lambda: m), "cos"), _n_(629912, "alpha", lambda: alpha))),  _c_(629925, _a_(629916, _n_(629915, "m", lambda: m), "multiply"), _c_(629920, _a_(629918, _n_(629917, "m", lambda: m), "cos"), _n_(629919, "theta", lambda: theta)),_c_(629924, _a_(629922, _n_(629921, "m", lambda: m), "cos"), _n_(629923, "alpha", lambda: alpha))), -_c_(629929, _a_(629927, _n_(629926, "m", lambda: m), "sin"), _n_(629928, "alpha", lambda: alpha)), _c_(629937, _a_(629931, _n_(629930, "m", lambda: m), "multiply"), -_c_(629935, _a_(629933, _n_(629932, "m", lambda: m), "sin"), _n_(629934, "alpha", lambda: alpha)),_n_(629936, "d", lambda: d))],
                                [_c_(629948, _a_(629939, _n_(629938, "m", lambda: m), "multiply"), _c_(629943, _a_(629941, _n_(629940, "m", lambda: m), "sin"), _n_(629942, "theta", lambda: theta)),_c_(629947, _a_(629945, _n_(629944, "m", lambda: m), "sin"), _n_(629946, "alpha", lambda: alpha))),  _c_(629959, _a_(629950, _n_(629949, "m", lambda: m), "multiply"), _c_(629954, _a_(629952, _n_(629951, "m", lambda: m), "cos"), _n_(629953, "theta", lambda: theta)),_c_(629958, _a_(629956, _n_(629955, "m", lambda: m), "sin"), _n_(629957, "alpha", lambda: alpha))),  _c_(629963, _a_(629961, _n_(629960, "m", lambda: m), "cos"), _n_(629962, "alpha", lambda: alpha)),  _c_(629971, _a_(629965, _n_(629964, "m", lambda: m), "multiply"), _c_(629969, _a_(629967, _n_(629966, "m", lambda: m), "cos"), _n_(629968, "alpha", lambda: alpha)),_n_(629970, "d", lambda: d))],
                                [        0,                             0,                     0,            1        ]])
        _l_(629973)
        aux = _a_(629975, _n_(629974, "self", lambda: self), "trans_matrix")
        _l_(629976)
        return aux
    
    @_a_(629979, _n_(629978, "tf", lambda: tf), "function")
    def to_pose(self,T):
        _l_(630138)

        # converts the transformation matrix to pose [x, y, z, alpha ]
        if(_c_(629983, _a_(629981, _n_(629980, "m", lambda: m), "abs"), _n_(629982, "T", lambda: T)[1,2]) <= _a_(629985, _n_(629984, "self", lambda: self), "TINY_VALUE") and _c_(629989, _a_(629987, _n_(629986, "m", lambda: m), "abs"), _n_(629988, "T", lambda: T)[2,2]) <= _a_(629991, _n_(629990, "self", lambda: self), "TINY_VALUE")):
            _l_(630120)

            _c_(630000, _a_(629994, _a_(629993, _n_(629992, "self", lambda: self), "C_Deg"), "assign"), _c_(629999, _a_(629996, _n_(629995, "tf", lambda: tf), "constant"), 0, dtype =_a_(629998, _n_(629997, "tf", lambda: tf), "float32")))
            _l_(630001)
            _c_(630021, _a_(630004, _a_(630003, _n_(630002, "self", lambda: self), "B_Deg"), "assign"), _c_(630020, _a_(630006, _n_(630005, "self", lambda: self), "degrees"), _c_(630019, _a_(630008, _n_(630007, "m", lambda: m), "atan2"), _n_(630009, "T", lambda: T)[0,2] , _c_(630018, _a_(630011, _n_(630010, "m", lambda: m), "divide_no_nan"), _n_(630012, "T", lambda: T)[2,2], _c_(630017, _a_(630014, _n_(630013, "m", lambda: m), "cos"), _a_(630016, _n_(630015, "self", lambda: self), "C_Deg"))) ))) #convert radians to degree
            _l_(630022) #convert radians to degree
            _c_(630042, _a_(630025, _a_(630024, _n_(630023, "self", lambda: self), "A_Deg"), "assign"), _c_(630041, _a_(630027, _n_(630026, "self", lambda: self), "degrees"), _c_(630040, _a_(630029, _n_(630028, "m", lambda: m), "atan2"), _n_(630030, "T", lambda: T)[1,0] ,  _c_(630039, _a_(630032, _n_(630031, "m", lambda: m), "divide_no_nan"), _n_(630033, "T", lambda: T)[1,1], _c_(630038, _a_(630035, _n_(630034, "m", lambda: m), "cos"), _a_(630037, _n_(630036, "self", lambda: self), "C_Deg"))) ))) #convert radians to degree
            _l_(630043) #convert radians to degree
        
        else:
            _c_(630055, _a_(630046, _a_(630045, _n_(630044, "self", lambda: self), "A_Deg"), "assign"), _c_(630054, _a_(630048, _n_(630047, "self", lambda: self), "degrees"), _c_(630053, _a_(630050, _n_(630049, "m", lambda: m), "atan2"), -_n_(630051, "T", lambda: T)[0,1] , _n_(630052, "T", lambda: T)[0,0]))) #convert radians to degree
            _l_(630056) #convert radians to degree
            _c_(630068, _a_(630059, _a_(630058, _n_(630057, "self", lambda: self), "sA"), "assign"), _c_(630067, _a_(630061, _n_(630060, "m", lambda: m), "sin"), _c_(630066, _a_(630063, _n_(630062, "self", lambda: self), "radians"), _a_(630065, _n_(630064, "self", lambda: self), "A_Deg"))))
            _l_(630069)
            _c_(630081, _a_(630072, _a_(630071, _n_(630070, "self", lambda: self), "cA"), "assign"), _c_(630080, _a_(630074, _n_(630073, "m", lambda: m), "cos"), _c_(630079, _a_(630076, _n_(630075, "self", lambda: self), "radians"), _a_(630078, _n_(630077, "self", lambda: self), "A_Deg"))))
            _l_(630082)
            _c_(630105, _a_(630085, _a_(630084, _n_(630083, "self", lambda: self), "B_Deg"), "assign"), _c_(630104, _a_(630087, _n_(630086, "self", lambda: self), "degrees"), _c_(630103, _a_(630089, _n_(630088, "m", lambda: m), "atan2"), _n_(630090, "T", lambda: T)[0,2] , _c_(630096, _a_(630092, _n_(630091, "m", lambda: m), "multiply"), _a_(630094, _n_(630093, "self", lambda: self), "cA"),_n_(630095, "T", lambda: T)[0,0]) - _c_(630102, _a_(630098, _n_(630097, "m", lambda: m), "multiply"), _a_(630100, _n_(630099, "self", lambda: self), "sA"),_n_(630101, "T", lambda: T)[0,1]))))#convert radians to degree
            _l_(630106)#convert radians to degree
            _c_(630118, _a_(630109, _a_(630108, _n_(630107, "self", lambda: self), "C_Deg"), "assign"), _c_(630117, _a_(630111, _n_(630110, "self", lambda: self), "degrees"), _c_(630116, _a_(630113, _n_(630112, "m", lambda: m), "atan2"), -_n_(630114, "T", lambda: T)[1,2] , _n_(630115, "T", lambda: T)[2,2]))) #convert radians to degree
            _l_(630119) #convert radians to degree
        
        _c_(630133, _a_(630123, _a_(630122, _n_(630121, "self", lambda: self), "out_Pose"), "assign"), [ _n_(630124, "T", lambda: T)[0,3], _n_(630125, "T", lambda: T)[1,3], _n_(630126, "T", lambda: T)[2,3],_a_(630128, _n_(630127, "self", lambda: self), "A_Deg"), _a_(630130, _n_(630129, "self", lambda: self), "B_Deg") , _a_(630132, _n_(630131, "self", lambda: self), "C_Deg")])
        _l_(630134)
        aux = _a_(630136, _n_(630135, "self", lambda: self), "out_Pose")
        _l_(630137)
        return aux
    
    
    @_a_(630140, _n_(630139, "tf", lambda: tf), "function")
    def forward_kinematics(self, theta):
        _l_(630202)

        
        # add the dh_theta to measured theta to get the final theta
        actual_theta = _c_(630146, _a_(630142, _n_(630141, "m", lambda: m), "add"), _a_(630144, _n_(630143, "self", lambda: self), "dh")[:,3] ,_n_(630145, "theta", lambda: theta))
        _l_(630147)
        
        # create new dh_table with modified theta for forward kinematics calculation
        _c_(630153, _a_(630150, _a_(630149, _n_(630148, "self", lambda: self), "dh_processed")[:,0], "assign"), _a_(630152, _n_(630151, "self", lambda: self), "dh")[:,0])
        _l_(630154)
        _c_(630160, _a_(630157, _a_(630156, _n_(630155, "self", lambda: self), "dh_processed")[:,1], "assign"), _a_(630159, _n_(630158, "self", lambda: self), "dh")[:,1])
        _l_(630161)
        _c_(630167, _a_(630164, _a_(630163, _n_(630162, "self", lambda: self), "dh_processed")[:,2], "assign"), _a_(630166, _n_(630165, "self", lambda: self), "dh")[:,2])
        _l_(630168)
        _c_(630173, _a_(630171, _a_(630170, _n_(630169, "self", lambda: self), "dh_processed")[:,3], "assign"), _n_(630172, "actual_theta", lambda: actual_theta))
        _l_(630174)
        b = _c_(630179, _a_(630176, _n_(630175, "tf", lambda: tf), "eye"), 4, dtype = _a_(630178, _n_(630177, "tf", lambda: tf), "float32"))
        _l_(630180)
        for i in _c_(630183, _a_(630182, _n_(630181, "tf", lambda: tf), "range"), 6):
            _l_(630196)

            b = _c_(630194, _a_(630186, _a_(630185, _n_(630184, "tf", lambda: tf), "linalg"), "matmul"), _n_(630187, "b", lambda: b),_c_(630193, _a_(630189, _n_(630188, "self", lambda: self), "joint_transform"), _a_(630191, _n_(630190, "self", lambda: self), "dh_processed")[_n_(630192, "i", lambda: i)]))
            _l_(630195)
        aux = _c_(630200, _a_(630198, _n_(630197, "self", lambda: self), "to_pose"), _n_(630199, "b", lambda: b))
        _l_(630201)
        return aux
      
    def __call__(self, inputs):
        _l_(630212)

        aux = _c_(630210, _a_(630204, _n_(630203, "tf", lambda: tf), "map_fn"), _a_(630206, _n_(630205, "self", lambda: self), "forward_kinematics"), _n_(630207, "inputs", lambda: inputs), parallel_iterations=True, dtype=_a_(630209, _n_(630208, "tf", lambda: tf), "float32"))
        _l_(630211)
        return aux
    
    def get_config(self):
        _l_(630221)

        config = _c_(630217, _a_(630216, _n_(630213, "super", lambda: super)(_n_(630214, "Kinematics_Physics", lambda: Kinematics_Physics), _n_(630215, "self", lambda: self)), "get_config"))
        _l_(630218)
        aux = _n_(630219, "config", lambda: config)
        _l_(630220)
        return aux
# Loss function
def Euclidean_distance(y,y_hat):
    _l_(630242)

    aux = _c_(630240, _a_(630224, _n_(630223, "tf", lambda: tf), "sqrt"), _c_(630229, _a_(630226, _n_(630225, "tf", lambda: tf), "square"), _n_(630227, "y", lambda: y)[:,0]-_n_(630228, "y_hat", lambda: y_hat)[:,0])+_c_(630234, _a_(630231, _n_(630230, "tf", lambda: tf), "square"), _n_(630232, "y", lambda: y)[:,1]-_n_(630233, "y_hat", lambda: y_hat)[:,1])+_c_(630239, _a_(630236, _n_(630235, "tf", lambda: tf), "square"), _n_(630237, "y", lambda: y)[:,2]-_n_(630238, "y_hat", lambda: y_hat)[:,2]))
    _l_(630241)
    #Euclidean distance between true and predicted values 
    # ony calculates errors for the distance between two points and ignores the orientation error.
    return aux

if _n_(630243, "__name__", lambda: __name__) == "__main__":
    _l_(630313)

    # create a list of six joint angles
    ang = _c_(630248, _a_(630245, _n_(630244, "tf", lambda: tf), "Variable"), [[20,10,20,10,10,20],[15,10,20,22,20,32]], dtype = _a_(630247, _n_(630246, "tf", lambda: tf), "float32"), trainable=False)
    _l_(630249)
    # Call the Kinematics_physics layer
    fk = _c_(630251, _n_(630250, "Kinematics_Physics", lambda: Kinematics_Physics))
    _l_(630252)
    _c_(630258, _n_(630253, "print", lambda: print), "trainable weights: ", _c_(630257, _n_(630254, "len", lambda: len), _a_(630256, _n_(630255, "fk", lambda: fk), "trainable_weights")))
    _l_(630259)
    _c_(630265, _n_(630260, "print", lambda: print), "non-trainable weights: ", _c_(630264, _n_(630261, "len", lambda: len), _a_(630263, _n_(630262, "fk", lambda: fk), "non_trainable_weights")))
    _l_(630266)
    _c_(630270, _n_(630267, "print", lambda: print), "trainable_weights: ", _a_(630269, _n_(630268, "fk", lambda: fk), "trainable_weights"))
    _l_(630271)
    _c_(630276, _n_(630272, "print", lambda: print), "forward kinematic transform: ", _c_(630275, _n_(630273, "fk", lambda: fk), _n_(630274, "ang", lambda: ang)[:10]))
    _l_(630277)
    # Everything works up to this.

    # create a model using functional API
    in_= _c_(630282, _a_(630281, _a_(630280, _a_(630279, _n_(630278, "tf", lambda: tf), "keras"), "layers"), "Input"), shape=(6,))
    _l_(630283)
    for_kin = _c_(630287, _c_(630285, _n_(630284, "Kinematics_Physics", lambda: Kinematics_Physics)), _n_(630286, "in_", lambda: in_))
    _l_(630288)
    model = _c_(630295, _a_(630292, _a_(630291, _a_(630290, _n_(630289, "tf", lambda: tf), "keras"), "models"), "Model"), inputs=_n_(630293, "in_", lambda: in_), outputs=_n_(630294, "for_kin", lambda: for_kin)) 
    _l_(630296) 
    _c_(630299, _a_(630298, _n_(630297, "model", lambda: model), "summary")) 
    _l_(630300) 
    # Error: expected behavior => should create a model with 24 trainable parameters
    #        but the error happens in tf.map_fn of Kinematics_Physics().__call__ function
    
    opt = _c_(630305, _a_(630304, _a_(630303, _a_(630302, _n_(630301, "tf", lambda: tf), "keras"), "optimizers"), "Adam"), lr=1e-3)
    _l_(630306)
    _c_(630311, _a_(630308, _n_(630307, "model", lambda: model), "compile"), optimizer=_n_(630309, "opt", lambda: opt), loss=_n_(630310, "Euclidean_distance", lambda: Euclidean_distance))
    _l_(630312)
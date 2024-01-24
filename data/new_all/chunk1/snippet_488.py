# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53179795/attributeerror-module-tensorflow-app-has-no-attribute-flags
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(375198)

except ImportError:
    pass
try:
    from models.nets import cpm_hand_slim
    _l_(375200)

except ImportError:
    pass
try:
    import numpy as np
    _l_(375202)

except ImportError:
    pass
try:
    from utils import cpm_utils
    _l_(375204)

except ImportError:
    pass
try:
    import cv2
    _l_(375206)

except ImportError:
    pass
try:
    import time
    _l_(375208)

except ImportError:
    pass
try:
    import math
    _l_(375210)

except ImportError:
    pass
try:
    import sys
    _l_(375212)

except ImportError:
    pass
def del_all_flags(FLAGS):
    _l_(375227)

    flags_dict = _c_(375215, _a_(375214, _n_(375213, "FLAGS", lambda: FLAGS), "_flags"))    
    _l_(375216)    
    keys_list = [_n_(375217, "keys", lambda: keys) for keys in _n_(375218, "flags_dict", lambda: flags_dict)]    
    _l_(375219)    
    for keys in _n_(375220, "keys_list", lambda: keys_list):
        _l_(375226)

        _c_(375224, _a_(375222, _n_(375221, "FLAGS", lambda: FLAGS), "__delattr__"), _n_(375223, "keys", lambda: keys))
        _l_(375225)

_c_(375232, _n_(375228, "del_all_flags", lambda: del_all_flags), _a_(375231, _a_(375230, _n_(375229, "tf", lambda: tf), "flags"), "FLAGS"))
_l_(375233)
FLAGS = _a_(375237, _a_(375236, _a_(375235, _n_(375234, "tf", lambda: tf), "app"), "flags"), "FLAGS")
_l_(375238)
_c_(375243, _a_(375242, _a_(375241, _a_(375240, _n_(375239, "tf", lambda: tf), "app"), "flags"), "DEFINE_string"), 'DEMO_TYPE',
                           #default_value='test_imgs/roger.png',
                           default_value='test_imgs/longhand.jpg',
                           #default_value='SINGLE',
                           docstring='MULTI: show multiple stage,'
                                    'SINGLE: only last stage,'
                                     'HM: show last stage heatmap,'
                                     'paths to .jpg or .png image')
_l_(375244)
_c_(375249, _a_(375248, _a_(375247, _a_(375246, _n_(375245, "tf", lambda: tf), "app"), "flags"), "DEFINE_string"), 'model_path',
                           default_value='models/weights/cpm_hand.pkl',
                           docstring='Your model')
_l_(375250)
_c_(375255, _a_(375254, _a_(375253, _a_(375252, _n_(375251, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'input_size',
                            default_value=368,
                            docstring='Input image size')
_l_(375256)
_c_(375261, _a_(375260, _a_(375259, _a_(375258, _n_(375257, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'hmap_size',
                            default_value=46,
                            docstring='Output heatmap size')
_l_(375262)
_c_(375267, _a_(375266, _a_(375265, _a_(375264, _n_(375263, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'cmap_radius',
                            default_value=21,
                            docstring='Center map gaussian variance')
_l_(375268)
_c_(375273, _a_(375272, _a_(375271, _a_(375270, _n_(375269, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'joints',
                            default_value=21,
                            docstring='Number of joints')
_l_(375274)
_c_(375279, _a_(375278, _a_(375277, _a_(375276, _n_(375275, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'stages',
                            default_value=6,
                            docstring='How many CPM stages')
_l_(375280)
_c_(375285, _a_(375284, _a_(375283, _a_(375282, _n_(375281, "tf", lambda: tf), "app"), "flags"), "DEFINE_integer"), 'cam_num',
                            default_value=0,
                            docstring='Webcam device number')
_l_(375286)
_c_(375291, _a_(375290, _a_(375289, _a_(375288, _n_(375287, "tf", lambda: tf), "app"), "flags"), "DEFINE_bool"), 'KALMAN_ON',
                         default_value=True,
                         docstring='enalbe kalman filter')
_l_(375292)
_c_(375297, _a_(375296, _a_(375295, _a_(375294, _n_(375293, "tf", lambda: tf), "app"), "flags"), "DEFINE_float"), 'kalman_noise',
                            default_value=3e-2,
                            docstring='Kalman filter noise value')
_l_(375298)
_c_(375303, _a_(375302, _a_(375301, _a_(375300, _n_(375299, "tf", lambda: tf), "app"), "flags"), "DEFINE_string"), 'color_channel',
                           default_value='RGB',
                           docstring='')
_l_(375304)

# Set color for each finger
joint_color_code = [[139, 53, 255],
                    [0, 56, 255],
                    [43, 140, 237],
                    [37, 168, 36],
                    [147, 147, 0],
                    [70, 17, 145]]
_l_(375305)


limbs = [[0, 1],
         [1, 2],
         [2, 3],
         [3, 4],
         [0, 5],
         [5, 6],
         [6, 7],
         [7, 8],
         [0, 9],
         [9, 10],
         [10, 11],
         [11, 12],
         [0, 13],
         [13, 14],
         [14, 15],
         [15, 16],
         [0, 17],
         [17, 18],
         [18, 19],
         [19, 20]
         ]
_l_(375306)

if _a_(375309, _a_(375308, _n_(375307, "sys", lambda: sys), "version_info"), "major") == 3:
    _l_(375312)

    PYTHON_VERSION = 3
    _l_(375310)
else:
    PYTHON_VERSION = 2
    _l_(375311)


def main(argv):
    _l_(376106)

    tf_device = '/gpu:0'
    _l_(375313)
    with _c_(375317, _a_(375315, _n_(375314, "tf", lambda: tf), "device"), _n_(375316, "tf_device", lambda: tf_device)):
        _l_(375365)

        """Build graph
        """
        if _a_(375319, _n_(375318, "FLAGS", lambda: FLAGS), "color_channel") == 'RGB':
            _l_(375340)

            input_data = _c_(375328, _a_(375321, _n_(375320, "tf", lambda: tf), "placeholder"), dtype=_a_(375323, _n_(375322, "tf", lambda: tf), "float32"), shape=[None, _a_(375325, _n_(375324, "FLAGS", lambda: FLAGS), "input_size"), _a_(375327, _n_(375326, "FLAGS", lambda: FLAGS), "input_size"), 3],
                                        name='input_image')
            _l_(375329)
        else:
            input_data = _c_(375338, _a_(375331, _n_(375330, "tf", lambda: tf), "placeholder"), dtype=_a_(375333, _n_(375332, "tf", lambda: tf), "float32"), shape=[None, _a_(375335, _n_(375334, "FLAGS", lambda: FLAGS), "input_size"), _a_(375337, _n_(375336, "FLAGS", lambda: FLAGS), "input_size"), 1],
                                        name='input_image')
            _l_(375339)

        center_map = _c_(375349, _a_(375342, _n_(375341, "tf", lambda: tf), "placeholder"), dtype=_a_(375344, _n_(375343, "tf", lambda: tf), "float32"), shape=[None, _a_(375346, _n_(375345, "FLAGS", lambda: FLAGS), "input_size"), _a_(375348, _n_(375347, "FLAGS", lambda: FLAGS), "input_size"), 1],
                                    name='center_map')
        _l_(375350)

        model = _c_(375357, _a_(375352, _n_(375351, "cpm_hand_slim", lambda: cpm_hand_slim), "CPM_Model"), _a_(375354, _n_(375353, "FLAGS", lambda: FLAGS), "stages"), _a_(375356, _n_(375355, "FLAGS", lambda: FLAGS), "joints") + 1)
        _l_(375358)
        _c_(375363, _a_(375360, _n_(375359, "model", lambda: model), "build_model"), _n_(375361, "input_data", lambda: input_data), _n_(375362, "center_map", lambda: center_map), 1)
        _l_(375364)

    saver = _c_(375369, _a_(375368, _a_(375367, _n_(375366, "tf", lambda: tf), "train"), "Saver"))
    _l_(375370)

    """Create session and restore weights
    """
    sess = _c_(375373, _a_(375372, _n_(375371, "tf", lambda: tf), "Session"))
    _l_(375374)

    _c_(375380, _a_(375376, _n_(375375, "sess", lambda: sess), "run"), _c_(375379, _a_(375378, _n_(375377, "tf", lambda: tf), "global_variables_initializer")))
    _l_(375381)
    if _c_(375385, _a_(375384, _a_(375383, _n_(375382, "FLAGS", lambda: FLAGS), "model_path"), "endswith"), 'pkl'):
        _l_(375400)

        _c_(375391, _a_(375387, _n_(375386, "model", lambda: model), "load_weights_from_file"), _a_(375389, _n_(375388, "FLAGS", lambda: FLAGS), "model_path"), _n_(375390, "sess", lambda: sess), False)
        _l_(375392)
    else:
        _c_(375398, _a_(375394, _n_(375393, "saver", lambda: saver), "restore"), _n_(375395, "sess", lambda: sess), _a_(375397, _n_(375396, "FLAGS", lambda: FLAGS), "model_path"))
        _l_(375399)

    test_center_map = _c_(375413, _a_(375402, _n_(375401, "cpm_utils", lambda: cpm_utils), "gaussian_img"), _a_(375404, _n_(375403, "FLAGS", lambda: FLAGS), "input_size"), _a_(375406, _n_(375405, "FLAGS", lambda: FLAGS), "input_size"), _a_(375408, _n_(375407, "FLAGS", lambda: FLAGS), "input_size") / 2,
                                             _a_(375410, _n_(375409, "FLAGS", lambda: FLAGS), "input_size") / 2,
                                             _a_(375412, _n_(375411, "FLAGS", lambda: FLAGS), "cmap_radius"))
    _l_(375414)
    test_center_map = _c_(375422, _a_(375416, _n_(375415, "np", lambda: np), "reshape"), _n_(375417, "test_center_map", lambda: test_center_map), [1, _a_(375419, _n_(375418, "FLAGS", lambda: FLAGS), "input_size"), _a_(375421, _n_(375420, "FLAGS", lambda: FLAGS), "input_size"), 1])
    _l_(375423)

    # Check weights
    for variable in _c_(375426, _a_(375425, _n_(375424, "tf", lambda: tf), "trainable_variables")):
        _l_(375451)

        with _c_(375429, _a_(375428, _n_(375427, "tf", lambda: tf), "variable_scope"), '', reuse=True):
            _l_(375450)

            var = _c_(375436, _a_(375431, _n_(375430, "tf", lambda: tf), "get_variable"), _c_(375435, _a_(375434, _a_(375433, _n_(375432, "variable", lambda: variable), "name"), "split"), ':0')[0])
            _l_(375437)
            _c_(375448, _n_(375438, "print", lambda: print), _a_(375440, _n_(375439, "variable", lambda: variable), "name"), _c_(375447, _a_(375442, _n_(375441, "np", lambda: np), "mean"), _c_(375446, _a_(375444, _n_(375443, "sess", lambda: sess), "run"), _n_(375445, "var", lambda: var))))
            _l_(375449)

    if not _c_(375455, _a_(375454, _a_(375453, _n_(375452, "FLAGS", lambda: FLAGS), "DEMO_TYPE"), "endswith"), ('png', 'jpg')):
        _l_(375462)

        cam = _c_(375460, _a_(375457, _n_(375456, "cv2", lambda: cv2), "VideoCapture"), _a_(375459, _n_(375458, "FLAGS", lambda: FLAGS), "cam_num"))
        _l_(375461)

    # Create kalman filters
    if _a_(375464, _n_(375463, "FLAGS", lambda: FLAGS), "KALMAN_ON"):
        _l_(375501)

        kalman_filter_array = [_c_(375467, _a_(375466, _n_(375465, "cv2", lambda: cv2), "KalmanFilter"), 4, 2) for _ in _c_(375471, _n_(375468, "range", lambda: range), _a_(375470, _n_(375469, "FLAGS", lambda: FLAGS), "joints"))]
        _l_(375472)
        for _, joint_kalman_filter in _c_(375475, _n_(375473, "enumerate", lambda: enumerate), _n_(375474, "kalman_filter_array", lambda: kalman_filter_array)):
            _l_(375499)

            _n_(375476, "joint_kalman_filter", lambda: joint_kalman_filter).transitionMatrix = _c_(375481, _a_(375478, _n_(375477, "np", lambda: np), "array"), [[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]],
                                                            _a_(375480, _n_(375479, "np", lambda: np), "float32"))
            _l_(375482)
            _n_(375483, "joint_kalman_filter", lambda: joint_kalman_filter).measurementMatrix = _c_(375488, _a_(375485, _n_(375484, "np", lambda: np), "array"), [[1, 0, 0, 0], [0, 1, 0, 0]], _a_(375487, _n_(375486, "np", lambda: np), "float32"))
            _l_(375489)
            _n_(375490, "joint_kalman_filter", lambda: joint_kalman_filter).processNoiseCov = _c_(375495, _a_(375492, _n_(375491, "np", lambda: np), "array"), [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                                                           _a_(375494, _n_(375493, "np", lambda: np), "float32")) * _a_(375497, _n_(375496, "FLAGS", lambda: FLAGS), "kalman_noise")
            _l_(375498)
    else:
        kalman_filter_array = None
        _l_(375500)

    with _c_(375505, _a_(375503, _n_(375502, "tf", lambda: tf), "device"), _n_(375504, "tf_device", lambda: tf_device)):
        _l_(376105)


        while True:
            _l_(376104)

            t1 = _c_(375508, _a_(375507, _n_(375506, "time", lambda: time), "time"))
            _l_(375509)
            if _c_(375513, _a_(375512, _a_(375511, _n_(375510, "FLAGS", lambda: FLAGS), "DEMO_TYPE"), "endswith"), ('png', 'jpg')):
                _l_(375529)

                test_img = _c_(375520, _a_(375515, _n_(375514, "cpm_utils", lambda: cpm_utils), "read_image"), _a_(375517, _n_(375516, "FLAGS", lambda: FLAGS), "DEMO_TYPE"), [], _a_(375519, _n_(375518, "FLAGS", lambda: FLAGS), "input_size"), 'IMAGE')
                _l_(375521)
            else:
                test_img = _c_(375527, _a_(375523, _n_(375522, "cpm_utils", lambda: cpm_utils), "read_image"), [], _n_(375524, "cam", lambda: cam), _a_(375526, _n_(375525, "FLAGS", lambda: FLAGS), "input_size"), 'WEBCAM')
                _l_(375528)

            test_img_resize = _c_(375537, _a_(375531, _n_(375530, "cv2", lambda: cv2), "resize"), _n_(375532, "test_img", lambda: test_img), (_a_(375534, _n_(375533, "FLAGS", lambda: FLAGS), "input_size"), _a_(375536, _n_(375535, "FLAGS", lambda: FLAGS), "input_size")))
            _l_(375538)
            _c_(375544, _n_(375539, "print", lambda: print), 'img read time %f' % (_c_(375542, _a_(375541, _n_(375540, "time", lambda: time), "time")) - _n_(375543, "t1", lambda: t1)))
            _l_(375545)

            if _a_(375547, _n_(375546, "FLAGS", lambda: FLAGS), "color_channel") == 'GRAY':
                _l_(375581)

                test_img_resize = _c_(375557, _a_(375552, _c_(375551, _a_(375549, _n_(375548, "np", lambda: np), "dot"), _n_(375550, "test_img_resize", lambda: test_img_resize)[..., :3], [0.299, 0.587, 0.114]), "reshape"), (_a_(375554, _n_(375553, "FLAGS", lambda: FLAGS), "input_size"), _a_(375556, _n_(375555, "FLAGS", lambda: FLAGS), "input_size"), 1))
                _l_(375558)
                _c_(375566, _a_(375560, _n_(375559, "cv2", lambda: cv2), "imshow"), 'color', _c_(375565, _a_(375562, _n_(375561, "test_img", lambda: test_img), "astype"), _a_(375564, _n_(375563, "np", lambda: np), "uint8")))
                _l_(375567)
                _c_(375575, _a_(375569, _n_(375568, "cv2", lambda: cv2), "imshow"), 'gray', _c_(375574, _a_(375571, _n_(375570, "test_img_resize", lambda: test_img_resize), "astype"), _a_(375573, _n_(375572, "np", lambda: np), "uint8")))
                _l_(375576)
                _c_(375579, _a_(375578, _n_(375577, "cv2", lambda: cv2), "waitKey"), 1)
                _l_(375580)

            test_img_input = _n_(375582, "test_img_resize", lambda: test_img_resize) / 256.0 - 0.5
            _l_(375583)
            test_img_input = _c_(375587, _a_(375585, _n_(375584, "np", lambda: np), "expand_dims"), _n_(375586, "test_img_input", lambda: test_img_input), axis=0)
            _l_(375588)


            if _c_(375592, _a_(375591, _a_(375590, _n_(375589, "FLAGS", lambda: FLAGS), "DEMO_TYPE"), "endswith"), ('png', 'jpg')):
                _l_(376103)

                # Inference
                t1 = _c_(375595, _a_(375594, _n_(375593, "time", lambda: time), "time"))
                _l_(375596)
                predict_heatmap, stage_heatmap_np = _c_(375605, _a_(375598, _n_(375597, "sess", lambda: sess), "run"), [_a_(375600, _n_(375599, "model", lambda: model), "current_heatmap"),
                                                              _a_(375602, _n_(375601, "model", lambda: model), "stage_heatmap"),
                                                              ],
                                                             feed_dict={'input_image:0': _n_(375603, "test_img_input", lambda: test_img_input),
                                                                        'center_map:0': _n_(375604, "test_center_map", lambda: test_center_map)})
                _l_(375606)

                # Show visualized image
                demo_img = _c_(375612, _n_(375607, "visualize_result", lambda: visualize_result), _n_(375608, "test_img", lambda: test_img), _n_(375609, "FLAGS", lambda: FLAGS), _n_(375610, "stage_heatmap_np", lambda: stage_heatmap_np), _n_(375611, "kalman_filter_array", lambda: kalman_filter_array))
                _l_(375613)
                _c_(375621, _a_(375615, _n_(375614, "cv2", lambda: cv2), "imshow"), 'demo_img', _c_(375620, _a_(375617, _n_(375616, "demo_img", lambda: demo_img), "astype"), _a_(375619, _n_(375618, "np", lambda: np), "uint8")))
                _l_(375622)
                if _c_(375625, _a_(375624, _n_(375623, "cv2", lambda: cv2), "waitKey"), 0) == _c_(375627, _n_(375626, "ord", lambda: ord), 'q'):
                    _l_(375628)

break                _c_(375634, _n_(375629, "print", lambda: print), 'fps: %.2f' % (1 / (_c_(375632, _a_(375631, _n_(375630, "time", lambda: time), "time")) - _n_(375633, "t1", lambda: t1))))
                _l_(375635)
            elif _a_(375637, _n_(375636, "FLAGS", lambda: FLAGS), "DEMO_TYPE") == 'MULTI':
                _l_(376102)


                # Inference
                t1 = _c_(375640, _a_(375639, _n_(375638, "time", lambda: time), "time"))
                _l_(375641)
                predict_heatmap, stage_heatmap_np = _c_(375650, _a_(375643, _n_(375642, "sess", lambda: sess), "run"), [_a_(375645, _n_(375644, "model", lambda: model), "current_heatmap"),
                                                              _a_(375647, _n_(375646, "model", lambda: model), "stage_heatmap"),
                                                              ],
                                                             feed_dict={'input_image:0': _n_(375648, "test_img_input", lambda: test_img_input),
                                                                        'center_map:0': _n_(375649, "test_center_map", lambda: test_center_map)})
                _l_(375651)

                # Show visualized image
                demo_img = _c_(375657, _n_(375652, "visualize_result", lambda: visualize_result), _n_(375653, "test_img", lambda: test_img), _n_(375654, "FLAGS", lambda: FLAGS), _n_(375655, "stage_heatmap_np", lambda: stage_heatmap_np), _n_(375656, "kalman_filter_array", lambda: kalman_filter_array))
                _l_(375658)
                _c_(375666, _a_(375660, _n_(375659, "cv2", lambda: cv2), "imshow"), 'demo_img', _c_(375665, _a_(375662, _n_(375661, "demo_img", lambda: demo_img), "astype"), _a_(375664, _n_(375663, "np", lambda: np), "uint8")))
                _l_(375667)
                if _c_(375670, _a_(375669, _n_(375668, "cv2", lambda: cv2), "waitKey"), 1) == _c_(375672, _n_(375671, "ord", lambda: ord), 'q'):
                    _l_(375673)

break                _c_(375679, _n_(375674, "print", lambda: print), 'fps: %.2f' % (1 / (_c_(375677, _a_(375676, _n_(375675, "time", lambda: time), "time")) - _n_(375678, "t1", lambda: t1))))
                _l_(375680)


            elif _a_(375682, _n_(375681, "FLAGS", lambda: FLAGS), "DEMO_TYPE") == 'SINGLE':
                _l_(376101)


                # Inference
                t1 = _c_(375685, _a_(375684, _n_(375683, "time", lambda: time), "time"))
                _l_(375686)
                stage_heatmap_np = _c_(375693, _a_(375688, _n_(375687, "sess", lambda: sess), "run"), [_a_(375690, _n_(375689, "model", lambda: model), "stage_heatmap")[5]],
                                            feed_dict={'input_image:0': _n_(375691, "test_img_input", lambda: test_img_input),
                                                       'center_map:0': _n_(375692, "test_center_map", lambda: test_center_map)})
                _l_(375694)

                # Show visualized image
                demo_img = _c_(375700, _n_(375695, "visualize_result", lambda: visualize_result), _n_(375696, "test_img", lambda: test_img), _n_(375697, "FLAGS", lambda: FLAGS), _n_(375698, "stage_heatmap_np", lambda: stage_heatmap_np), _n_(375699, "kalman_filter_array", lambda: kalman_filter_array))
                _l_(375701)
                _c_(375709, _a_(375703, _n_(375702, "cv2", lambda: cv2), "imshow"), 'current heatmap', _c_(375708, _a_(375705, _n_(375704, "demo_img", lambda: (demo_img)), "astype"), _a_(375707, _n_(375706, "np", lambda: np), "uint8")))
                _l_(375710)
                if _c_(375713, _a_(375712, _n_(375711, "cv2", lambda: cv2), "waitKey"), 1) == _c_(375715, _n_(375714, "ord", lambda: ord), 'q'):
                    _l_(375716)

break                _c_(375722, _n_(375717, "print", lambda: print), 'fps: %.2f' % (1 / (_c_(375720, _a_(375719, _n_(375718, "time", lambda: time), "time")) - _n_(375721, "t1", lambda: t1))))
                _l_(375723)


            elif _a_(375725, _n_(375724, "FLAGS", lambda: FLAGS), "DEMO_TYPE") == 'HM':
                _l_(376100)


                # Inference
                t1 = _c_(375728, _a_(375727, _n_(375726, "time", lambda: time), "time"))
                _l_(375729)
                stage_heatmap_np = _c_(375738, _a_(375731, _n_(375730, "sess", lambda: sess), "run"), [_a_(375733, _n_(375732, "model", lambda: model), "stage_heatmap")[_a_(375735, _n_(375734, "FLAGS", lambda: FLAGS), "stages") - 1]],
                                            feed_dict={'input_image:0': _n_(375736, "test_img_input", lambda: test_img_input),
                                                       'center_map:0': _n_(375737, "test_center_map", lambda: test_center_map)})
                _l_(375739)
                _c_(375745, _n_(375740, "print", lambda: print), 'fps: %.2f' % (1 / (_c_(375743, _a_(375742, _n_(375741, "time", lambda: time), "time")) - _n_(375744, "t1", lambda: t1))))
                _l_(375746)

                demo_stage_heatmap = _c_(375760, _a_(375753, _n_(375747, "stage_heatmap_np", lambda: stage_heatmap_np)[_c_(375750, _n_(375748, "len", lambda: len), _n_(375749, "stage_heatmap_np", lambda: stage_heatmap_np)) - 1][0, :, :, 0:_a_(375752, _n_(375751, "FLAGS", lambda: FLAGS), "joints")], "reshape"), (_a_(375755, _n_(375754, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(375757, _n_(375756, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(375759, _n_(375758, "FLAGS", lambda: FLAGS), "joints")))
                _l_(375761)
                demo_stage_heatmap = _c_(375769, _a_(375763, _n_(375762, "cv2", lambda: cv2), "resize"), _n_(375764, "demo_stage_heatmap", lambda: demo_stage_heatmap), (_a_(375766, _n_(375765, "FLAGS", lambda: FLAGS), "input_size"), _a_(375768, _n_(375767, "FLAGS", lambda: FLAGS), "input_size")))
                _l_(375770)

                vertical_imgs = []
                _l_(375771)
                tmp_img = None
                _l_(375772)
                joint_coord_set = _c_(375777, _a_(375774, _n_(375773, "np", lambda: np), "zeros"), (_a_(375776, _n_(375775, "FLAGS", lambda: FLAGS), "joints"), 2))
                _l_(375778)

                for joint_num in _c_(375782, _n_(375779, "range", lambda: range), _a_(375781, _n_(375780, "FLAGS", lambda: FLAGS), "joints")):
                    _l_(375922)

                    # Concat until 4 img
                    if (_n_(375783, "joint_num", lambda: joint_num) % 4) == 0 and _n_(375784, "joint_num", lambda: joint_num) != 0:
                        _l_(375791)

                        _c_(375788, _a_(375786, _n_(375785, "vertical_imgs", lambda: vertical_imgs), "append"), _n_(375787, "tmp_img", lambda: tmp_img))
                        _l_(375789)
                        tmp_img = None
                        _l_(375790)

                    _n_(375792, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375793, "joint_num", lambda: joint_num)] *= (255 / _c_(375798, _a_(375795, _n_(375794, "np", lambda: np), "max"), _n_(375796, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375797, "joint_num", lambda: joint_num)]))
                    _l_(375799)

                    # Plot color joints
                    if _c_(375804, _a_(375801, _n_(375800, "np", lambda: np), "min"), _n_(375802, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375803, "joint_num", lambda: joint_num)]) > -50:
                        _l_(375878)

                        joint_coord = _c_(375816, _a_(375806, _n_(375805, "np", lambda: np), "unravel_index"), _c_(375811, _a_(375808, _n_(375807, "np", lambda: np), "argmax"), _n_(375809, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375810, "joint_num", lambda: joint_num)]),
                                                       (_a_(375813, _n_(375812, "FLAGS", lambda: FLAGS), "input_size"), _a_(375815, _n_(375814, "FLAGS", lambda: FLAGS), "input_size")))
                        _l_(375817)
                        _n_(375818, "joint_coord_set", lambda: joint_coord_set)[_n_(375819, "joint_num", lambda: joint_num), :] = _n_(375820, "joint_coord", lambda: joint_coord)
                        _l_(375821)
                        color_code_num = (_n_(375822, "joint_num", lambda: joint_num) // 4)
                        _l_(375823)

                        if _n_(375824, "joint_num", lambda: joint_num) in [0, 4, 8, 12, 16]:
                            _l_(375877)

                            if _n_(375825, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                                _l_(375842)

                                joint_color = _c_(375833, _n_(375826, "list", lambda: list), _c_(375832, _n_(375827, "map", lambda: map), lambda x: _n_(375828, "x", lambda: x) + 35 * (_n_(375829, "joint_num", lambda: joint_num) % 4), _n_(375830, "joint_color_code", lambda: joint_color_code)[_n_(375831, "color_code_num", lambda: color_code_num)]))
                                _l_(375834)
                            else:
                                joint_color = _c_(375840, _n_(375835, "map", lambda: map), lambda x: _n_(375836, "x", lambda: x) + 35 * (_n_(375837, "joint_num", lambda: joint_num) % 4), _n_(375838, "joint_color_code", lambda: joint_color_code)[_n_(375839, "color_code_num", lambda: color_code_num)])
                                _l_(375841)

                            _c_(375849, _a_(375844, _n_(375843, "cv2", lambda: cv2), "circle"), _n_(375845, "test_img", lambda: test_img), center=(_n_(375846, "joint_coord", lambda: joint_coord)[1], _n_(375847, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(375848, "joint_color", lambda: joint_color),
                                       thickness=-1)
                            _l_(375850)
                        else:
                            if _n_(375851, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                                _l_(375868)

                                joint_color = _c_(375859, _n_(375852, "list", lambda: list), _c_(375858, _n_(375853, "map", lambda: map), lambda x: _n_(375854, "x", lambda: x) + 35 * (_n_(375855, "joint_num", lambda: joint_num) % 4), _n_(375856, "joint_color_code", lambda: joint_color_code)[_n_(375857, "color_code_num", lambda: color_code_num)]))
                                _l_(375860)
                            else:
                                joint_color = _c_(375866, _n_(375861, "map", lambda: map), lambda x: _n_(375862, "x", lambda: x) + 35 * (_n_(375863, "joint_num", lambda: joint_num) % 4), _n_(375864, "joint_color_code", lambda: joint_color_code)[_n_(375865, "color_code_num", lambda: color_code_num)])
                                _l_(375867)

                            _c_(375875, _a_(375870, _n_(375869, "cv2", lambda: cv2), "circle"), _n_(375871, "test_img", lambda: test_img), center=(_n_(375872, "joint_coord", lambda: joint_coord)[1], _n_(375873, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(375874, "joint_color", lambda: joint_color),
                                       thickness=-1)
                            _l_(375876)

                    # Put text
                    tmp = _c_(375884, _a_(375881, _n_(375879, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375880, "joint_num", lambda: joint_num)], "astype"), _a_(375883, _n_(375882, "np", lambda: np), "uint8"))
                    _l_(375885)
                    tmp = _c_(375898, _a_(375887, _n_(375886, "cv2", lambda: cv2), "putText"), _n_(375888, "tmp", lambda: tmp), 'Min:' + _c_(375895, _n_(375889, "str", lambda: str), _c_(375894, _a_(375891, _n_(375890, "np", lambda: np), "min"), _n_(375892, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375893, "joint_num", lambda: joint_num)])),
                                      org=(5, 20), fontFace=_a_(375897, _n_(375896, "cv2", lambda: cv2), "FONT_HERSHEY_COMPLEX"), fontScale=0.3, color=150)
                    _l_(375899)
                    tmp = _c_(375912, _a_(375901, _n_(375900, "cv2", lambda: cv2), "putText"), _n_(375902, "tmp", lambda: tmp), 'Mean:' + _c_(375909, _n_(375903, "str", lambda: str), _c_(375908, _a_(375905, _n_(375904, "np", lambda: np), "mean"), _n_(375906, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375907, "joint_num", lambda: joint_num)])),
                                      org=(5, 30), fontFace=_a_(375911, _n_(375910, "cv2", lambda: cv2), "FONT_HERSHEY_COMPLEX"), fontScale=0.3, color=150)
                    _l_(375913)
                    tmp_img = _c_(375918, _a_(375915, _n_(375914, "np", lambda: np), "concatenate"), (_n_(375916, "tmp_img", lambda: tmp_img), _n_(375917, "tmp", lambda: tmp)), axis=0) \
                        if _n_(375919, "tmp_img", lambda: tmp_img) is not None else _n_(375920, "tmp", lambda: tmp)
                    _l_(375921)

                # Plot limbs
                for limb_num in _c_(375927, _n_(375923, "range", lambda: range), _c_(375926, _n_(375924, "len", lambda: len), _n_(375925, "limbs", lambda: limbs))):
                    _l_(376021)

                    if _c_(375933, _a_(375929, _n_(375928, "np", lambda: np), "min"), _n_(375930, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375931, "limbs", lambda: limbs)[_n_(375932, "limb_num", lambda: limb_num)][0]]) > -2000 and _c_(375939, _a_(375935, _n_(375934, "np", lambda: np), "min"), _n_(375936, "demo_stage_heatmap", lambda: demo_stage_heatmap)[:, :, _n_(375937, "limbs", lambda: limbs)[_n_(375938, "limb_num", lambda: limb_num)][1]]) > -2000:
                        _l_(376020)

                        x1 = _n_(375940, "joint_coord_set", lambda: joint_coord_set)[_n_(375941, "limbs", lambda: limbs)[_n_(375942, "limb_num", lambda: limb_num)][0], 0]
                        _l_(375943)
                        y1 = _n_(375944, "joint_coord_set", lambda: joint_coord_set)[_n_(375945, "limbs", lambda: limbs)[_n_(375946, "limb_num", lambda: limb_num)][0], 1]
                        _l_(375947)
                        x2 = _n_(375948, "joint_coord_set", lambda: joint_coord_set)[_n_(375949, "limbs", lambda: limbs)[_n_(375950, "limb_num", lambda: limb_num)][1], 0]
                        _l_(375951)
                        y2 = _n_(375952, "joint_coord_set", lambda: joint_coord_set)[_n_(375953, "limbs", lambda: limbs)[_n_(375954, "limb_num", lambda: limb_num)][1], 1]
                        _l_(375955)
                        length = ((_n_(375956, "x1", lambda: x1) - _n_(375957, "x2", lambda: x2)) ** 2 + (_n_(375958, "y1", lambda: y1) - _n_(375959, "y2", lambda: y2)) ** 2) ** 0.5
                        _l_(375960)
                        if _n_(375961, "length", lambda: length) < 10000 and _n_(375962, "length", lambda: length) > 5:
                            _l_(376019)

                            deg = _c_(375972, _a_(375964, _n_(375963, "math", lambda: math), "degrees"), _c_(375971, _a_(375966, _n_(375965, "math", lambda: math), "atan2"), _n_(375967, "x1", lambda: x1) - _n_(375968, "x2", lambda: x2), _n_(375969, "y1", lambda: y1) - _n_(375970, "y2", lambda: y2)))
                            _l_(375973)
                            polygon = _c_(375990, _a_(375975, _n_(375974, "cv2", lambda: cv2), "ellipse2Poly"), (_c_(375979, _n_(375976, "int", lambda: int), (_n_(375977, "y1", lambda: y1) + _n_(375978, "y2", lambda: y2)) / 2), _c_(375983, _n_(375980, "int", lambda: int), (_n_(375981, "x1", lambda: x1) + _n_(375982, "x2", lambda: x2)) / 2)),
                                                       (_c_(375986, _n_(375984, "int", lambda: int), _n_(375985, "length", lambda: length) / 2), 3),
                                                       _c_(375989, _n_(375987, "int", lambda: int), _n_(375988, "deg", lambda: deg)),
                                                       0, 360, 1)
                            _l_(375991)
                            color_code_num = _n_(375992, "limb_num", lambda: limb_num) // 4
                            _l_(375993)
                            if _n_(375994, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                                _l_(376011)

                                limb_color = _c_(376002, _n_(375995, "list", lambda: list), _c_(376001, _n_(375996, "map", lambda: map), lambda x: _n_(375997, "x", lambda: x) + 35 * (_n_(375998, "limb_num", lambda: limb_num) % 4), _n_(375999, "joint_color_code", lambda: joint_color_code)[_n_(376000, "color_code_num", lambda: color_code_num)]))
                                _l_(376003)
                            else:
                                limb_color = _c_(376009, _n_(376004, "map", lambda: map), lambda x: _n_(376005, "x", lambda: x) + 35 * (_n_(376006, "limb_num", lambda: limb_num) % 4), _n_(376007, "joint_color_code", lambda: joint_color_code)[_n_(376008, "color_code_num", lambda: color_code_num)])
                                _l_(376010)

                            _c_(376017, _a_(376013, _n_(376012, "cv2", lambda: cv2), "fillConvexPoly"), _n_(376014, "test_img", lambda: test_img), _n_(376015, "polygon", lambda: polygon), color=_n_(376016, "limb_color", lambda: limb_color))
                            _l_(376018)

                if _n_(376022, "tmp_img", lambda: tmp_img) is not None:
                    _l_(376038)

                    tmp_img = _c_(376031, _a_(376025, _a_(376024, _n_(376023, "np", lambda: np), "lib"), "pad"), _n_(376026, "tmp_img", lambda: tmp_img), ((0, _a_(376028, _n_(376027, "vertical_imgs", lambda: vertical_imgs)[0], "shape")[0] - _a_(376030, _n_(376029, "tmp_img", lambda: tmp_img), "shape")[0]), (0, 0)),
                                         'constant', constant_values=(0, 0))
                    _l_(376032)
                    _c_(376036, _a_(376034, _n_(376033, "vertical_imgs", lambda: vertical_imgs), "append"), _n_(376035, "tmp_img", lambda: tmp_img))
                    _l_(376037)

                # Concat horizontally
                output_img = None
                _l_(376039)
                for col in _c_(376044, _n_(376040, "range", lambda: range), _c_(376043, _n_(376041, "len", lambda: len), _n_(376042, "vertical_imgs", lambda: vertical_imgs))):
                    _l_(376055)

                    output_img = _c_(376050, _a_(376046, _n_(376045, "np", lambda: np), "concatenate"), (_n_(376047, "output_img", lambda: output_img), _n_(376048, "vertical_imgs", lambda: vertical_imgs)[_n_(376049, "col", lambda: col)]), axis=1) if _n_(376051, "output_img", lambda: output_img) is not None else \
                        _n_(376052, "vertical_imgs", lambda: vertical_imgs)[_n_(376053, "col", lambda: col)]
                    _l_(376054)

                output_img = _c_(376060, _a_(376057, _n_(376056, "output_img", lambda: output_img), "astype"), _a_(376059, _n_(376058, "np", lambda: np), "uint8"))
                _l_(376061)
                output_img = _c_(376067, _a_(376063, _n_(376062, "cv2", lambda: cv2), "applyColorMap"), _n_(376064, "output_img", lambda: output_img), _a_(376066, _n_(376065, "cv2", lambda: cv2), "COLORMAP_JET"))
                _l_(376068)
                test_img = _c_(376074, _a_(376070, _n_(376069, "cv2", lambda: cv2), "resize"), _n_(376071, "test_img", lambda: test_img), (300, 300), _a_(376073, _n_(376072, "cv2", lambda: cv2), "INTER_LANCZOS4"))
                _l_(376075)
                _c_(376079, _a_(376077, _n_(376076, "cv2", lambda: cv2), "imshow"), 'hm', _n_(376078, "output_img", lambda: output_img))
                _l_(376080)
                _c_(376083, _a_(376082, _n_(376081, "cv2", lambda: cv2), "moveWindow"), 'hm', 2000, 200)
                _l_(376084)
                _c_(376088, _a_(376086, _n_(376085, "cv2", lambda: cv2), "imshow"), 'rgb', _n_(376087, "test_img", lambda: test_img))
                _l_(376089)
                _c_(376092, _a_(376091, _n_(376090, "cv2", lambda: cv2), "moveWindow"), 'rgb', 2000, 750) 
                _l_(376093) 
                if _c_(376096, _a_(376095, _n_(376094, "cv2", lambda: cv2), "waitKey"), 1) == _c_(376098, _n_(376097, "ord", lambda: ord), 'q'):
                    _l_(376099)

break

def visualize_result(test_img, FLAGS, stage_heatmap_np, kalman_filter_array):
    _l_(376554)

    t1 = _c_(376109, _a_(376108, _n_(376107, "time", lambda: time), "time"))
    _l_(376110)
    demo_stage_heatmaps = []
    _l_(376111)
    if _a_(376113, _n_(376112, "FLAGS", lambda: FLAGS), "DEMO_TYPE") == 'MULTI':
        _l_(376215)

        for stage in _c_(376118, _n_(376114, "range", lambda: range), _c_(376117, _n_(376115, "len", lambda: len), _n_(376116, "stage_heatmap_np", lambda: stage_heatmap_np))):
            _l_(376166)

            demo_stage_heatmap = _c_(376130, _a_(376123, _n_(376119, "stage_heatmap_np", lambda: stage_heatmap_np)[_n_(376120, "stage", lambda: stage)][0, :, :, 0:_a_(376122, _n_(376121, "FLAGS", lambda: FLAGS), "joints")], "reshape"), (_a_(376125, _n_(376124, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376127, _n_(376126, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376129, _n_(376128, "FLAGS", lambda: FLAGS), "joints")))
            _l_(376131)
            demo_stage_heatmap = _c_(376139, _a_(376133, _n_(376132, "cv2", lambda: cv2), "resize"), _n_(376134, "demo_stage_heatmap", lambda: demo_stage_heatmap), (_a_(376136, _n_(376135, "test_img", lambda: test_img), "shape")[1], _a_(376138, _n_(376137, "test_img", lambda: test_img), "shape")[0]))
            _l_(376140)
            demo_stage_heatmap = _c_(376144, _a_(376142, _n_(376141, "np", lambda: np), "amax"), _n_(376143, "demo_stage_heatmap", lambda: demo_stage_heatmap), axis=2)
            _l_(376145)
            demo_stage_heatmap = _c_(376153, _a_(376147, _n_(376146, "np", lambda: np), "reshape"), _n_(376148, "demo_stage_heatmap", lambda: demo_stage_heatmap), (_a_(376150, _n_(376149, "test_img", lambda: test_img), "shape")[1], _a_(376152, _n_(376151, "test_img", lambda: test_img), "shape")[0], 1))
            _l_(376154)
            demo_stage_heatmap = _c_(376158, _a_(376156, _n_(376155, "np", lambda: np), "repeat"), _n_(376157, "demo_stage_heatmap", lambda: demo_stage_heatmap), 3, axis=2)
            _l_(376159)
            demo_stage_heatmap *= 255
            _l_(376160)
            _c_(376164, _a_(376162, _n_(376161, "demo_stage_heatmaps", lambda: demo_stage_heatmaps), "append"), _n_(376163, "demo_stage_heatmap", lambda: demo_stage_heatmap))
            _l_(376165)

        last_heatmap = _c_(376180, _a_(376173, _n_(376167, "stage_heatmap_np", lambda: stage_heatmap_np)[_c_(376170, _n_(376168, "len", lambda: len), _n_(376169, "stage_heatmap_np", lambda: stage_heatmap_np)) - 1][0, :, :, 0:_a_(376172, _n_(376171, "FLAGS", lambda: FLAGS), "joints")], "reshape"), (_a_(376175, _n_(376174, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376177, _n_(376176, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376179, _n_(376178, "FLAGS", lambda: FLAGS), "joints")))
        _l_(376181)
        last_heatmap = _c_(376189, _a_(376183, _n_(376182, "cv2", lambda: cv2), "resize"), _n_(376184, "last_heatmap", lambda: last_heatmap), (_a_(376186, _n_(376185, "test_img", lambda: test_img), "shape")[1], _a_(376188, _n_(376187, "test_img", lambda: test_img), "shape")[0]))
        _l_(376190)
    else:
        last_heatmap = _c_(376204, _a_(376197, _n_(376191, "stage_heatmap_np", lambda: stage_heatmap_np)[_c_(376194, _n_(376192, "len", lambda: len), _n_(376193, "stage_heatmap_np", lambda: stage_heatmap_np)) - 1][0, :, :, 0:_a_(376196, _n_(376195, "FLAGS", lambda: FLAGS), "joints")], "reshape"), (_a_(376199, _n_(376198, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376201, _n_(376200, "FLAGS", lambda: FLAGS), "hmap_size"), _a_(376203, _n_(376202, "FLAGS", lambda: FLAGS), "joints")))
        _l_(376205)
        last_heatmap = _c_(376213, _a_(376207, _n_(376206, "cv2", lambda: cv2), "resize"), _n_(376208, "last_heatmap", lambda: last_heatmap), (_a_(376210, _n_(376209, "test_img", lambda: test_img), "shape")[1], _a_(376212, _n_(376211, "test_img", lambda: test_img), "shape")[0]))
        _l_(376214)
    _c_(376221, _n_(376216, "print", lambda: print), 'hm resize time %f' % (_c_(376219, _a_(376218, _n_(376217, "time", lambda: time), "time")) - _n_(376220, "t1", lambda: t1)))
    _l_(376222)

    t1 = _c_(376225, _a_(376224, _n_(376223, "time", lambda: time), "time"))
    _l_(376226)
    joint_coord_set = _c_(376231, _a_(376228, _n_(376227, "np", lambda: np), "zeros"), (_a_(376230, _n_(376229, "FLAGS", lambda: FLAGS), "joints"), 2))
    _l_(376232)

    # Plot joint colors
    if _n_(376233, "kalman_filter_array", lambda: kalman_filter_array) is not None:
        _l_(376419)

        for joint_num in _c_(376237, _n_(376234, "range", lambda: range), _a_(376236, _n_(376235, "FLAGS", lambda: FLAGS), "joints")):
            _l_(376339)

            joint_coord = _c_(376249, _a_(376239, _n_(376238, "np", lambda: np), "unravel_index"), _c_(376244, _a_(376241, _n_(376240, "np", lambda: np), "argmax"), _n_(376242, "last_heatmap", lambda: last_heatmap)[:, :, _n_(376243, "joint_num", lambda: joint_num)]),
                                           (_a_(376246, _n_(376245, "test_img", lambda: test_img), "shape")[0], _a_(376248, _n_(376247, "test_img", lambda: test_img), "shape")[1]))
            _l_(376250)
            joint_coord = _c_(376260, _a_(376257, _c_(376256, _a_(376255, _c_(376254, _a_(376252, _n_(376251, "np", lambda: np), "array"), _n_(376253, "joint_coord", lambda: joint_coord)), "reshape"), (2, 1)), "astype"), _a_(376259, _n_(376258, "np", lambda: np), "float32"))
            _l_(376261)
            _c_(376266, _a_(376264, _n_(376262, "kalman_filter_array", lambda: kalman_filter_array)[_n_(376263, "joint_num", lambda: joint_num)], "correct"), _n_(376265, "joint_coord", lambda: joint_coord))
            _l_(376267)
            kalman_pred = _c_(376271, _a_(376270, _n_(376268, "kalman_filter_array", lambda: kalman_filter_array)[_n_(376269, "joint_num", lambda: joint_num)], "predict"))
            _l_(376272)
            _n_(376273, "joint_coord_set", lambda: joint_coord_set)[_n_(376274, "joint_num", lambda: joint_num), :] = _c_(376281, _a_(376280, _c_(376279, _a_(376276, _n_(376275, "np", lambda: np), "array"), [_n_(376277, "kalman_pred", lambda: kalman_pred)[0], _n_(376278, "kalman_pred", lambda: kalman_pred)[1]]), "reshape"), (2))
            _l_(376282)

            color_code_num = (_n_(376283, "joint_num", lambda: joint_num) // 4)
            _l_(376284)
            if _n_(376285, "joint_num", lambda: joint_num) in [0, 4, 8, 12, 16]:
                _l_(376338)

                if _n_(376286, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                    _l_(376303)

                    joint_color = _c_(376294, _n_(376287, "list", lambda: list), _c_(376293, _n_(376288, "map", lambda: map), lambda x: _n_(376289, "x", lambda: x) + 35 * (_n_(376290, "joint_num", lambda: joint_num) % 4), _n_(376291, "joint_color_code", lambda: joint_color_code)[_n_(376292, "color_code_num", lambda: color_code_num)]))
                    _l_(376295)
                else:
                    joint_color = _c_(376301, _n_(376296, "map", lambda: map), lambda x: _n_(376297, "x", lambda: x) + 35 * (_n_(376298, "joint_num", lambda: joint_num) % 4), _n_(376299, "joint_color_code", lambda: joint_color_code)[_n_(376300, "color_code_num", lambda: color_code_num)])
                    _l_(376302)

                _c_(376310, _a_(376305, _n_(376304, "cv2", lambda: cv2), "circle"), _n_(376306, "test_img", lambda: test_img), center=(_n_(376307, "joint_coord", lambda: joint_coord)[1], _n_(376308, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(376309, "joint_color", lambda: joint_color), thickness=-1)
                _l_(376311)
            else:
                if _n_(376312, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                    _l_(376329)

                    joint_color = _c_(376320, _n_(376313, "list", lambda: list), _c_(376319, _n_(376314, "map", lambda: map), lambda x: _n_(376315, "x", lambda: x) + 35 * (_n_(376316, "joint_num", lambda: joint_num) % 4), _n_(376317, "joint_color_code", lambda: joint_color_code)[_n_(376318, "color_code_num", lambda: color_code_num)]))
                    _l_(376321)
                else:
                    joint_color = _c_(376327, _n_(376322, "map", lambda: map), lambda x: _n_(376323, "x", lambda: x) + 35 * (_n_(376324, "joint_num", lambda: joint_num) % 4), _n_(376325, "joint_color_code", lambda: joint_color_code)[_n_(376326, "color_code_num", lambda: color_code_num)])
                    _l_(376328)

                _c_(376336, _a_(376331, _n_(376330, "cv2", lambda: cv2), "circle"), _n_(376332, "test_img", lambda: test_img), center=(_n_(376333, "joint_coord", lambda: joint_coord)[1], _n_(376334, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(376335, "joint_color", lambda: joint_color), thickness=-1)
                _l_(376337)
    else:
        for joint_num in _c_(376343, _n_(376340, "range", lambda: range), _a_(376342, _n_(376341, "FLAGS", lambda: FLAGS), "joints")):
            _l_(376418)

            joint_coord = _c_(376355, _a_(376345, _n_(376344, "np", lambda: np), "unravel_index"), _c_(376350, _a_(376347, _n_(376346, "np", lambda: np), "argmax"), _n_(376348, "last_heatmap", lambda: last_heatmap)[:, :, _n_(376349, "joint_num", lambda: joint_num)]),
                                           (_a_(376352, _n_(376351, "test_img", lambda: test_img), "shape")[0], _a_(376354, _n_(376353, "test_img", lambda: test_img), "shape")[1]))
            _l_(376356)
            _n_(376357, "joint_coord_set", lambda: joint_coord_set)[_n_(376358, "joint_num", lambda: joint_num), :] = [_n_(376359, "joint_coord", lambda: joint_coord)[0], _n_(376360, "joint_coord", lambda: joint_coord)[1]]
            _l_(376361)

            color_code_num = (_n_(376362, "joint_num", lambda: joint_num) // 4)
            _l_(376363)
            if _n_(376364, "joint_num", lambda: joint_num) in [0, 4, 8, 12, 16]:
                _l_(376417)

                if _n_(376365, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                    _l_(376382)

                    joint_color = _c_(376373, _n_(376366, "list", lambda: list), _c_(376372, _n_(376367, "map", lambda: map), lambda x: _n_(376368, "x", lambda: x) + 35 * (_n_(376369, "joint_num", lambda: joint_num) % 4), _n_(376370, "joint_color_code", lambda: joint_color_code)[_n_(376371, "color_code_num", lambda: color_code_num)]))
                    _l_(376374)
                else:
                    joint_color = _c_(376380, _n_(376375, "map", lambda: map), lambda x: _n_(376376, "x", lambda: x) + 35 * (_n_(376377, "joint_num", lambda: joint_num) % 4), _n_(376378, "joint_color_code", lambda: joint_color_code)[_n_(376379, "color_code_num", lambda: color_code_num)])
                    _l_(376381)

                _c_(376389, _a_(376384, _n_(376383, "cv2", lambda: cv2), "circle"), _n_(376385, "test_img", lambda: test_img), center=(_n_(376386, "joint_coord", lambda: joint_coord)[1], _n_(376387, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(376388, "joint_color", lambda: joint_color), thickness=-1)
                _l_(376390)
            else:
                if _n_(376391, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                    _l_(376408)

                    joint_color = _c_(376399, _n_(376392, "list", lambda: list), _c_(376398, _n_(376393, "map", lambda: map), lambda x: _n_(376394, "x", lambda: x) + 35 * (_n_(376395, "joint_num", lambda: joint_num) % 4), _n_(376396, "joint_color_code", lambda: joint_color_code)[_n_(376397, "color_code_num", lambda: color_code_num)]))
                    _l_(376400)
                else:
                    joint_color = _c_(376406, _n_(376401, "map", lambda: map), lambda x: _n_(376402, "x", lambda: x) + 35 * (_n_(376403, "joint_num", lambda: joint_num) % 4), _n_(376404, "joint_color_code", lambda: joint_color_code)[_n_(376405, "color_code_num", lambda: color_code_num)])
                    _l_(376407)

                _c_(376415, _a_(376410, _n_(376409, "cv2", lambda: cv2), "circle"), _n_(376411, "test_img", lambda: test_img), center=(_n_(376412, "joint_coord", lambda: joint_coord)[1], _n_(376413, "joint_coord", lambda: joint_coord)[0]), radius=3, color=_n_(376414, "joint_color", lambda: joint_color), thickness=-1)
                _l_(376416)
    _c_(376425, _n_(376420, "print", lambda: print), 'plot joint time %f' % (_c_(376423, _a_(376422, _n_(376421, "time", lambda: time), "time")) - _n_(376424, "t1", lambda: t1)))
    _l_(376426)

    t1 = _c_(376429, _a_(376428, _n_(376427, "time", lambda: time), "time"))
    _l_(376430)
    # Plot limb colors
    for limb_num in _c_(376435, _n_(376431, "range", lambda: range), _c_(376434, _n_(376432, "len", lambda: len), _n_(376433, "limbs", lambda: limbs))):
        _l_(376516)


        x1 = _n_(376436, "joint_coord_set", lambda: joint_coord_set)[_n_(376437, "limbs", lambda: limbs)[_n_(376438, "limb_num", lambda: limb_num)][0], 0]
        _l_(376439)
        y1 = _n_(376440, "joint_coord_set", lambda: joint_coord_set)[_n_(376441, "limbs", lambda: limbs)[_n_(376442, "limb_num", lambda: limb_num)][0], 1]
        _l_(376443)
        x2 = _n_(376444, "joint_coord_set", lambda: joint_coord_set)[_n_(376445, "limbs", lambda: limbs)[_n_(376446, "limb_num", lambda: limb_num)][1], 0]
        _l_(376447)
        y2 = _n_(376448, "joint_coord_set", lambda: joint_coord_set)[_n_(376449, "limbs", lambda: limbs)[_n_(376450, "limb_num", lambda: limb_num)][1], 1]
        _l_(376451)
        length = ((_n_(376452, "x1", lambda: x1) - _n_(376453, "x2", lambda: x2)) ** 2 + (_n_(376454, "y1", lambda: y1) - _n_(376455, "y2", lambda: y2)) ** 2) ** 0.5
        _l_(376456)
        if _n_(376457, "length", lambda: length) < 150 and _n_(376458, "length", lambda: length) > 5:
            _l_(376515)

            deg = _c_(376468, _a_(376460, _n_(376459, "math", lambda: math), "degrees"), _c_(376467, _a_(376462, _n_(376461, "math", lambda: math), "atan2"), _n_(376463, "x1", lambda: x1) - _n_(376464, "x2", lambda: x2), _n_(376465, "y1", lambda: y1) - _n_(376466, "y2", lambda: y2)))
            _l_(376469)
            polygon = _c_(376486, _a_(376471, _n_(376470, "cv2", lambda: cv2), "ellipse2Poly"), (_c_(376475, _n_(376472, "int", lambda: int), (_n_(376473, "y1", lambda: y1) + _n_(376474, "y2", lambda: y2)) / 2), _c_(376479, _n_(376476, "int", lambda: int), (_n_(376477, "x1", lambda: x1) + _n_(376478, "x2", lambda: x2)) / 2)),
                                       (_c_(376482, _n_(376480, "int", lambda: int), _n_(376481, "length", lambda: length) / 2), 3),
                                       _c_(376485, _n_(376483, "int", lambda: int), _n_(376484, "deg", lambda: deg)),
                                       0, 360, 1)
            _l_(376487)
            color_code_num = _n_(376488, "limb_num", lambda: limb_num) // 4
            _l_(376489)
            if _n_(376490, "PYTHON_VERSION", lambda: PYTHON_VERSION) == 3:
                _l_(376507)

                limb_color = _c_(376498, _n_(376491, "list", lambda: list), _c_(376497, _n_(376492, "map", lambda: map), lambda x: _n_(376493, "x", lambda: x) + 35 * (_n_(376494, "limb_num", lambda: limb_num) % 4), _n_(376495, "joint_color_code", lambda: joint_color_code)[_n_(376496, "color_code_num", lambda: color_code_num)]))
                _l_(376499)
            else:
                limb_color = _c_(376505, _n_(376500, "map", lambda: map), lambda x: _n_(376501, "x", lambda: x) + 35 * (_n_(376502, "limb_num", lambda: limb_num) % 4), _n_(376503, "joint_color_code", lambda: joint_color_code)[_n_(376504, "color_code_num", lambda: color_code_num)])
                _l_(376506)

            _c_(376513, _a_(376509, _n_(376508, "cv2", lambda: cv2), "fillConvexPoly"), _n_(376510, "test_img", lambda: test_img), _n_(376511, "polygon", lambda: polygon), color=_n_(376512, "limb_color", lambda: limb_color))
            _l_(376514)
    _c_(376522, _n_(376517, "print", lambda: print), 'plot limb time %f' % (_c_(376520, _a_(376519, _n_(376518, "time", lambda: time), "time")) - _n_(376521, "t1", lambda: t1)))
    _l_(376523)

    if _a_(376525, _n_(376524, "FLAGS", lambda: FLAGS), "DEMO_TYPE") == 'MULTI':
        _l_(376553)

        upper_img = _c_(376531, _a_(376527, _n_(376526, "np", lambda: np), "concatenate"), (_n_(376528, "demo_stage_heatmaps", lambda: demo_stage_heatmaps)[0], _n_(376529, "demo_stage_heatmaps", lambda: demo_stage_heatmaps)[1], _n_(376530, "demo_stage_heatmaps", lambda: demo_stage_heatmaps)[2]), axis=1)
        _l_(376532)
        lower_img = _c_(376541, _a_(376534, _n_(376533, "np", lambda: np), "concatenate"), (_n_(376535, "demo_stage_heatmaps", lambda: demo_stage_heatmaps)[3], _n_(376536, "demo_stage_heatmaps", lambda: demo_stage_heatmaps)[_c_(376539, _n_(376537, "len", lambda: len), _n_(376538, "stage_heatmap_np", lambda: stage_heatmap_np)) - 1], _n_(376540, "test_img", lambda: test_img)),
                                   axis=1)
        _l_(376542)
        demo_img = _c_(376547, _a_(376544, _n_(376543, "np", lambda: np), "concatenate"), (_n_(376545, "upper_img", lambda: upper_img), _n_(376546, "lower_img", lambda: lower_img)), axis=0)
        _l_(376548)
        aux = _n_(376549, "demo_img", lambda: demo_img)
        _l_(376550)
        return aux
    else:
        aux = _n_(376551, "test_img", lambda: test_img)
        _l_(376552)
        return aux


if _n_(376555, "__name__", lambda: __name__) == '__main__':
    _l_(376561)

    _c_(376559, _a_(376558, _a_(376557, _n_(376556, "tf", lambda: tf), "app"), "run"))
    _l_(376560)
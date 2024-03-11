# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57342515/error-with-opencv-and-tensorflow-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(378237)

except ImportError:
    pass
cap = _c_(378240, _a_(378239, _n_(378238, "cv2", lambda: cv2), "VideoCapture"), 0)
_l_(378241)

with _c_(378244, _a_(378243, _n_(378242, "detection_graph", lambda: detection_graph), "as_default")):
    _l_(378326)

    with _c_(378247, _a_(378246, _n_(378245, "tf", lambda: tf), "Session")) as sess:
        _l_(378254)

        # Get handles to input and output tensors
        ops = _c_(378252, _a_(378251, _c_(378250, _a_(378249, _n_(378248, "tf", lambda: tf), "get_default_graph")), "get_operations"))
        _l_(378253)
    all_tensor_names = {_a_(378256, _n_(378255, "output", lambda: output), "name") for op in _n_(378257, "ops", lambda: ops) for output in _a_(378259, _n_(378258, "op", lambda: op), "outputs")}
    _l_(378260)
    tensor_dict = {}
    _l_(378261)
    for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
        ]:
        _l_(378276)

        tensor_name = _n_(378262, "key", lambda: key) + ':0'
        _l_(378263)
        if _n_(378264, "tensor_name", lambda: tensor_name) in _n_(378265, "all_tensor_names", lambda: all_tensor_names):
            _l_(378275)

            _n_(378266, "tensor_dict", lambda: tensor_dict)[_n_(378267, "key", lambda: key)] = _c_(378273, _a_(378271, _c_(378270, _a_(378269, _n_(378268, "tf", lambda: tf), "get_default_graph")), "get_tensor_by_name"), _n_(378272, "tensor_name", lambda: tensor_name))
            _l_(378274)

    while True:
        _l_(378325)

        ret, image_np = _c_(378279, _a_(378278, _n_(378277, "cap", lambda: cap), "read"))
        _l_(378280)
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = _c_(378284, _a_(378282, _n_(378281, "np", lambda: np), "expand_dims"), _n_(378283, "image_np", lambda: image_np), axis=0)
        _l_(378285)
        # Actual detection.
        output_dict = _c_(378289, _n_(378286, "run_inference_for_single_image", lambda: run_inference_for_single_image), _n_(378287, "image_np_expanded", lambda: image_np_expanded), _n_(378288, "detection_graph", lambda: detection_graph))
        _l_(378290)
        # Visualization of the results of a detection.
        _c_(378301, _a_(378292, _n_(378291, "vis_util", lambda: vis_util), "visualize_boxes_and_labels_on_image_array"), _n_(378293, "image_np", lambda: image_np),
            _n_(378294, "output_dict", lambda: output_dict)['detection_boxes'],
            _n_(378295, "output_dict", lambda: output_dict)['detection_classes'],
            _n_(378296, "output_dict", lambda: output_dict)['detection_scores'],
            _n_(378297, "category_index", lambda: category_index),
            instance_masks=_c_(378300, _a_(378299, _n_(378298, "output_dict", lambda: output_dict), "get"), 'detection_masks'),
            use_normalized_coordinates=True,
            line_thickness=8)
        _l_(378302)
        _c_(378309, _a_(378304, _n_(378303, "cv2", lambda: cv2), "imshow"), 'object_detection',_c_(378308, _a_(378306, _n_(378305, "cv2", lambda: cv2), "resize"), _n_(378307, "image_np", lambda: image_np),(800,600)))
        _l_(378310)
        if _c_(378313, _a_(378312, _n_(378311, "cv2", lambda: cv2), "waitKey"), 25) & 0xff == _n_(378314, "ord", lambda: ord)==('q'):
            _l_(378324)

            _c_(378317, _a_(378316, _n_(378315, "cap", lambda: cap), "release"))
            _l_(378318)
            _c_(378321, _a_(378320, _n_(378319, "cv2", lambda: cv2), "destroyAllWindows"))
            _l_(378322)
            break
            _l_(378323)
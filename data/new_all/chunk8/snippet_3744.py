# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68691767/mediapipe-pose-estimation-typeerror-type-list-doesnt-define-round-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(594599)

except ImportError:
    pass
try:
    import mediapipe as mp
    _l_(594601)

except ImportError:
    pass
try:
    import numpy as np
    _l_(594603)

except ImportError:
    pass
try:
    import time
    _l_(594605)

except ImportError:
    pass
try:
    import pyautogui
    _l_(594607)

except ImportError:
    pass
try:
    import mouse
    _l_(594609)

except ImportError:
    pass

mp_drawing = _a_(594612, _a_(594611, _n_(594610, "mp", lambda: mp), "solutions"), "drawing_utils")
_l_(594613)
mp_pose = _a_(594616, _a_(594615, _n_(594614, "mp", lambda: mp), "solutions"), "pose")
_l_(594617)


# display screen resolution, get it from your OS settings
SCREEN_SIZEX = (1920)
_l_(594618)
SCREEN_SIZEY = (1080)
_l_(594619)
# define the codec
fourcc = _c_(594622, _a_(594621, _n_(594620, "cv2", lambda: cv2), "VideoWriter_fourcc"), *"XVID")
_l_(594623)
# create the video write object
out = _c_(594629, _a_(594625, _n_(594624, "cv2", lambda: cv2), "VideoWriter"), "output.avi", _n_(594626, "fourcc", lambda: fourcc), 20.0, (_n_(594627, "SCREEN_SIZEX", lambda: SCREEN_SIZEX), _n_(594628, "SCREEN_SIZEY", lambda: SCREEN_SIZEY)))
_l_(594630)

with _c_(594633, _a_(594632, _n_(594631, "mp_pose", lambda: mp_pose), "Pose"), min_detection_confidence=0.1, min_tracking_confidence=0.9) as pose:
    _l_(594784)

    while True:
        _l_(594775)

        # make a screenshot
        img = _c_(594636, _a_(594635, _n_(594634, "pyautogui", lambda: pyautogui), "screenshot"))
        _l_(594637)
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = _c_(594641, _a_(594639, _n_(594638, "np", lambda: np), "array"), _n_(594640, "img", lambda: img))
        _l_(594642)
        # convert colors from BGR to RGB
        frame = _c_(594648, _a_(594644, _n_(594643, "cv2", lambda: cv2), "cvtColor"), _n_(594645, "frame", lambda: frame), _a_(594647, _n_(594646, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
        _l_(594649)
        # Recolor image to RGB
        image = _c_(594655, _a_(594651, _n_(594650, "cv2", lambda: cv2), "cvtColor"), _n_(594652, "frame", lambda: frame), _a_(594654, _n_(594653, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
        _l_(594656)
        _a_(594658, _n_(594657, "image", lambda: image), "flags").writeable = False
        _l_(594659)

        # Make detection
        results = _c_(594663, _a_(594661, _n_(594660, "pose", lambda: pose), "process"), _n_(594662, "image", lambda: image))
        _l_(594664)

        # Recolor back to BGR
        _a_(594666, _n_(594665, "image", lambda: image), "flags").writeable = True
        _l_(594667)
        image = _c_(594673, _a_(594669, _n_(594668, "cv2", lambda: cv2), "cvtColor"), _n_(594670, "image", lambda: image), _a_(594672, _n_(594671, "cv2", lambda: cv2), "COLOR_RGB2BGR"))
        _l_(594674)


        landmarks = _a_(594677, _a_(594676, _n_(594675, "results", lambda: results), "pose_landmarks"), "landmark")
        _l_(594678)
        lndmark = _n_(594679, "landmarks", lambda: landmarks)[_a_(594683, _a_(594682, _a_(594681, _n_(594680, "mp_pose", lambda: mp_pose), "PoseLandmark"), "NOSE"), "value")]
        _l_(594684)
        x = [_a_(594690, _n_(594685, "landmarks", lambda: landmarks)[_a_(594689, _a_(594688, _a_(594687, _n_(594686, "mp_pose", lambda: mp_pose), "PoseLandmark"), "NOSE"), "value")], "x")]
        _l_(594691)
        y = [_a_(594697, _n_(594692, "landmarks", lambda: landmarks)[_a_(594696, _a_(594695, _a_(594694, _n_(594693, "mp_pose", lambda: mp_pose), "PoseLandmark"), "NOSE"), "value")], "y")]
        _l_(594698)

        #xx = ''.join(str(e) for e in x)
        #yy = ''.join(str(e) for e in y)

        #xx = [int(i) for i in xx]
        #yy = [int(i) for i in yy]

        test_coord = (_n_(594699, "x", lambda: x), _n_(594700, "y", lambda: y))
        _l_(594701)

        SCREEN_DIMENSIONS = (1920, 1080)
        _l_(594702)


        def to_pixel_coords(relative_coords):
            _l_(594714)

            aux = _c_(594712, _n_(594703, "tuple", lambda: tuple), (_c_(594707, _n_(594704, "round", lambda: round), _n_(594705, "coord", lambda: coord) * _n_(594706, "dimension", lambda: dimension)) for coord, dimension in _c_(594711, _n_(594708, "zip", lambda: zip), _n_(594709, "relative_coords", lambda: relative_coords), _n_(594710, "SCREEN_DIMENSIONS", lambda: SCREEN_DIMENSIONS))))
            _l_(594713)
            return aux


        _c_(594719, _n_(594715, "print", lambda: print), _c_(594718, _n_(594716, "to_pixel_coords", lambda: to_pixel_coords), _n_(594717, "test_coord", lambda: test_coord)))
        _l_(594720)




        #print(xxx)
        #print(yyy)

        #mouse.move(xxx, yyy)


        # Render detections
        _c_(594734, _a_(594722, _n_(594721, "mp_drawing", lambda: mp_drawing), "draw_landmarks"), _n_(594723, "image", lambda: image), _a_(594725, _n_(594724, "results", lambda: results), "pose_landmarks"), _a_(594727, _n_(594726, "mp_pose", lambda: mp_pose), "POSE_CONNECTIONS"),
                                _c_(594730, _a_(594729, _n_(594728, "mp_drawing", lambda: mp_drawing), "DrawingSpec"), color=(245,117,66), thickness=2, circle_radius=2),
                                _c_(594733, _a_(594732, _n_(594731, "mp_drawing", lambda: mp_drawing), "DrawingSpec"), color=(245,66,230), thickness=2, circle_radius=2)
                                 )
        _l_(594735)

        # write the frame
        _c_(594739, _a_(594737, _n_(594736, "out", lambda: out), "write"), _n_(594738, "frame", lambda: frame))
        _l_(594740)

        pTime = 0
        _l_(594741)

        cTime = _c_(594744, _a_(594743, _n_(594742, "time", lambda: time), "time"))
        _l_(594745)
        fps = 1 / (_n_(594746, "cTime", lambda: cTime) - _n_(594747, "pTime", lambda: pTime))
        _l_(594748)
        pTime = _n_(594749, "cTime", lambda: cTime)
        _l_(594750)
        _c_(594761, _a_(594752, _n_(594751, "cv2", lambda: cv2), "putText"), _n_(594753, "image", lambda: image), _c_(594758, _n_(594754, "str", lambda: str), _c_(594757, _n_(594755, "int", lambda: int), _n_(594756, "fps", lambda: fps))), (20, 50), _a_(594760, _n_(594759, "cv2", lambda: cv2), "FONT_HERSHEY_PLAIN"), 3,
        (255, 0, 0), 3)
        _l_(594762)



        _c_(594766, _a_(594764, _n_(594763, "cv2", lambda: cv2), "imshow"), 'Mediapipe Feed', _n_(594765, "image", lambda: image))
        _l_(594767)

        if _c_(594770, _a_(594769, _n_(594768, "cv2", lambda: cv2), "waitKey"), 10) & 0xFF == _c_(594772, _n_(594771, "ord", lambda: ord), 'q'):
            _l_(594774)

            break
            _l_(594773)

    _c_(594778, _a_(594777, _n_(594776, "out", lambda: out), "release"))
    _l_(594779)
    _c_(594782, _a_(594781, _n_(594780, "cv2", lambda: cv2), "destroyAllWindows"))
    _l_(594783)
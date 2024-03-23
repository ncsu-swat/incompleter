# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51116095/google-cloud-vision-api-attributeerror-webdetection-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def detect_web(path):
    _l_(544645)

    """Detects web annotations given an image."""
    client = _c_(544643, _a_(544642, _n_(544641, "vision", lambda: vision), "ImageAnnotatorClient"))
    _l_(544644)

with _c_(544649, _a_(544647, _n_(544646, "io", lambda: io), "open"), _n_(544648, "path", lambda: path), 'rb') as image_file:
    _l_(544654)

    content = _c_(544652, _a_(544651, _n_(544650, "image_file", lambda: image_file), "read"))
    _l_(544653)

image = _c_(544659, _a_(544657, _a_(544656, _n_(544655, "vision", lambda: vision), "types"), "Image"), content=_n_(544658, "content", lambda: content))
_l_(544660)

response = _c_(544664, _a_(544662, _n_(544661, "client", lambda: client), "web_detection"), image=_n_(544663, "image", lambda: image))
_l_(544665)
annotations = _a_(544667, _n_(544666, "response", lambda: response), "web_detection")
_l_(544668)

if _a_(544670, _n_(544669, "annotations", lambda: annotations), "best_guess_labels"):
    _l_(544681)

    for label in _a_(544672, _n_(544671, "annotations", lambda: annotations), "best_guess_labels"):
        _l_(544680)

        _c_(544678, _n_(544673, "print", lambda: print), _c_(544677, _a_(544674, '\nBest guess label: {}', "format"), _a_(544676, _n_(544675, "label", lambda: label), "label")))
        _l_(544679)

if _a_(544683, _n_(544682, "annotations", lambda: annotations), "pages_with_matching_images"):
    _l_(544747)

    _c_(544691, _n_(544684, "print", lambda: print), _c_(544690, _a_(544685, '\n{} Pages with matching images found:', "format"), _c_(544689, _n_(544686, "len", lambda: len), _a_(544688, _n_(544687, "annotations", lambda: annotations), "pages_with_matching_images"))))
    _l_(544692)

    for page in _a_(544694, _n_(544693, "annotations", lambda: annotations), "pages_with_matching_images"):
        _l_(544746)

        _c_(544700, _n_(544695, "print", lambda: print), _c_(544699, _a_(544696, '\n\tPage url   : {}', "format"), _a_(544698, _n_(544697, "page", lambda: page), "url")))
        _l_(544701)

        if _a_(544703, _n_(544702, "page", lambda: page), "full_matching_images"):
            _l_(544723)

            _c_(544711, _n_(544704, "print", lambda: print), _c_(544710, _a_(544705, '\t{} Full Matches found: ', "format"), _c_(544709, _n_(544706, "len", lambda: len), _a_(544708, _n_(544707, "page", lambda: page), "full_matching_images"))))
            _l_(544712)

            for image in _a_(544714, _n_(544713, "page", lambda: page), "full_matching_images"):
                _l_(544722)

                _c_(544720, _n_(544715, "print", lambda: print), _c_(544719, _a_(544716, '\t\tImage url  : {}', "format"), _a_(544718, _n_(544717, "image", lambda: image), "url")))
                _l_(544721)

        if _a_(544725, _n_(544724, "page", lambda: page), "partial_matching_images"):
            _l_(544745)

            _c_(544733, _n_(544726, "print", lambda: print), _c_(544732, _a_(544727, '\t{} Partial Matches found: ', "format"), _c_(544731, _n_(544728, "len", lambda: len), _a_(544730, _n_(544729, "page", lambda: page), "partial_matching_images"))))
            _l_(544734)

            for image in _a_(544736, _n_(544735, "page", lambda: page), "partial_matching_images"):
                _l_(544744)

                _c_(544742, _n_(544737, "print", lambda: print), _c_(544741, _a_(544738, '\t\tImage url  : {}', "format"), _a_(544740, _n_(544739, "image", lambda: image), "url")))
                _l_(544743)

if _a_(544749, _n_(544748, "annotations", lambda: annotations), "web_entities"):
    _l_(544776)

    _c_(544757, _n_(544750, "print", lambda: print), _c_(544756, _a_(544751, '\n{} Web entities found: ', "format"), _c_(544755, _n_(544752, "len", lambda: len), _a_(544754, _n_(544753, "annotations", lambda: annotations), "web_entities"))))
    _l_(544758)

    for entity in _a_(544760, _n_(544759, "annotations", lambda: annotations), "web_entities"):
        _l_(544775)

        _c_(544766, _n_(544761, "print", lambda: print), _c_(544765, _a_(544762, '\n\tScore      : {}', "format"), _a_(544764, _n_(544763, "entity", lambda: entity), "score")))
        _l_(544767)
        _c_(544773, _n_(544768, "print", lambda: print), _c_(544772, _a_(544769, u'\tDescription: {}', "format"), _a_(544771, _n_(544770, "entity", lambda: entity), "description")))
        _l_(544774)

if _a_(544778, _n_(544777, "annotations", lambda: annotations), "visually_similar_images"):
    _l_(544798)

    _c_(544786, _n_(544779, "print", lambda: print), _c_(544785, _a_(544780, '\n{} visually similar images found:\n', "format"), _c_(544784, _n_(544781, "len", lambda: len), _a_(544783, _n_(544782, "annotations", lambda: annotations), "visually_similar_images"))))
    _l_(544787)

    for image in _a_(544789, _n_(544788, "annotations", lambda: annotations), "visually_similar_images"):
        _l_(544797)

        _c_(544795, _n_(544790, "print", lambda: print), _c_(544794, _a_(544791, '\tImage url    : {}', "format"), _a_(544793, _n_(544792, "image", lambda: image), "url")))
        _l_(544796)
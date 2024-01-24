# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67562261/typeerror-a-bytes-like-object-is-required-not-str-what-do-i-change
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def convertAudioToByteArray(audio):
    _l_(574850)

    image_data = _c_(574846, _a_(574845, _c_(574844, _a_(574843, _c_(574842, _a_(574840, _n_(574839, "base64", lambda: base64), "b64encode"), _n_(574841, "audio", lambda: audio)), "decode"), 'utf-8'), "encode"), 'ascii')
    _l_(574847)
    aux = _n_(574848, "image_data", lambda: image_data)
    _l_(574849)
    return aux

converted_sound = _c_(574858, _n_(574851, "convertAudioToByteArray", lambda: convertAudioToByteArray), ("sounds" + _c_(574854, _a_(574853, _n_(574852, "device", lambda: device), "get_id")) + "/speech" + _c_(574857, _n_(574855, "str", lambda: str), _n_(574856, "count", lambda: count)) + ".mp3"))
_l_(574859)
payload_json = {'type': 'POLRES', 'img_name':_n_(574860, "data", lambda: data)['img_name'], 'audio': _n_(574861, "converted_sound", lambda: converted_sound), 'node_id': _c_(574864, _a_(574863, _n_(574862, "device", lambda: device), "get_id"))}
_l_(574865)
payload = _c_(574869, _a_(574867, _n_(574866, "json", lambda: json), "dumps"), _n_(574868, "payload_json", lambda: payload_json))
_l_(574870)
device_project_id = _a_(574872, _n_(574871, "args", lambda: args), "project_id")
_l_(574873)
device_registry_id = _a_(574875, _n_(574874, "args", lambda: args), "registry_id")
_l_(574876)
device_id = _n_(574877, "data", lambda: data)['dev_id']
_l_(574878)
device_region = _a_(574880, _n_(574879, "args", lambda: args), "cloud_region")
_l_(574881)
_c_(574885, _n_(574882, "print", lambda: print), "Publishing Polly results to device " + _n_(574883, "data", lambda: data)['dev_id'] + "for image " + _n_(574884, "data", lambda: data)['img_name'])
_l_(574886)
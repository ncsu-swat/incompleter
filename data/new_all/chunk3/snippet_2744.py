# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
footage_socket = _c_(543110, _a_(543107, _n_(543106, "context", lambda: context), "socket"), _a_(543109, _n_(543108, "zmq", lambda: zmq), "SUB") )
_l_(543111)
_c_(543114, _a_(543113, _n_(543112, "footage_socket", lambda: footage_socket), "bind"), 'tcp://0.0.0.0:5555')
_l_(543115)
_c_(543123, _a_(543117, _n_(543116, "footage_socket", lambda: footage_socket), "setsockopt_string"), _a_(543119, _n_(543118, "zmq", lambda: zmq), "SUBSCRIBE"), _c_(543122, _a_(543121, _n_(543120, "np", lambda: np), "unicode"), ''))
_l_(543124)
PUB_TARGET = 'tcp://192.168.56.103:9999'
_l_(543125)
while True:
   _l_(543191)

   frame  = _c_(543128, _a_(543127, _n_(543126, "footage_socket", lambda: footage_socket), "recv_string"))                         
   _l_(543129)                         
   source = _c_(543141, _a_(543131, _n_(543130, "cv2", lambda: cv2), "imdecode"), _c_(543140, _a_(543133, _n_(543132, "np", lambda: np), "fromstring"), _c_(543137, _a_(543135, _n_(543134, "base64", lambda: base64), "b64decode"), _n_(543136, "frame", lambda: frame) ), dtype = _a_(543139, _n_(543138, "np", lambda: np), "uint8")),1 )
   _l_(543142)
   frame  = _c_(543148, _a_(543147, _c_(543146, _a_(543144, _n_(543143, "cv2", lambda: cv2), "resize"), _n_(543145, "source", lambda: source),
                     (224,224)
                     ), "astype"), "float32" )
   _l_(543149)
   image = _c_(543152, _n_(543150, "img_to_array", lambda: img_to_array), _n_(543151, "source", lambda: source) )
   _l_(543153)
   image = _c_(543162, _a_(543155, _n_(543154, "image", lambda: image), "reshape"), ( 1,_a_(543157, _n_(543156, "image", lambda: image), "shape")[0],_a_(543159, _n_(543158, "image", lambda: image), "shape")[1], _a_(543161, _n_(543160, "image", lambda: image), "shape")[2]))
   _l_(543163)
   preds = _c_(543169, _a_(543165, _n_(543164, "model", lambda: model), "predict"), _c_(543168, _n_(543166, "preprocess_input", lambda: preprocess_input), _n_(543167, "image", lambda: image) ) )
   _l_(543170)
   ## connecting to server #######
   context1=_c_(543173, _a_(543172, _n_(543171, "zmq", lambda: zmq), "Context"))                          
   _l_(543174)                          
   footage_socket = _c_(543179, _a_(543176, _n_(543175, "context1", lambda: context1), "socket"), _a_(543178, _n_(543177, "zmq", lambda: zmq), "PUB") )      
   _l_(543180)      
   _c_(543184, _a_(543182, _n_(543181, "footage_socket", lambda: footage_socket), "connect"), _n_(543183, "PUB_TARGET", lambda: PUB_TARGET) )            
   _l_(543185)            
   _c_(543189, _a_(543187, _n_(543186, "footage_socket", lambda: footage_socket), "send"), _n_(543188, "preds", lambda: preds))
   _l_(543190)
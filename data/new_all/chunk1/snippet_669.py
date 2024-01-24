# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62995534/raspberry-pi-script-attributeerror-module-datetime-has-no-attribute-now
# combine the MQTT and RF receive codes 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import paho.mqtt.client as mqtt
   _l_(378415)

except ImportError:
   pass
try:
   import paho.mqtt.publish as publish
   _l_(378417)

except ImportError:
   pass
try:
   import picamera
   _l_(378419)

except ImportError:
   pass
try:
   import argparse
   _l_(378421)

except ImportError:
   pass
try:
   import signal
   _l_(378423)

except ImportError:
   pass
try:
   import sys
   _l_(378425)

except ImportError:
   pass
try:
   import time
   _l_(378427)

except ImportError:
   pass
try:
   import datetime
   _l_(378429)

except ImportError:
   pass
try:
   import logging
   _l_(378431)

except ImportError:
   pass
try:
   from rpi_rf import RFDevice
   _l_(378433)

except ImportError:
   pass
rfdevice = None 
_l_(378434) 
### camera 
camera = _c_(378437, _a_(378436, _n_(378435, "picamera", lambda: picamera), "PiCamera")) 
_l_(378438) 
_n_(378439, "camera", lambda: camera).vflip=True 
_l_(378440) 
#
def post_image():
   _l_(378485)

   _c_(378442, _n_(378441, "print", lambda: print), 'Taking photo') 
   _l_(378443) 
   _c_(378446, _a_(378445, _n_(378444, "camera", lambda: camera), "capture"), 'image.jpg') 
   _l_(378447) 
   file_name = 'image_' + _c_(378452, _n_(378448, "str", lambda: str), _c_(378451, _a_(378450, _n_(378449, "datetime", lambda: datetime), "now"))) + '.jpg' 
   _l_(378453) 
   _c_(378457, _a_(378455, _n_(378454, "camera", lambda: camera), "capture"), _n_(378456, "file_name", lambda: file_name))  # time-stamped image 
   _l_(378458)  # time-stamped image 
   with _c_(378460, _n_(378459, "open", lambda: open), 'image.jpg', "rb") as imageFile:
      _l_(378469)

      myFile = _c_(378463, _a_(378462, _n_(378461, "imageFile", lambda: imageFile), "read")) 
      _l_(378464) 
      data = _c_(378467, _n_(378465, "bytearray", lambda: bytearray), _n_(378466, "myFile", lambda: myFile)) 
      _l_(378468) 
   _c_(378475, _a_(378471, _n_(378470, "client", lambda: client), "publish"), 'dev/camera', _n_(378472, "data", lambda: data), _n_(378473, "mqttQos", lambda: mqttQos), _n_(378474, "mqttRetained", lambda: mqttRetained))  # 
   _l_(378476)  # 
   _c_(378479, _a_(378478, _n_(378477, "client", lambda: client), "publish"), 'dev/test', 'Capture!')  # to trigger an automation later
   _l_(378480)  # to trigger an automation later
   _c_(378483, _n_(378481, "print", lambda: print), _n_(378482, "file_name", lambda: file_name) + 'image published') 
   _l_(378484) 
#
### MQTT 
broker = '192.168.1.15' 
_l_(378486) 
topic ='dev/test' 
_l_(378487) 
mqttQos = 0 
_l_(378488) 
mqttRetained = False 
_l_(378489) 
#
def on_connect(client, userdata, flags, rc):
   _l_(378501)

   _c_(378494, _n_(378490, "print", lambda: print), "Connected with result code "+_c_(378493, _n_(378491, "str", lambda: str), _n_(378492, "rc", lambda: rc))) 
   _l_(378495) 
   _c_(378499, _a_(378497, _n_(378496, "client", lambda: client), "subscribe"), _n_(378498, "topic", lambda: topic)) 
   _l_(378500) 
# The callback for when a PUBLISH message is received from the server.
# 
def on_message(client, userdata, msg):
   _l_(378519)

   payload = _c_(378507, _n_(378502, "str", lambda: str), _c_(378506, _a_(378505, _a_(378504, _n_(378503, "msg", lambda: msg), "payload"), "decode"), 'ascii'))  # decode the binary string 
   _l_(378508)  # decode the binary string 
   _c_(378513, _n_(378509, "print", lambda: print), _a_(378511, _n_(378510, "msg", lambda: msg), "topic") + " " + _n_(378512, "payload", lambda: payload)) 
   _l_(378514) 
   _c_(378517, _n_(378515, "process_trigger", lambda: process_trigger), _n_(378516, "payload", lambda: payload)) 
   _l_(378518) 
#
def process_trigger(payload):
   _l_(378528)

   if _n_(378520, "payload", lambda: payload) == 'ON':
      _l_(378527)

      _c_(378522, _n_(378521, "print", lambda: print), 'ON triggered') 
      _l_(378523) 
      _c_(378525, _n_(378524, "post_image", lambda: post_image)) 
      _l_(378526) 
#
client = _c_(378531, _a_(378530, _n_(378529, "mqtt", lambda: mqtt), "Client")) 
_l_(378532) 
_n_(378533, "client", lambda: client).on_connect = _n_(378534, "on_connect", lambda: on_connect)    # call these on connect and on message 
_l_(378535)    # call these on connect and on message 
_n_(378536, "client", lambda: client).on_message = _n_(378537, "on_message", lambda: on_message) 
_l_(378538) 
_c_(378541, _a_(378540, _n_(378539, "client", lambda: client), "username_pw_set"), username='',password='')  # need this 
_l_(378542)  # need this 
_c_(378546, _a_(378544, _n_(378543, "client", lambda: client), "connect"), _n_(378545, "broker", lambda: broker)) 
_l_(378547) 
_c_(378550, _a_(378549, _n_(378548, "client", lambda: client), "loop_start"))    #  run in background and free up main thread 
_l_(378551)    #  run in background and free up main thread 
### RF 
#
def exithandler(signal, frame):
   _l_(378560)

   _c_(378554, _a_(378553, _n_(378552, "rfdevice", lambda: rfdevice), "cleanup")) 
   _l_(378555) 
   _c_(378558, _a_(378557, _n_(378556, "sys", lambda: sys), "exit"), 0) 
   _l_(378559) 
_c_(378565, _a_(378562, _n_(378561, "logging", lambda: logging), "basicConfig"), level=_a_(378564, _n_(378563, "logging", lambda: logging), "INFO"), datefmt='%Y-%m-%d %H:%M:%S', 
                   format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', ) 
_l_(378566) 
parser = _c_(378569, _a_(378568, _n_(378567, "argparse", lambda: argparse), "ArgumentParser"), description='Receives a decimal code via a 433/315MHz GPIO device') 
_l_(378570) 
_c_(378574, _a_(378572, _n_(378571, "parser", lambda: parser), "add_argument"), '-g', dest='gpio', type=_n_(378573, "int", lambda: int), default=27, 
                   help="GPIO pin (Default: 27)") 
_l_(378575) 
args = _c_(378578, _a_(378577, _n_(378576, "parser", lambda: parser), "parse_args")) 
_l_(378579) 
_c_(378585, _a_(378581, _n_(378580, "signal", lambda: signal), "signal"), _a_(378583, _n_(378582, "signal", lambda: signal), "SIGINT"), _n_(378584, "exithandler", lambda: exithandler)) 
_l_(378586) 
rfdevice = _c_(378590, _n_(378587, "RFDevice", lambda: RFDevice), _a_(378589, _n_(378588, "args", lambda: args), "gpio")) 
_l_(378591) 
_c_(378594, _a_(378593, _n_(378592, "rfdevice", lambda: rfdevice), "enable_rx")) 
_l_(378595) 
timestamp = None 
_l_(378596) 
_c_(378603, _a_(378598, _n_(378597, "logging", lambda: logging), "info"), "Listening for codes on GPIO " + _c_(378602, _n_(378599, "str", lambda: str), _a_(378601, _n_(378600, "args", lambda: args), "gpio"))) 
_l_(378604) 
code_of_interest = '384450' 
_l_(378605) 
#
while True:
   _l_(378637)

   if _a_(378607, _n_(378606, "rfdevice", lambda: rfdevice), "rx_code_timestamp") != _n_(378608, "timestamp", lambda: timestamp):
      _l_(378632)

      timestamp = _a_(378610, _n_(378609, "rfdevice", lambda: rfdevice), "rx_code_timestamp") 
      _l_(378611) 
      _c_(378617, _n_(378612, "print", lambda: print), _c_(378616, _n_(378613, "str", lambda: str), _a_(378615, _n_(378614, "rfdevice", lambda: rfdevice), "rx_code"))) 
      _l_(378618) 
      if _c_(378622, _n_(378619, "str", lambda: str), _a_(378621, _n_(378620, "rfdevice", lambda: rfdevice), "rx_code")) == _n_(378623, "code_of_interest", lambda: code_of_interest):
         _l_(378631)

         _c_(378625, _n_(378624, "post_image", lambda: post_image)) 
         _l_(378626) 
         _c_(378629, _a_(378628, _n_(378627, "time", lambda: time), "sleep"), 1)  # prevent registering multiple times
         _l_(378630)  # prevent registering multiple times
   _c_(378635, _a_(378634, _n_(378633, "time", lambda: time), "sleep"), 0.01) 
   _l_(378636) 
_c_(378640, _a_(378639, _n_(378638, "rfdevice", lambda: rfdevice), "cleanup")) 
_l_(378641) 
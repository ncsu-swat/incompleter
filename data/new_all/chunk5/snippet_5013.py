# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72986198/policy-attribute-error-when-sending-email-by-smtp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from email.encoders import encode_base64
   _l_(696890)

except ImportError:
   pass
try:
   from email.mime.base import MIMEBase
   _l_(696892)

except ImportError:
   pass
try:
   from PIL import Image
   _l_(696894)

except ImportError:
   pass
try:
   from io import BytesIO
   _l_(696896)

except ImportError:
   pass
try:
   from smtplib import SMTPException
   _l_(696898)

except ImportError:
   pass
try:
   from email.mime.text import MIMEText
   _l_(696900)

except ImportError:
   pass
try:
   from email.mime.multipart import MIMEMultipart
   _l_(696902)

except ImportError:
   pass
try:
   from smtplib import SMTP
   _l_(696904)

except ImportError:
   pass
try:
   import smtplib
   _l_(696906)

except ImportError:
   pass


msg = _c_(696908, _n_(696907, "MIMEMultipart", lambda: MIMEMultipart), "related")
_l_(696909)
_n_(696910, "msg", lambda: msg)['Subject'] = _n_(696911, "subject", lambda: subject) #time
_l_(696912) #time
_n_(696913, "msg", lambda: msg)['From'] = _n_(696914, "from_addr", lambda: from_addr)
_l_(696915)
_n_(696916, "msg", lambda: msg)['To'] = _n_(696917, "to_addr", lambda: to_addr)
_l_(696918)

html_output = "your html here"
_l_(696919)

_c_(696925, _a_(696921, _n_(696920, "msg", lambda: msg), "attach"), _c_(696924, _n_(696922, "MIMEText", lambda: MIMEText), _n_(696923, "html_output", lambda: html_output), "html"))
_l_(696926)

#plots is a dictionary of images

for image_name, image_location in _c_(696929, _a_(696928, _n_(696927, "plots", lambda: plots), "items")):
   _l_(696942)

   img = _c_(696935, _a_(696931, _n_(696930, "Image", lambda: Image), "open"), _c_(696934, _n_(696932, "BytesIO", lambda: BytesIO), _n_(696933, "image_location", lambda: image_location)))
   _l_(696936)
   _c_(696940, _a_(696938, _n_(696937, "msg", lambda: msg), "attach"), _n_(696939, "img", lambda: img))
   _l_(696941)
_c_(696953, _a_(696947, _c_(696946, _a_(696944, _n_(696943, "smtplib", lambda: smtplib), "SMTP"), _n_(696945, "host", lambda: host)), "sendmail"), _n_(696948, "from_addr", lambda: from_addr), _n_(696949, "to_addr", lambda: to_addr), _c_(696952, _a_(696951, _n_(696950, "msg", lambda: msg), "as_string")))
_l_(696954)
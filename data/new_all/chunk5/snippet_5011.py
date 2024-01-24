# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72986198/policy-attribute-error-when-sending-email-by-smtp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from email.encoders import encode_base64
   _l_(671788)

except ImportError:
   pass
try:
   from email.mime.base import MIMEBase
   _l_(671790)

except ImportError:
   pass
try:
   from PIL import Image
   _l_(671792)

except ImportError:
   pass
try:
   from io import BytesIO
   _l_(671794)

except ImportError:
   pass
try:
   from smtplib import SMTPException
   _l_(671796)

except ImportError:
   pass
try:
   from email.mime.text import MIMEText
   _l_(671798)

except ImportError:
   pass
try:
   from email.mime.multipart import MIMEMultipart
   _l_(671800)

except ImportError:
   pass
try:
   from smtplib import SMTP
   _l_(671802)

except ImportError:
   pass
try:
   import smtplib
   _l_(671804)

except ImportError:
   pass


msg = _c_(671806, _n_(671805, "MIMEMultipart", lambda: MIMEMultipart), "related")
_l_(671807)
_n_(671808, "msg", lambda: msg)['Subject'] = _n_(671809, "subject", lambda: subject) #time
_l_(671810) #time
_n_(671811, "msg", lambda: msg)['From'] = _n_(671812, "from_addr", lambda: from_addr)
_l_(671813)
_n_(671814, "msg", lambda: msg)['To'] = _n_(671815, "to_addr", lambda: to_addr)
_l_(671816)

html_output = "your html here"
_l_(671817)

_c_(671823, _a_(671819, _n_(671818, "msg", lambda: msg), "attach"), _c_(671822, _n_(671820, "MIMEText", lambda: MIMEText), _n_(671821, "html_output", lambda: html_output), "html"))
_l_(671824)

#plots is a dictionary of images

for image_name, image_location in _c_(671827, _a_(671826, _n_(671825, "plots", lambda: plots), "items")):
   _l_(671840)

   img = _c_(671833, _a_(671829, _n_(671828, "Image", lambda: Image), "open"), _c_(671832, _n_(671830, "BytesIO", lambda: BytesIO), _n_(671831, "image_location", lambda: image_location)))
   _l_(671834)
   _c_(671838, _a_(671836, _n_(671835, "msg", lambda: msg), "attach"), _n_(671837, "img", lambda: img))
   _l_(671839)
_c_(671851, _a_(671845, _c_(671844, _a_(671842, _n_(671841, "smtplib", lambda: smtplib), "SMTP"), _n_(671843, "host", lambda: host)), "sendmail"), _n_(671846, "from_addr", lambda: from_addr), _n_(671847, "to_addr", lambda: to_addr), _c_(671850, _a_(671849, _n_(671848, "msg", lambda: msg), "as_string")))
_l_(671852)
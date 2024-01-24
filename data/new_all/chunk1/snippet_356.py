# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57141694/why-encode-base64-give-me-typeerror-expected-bytes-like-object-not-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import smtplib
    _l_(410299)

except ImportError:
    pass
try:
    from email.mime.multipart import MIMEMultipart
    _l_(410301)

except ImportError:
    pass
try:
    from email.mime.base import MIMEBase
    _l_(410303)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(410305)

except ImportError:
    pass
try:
    from email.utils import COMMASPACE, formatdate
    _l_(410307)

except ImportError:
    pass
try:
    from email import encoders
    _l_(410309)

except ImportError:
    pass
try:
    import os,datetime
    _l_(410311)

except ImportError:
    pass

CRLF = "\r\n"
_l_(410312)
login = "my@email.com"
_l_(410313)
password = "mypassword"
_l_(410314)
attendees = ["attendees1@gmail.com", "attendees2@gmail.com","attendees3@gmail.com"]
_l_(410315)
organizer = "ORGANIZER;CN=organiser:mailto:first"+_n_(410316, "CRLF", lambda: CRLF)+" @ada-asia.com"
_l_(410317)
fro = "Fahim Maula <fahim.maula@ada-asia.com>"
_l_(410318)

ddtstart = _c_(410322, _a_(410321, _a_(410320, _n_(410319, "datetime", lambda: datetime), "datetime"), "now"))
_l_(410323)
dtoff = _c_(410326, _a_(410325, _n_(410324, "datetime", lambda: datetime), "timedelta"), days = 1)
_l_(410327)
dur = _c_(410330, _a_(410329, _n_(410328, "datetime", lambda: datetime), "timedelta"), hours = 1)
_l_(410331)
ddtstart = _n_(410332, "ddtstart", lambda: ddtstart) +_n_(410333, "dtoff", lambda: dtoff)
_l_(410334)
dtend = _n_(410335, "ddtstart", lambda: ddtstart) + _n_(410336, "dur", lambda: dur)
_l_(410337)
dtstamp = _c_(410343, _a_(410342, _c_(410341, _a_(410340, _a_(410339, _n_(410338, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%Y%m%dT%H%M%SZ")
_l_(410344)
dtstart = _c_(410347, _a_(410346, _n_(410345, "ddtstart", lambda: ddtstart), "strftime"), "%Y%m%dT%H%M%SZ")
_l_(410348)
dtend = _c_(410351, _a_(410350, _n_(410349, "dtend", lambda: dtend), "strftime"), "%Y%m%dT%H%M%SZ")
_l_(410352)

description = "DESCRIPTION: test invitation from pyICSParser"+_n_(410353, "CRLF", lambda: CRLF)
_l_(410354)
attendee = ""
_l_(410355)
for att in _n_(410356, "attendees", lambda: attendees):
    _l_(410363)

    attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+_n_(410357, "CRLF", lambda: CRLF)+" ;CN="+_n_(410358, "att", lambda: att)+";X-NUM-GUESTS=0:"+_n_(410359, "CRLF", lambda: CRLF)+" mailto:"+_n_(410360, "att", lambda: att)+_n_(410361, "CRLF", lambda: CRLF)
    _l_(410362)
ical = "BEGIN:VCALENDAR"+_n_(410364, "CRLF", lambda: CRLF)+"PRODID:pyICSParser"+_n_(410365, "CRLF", lambda: CRLF)+"VERSION:2.0"+_n_(410366, "CRLF", lambda: CRLF)+"CALSCALE:GREGORIAN"+_n_(410367, "CRLF", lambda: CRLF)
_l_(410368)
ical+="METHOD:REQUEST"+_n_(410369, "CRLF", lambda: CRLF)+"BEGIN:VEVENT"+_n_(410370, "CRLF", lambda: CRLF)+"DTSTART:"+_n_(410371, "dtstart", lambda: dtstart)+_n_(410372, "CRLF", lambda: CRLF)+"DTEND:"+_n_(410373, "dtend", lambda: dtend)+_n_(410374, "CRLF", lambda: CRLF)+"DTSTAMP:"+_n_(410375, "dtstamp", lambda: dtstamp)+_n_(410376, "CRLF", lambda: CRLF)+_n_(410377, "organizer", lambda: organizer)+_n_(410378, "CRLF", lambda: CRLF)
_l_(410379)
ical+= "UID:FIXMEUID"+_n_(410380, "dtstamp", lambda: dtstamp)+_n_(410381, "CRLF", lambda: CRLF)
_l_(410382)
ical+= _n_(410383, "attendee", lambda: attendee)+"CREATED:"+_n_(410384, "dtstamp", lambda: dtstamp)+_n_(410385, "CRLF", lambda: CRLF)+_n_(410386, "description", lambda: description)+"LAST-MODIFIED:"+_n_(410387, "dtstamp", lambda: dtstamp)+_n_(410388, "CRLF", lambda: CRLF)+"LOCATION:"+_n_(410389, "CRLF", lambda: CRLF)+"SEQUENCE:0"+_n_(410390, "CRLF", lambda: CRLF)+"STATUS:CONFIRMED"+_n_(410391, "CRLF", lambda: CRLF)
_l_(410392)
ical+= "SUMMARY:test "+_c_(410395, _a_(410394, _n_(410393, "ddtstart", lambda: ddtstart), "strftime"), "%Y%m%d @ %H:%M")+_n_(410396, "CRLF", lambda: CRLF)+"TRANSP:OPAQUE"+_n_(410397, "CRLF", lambda: CRLF)+"END:VEVENT"+_n_(410398, "CRLF", lambda: CRLF)+"END:VCALENDAR"+_n_(410399, "CRLF", lambda: CRLF)
_l_(410400)

eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
_l_(410401)
eml_body_bin = "This is the email body in binary - two steps"
_l_(410402)
msg = _c_(410404, _n_(410403, "MIMEMultipart", lambda: MIMEMultipart), 'mixed')
_l_(410405)
_n_(410406, "msg", lambda: msg)['Reply-To']=_n_(410407, "fro", lambda: fro)
_l_(410408)
_n_(410409, "msg", lambda: msg)['Date'] = _c_(410411, _n_(410410, "formatdate", lambda: formatdate), localtime=True)
_l_(410412)
_n_(410413, "msg", lambda: msg)['Subject'] = "pyICSParser invite"+_n_(410414, "dtstart", lambda: dtstart)
_l_(410415)
_n_(410416, "msg", lambda: msg)['From'] = _n_(410417, "fro", lambda: fro)
_l_(410418)
_n_(410419, "msg", lambda: msg)['To'] = _c_(410422, _a_(410420, ",", "join"), _n_(410421, "attendees", lambda: attendees))
_l_(410423)

part_email = _c_(410426, _n_(410424, "MIMEText", lambda: MIMEText), _n_(410425, "eml_body", lambda: eml_body),"html")
_l_(410427)
part_cal = _c_(410430, _n_(410428, "MIMEText", lambda: MIMEText), _n_(410429, "ical", lambda: ical),'calendar;method=REQUEST')
_l_(410431)

msgAlternative = _c_(410433, _n_(410432, "MIMEMultipart", lambda: MIMEMultipart), 'alternative')
_l_(410434)
_c_(410438, _a_(410436, _n_(410435, "msg", lambda: msg), "attach"), _n_(410437, "msgAlternative", lambda: msgAlternative))
_l_(410439)

ical_atch = _c_(410441, _n_(410440, "MIMEBase", lambda: MIMEBase), 'application/ics',' ;name="%s"'%("invite.ics"))
_l_(410442)
_c_(410446, _a_(410444, _n_(410443, "ical_atch", lambda: ical_atch), "set_payload"), _n_(410445, "ical", lambda: ical))
_l_(410447)
_c_(410451, _a_(410449, _n_(410448, "encoders", lambda: encoders), "encode_base64"), _n_(410450, "ical_atch", lambda: ical_atch))
_l_(410452)
_c_(410455, _a_(410454, _n_(410453, "ical_atch", lambda: ical_atch), "add_header"), 'Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))
_l_(410456)

eml_atch = _c_(410458, _n_(410457, "MIMEBase", lambda: MIMEBase), 'text/plain','')
_l_(410459)
_c_(410463, _a_(410461, _n_(410460, "encoders", lambda: encoders), "encode_base64"), _n_(410462, "eml_atch", lambda: eml_atch))
_l_(410464)
_c_(410467, _a_(410466, _n_(410465, "eml_atch", lambda: eml_atch), "add_header"), 'Content-Transfer-Encoding', "")
_l_(410468)

_c_(410472, _a_(410470, _n_(410469, "msgAlternative", lambda: msgAlternative), "attach"), _n_(410471, "part_email", lambda: part_email))
_l_(410473)
_c_(410477, _a_(410475, _n_(410474, "msgAlternative", lambda: msgAlternative), "attach"), _n_(410476, "part_cal", lambda: part_cal))
_l_(410478)

mailServer = _c_(410481, _a_(410480, _n_(410479, "smtplib", lambda: smtplib), "SMTP"), 'smtp.gmail.com', 587)
_l_(410482)
_c_(410485, _a_(410484, _n_(410483, "mailServer", lambda: mailServer), "ehlo"))
_l_(410486)
_c_(410489, _a_(410488, _n_(410487, "mailServer", lambda: mailServer), "starttls"))
_l_(410490)
_c_(410493, _a_(410492, _n_(410491, "mailServer", lambda: mailServer), "ehlo"))
_l_(410494)
_c_(410499, _a_(410496, _n_(410495, "mailServer", lambda: mailServer), "login"), _n_(410497, "login", lambda: login), _n_(410498, "password", lambda: password))
_l_(410500)
_c_(410508, _a_(410502, _n_(410501, "mailServer", lambda: mailServer), "sendmail"), _n_(410503, "fro", lambda: fro), _n_(410504, "attendees", lambda: attendees), _c_(410507, _a_(410506, _n_(410505, "msg", lambda: msg), "as_string")))
_l_(410509)
_c_(410512, _a_(410511, _n_(410510, "mailServer", lambda: mailServer), "close"))
_l_(410513)
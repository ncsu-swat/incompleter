# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58803820/unable-to-attach-excel-file-to-email-using-python-typeerror-expected-bytes-li
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(381931)

except ImportError:
    pass
try:
    import xlsxwriter
    _l_(381933)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(381935)

except ImportError:
    pass
try:
    from email.mime.application import MIMEApplication
    _l_(381937)

except ImportError:
    pass
try:
    from email.mime.multipart import MIMEMultipart
    _l_(381939)

except ImportError:
    pass


def lambda_handler(event, context):
    _l_(382001)

    client = _c_(381943, _a_(381941, _n_(381940, "boto3", lambda: boto3), "client"), 'ses',region_name=_n_(381942, "AWS_REGION", lambda: AWS_REGION))
    _l_(381944)
    sender = "xxx@gmail.com"
    _l_(381945)
    to = "aaa@gmail.com"
    _l_(381946)
    workbook = _c_(381949, _a_(381948, _n_(381947, "xlsxwriter", lambda: xlsxwriter), "Workbook"), 'abc.xlsx') 
    _l_(381950) 
    worksheet = _c_(381953, _a_(381952, _n_(381951, "workbook", lambda: workbook), "add_worksheet")) 
    _l_(381954) 
    _c_(381957, _a_(381956, _n_(381955, "worksheet", lambda: worksheet), "write"), 'A1', 'Hello..')
    _l_(381958)
    #send email with attachment
    msg = _c_(381960, _n_(381959, "MIMEMultipart", lambda: MIMEMultipart))
    _l_(381961)
    _n_(381962, "msg", lambda: msg)['Subject'] = 'Test Email'
    _l_(381963)
    _n_(381964, "msg", lambda: msg)['From'] = _n_(381965, "sender", lambda: sender)
    _l_(381966)
    _n_(381967, "msg", lambda: msg)['To'] = _n_(381968, "to", lambda: to)
    _l_(381969)
    body_text = _c_(381972, _n_(381970, "MIMEText", lambda: MIMEText), _n_(381971, "BODY_TEXT", lambda: BODY_TEXT), "html")
    _l_(381973)
    attachment = _c_(381976, _n_(381974, "MIMEApplication", lambda: MIMEApplication), _n_(381975, "workbook", lambda: workbook))
    _l_(381977)
    _c_(381980, _a_(381979, _n_(381978, "attachment", lambda: attachment), "add_header"), 'Content-Disposition', 'attachment', filename='Expenses01.xlsx')
    _l_(381981)
    _c_(381985, _a_(381983, _n_(381982, "msg", lambda: msg), "attach"), _n_(381984, "attachment", lambda: attachment))
    _l_(381986)
    _c_(381990, _a_(381988, _n_(381987, "msg", lambda: msg), "attach"), _n_(381989, "body_text", lambda: body_text))
    _l_(381991)
    response = _c_(381999, _a_(381993, _n_(381992, "client", lambda: client), "send_raw_email"), Source=_n_(381994, "sender", lambda: sender),
        Destinations=[_n_(381995, "to", lambda: to)],
        RawMessage={"Data": _c_(381998, _a_(381997, _n_(381996, "msg", lambda: msg), "as_string"))}

    )
    _l_(382000)
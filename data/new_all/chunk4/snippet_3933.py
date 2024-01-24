# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(593893)

except ImportError:
    pass
try:
    import time
    _l_(593895)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(593897)

except ImportError:
    pass
try:
    import SendEmail
    _l_(593899)

except ImportError:
    pass

# Main Screen
root = _c_(593902, _a_(593901, _n_(593900, "tk", lambda: tk), "Tk"))
_l_(593903)
_c_(593906, _a_(593905, _n_(593904, "root", lambda: root), "resizable"), False, False)
_l_(593907)
_c_(593910, _a_(593909, _n_(593908, "root", lambda: root), "title"), 'Mail Sender')
_l_(593911)

# Icon
icon = _c_(593914, _a_(593913, _n_(593912, "tk", lambda: tk), "PhotoImage"), file='icon.png')
_l_(593915)
_c_(593919, _a_(593917, _n_(593916, "root", lambda: root), "iconphoto"), False, _n_(593918, "icon", lambda: icon))
_l_(593920)

# Canvas
canvas = _c_(593924, _a_(593922, _n_(593921, "tk", lambda: tk), "Canvas"), _n_(593923, "root", lambda: root), height=600, width=700)
_l_(593925)
_c_(593928, _a_(593927, _n_(593926, "canvas", lambda: canvas), "pack"))
_l_(593929)

# title
titleFrame = _c_(593933, _a_(593931, _n_(593930, "tk", lambda: tk), "Frame"), _n_(593932, "root", lambda: root))
_l_(593934)
_c_(593937, _a_(593936, _n_(593935, "titleFrame", lambda: titleFrame), "place"), relx=0.5, rely=0.025, relwidth=0.75, relheight=0.1, anchor='n')
_l_(593938)

title = _c_(593942, _a_(593940, _n_(593939, "tk", lambda: tk), "Label"), _n_(593941, "titleFrame", lambda: titleFrame), text="Mail Sender", font=('Calibri', 20))
_l_(593943)
_c_(593946, _a_(593945, _n_(593944, "title", lambda: title), "pack"))
_l_(593947)

# Main frame
mainframe = _c_(593951, _a_(593949, _n_(593948, "tk", lambda: tk), "Frame"), _n_(593950, "root", lambda: root), bg='#80c1ff', bd=10)
_l_(593952)
_c_(593955, _a_(593954, _n_(593953, "mainframe", lambda: mainframe), "place"), relx=0.5, rely=0.15, relwidth=1, relheight=0.85, anchor='n')
_l_(593956)

# Email
email = _c_(593960, _a_(593958, _n_(593957, "tk", lambda: tk), "Label"), _n_(593959, "mainframe", lambda: mainframe), text="Enter Email:", font=('Calibri', 15))
_l_(593961)
_c_(593964, _a_(593963, _n_(593962, "email", lambda: email), "place"), y=2.5)
_l_(593965)

email_str = _c_(593968, _a_(593967, _n_(593966, "tk", lambda: tk), "StringVar"))
_l_(593969)

emailEntry = _c_(593974, _a_(593971, _n_(593970, "tk", lambda: tk), "Entry"), _n_(593972, "mainframe", lambda: mainframe), textvariable=_n_(593973, "email_str", lambda: email_str), font=('Calibri', 15))
_l_(593975)
_c_(593978, _a_(593977, _n_(593976, "emailEntry", lambda: emailEntry), "place"), y=35, width=300)
_l_(593979)

# password
password = _c_(593983, _a_(593981, _n_(593980, "tk", lambda: tk), "Label"), _n_(593982, "mainframe", lambda: mainframe), text="Enter Password:", font=('Calibri', 15))
_l_(593984)
_c_(593987, _a_(593986, _n_(593985, "password", lambda: password), "place"), y=80)
_l_(593988)

password_str = _c_(593991, _a_(593990, _n_(593989, "tk", lambda: tk), "StringVar"))
_l_(593992)

passwordEntry = _c_(593997, _a_(593994, _n_(593993, "tk", lambda: tk), "Entry"), _n_(593995, "mainframe", lambda: mainframe), textvariable=_n_(593996, "password_str", lambda: password_str), show="\u2022", font=('Calibri', 15))
_l_(593998)
_c_(594001, _a_(594000, _n_(593999, "passwordEntry", lambda: passwordEntry), "place"), y=115, width=300)
_l_(594002)

# receiver
receiver = _c_(594006, _a_(594004, _n_(594003, "tk", lambda: tk), "Label"), _n_(594005, "mainframe", lambda: mainframe), text="Enter Receiver Email:", font=('Calibri', 15))
_l_(594007)
_c_(594010, _a_(594009, _n_(594008, "receiver", lambda: receiver), "place"), y=150)
_l_(594011)

receiver_str = _c_(594014, _a_(594013, _n_(594012, "tk", lambda: tk), "StringVar"))
_l_(594015)

receiverEntry = _c_(594020, _a_(594017, _n_(594016, "tk", lambda: tk), "Entry"), _n_(594018, "mainframe", lambda: mainframe), textvariable=_n_(594019, "receiver_str", lambda: receiver_str), font=('Calibri', 15))
_l_(594021)
_c_(594024, _a_(594023, _n_(594022, "receiverEntry", lambda: receiverEntry), "place"), y=185, width=300)
_l_(594025)

# subject
subject = _c_(594029, _a_(594027, _n_(594026, "tk", lambda: tk), "Label"), _n_(594028, "mainframe", lambda: mainframe), text="Enter Subject:", font=('Calibri', 15))
_l_(594030)
_c_(594033, _a_(594032, _n_(594031, "subject", lambda: subject), "place"), y=220)
_l_(594034)

subject_str = _c_(594037, _a_(594036, _n_(594035, "tk", lambda: tk), "StringVar"))
_l_(594038)

subjectEntry = _c_(594043, _a_(594040, _n_(594039, "tk", lambda: tk), "Entry"), _n_(594041, "mainframe", lambda: mainframe), textvariable=_n_(594042, "subject_str", lambda: subject_str), font=('Calibri', 15))
_l_(594044)
_c_(594047, _a_(594046, _n_(594045, "subjectEntry", lambda: subjectEntry), "place"), y=255, width=300)
_l_(594048)

# body
body = _c_(594052, _a_(594050, _n_(594049, "tk", lambda: tk), "Label"), _n_(594051, "mainframe", lambda: mainframe), text="Enter Body:", font=('Calibri', 15))
_l_(594053)
_c_(594056, _a_(594055, _n_(594054, "body", lambda: body), "place"), x=500, y=2.5)
_l_(594057)

body_str = _c_(594060, _a_(594059, _n_(594058, "tk", lambda: tk), "StringVar"))
_l_(594061)

bodyEntry = _c_(594065, _a_(594063, _n_(594062, "tk", lambda: tk), "Text"), _n_(594064, "mainframe", lambda: mainframe))
_l_(594066)
_c_(594069, _a_(594068, _n_(594067, "bodyEntry", lambda: bodyEntry), "place"), x=380, y=35, width=300)
_l_(594070)

# notification
notif = _c_(594074, _a_(594072, _n_(594071, "tk", lambda: tk), "Label"), _n_(594073, "mainframe", lambda: mainframe), bg='#80c1ff', font=('Calibri', 15))
_l_(594075)
_c_(594078, _a_(594077, _n_(594076, "notif", lambda: notif), "place"), x=250, y=450)
_l_(594079)

# attachments array
attachments = []
_l_(594080)


# add attacments function
def add_attachments():
    _l_(594111)

    filename = _c_(594083, _a_(594082, _n_(594081, "filedialog", lambda: filedialog), "askopenfilename"), initialdir='C:/', title="Select a file to attach to the email")
    _l_(594084)
    _c_(594088, _a_(594086, _n_(594085, "attachments", lambda: attachments), "append"), _n_(594087, "filename", lambda: filename))
    _l_(594089)

    _c_(594097, _a_(594091, _n_(594090, "notif", lambda: notif), "config"), text="Attached " + _c_(594096, _n_(594092, "str", lambda: str), _c_(594095, _n_(594093, "len", lambda: len), _n_(594094, "attachments", lambda: attachments))) + " file", fg="green")
    _l_(594098)

    _c_(594101, _a_(594100, _n_(594099, "root", lambda: root), "update"))
    _l_(594102)
    _c_(594105, _a_(594104, _n_(594103, "time", lambda: time), "sleep"), 2.5)
    _l_(594106)

    _c_(594109, _a_(594108, _n_(594107, "notif", lambda: notif), "config"), text="")
    _l_(594110)


def reset_entries():
    _l_(594148)

    _c_(594114, _a_(594113, _n_(594112, "emailEntry", lambda: emailEntry), "delete"), 0, 'end')
    _l_(594115)
    _c_(594118, _a_(594117, _n_(594116, "passwordEntry", lambda: passwordEntry), "delete"), 0, 'end')
    _l_(594119)
    _c_(594122, _a_(594121, _n_(594120, "receiverEntry", lambda: receiverEntry), "delete"), 0, 'end')
    _l_(594123)
    _c_(594126, _a_(594125, _n_(594124, "subjectEntry", lambda: subjectEntry), "delete"), 0, 'end')
    _l_(594127)
    _c_(594130, _a_(594129, _n_(594128, "bodyEntry", lambda: bodyEntry), "delete"), "1.0", "end-1c")
    _l_(594131)

    _c_(594134, _a_(594133, _n_(594132, "notif", lambda: notif), "config"), text="Entries were reset", fg="green")
    _l_(594135)

    _c_(594138, _a_(594137, _n_(594136, "root", lambda: root), "update"))
    _l_(594139)
    _c_(594142, _a_(594141, _n_(594140, "time", lambda: time), "sleep"), 2.5)
    _l_(594143)

    _c_(594146, _a_(594145, _n_(594144, "notif", lambda: notif), "config"), text="")
    _l_(594147)


# send button
send = _c_(594155, _a_(594150, _n_(594149, "tk", lambda: tk), "Button"), _n_(594151, "mainframe", lambda: mainframe), text="Send Email", font=('Calibri', 15), command=lambda: _c_(594154, _a_(594153, _n_(594152, "SendEmail", lambda: SendEmail), "send_email")))
_l_(594156)
_c_(594159, _a_(594158, _n_(594157, "send", lambda: send), "place"), y=310, width=150)
_l_(594160)

# reset button
reset = _c_(594167, _a_(594162, _n_(594161, "tk", lambda: tk), "Button"), _n_(594163, "mainframe", lambda: mainframe), text="Reset", font=('Calibri', 15), command=lambda: _c_(594166, _a_(594165, _n_(594164, "ResetEntries", lambda: ResetEntries), "reset_entries")))
_l_(594168)
_c_(594171, _a_(594170, _n_(594169, "reset", lambda: reset), "place"), x=220, y=310, width=150)
_l_(594172)

# attachments button
attachment = _c_(594178, _a_(594174, _n_(594173, "tk", lambda: tk), "Button"), _n_(594175, "mainframe", lambda: mainframe), text="Add Attachments", font=('Calibri', 15), command=lambda: _c_(594177, _n_(594176, "add_attachments", lambda: add_attachments)))
_l_(594179)
_c_(594182, _a_(594181, _n_(594180, "attachment", lambda: attachment), "place"), x=90, y=365, width=200)
_l_(594183)

# Main loop
_c_(594186, _a_(594185, _n_(594184, "root", lambda: root), "mainloop"))
_l_(594187)
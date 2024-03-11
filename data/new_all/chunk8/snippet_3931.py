# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(637827)

except ImportError:
    pass
try:
    import time
    _l_(637829)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(637831)

except ImportError:
    pass
try:
    import SendEmail
    _l_(637833)

except ImportError:
    pass

# Main Screen
root = _c_(637836, _a_(637835, _n_(637834, "tk", lambda: tk), "Tk"))
_l_(637837)
_c_(637840, _a_(637839, _n_(637838, "root", lambda: root), "resizable"), False, False)
_l_(637841)
_c_(637844, _a_(637843, _n_(637842, "root", lambda: root), "title"), 'Mail Sender')
_l_(637845)

# Icon
icon = _c_(637848, _a_(637847, _n_(637846, "tk", lambda: tk), "PhotoImage"), file='icon.png')
_l_(637849)
_c_(637853, _a_(637851, _n_(637850, "root", lambda: root), "iconphoto"), False, _n_(637852, "icon", lambda: icon))
_l_(637854)

# Canvas
canvas = _c_(637858, _a_(637856, _n_(637855, "tk", lambda: tk), "Canvas"), _n_(637857, "root", lambda: root), height=600, width=700)
_l_(637859)
_c_(637862, _a_(637861, _n_(637860, "canvas", lambda: canvas), "pack"))
_l_(637863)

# title
titleFrame = _c_(637867, _a_(637865, _n_(637864, "tk", lambda: tk), "Frame"), _n_(637866, "root", lambda: root))
_l_(637868)
_c_(637871, _a_(637870, _n_(637869, "titleFrame", lambda: titleFrame), "place"), relx=0.5, rely=0.025, relwidth=0.75, relheight=0.1, anchor='n')
_l_(637872)

title = _c_(637876, _a_(637874, _n_(637873, "tk", lambda: tk), "Label"), _n_(637875, "titleFrame", lambda: titleFrame), text="Mail Sender", font=('Calibri', 20))
_l_(637877)
_c_(637880, _a_(637879, _n_(637878, "title", lambda: title), "pack"))
_l_(637881)

# Main frame
mainframe = _c_(637885, _a_(637883, _n_(637882, "tk", lambda: tk), "Frame"), _n_(637884, "root", lambda: root), bg='#80c1ff', bd=10)
_l_(637886)
_c_(637889, _a_(637888, _n_(637887, "mainframe", lambda: mainframe), "place"), relx=0.5, rely=0.15, relwidth=1, relheight=0.85, anchor='n')
_l_(637890)

# Email
email = _c_(637894, _a_(637892, _n_(637891, "tk", lambda: tk), "Label"), _n_(637893, "mainframe", lambda: mainframe), text="Enter Email:", font=('Calibri', 15))
_l_(637895)
_c_(637898, _a_(637897, _n_(637896, "email", lambda: email), "place"), y=2.5)
_l_(637899)

email_str = _c_(637902, _a_(637901, _n_(637900, "tk", lambda: tk), "StringVar"))
_l_(637903)

emailEntry = _c_(637908, _a_(637905, _n_(637904, "tk", lambda: tk), "Entry"), _n_(637906, "mainframe", lambda: mainframe), textvariable=_n_(637907, "email_str", lambda: email_str), font=('Calibri', 15))
_l_(637909)
_c_(637912, _a_(637911, _n_(637910, "emailEntry", lambda: emailEntry), "place"), y=35, width=300)
_l_(637913)

# password
password = _c_(637917, _a_(637915, _n_(637914, "tk", lambda: tk), "Label"), _n_(637916, "mainframe", lambda: mainframe), text="Enter Password:", font=('Calibri', 15))
_l_(637918)
_c_(637921, _a_(637920, _n_(637919, "password", lambda: password), "place"), y=80)
_l_(637922)

password_str = _c_(637925, _a_(637924, _n_(637923, "tk", lambda: tk), "StringVar"))
_l_(637926)

passwordEntry = _c_(637931, _a_(637928, _n_(637927, "tk", lambda: tk), "Entry"), _n_(637929, "mainframe", lambda: mainframe), textvariable=_n_(637930, "password_str", lambda: password_str), show="\u2022", font=('Calibri', 15))
_l_(637932)
_c_(637935, _a_(637934, _n_(637933, "passwordEntry", lambda: passwordEntry), "place"), y=115, width=300)
_l_(637936)

# receiver
receiver = _c_(637940, _a_(637938, _n_(637937, "tk", lambda: tk), "Label"), _n_(637939, "mainframe", lambda: mainframe), text="Enter Receiver Email:", font=('Calibri', 15))
_l_(637941)
_c_(637944, _a_(637943, _n_(637942, "receiver", lambda: receiver), "place"), y=150)
_l_(637945)

receiver_str = _c_(637948, _a_(637947, _n_(637946, "tk", lambda: tk), "StringVar"))
_l_(637949)

receiverEntry = _c_(637954, _a_(637951, _n_(637950, "tk", lambda: tk), "Entry"), _n_(637952, "mainframe", lambda: mainframe), textvariable=_n_(637953, "receiver_str", lambda: receiver_str), font=('Calibri', 15))
_l_(637955)
_c_(637958, _a_(637957, _n_(637956, "receiverEntry", lambda: receiverEntry), "place"), y=185, width=300)
_l_(637959)

# subject
subject = _c_(637963, _a_(637961, _n_(637960, "tk", lambda: tk), "Label"), _n_(637962, "mainframe", lambda: mainframe), text="Enter Subject:", font=('Calibri', 15))
_l_(637964)
_c_(637967, _a_(637966, _n_(637965, "subject", lambda: subject), "place"), y=220)
_l_(637968)

subject_str = _c_(637971, _a_(637970, _n_(637969, "tk", lambda: tk), "StringVar"))
_l_(637972)

subjectEntry = _c_(637977, _a_(637974, _n_(637973, "tk", lambda: tk), "Entry"), _n_(637975, "mainframe", lambda: mainframe), textvariable=_n_(637976, "subject_str", lambda: subject_str), font=('Calibri', 15))
_l_(637978)
_c_(637981, _a_(637980, _n_(637979, "subjectEntry", lambda: subjectEntry), "place"), y=255, width=300)
_l_(637982)

# body
body = _c_(637986, _a_(637984, _n_(637983, "tk", lambda: tk), "Label"), _n_(637985, "mainframe", lambda: mainframe), text="Enter Body:", font=('Calibri', 15))
_l_(637987)
_c_(637990, _a_(637989, _n_(637988, "body", lambda: body), "place"), x=500, y=2.5)
_l_(637991)

body_str = _c_(637994, _a_(637993, _n_(637992, "tk", lambda: tk), "StringVar"))
_l_(637995)

bodyEntry = _c_(637999, _a_(637997, _n_(637996, "tk", lambda: tk), "Text"), _n_(637998, "mainframe", lambda: mainframe))
_l_(638000)
_c_(638003, _a_(638002, _n_(638001, "bodyEntry", lambda: bodyEntry), "place"), x=380, y=35, width=300)
_l_(638004)

# notification
notif = _c_(638008, _a_(638006, _n_(638005, "tk", lambda: tk), "Label"), _n_(638007, "mainframe", lambda: mainframe), bg='#80c1ff', font=('Calibri', 15))
_l_(638009)
_c_(638012, _a_(638011, _n_(638010, "notif", lambda: notif), "place"), x=250, y=450)
_l_(638013)

# attachments array
attachments = []
_l_(638014)


# add attacments function
def add_attachments():
    _l_(638045)

    filename = _c_(638017, _a_(638016, _n_(638015, "filedialog", lambda: filedialog), "askopenfilename"), initialdir='C:/', title="Select a file to attach to the email")
    _l_(638018)
    _c_(638022, _a_(638020, _n_(638019, "attachments", lambda: attachments), "append"), _n_(638021, "filename", lambda: filename))
    _l_(638023)

    _c_(638031, _a_(638025, _n_(638024, "notif", lambda: notif), "config"), text="Attached " + _c_(638030, _n_(638026, "str", lambda: str), _c_(638029, _n_(638027, "len", lambda: len), _n_(638028, "attachments", lambda: attachments))) + " file", fg="green")
    _l_(638032)

    _c_(638035, _a_(638034, _n_(638033, "root", lambda: root), "update"))
    _l_(638036)
    _c_(638039, _a_(638038, _n_(638037, "time", lambda: time), "sleep"), 2.5)
    _l_(638040)

    _c_(638043, _a_(638042, _n_(638041, "notif", lambda: notif), "config"), text="")
    _l_(638044)


def reset_entries():
    _l_(638082)

    _c_(638048, _a_(638047, _n_(638046, "emailEntry", lambda: emailEntry), "delete"), 0, 'end')
    _l_(638049)
    _c_(638052, _a_(638051, _n_(638050, "passwordEntry", lambda: passwordEntry), "delete"), 0, 'end')
    _l_(638053)
    _c_(638056, _a_(638055, _n_(638054, "receiverEntry", lambda: receiverEntry), "delete"), 0, 'end')
    _l_(638057)
    _c_(638060, _a_(638059, _n_(638058, "subjectEntry", lambda: subjectEntry), "delete"), 0, 'end')
    _l_(638061)
    _c_(638064, _a_(638063, _n_(638062, "bodyEntry", lambda: bodyEntry), "delete"), "1.0", "end-1c")
    _l_(638065)

    _c_(638068, _a_(638067, _n_(638066, "notif", lambda: notif), "config"), text="Entries were reset", fg="green")
    _l_(638069)

    _c_(638072, _a_(638071, _n_(638070, "root", lambda: root), "update"))
    _l_(638073)
    _c_(638076, _a_(638075, _n_(638074, "time", lambda: time), "sleep"), 2.5)
    _l_(638077)

    _c_(638080, _a_(638079, _n_(638078, "notif", lambda: notif), "config"), text="")
    _l_(638081)


# send button
send = _c_(638089, _a_(638084, _n_(638083, "tk", lambda: tk), "Button"), _n_(638085, "mainframe", lambda: mainframe), text="Send Email", font=('Calibri', 15), command=lambda: _c_(638088, _a_(638087, _n_(638086, "SendEmail", lambda: SendEmail), "send_email")))
_l_(638090)
_c_(638093, _a_(638092, _n_(638091, "send", lambda: send), "place"), y=310, width=150)
_l_(638094)

# reset button
reset = _c_(638101, _a_(638096, _n_(638095, "tk", lambda: tk), "Button"), _n_(638097, "mainframe", lambda: mainframe), text="Reset", font=('Calibri', 15), command=lambda: _c_(638100, _a_(638099, _n_(638098, "ResetEntries", lambda: ResetEntries), "reset_entries")))
_l_(638102)
_c_(638105, _a_(638104, _n_(638103, "reset", lambda: reset), "place"), x=220, y=310, width=150)
_l_(638106)

# attachments button
attachment = _c_(638112, _a_(638108, _n_(638107, "tk", lambda: tk), "Button"), _n_(638109, "mainframe", lambda: mainframe), text="Add Attachments", font=('Calibri', 15), command=lambda: _c_(638111, _n_(638110, "add_attachments", lambda: add_attachments)))
_l_(638113)
_c_(638116, _a_(638115, _n_(638114, "attachment", lambda: attachment), "place"), x=90, y=365, width=200)
_l_(638117)

# Main loop
_c_(638120, _a_(638119, _n_(638118, "root", lambda: root), "mainloop"))
_l_(638121)
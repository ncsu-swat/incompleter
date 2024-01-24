# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53162259/populating-word-template-with-python-merge-but-typeerror-merge-argument-af
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
stress_notes_document = _c_(694922, _n_(694915, "MailMerge", lambda: MailMerge), _c_(694921, _a_(694918, _a_(694917, _n_(694916, "os", lambda: os), "path"), "join"), _n_(694919, "new_path", lambda: new_path),_n_(694920, "new_notes", lambda: new_notes)))
_l_(694923)
_c_(694941, _a_(694925, _n_(694924, "stress_notes_document", lambda: stress_notes_document), "merge"), TR_num = _n_(694926, "packet_info", lambda: packet_info)['TR#'],
        pckg_num = _n_(694927, "packet_info", lambda: packet_info)['Package#'],
        TED_num = _n_(694928, "packet_info", lambda: packet_info)['TED#'],
        Charge_Line = _n_(694929, "packet_info", lambda: packet_info)['Charge Line'],
        Change_num = _n_(694930, "packet_info", lambda: packet_info)['Change#'],
        Installation_list  = _n_(694931, "packet_list", lambda: packet_list)['Installations list'],
        Drawings_list   = _n_(694932, "packet_list", lambda: packet_list)['Drawings list'],
        Designer  = _n_(694933, "packet_info", lambda: packet_info)['Designer'],
        phone_number_designer = _n_(694934, "packet_info", lambda: packet_info)['Phone Number of designer'],
        Date_in = _n_(694935, "packet_info", lambda: packet_info)['Date in'],
        Stress_Due_Date = _n_(694936, "packet_info", lambda: packet_info)['Stress Due Date'],
        Date_out = _n_(694937, "packet_info", lambda: packet_info)['Date out'],
        model = _n_(694938, "packet_info", lambda: packet_info)['model'],
        Customer = _n_(694939, "packet_info", lambda: packet_info)['Customer'],
        Effectivity  = _n_(694940, "packet_info", lambda: packet_info)['Effectivity'],
        panel_excel = 'new_panel')
_l_(694942)

_c_(694951, _a_(694944, _n_(694943, "stress_notes_document", lambda: stress_notes_document), "write"), _c_(694950, _a_(694947, _a_(694946, _n_(694945, "os", lambda: os), "path"), "join"), _n_(694948, "new_path", lambda: new_path),_n_(694949, "new_notes", lambda: new_notes) + "ver A"))
_l_(694952)
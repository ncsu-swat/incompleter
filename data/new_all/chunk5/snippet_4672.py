# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53162259/populating-word-template-with-python-merge-but-typeerror-merge-argument-af
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
stress_notes_document = _c_(692058, _n_(692051, "MailMerge", lambda: MailMerge), _c_(692057, _a_(692054, _a_(692053, _n_(692052, "os", lambda: os), "path"), "join"), _n_(692055, "new_path", lambda: new_path),_n_(692056, "new_notes", lambda: new_notes)))
_l_(692059)
_c_(692077, _a_(692061, _n_(692060, "stress_notes_document", lambda: stress_notes_document), "merge"), TR_num = _n_(692062, "packet_info", lambda: packet_info)['TR#'],
        pckg_num = _n_(692063, "packet_info", lambda: packet_info)['Package#'],
        TED_num = _n_(692064, "packet_info", lambda: packet_info)['TED#'],
        Charge_Line = _n_(692065, "packet_info", lambda: packet_info)['Charge Line'],
        Change_num = _n_(692066, "packet_info", lambda: packet_info)['Change#'],
        Installation_list  = _n_(692067, "packet_list", lambda: packet_list)['Installations list'],
        Drawings_list   = _n_(692068, "packet_list", lambda: packet_list)['Drawings list'],
        Designer  = _n_(692069, "packet_info", lambda: packet_info)['Designer'],
        phone_number_designer = _n_(692070, "packet_info", lambda: packet_info)['Phone Number of designer'],
        Date_in = _n_(692071, "packet_info", lambda: packet_info)['Date in'],
        Stress_Due_Date = _n_(692072, "packet_info", lambda: packet_info)['Stress Due Date'],
        Date_out = _n_(692073, "packet_info", lambda: packet_info)['Date out'],
        model = _n_(692074, "packet_info", lambda: packet_info)['model'],
        Customer = _n_(692075, "packet_info", lambda: packet_info)['Customer'],
        Effectivity  = _n_(692076, "packet_info", lambda: packet_info)['Effectivity'],
        panel_excel = 'new_panel')
_l_(692078)

_c_(692087, _a_(692080, _n_(692079, "stress_notes_document", lambda: stress_notes_document), "write"), _c_(692086, _a_(692083, _a_(692082, _n_(692081, "os", lambda: os), "path"), "join"), _n_(692084, "new_path", lambda: new_path),_n_(692085, "new_notes", lambda: new_notes) + "ver A"))
_l_(692088)
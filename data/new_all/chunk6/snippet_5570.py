# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46923475/attributeerror-str-object-has-no-attribute-text-printing-css-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(370203, _n_(370202, "open", lambda: open), 'Aperture Science.csv', 'a+', newline='\n') as file:
        _l_(370274)

        writer = _c_(370207, _a_(370205, _n_(370204, "csv", lambda: csv), "writer"), _n_(370206, "file", lambda: file))
        _l_(370208)
        for section in _n_(370209, "sections", lambda: sections):
                _l_(370273)

                try:
                        _l_(370225)

                        link = _c_(370214, _a_(370213, _c_(370212, _a_(370211, _n_(370210, "section", lambda: section), "find_element_by_css_selector"), "h3 a"), "get_attribute"), "href")
                        _l_(370215)
                        _c_(370220, _n_(370216, "print", lambda: print), _c_(370219, _a_(370218, _n_(370217, "section", lambda: section), "get_attribute"), 'href'))
                        _l_(370221)
                except _n_(370222, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(370224)

                        pass
                        _l_(370223)
                _c_(370228, _a_(370227, _n_(370226, "time", lambda: time), "sleep"), 7)
                _l_(370229)
                try:
                        _l_(370243)

                        team_name = _a_(370233, _c_(370232, _a_(370231, _n_(370230, "section", lambda: section), "find_element_by_css_selector"), ".row:nth-child(1) td:nth-child(1)"), "text")
                        _l_(370234)
                        _c_(370238, _n_(370235, "print", lambda: print), _a_(370237, _n_(370236, "section", lambda: section), "text"))
                        _l_(370239)
                except _n_(370240, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(370242)

                        pass
                        _l_(370241)
                _c_(370246, _a_(370245, _n_(370244, "time", lambda: time), "sleep"), 7)
                _l_(370247)
                try:
                        _l_(370261)

                        bet = _a_(370251, _c_(370250, _a_(370249, _n_(370248, "section", lambda: section), "find_element_by_css_selector"), ".odds .odds span"), "text")
                        _l_(370252)
                        _c_(370256, _n_(370253, "print", lambda: print), _a_(370255, _n_(370254, "bet", lambda: bet), "text"))
                        _l_(370257)
                except _n_(370258, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(370260)

                        pass
                        _l_(370259)
                _c_(370264, _a_(370263, _n_(370262, "time", lambda: time), "sleep"), 7)
                _l_(370265)
                _c_(370271, _a_(370267, _n_(370266, "writer", lambda: writer), "writerow"), (_n_(370268, "bet", lambda: bet), _n_(370269, "team_name", lambda: team_name), _n_(370270, "link", lambda: link)))
                _l_(370272)
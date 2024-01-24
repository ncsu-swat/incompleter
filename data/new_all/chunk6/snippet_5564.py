# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46923475/attributeerror-str-object-has-no-attribute-text-printing-css-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(366571, _n_(366570, "open", lambda: open), 'Aperture Science.csv', 'a+', newline='\n') as file:
        _l_(366642)

        writer = _c_(366575, _a_(366573, _n_(366572, "csv", lambda: csv), "writer"), _n_(366574, "file", lambda: file))
        _l_(366576)
        for section in _n_(366577, "sections", lambda: sections):
                _l_(366641)

                try:
                        _l_(366593)

                        link = _c_(366582, _a_(366581, _c_(366580, _a_(366579, _n_(366578, "section", lambda: section), "find_element_by_css_selector"), "h3 a"), "get_attribute"), "href")
                        _l_(366583)
                        _c_(366588, _n_(366584, "print", lambda: print), _c_(366587, _a_(366586, _n_(366585, "section", lambda: section), "get_attribute"), 'href'))
                        _l_(366589)
                except _n_(366590, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(366592)

                        pass
                        _l_(366591)
                _c_(366596, _a_(366595, _n_(366594, "time", lambda: time), "sleep"), 7)
                _l_(366597)
                try:
                        _l_(366611)

                        team_name = _a_(366601, _c_(366600, _a_(366599, _n_(366598, "section", lambda: section), "find_element_by_css_selector"), ".row:nth-child(1) td:nth-child(1)"), "text")
                        _l_(366602)
                        _c_(366606, _n_(366603, "print", lambda: print), _a_(366605, _n_(366604, "section", lambda: section), "text"))
                        _l_(366607)
                except _n_(366608, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(366610)

                        pass
                        _l_(366609)
                _c_(366614, _a_(366613, _n_(366612, "time", lambda: time), "sleep"), 7)
                _l_(366615)
                try:
                        _l_(366629)

                        bet = _a_(366619, _c_(366618, _a_(366617, _n_(366616, "section", lambda: section), "find_element_by_css_selector"), ".odds .odds span"), "text")
                        _l_(366620)
                        _c_(366624, _n_(366621, "print", lambda: print), _a_(366623, _n_(366622, "bet", lambda: bet), "text"))
                        _l_(366625)
                except _n_(366626, "NoSuchElementException", lambda: NoSuchElementException):
                        _l_(366628)

                        pass
                        _l_(366627)
                _c_(366632, _a_(366631, _n_(366630, "time", lambda: time), "sleep"), 7)
                _l_(366633)
                _c_(366639, _a_(366635, _n_(366634, "writer", lambda: writer), "writerow"), (_n_(366636, "bet", lambda: bet), _n_(366637, "team_name", lambda: team_name), _n_(366638, "link", lambda: link)))
                _l_(366640)
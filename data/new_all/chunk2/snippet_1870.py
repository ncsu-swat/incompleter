# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45944787/attributeerror-across-typeerror-issue-in-python-3-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def write_cbs_from_poll_response_11(self, poll_response, dest_dir, write_type_=_n_(462741, "W_CLOBBER", lambda: W_CLOBBER)):
    _l_(462835)


    for cb in _a_(462743, _n_(462742, "poll_response", lambda: poll_response), "content_blocks"):
        _l_(462834)

        if _a_(462746, _a_(462745, _n_(462744, "cb", lambda: cb), "content_binding"), "binding_id") == _n_(462747, "CB_STIX_XML_10", lambda: CB_STIX_XML_10):
            _l_(462780)

            format_ = '_STIX10_'
            _l_(462748)
            ext = '.xml'
            _l_(462749)
        elif _a_(462752, _a_(462751, _n_(462750, "cb", lambda: cb), "content_binding"), "binding_id") == _n_(462753, "CB_STIX_XML_101", lambda: CB_STIX_XML_101):
            _l_(462779)

            format_ = '_STIX101_'
            _l_(462754)
            ext = '.xml'
            _l_(462755)
        elif _a_(462758, _a_(462757, _n_(462756, "cb", lambda: cb), "content_binding"), "binding_id") == _n_(462759, "CB_STIX_XML_11", lambda: CB_STIX_XML_11):
            _l_(462778)

            format_ = '_STIX11_'
            _l_(462760)
            ext = '.xml'
            _l_(462761)
        elif _a_(462764, _a_(462763, _n_(462762, "cb", lambda: cb), "content_binding"), "binding_id") == _n_(462765, "CB_STIX_XML_111", lambda: CB_STIX_XML_111):
            _l_(462777)

            format_ = '_STIX111_'
            _l_(462766)
            ext = '.xml'
            _l_(462767)
        elif _a_(462770, _a_(462769, _n_(462768, "cb", lambda: cb), "content_binding"), "binding_id") == _n_(462771, "CB_STIX_XML_12", lambda: CB_STIX_XML_12):
            _l_(462776)

            format_ = '_STIX12_'
            _l_(462772)
            ext = '.xml'
            _l_(462773)
        else:  # Format and extension are unknown
            format_ = ''
            _l_(462774)
            ext = ''
            _l_(462775)

        if _a_(462782, _n_(462781, "cb", lambda: cb), "timestamp_label"):
            _l_(462795)

            date_string = 't' + _c_(462786, _a_(462785, _a_(462784, _n_(462783, "cb", lambda: cb), "timestamp_label"), "isoformat"))
            _l_(462787)
        else:
            date_string = 's' + _c_(462793, _a_(462792, _c_(462791, _a_(462790, _a_(462789, _n_(462788, "datetime", lambda: datetime), "datetime"), "now")), "isoformat"))
            _l_(462794)

        filename = _c_(462802, _n_(462796, "gen_filename", lambda: gen_filename), _a_(462798, _n_(462797, "poll_response", lambda: poll_response), "collection_name"),
                                _n_(462799, "format_", lambda: format_),
                                _n_(462800, "date_string", lambda: date_string),
                                _n_(462801, "ext", lambda: ext))
        _l_(462803)
        filename = _c_(462809, _a_(462806, _a_(462805, _n_(462804, "os", lambda: os), "path"), "join"), _n_(462807, "dest_dir", lambda: dest_dir), _n_(462808, "filename", lambda: filename))
        _l_(462810)
        write, message = _c_(462815, _a_(462812, _n_(462811, "TaxiiScript", lambda: TaxiiScript), "get_write_and_message"), _n_(462813, "filename", lambda: filename), _n_(462814, "write_type_", lambda: write_type_))
        _l_(462816)

        if _n_(462817, "write", lambda: write):
            _l_(462828)

            with _c_(462820, _n_(462818, "open", lambda: open), _n_(462819, "filename", lambda: filename), 'w') as f:
                _l_(462827)

                _c_(462825, _a_(462822, _n_(462821, "f", lambda: f), "write"), _a_(462824, _n_(462823, "cb", lambda: cb), "content"))           # The TypeError is thrown here
                _l_(462826)           # The TypeError is thrown here

        _c_(462832, _n_(462829, "print", lambda: print), "%s%s" % (_n_(462830, "message", lambda: message), _n_(462831, "filename", lambda: filename)))
        _l_(462833)
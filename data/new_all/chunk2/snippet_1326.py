# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42498700/filenotfounderror-when-generating-latex-pdf-with-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(437538)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(437540)

except ImportError:
    pass
try:
    from django.template import Context
    _l_(437542)

except ImportError:
    pass
try:
    from django.template.loader import get_template
    _l_(437544)

except ImportError:
    pass
try:
    from subprocess import Popen, PIPE
    _l_(437546)

except ImportError:
    pass
try:
    import tempfile
    _l_(437548)

except ImportError:
    pass

def pdf(request):
    _l_(437602)

    context = _c_(437550, _n_(437549, "Context", lambda: Context), {})
    _l_(437551)
    template = _c_(437553, _n_(437552, "get_template", lambda: get_template), 'cv.tex')
    _l_(437554)
    rendered_tpl = _c_(437560, _a_(437559, _c_(437558, _a_(437556, _n_(437555, "template", lambda: template), "render"), _n_(437557, "context", lambda: context)), "encode"), 'utf-8')  
    _l_(437561)  
    with _c_(437564, _a_(437563, _n_(437562, "tempfile", lambda: tempfile), "TemporaryDirectory")) as tempdir:
        _l_(437591)

        # Create subprocess, supress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in _c_(437566, _n_(437565, "range", lambda: range), 2):
            _l_(437578)

            process = _c_(437571, _n_(437567, "Popen", lambda: Popen), ['pdflatex', '-output-directory', _n_(437568, "tempdir", lambda: tempdir)],
                stdin=_n_(437569, "PIPE", lambda: PIPE),
                stdout=_n_(437570, "PIPE", lambda: PIPE),
            )
            _l_(437572)
            _c_(437576, _a_(437574, _n_(437573, "process", lambda: process), "communicate"), _n_(437575, "rendered_tpl", lambda: rendered_tpl))
            _l_(437577)
        with _c_(437585, _n_(437579, "open", lambda: open), _c_(437584, _a_(437582, _a_(437581, _n_(437580, "os", lambda: os), "path"), "join"), _n_(437583, "tempdir", lambda: tempdir), 'texput.pdf'), 'rb') as f:
            _l_(437590)

            pdf = _c_(437588, _a_(437587, _n_(437586, "f", lambda: f), "read"))
            _l_(437589)
    r = _c_(437593, _n_(437592, "HttpResponse", lambda: HttpResponse), content_type='application/pdf')  
    _l_(437594)  
    _c_(437598, _a_(437596, _n_(437595, "r", lambda: r), "write"), _n_(437597, "pdf", lambda: pdf))
    _l_(437599)
    aux = _n_(437600, "r", lambda: r)
    _l_(437601)
    return aux
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60146977/filenotfounderror-on-file-upload-using-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(404747, _n_(404746, "jwt_required", lambda: jwt_required))
def post(request):
    _l_(404800)

    if 'file' not in _a_(404749, _n_(404748, "request", lambda: request), "files"):
        _l_(404751)

        aux = {
            'success': False,
            'message': 'No file part in the request',
        }, 200
        _l_(404750)
        return aux
    file = _a_(404753, _n_(404752, "request", lambda: request), "files")['file']
    _l_(404754)
    if _a_(404756, _n_(404755, "file", lambda: file), "filename") == '':
        _l_(404758)

        aux = {
            'success': False,
            'message': 'No file selected for uploading',
        }, 200
        _l_(404757)
        return aux
    if _n_(404759, "file", lambda: file) and _c_(404763, _n_(404760, "allowed_file", lambda: allowed_file), _a_(404762, _n_(404761, "file", lambda: file), "mimetype")):
        _l_(404798)

        filepath = _c_(404767, _n_(404764, "makepath", lambda: makepath), _a_(404766, _n_(404765, "file", lambda: file), "mimetype"))
        _l_(404768)
        _c_(404772, _a_(404770, _n_(404769, "file", lambda: file), "save"), _n_(404771, "filepath", lambda: filepath))
        _l_(404773)
        post = _c_(404789, _a_(404775, _n_(404774, "post_repo", lambda: post_repo), "create"), _a_(404777, _n_(404776, "current_identity", lambda: current_identity), "id"),
            _a_(404779, _n_(404778, "request", lambda: request), "form")['matchId'],
            _a_(404781, _n_(404780, "request", lambda: request), "form")['teamSelected'],
            _a_(404783, _n_(404782, "request", lambda: request), "form")['content'],
            _a_(404785, _n_(404784, "request", lambda: request), "form")['postType'],
            _n_(404786, "filepath", lambda: filepath),
            _a_(404788, _n_(404787, "request", lambda: request), "form")['location']
        )
        _l_(404790)
        if _n_(404791, "post", lambda: post):
            _l_(404797)

            aux = {
                'success': True,
                'message': 'Post successfully created',
                'post': _c_(404795, _a_(404793, _n_(404792, "post_repo", lambda: post_repo), "to_dto"), _n_(404794, "post", lambda: post)),
            }, 201
            _l_(404796)
            return aux
    aux = {
        'success': False,
        'message': 'File extension not allowed',
    }, 200
    _l_(404799)
    return aux
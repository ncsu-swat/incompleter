# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67349684/typeerror-while-joining-a-room-with-flask-socketio-5-0-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(558642, _a_(558641, _n_(558640, "socketio", lambda: socketio), "on"), 'connect')
def connection():
    _l_(558671)

    @_c_(558645, _a_(558644, _n_(558643, "socketio", lambda: socketio), "on"), 'join-room')
    def join_room(data):
        _l_(558670)

        roomId = _n_(558646, "data", lambda: data)['roomId']
        _l_(558647)
        camId = _n_(558648, "data", lambda: data)['camId']
        _l_(558649)
        _c_(558652, _n_(558650, "join_room", lambda: join_room), _n_(558651, "roomId", lambda: roomId))
        _l_(558653)
        _c_(558656, _n_(558654, "emit", lambda: emit), 'cam-connected', {'camId': _n_(558655, "camId", lambda: camId)}, broadcast=True)
        _l_(558657)
        @_c_(558660, _a_(558659, _n_(558658, "socketio", lambda: socketio), "on"), 'disconnect')
        def on_disconnect():
            _l_(558669)

            _c_(558663, _n_(558661, "leave_room", lambda: leave_room), _n_(558662, "roomId", lambda: roomId))
            _l_(558664)
            _c_(558667, _n_(558665, "emit", lambda: emit), 'cam-disconnected', {'camId': _n_(558666, "camId", lambda: camId)}, broadcast=True)
            _l_(558668)
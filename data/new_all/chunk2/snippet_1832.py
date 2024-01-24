# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(429074)

except ImportError:
    pass
try:
    import asyncio
    _l_(429076)

except ImportError:
    pass
try:
    from django.contrib.auth import get_user_model
    _l_(429078)

except ImportError:
    pass
try:
    from channels.consumer import AsyncConsumer
    _l_(429080)

except ImportError:
    pass
try:
    from channels.db import database_sync_to_async
    _l_(429082)

except ImportError:
    pass
try:
    from .models import Thread, ChatMessage
    _l_(429084)

except ImportError:
    pass

class ChatConsumer(_n_(429085, "AsyncConsumer", lambda: AsyncConsumer)):
    _l_(429215)

    async def websocket_connect(self, event):
        _l_(429123)

        _c_(429088, _n_(429086, "print", lambda: print), "connected", _n_(429087, "event", lambda: event))
        _l_(429089)

        other_user = _a_(429091, _n_(429090, "self", lambda: self), "scope")['url_route']['kwargs']['username']
        _l_(429092)
        me = _a_(429094, _n_(429093, "self", lambda: self), "scope")['user']
        _l_(429095)
        # print(other_user, me)
        thread_obj = await _c_(429100, _a_(429097, _n_(429096, "self", lambda: self), "get_thread"), _n_(429098, "me", lambda: me), _n_(429099, "other_user", lambda: other_user))
        _l_(429101)
        _n_(429102, "self", lambda: self).thread_obj = _n_(429103, "thread_obj", lambda: thread_obj)
        _l_(429104)
        chat_room = f"thread_{_a_(429106, _n_(429105, 'thread_obj', lambda: thread_obj), 'id')}"
        _l_(429107)
        _n_(429108, "self", lambda: self).chat_room = _n_(429109, "chat_room", lambda: chat_room)
        _l_(429110)

        # await asyncio.sleep(10)
        await _c_(429117, _a_(429113, _a_(429112, _n_(429111, "self", lambda: self), "channel_layer"), "group_add"), _n_(429114, "chat_room", lambda: chat_room),
        _a_(429116, _n_(429115, "self", lambda: self), "channel_name"),
        )
        _l_(429118)

        await _c_(429121, _a_(429120, _n_(429119, "self", lambda: self), "send"), {
            "type": "websocket.accept",
        })
        _l_(429122)

    async def websocket_receive(self, event):
        _l_(429177)

        # when a message is received from the websocket
        _c_(429126, _n_(429124, "print", lambda: print), "receive", _n_(429125, "event", lambda: event))
        _l_(429127)
        front_text = _c_(429130, _a_(429129, _n_(429128, "event", lambda: event), "get"), 'text', None)
        _l_(429131)
        if _n_(429132, "front_text", lambda: front_text) is not None:
            _l_(429176)

            loaded_dict_data = _c_(429136, _a_(429134, _n_(429133, "json", lambda: json), "loads"), _n_(429135, "front_text", lambda: front_text))
            _l_(429137)
            msg = _c_(429140, _a_(429139, _n_(429138, "loaded_dict_data", lambda: loaded_dict_data), "get"), 'message')
            _l_(429141)
            _c_(429144, _n_(429142, "print", lambda: print), _n_(429143, "msg", lambda: msg))
            _l_(429145)
            user = _a_(429147, _n_(429146, "self", lambda: self), "scope")['user']
            _l_(429148)
            username = 'default'
            _l_(429149)
            if _a_(429151, _n_(429150, "user", lambda: user), "is_authenticated"):
                _l_(429155)

                username = _a_(429153, _n_(429152, "user", lambda: user), "username")
                _l_(429154)
            myResponse = {
                'message': _n_(429156, "msg", lambda: msg),
                'username': _n_(429157, "username", lambda: username),
            }
            _l_(429158)
            await _c_(429163, _a_(429160, _n_(429159, "self", lambda: self), "create_chat_message"), _n_(429161, "user", lambda: user), _n_(429162, "msg", lambda: msg))
            _l_(429164)

            # broadcasts the message event to be sent
            await _c_(429174, _a_(429167, _a_(429166, _n_(429165, "self", lambda: self), "channel_layer"), "group_send"), _a_(429169, _n_(429168, "self", lambda: self), "chat_room"),
                {
                    "type": "chat_message",
                    "text": _c_(429173, _a_(429171, _n_(429170, "json", lambda: json), "dumps"), _n_(429172, "myResponse", lambda: myResponse)),
                }
            )
            _l_(429175)

    async def chat_message(self, event):
        _l_(429187)

        # sends the message
        _c_(429180, _n_(429178, "print", lambda: print), 'message', _n_(429179, "event", lambda: event))
        _l_(429181)
        await _c_(429185, _a_(429183, _n_(429182, "self", lambda: self), "send"), {
            "type": "websocket.send",
            "text": _n_(429184, "event", lambda: event)['text'],
        })
        _l_(429186)


    async def websocket_disconnect(self, event):
        _l_(429192)

        _c_(429190, _n_(429188, "print", lambda: print), "disconnected", _n_(429189, "event", lambda: event))
        _l_(429191)

    @_n_(429193, "database_sync_to_async", lambda: database_sync_to_async)
    def get_thread(self, user, other_username):
        _l_(429201)

        aux = _c_(429199, _a_(429196, _a_(429195, _n_(429194, "Thread", lambda: Thread), "objects"), "get_or_new"), _n_(429197, "user", lambda: user), _n_(429198, "other_username", lambda: other_username))[0]
        _l_(429200)
        return aux

    @_n_(429202, "database_sync_to_async", lambda: database_sync_to_async)
    def create_chat_message(self, me, msg):
        _l_(429214)

        thread_obj = _a_(429204, _n_(429203, "self", lambda: self), "thread_obj")
        _l_(429205)
        aux = _c_(429212, _a_(429208, _a_(429207, _n_(429206, "ChatMessage", lambda: ChatMessage), "objects"), "create"), thread=_n_(429209, "thread_obj", lambda: thread_obj), user=_n_(429210, "me", lambda: me), message=_n_(429211, "msg", lambda: msg))
        _l_(429213)
        # me         = self.scope['user']
        return aux
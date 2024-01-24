# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75236264/typeerror-bot-edit-message-media-got-multiple-values-for-argument-media
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from aiogram import types
    _l_(602122)

except ImportError:
    pass
try:
    from keyboards.inline.choise_buttons import choice, shop_keyboard
    _l_(602124)

except ImportError:
    pass
try:
    from keyboards.inline.callback_datas import get_callback
    _l_(602126)

except ImportError:
    pass
try:
    from aiogram.types import CallbackQuery, InputMediaPhoto
    _l_(602128)

except ImportError:
    pass
try:
    from loader import dp,bot
    _l_(602130)

except ImportError:
    pass


@_c_(602133, _a_(602132, _n_(602131, "dp", lambda: dp), "message_handler"))
async def bot_reply(message: _a_(602135, _n_(602134, "types", lambda: types), "Message")):
    _l_(602218)

    photo_url = 'https://pbs.twimg.com/profile_images/1187438234382548994/SesNEhbs_400x400.jpg'
    _l_(602136)
    await _c_(602144, _a_(602138, _n_(602137, "bot", lambda: bot), "send_photo"), photo=_n_(602139, "photo_url", lambda: photo_url),
                         chat_id=_a_(602142, _a_(602141, _n_(602140, "message", lambda: message), "chat"), "id"),
                         caption='Главное меню',
                         reply_markup=_n_(602143, "choice", lambda: choice),
                               )
    _l_(602145)
    @_c_(602151, _a_(602147, _n_(602146, "dp", lambda: dp), "callback_query_handler"), _c_(602150, _a_(602149, _n_(602148, "get_callback", lambda: get_callback), "filter"), category_name='shop'))
    async def open_shop(call: _n_(602152, "CallbackQuery", lambda: CallbackQuery)):
        _l_(602193)

        await _c_(602155, _a_(602154, _n_(602153, "call", lambda: call), "answer"), cache_time=60)
        _l_(602156)
        await _c_(602168, _a_(602158, _n_(602157, "bot", lambda: bot), "edit_message_media"), _a_(602162, _a_(602161, _a_(602160, _n_(602159, "call", lambda: call), "message"), "chat"), "id"),
                                     _a_(602165, _a_(602164, _n_(602163, "call", lambda: call), "message"), "message_id"),
                                     media = _c_(602167, _n_(602166, "InputMediaPhoto", lambda: InputMediaPhoto), 'https://fikiwiki.com/uploads/posts/2022-02/1645044676_1-fikiwiki-com-p-kartinki-lami-1.jpg'))
        _l_(602169)
        await _c_(602179, _a_(602171, _n_(602170, "bot", lambda: bot), "edit_message_caption"), _a_(602175, _a_(602174, _a_(602173, _n_(602172, "call", lambda: call), "message"), "chat"), "id"),
                                       _a_(602178, _a_(602177, _n_(602176, "call", lambda: call), "message"), "message_id"),
                                       caption='Выберите категорию'
                                       )
        _l_(602180)
        await _c_(602191, _a_(602182, _n_(602181, "bot", lambda: bot), "edit_message_reply_markup"), _a_(602186, _a_(602185, _a_(602184, _n_(602183, "call", lambda: call), "message"), "chat"), "id"),
                                      _a_(602189, _a_(602188, _n_(602187, "call", lambda: call), "message"), "message_id"),
                                      reply_markup=_n_(602190, "shop_keyboard", lambda: shop_keyboard)
                                      )
        _l_(602192)
    @_c_(602199, _a_(602195, _n_(602194, "dp", lambda: dp), "callback_query_handler"), _c_(602198, _a_(602197, _n_(602196, "get_callback", lambda: get_callback), "filter"), category_name='shop'))
    async def open_shop(call: _n_(602200, "CallbackQuery", lambda: CallbackQuery)):
        _l_(602217)

        await _c_(602203, _a_(602202, _n_(602201, "call", lambda: call), "answer"), cache_time=60)
        _l_(602204)
        await _c_(602215, _a_(602206, _n_(602205, "bot", lambda: bot), "edit_message_reply_markup"), _a_(602210, _a_(602209, _a_(602208, _n_(602207, "call", lambda: call), "message"), "chat"), "id"),
                                      _a_(602213, _a_(602212, _n_(602211, "call", lambda: call), "message"), "message_id"),
                                      reply_markup=_n_(602214, "shop_keyboard", lambda: shop_keyboard)
                                      )
        _l_(602216)

# await call.message.delete()
#     await call.message.answer_photo(photo=photo_url2,
#                               reply_markup=shop_keyboard)
#     @dp.callback_query_handler(get_callback.filter(category_name='royale'))
#     async def open_shop(call: CallbackQuery):
#         photo_url2 = 'https://i.ytimg.com/vi/P2TifLd5OIQ/maxresdefault.jpg'
#         await call.answer(cache_time=60)
#         await call.message.delete()
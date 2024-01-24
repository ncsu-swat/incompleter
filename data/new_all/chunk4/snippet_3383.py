# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(621955)

except ImportError:
    pass
try:
    import openai
    _l_(621957)

except ImportError:
    pass


# Create your views here.

def chatbot_view(request):
    _l_(621979)

    # Get the user's input from the request
    user_input = _c_(621961, _a_(621960, _a_(621959, _n_(621958, "request", lambda: request), "POST"), "get"), "user_input") 
    _l_(621962) 
    # Use the OpenAI library to generate a response
    _n_(621963, "openai", lambda: openai).api_key = "MY-API"
    _l_(621964)
    response = _c_(621969, _a_(621967, _a_(621966, _n_(621965, "openai", lambda: openai), "Completion"), "create"), engine="text-davinci-003",
        prompt=_n_(621968, "user_input", lambda: user_input),
        max_tokens=1024,
        temperature=0.7,
    )
    _l_(621970)
    chatbot_response = _a_(621972, _n_(621971, "response", lambda: response), "text")
    _l_(621973)
    aux = _c_(621977, _n_(621974, "render", lambda: render), _n_(621975, "request", lambda: request), 'chat/index.html', {"chatbot_response": _n_(621976, "chatbot_response", lambda: chatbot_response)})
    _l_(621978)

    # Render the response in a template
    return aux
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75900017/attributeerror-list-object-has-no-attribute-lower-in-sklearn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(423952)

except ImportError:
    pass
try:
    import string
    _l_(423954)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(423956)

except ImportError:
    pass
try:
    from sklearn.metrics.pairwise import cosine_similarity
    _l_(423958)

except ImportError:
    pass

conversations = [   'Hello',   'Hi there!',   'How are you?',   'I am doing well.',   'That is good to hear.',   'Thank you',   'You are welcome.',   'What is your name?',   'My name is ChatBot.',   'Who created you?',   'I was created by OpenAI.']
_l_(423959)

def preprocess_text(text):
    _l_(423986)

    if not _c_(423963, _n_(423960, "isinstance", lambda: isinstance), _n_(423961, "text", lambda: text), _n_(423962, "str", lambda: str)):
        _l_(423967)

        raise _c_(423965, _n_(423964, "TypeError", lambda: TypeError), "Input must be a string")
        _l_(423966)
    text = _c_(423970, _a_(423969, _n_(423968, "text", lambda: text), "lower"))
    _l_(423971)
    text = _c_(423978, _a_(423972, '', "join"), [_n_(423973, "char", lambda: char) for char in _n_(423974, "text", lambda: text) if _n_(423975, "char", lambda: char) not in _a_(423977, _n_(423976, "string", lambda: string), "punctuation")])
    _l_(423979)
    tokens = _c_(423982, _a_(423981, _n_(423980, "text", lambda: text), "split"))
    _l_(423983)
    aux = _n_(423984, "tokens", lambda: tokens)
    _l_(423985)
    return aux

def generate_response(user_input, conversations):
    _l_(424045)

    response = ''
    _l_(423987)
    conversation_tokens = []
    _l_(423988)
    _c_(423994, _a_(423990, _n_(423989, "conversation_tokens", lambda: conversation_tokens), "append"), _c_(423993, _n_(423991, "preprocess_text", lambda: preprocess_text), _n_(423992, "user_input", lambda: user_input)))
    _l_(423995)
    for conversation in _n_(423996, "conversations", lambda: conversations):
        _l_(424006)

        _c_(424004, _a_(423998, _n_(423997, "conversation_tokens", lambda: conversation_tokens), "append"), _c_(424003, _n_(423999, "preprocess_text", lambda: preprocess_text), _c_(424002, _n_(424000, "str", lambda: str), _n_(424001, "conversation", lambda: conversation))))
        _l_(424005)
    tfidf_vectorizer = _c_(424009, _n_(424007, "TfidfVectorizer", lambda: TfidfVectorizer), tokenizer=_n_(424008, "preprocess_text", lambda: preprocess_text))
    _l_(424010)
    tfidf_matrix = _c_(424014, _a_(424012, _n_(424011, "tfidf_vectorizer", lambda: tfidf_vectorizer), "fit_transform"), _n_(424013, "conversation_tokens", lambda: conversation_tokens))
    _l_(424015)
    similarity_scores = _c_(424019, _n_(424016, "cosine_similarity", lambda: cosine_similarity), _n_(424017, "tfidf_matrix", lambda: tfidf_matrix)[-1], _n_(424018, "tfidf_matrix", lambda: tfidf_matrix))
    _l_(424020)
    idx = _c_(424023, _a_(424022, _n_(424021, "similarity_scores", lambda: similarity_scores), "argsort"))[0][-2]
    _l_(424024)
    flat = _c_(424027, _a_(424026, _n_(424025, "similarity_scores", lambda: similarity_scores), "flatten"))
    _l_(424028)
    _c_(424031, _a_(424030, _n_(424029, "flat", lambda: flat), "sort"))
    _l_(424032)
    score = _n_(424033, "flat", lambda: flat)[-2]
    _l_(424034)
    if _n_(424035, "score", lambda: score) == 0:
        _l_(424042)

        response = _n_(424036, "response", lambda: response) + 'I apologize, I do not understand.'
        _l_(424037)
    else:
       response = _n_(424038, "response", lambda: response) + _n_(424039, "conversations", lambda: conversations)[_n_(424040, "idx", lambda: idx)]
       _l_(424041)
    aux = _n_(424043, "response", lambda: response)
    _l_(424044)
    return aux

while True:
    _l_(424058)

    user_input = _c_(424047, _n_(424046, "input", lambda: input), 'You: ')
    _l_(424048)
    response = _c_(424052, _n_(424049, "generate_response", lambda: generate_response), _n_(424050, "user_input", lambda: user_input), _n_(424051, "conversations", lambda: conversations))
    _l_(424053)
    _c_(424056, _n_(424054, "print", lambda: print), 'ChatBot:', _n_(424055, "response", lambda: response))
    _l_(424057)
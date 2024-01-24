# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77457590/creating-chat-agent-with-langchain-and-openai-getting-no-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from config import api_key,new_personal_api_key
    _l_(466059)

except ImportError:
    pass

apikey=_n_(466060, "new_personal_api_key", lambda: new_personal_api_key)
_l_(466061)
try:
    import os
    _l_(466063)

except ImportError:
    pass

_a_(466065, _n_(466064, "os", lambda: os), "environ")['OPENAI_API_KEY'] = _n_(466066, "apikey", lambda: apikey)
_l_(466067)
try:
    from langchain.chains.conversation.memory import ConversationBufferWindowMemory
    _l_(466069)

except ImportError:
    pass
try:
    from langchain.agents import Tool
    _l_(466071)

except ImportError:
    pass
try:
    from langchain.tools import BaseTool
    _l_(466073)

except ImportError:
    pass

def meaning_of_life(input=""):
    _l_(466075)

    aux = 'The meaning of life is 42 if rounded but is actually 42.17658'
    _l_(466074)
    return aux
life_tool = _c_(466078, _n_(466076, "Tool", lambda: Tool), name='Meaning of Life',
    func= _n_(466077, "meaning_of_life", lambda: meaning_of_life),
    description="Useful for when you need to answer questions about the meaning of life. input should be MOL "
)
_l_(466079)
try:
    import random
    _l_(466081)

except ImportError:
    pass

def random_num(input=""):
    _l_(466086)

    aux = _c_(466084, _a_(466083, _n_(466082, "random", lambda: random), "randint"), 0,5)
    _l_(466085)
    return aux
random_tool = _c_(466089, _n_(466087, "Tool", lambda: Tool), name='Random number',
    func= _n_(466088, "random_num", lambda: random_num),
    description="Useful for when you need to get a random number. input should be 'random'"
)
_l_(466090)
try:
    from langchain import OpenAI
    _l_(466092)

except ImportError:
    pass
try:
    from langchain.chat_models import ChatOpenAI
    _l_(466094)

except ImportError:
    pass

# Set up the turbo LLM
turbo_llm = _c_(466096, _n_(466095, "ChatOpenAI", lambda: ChatOpenAI), temperature=0,
    model_name='gpt-3.5-turbo'
)
_l_(466097)
try:
    from langchain.agents import initialize_agent
    _l_(466099)

except ImportError:
    pass

tools = [_n_(466100, "random_tool", lambda: random_tool), _n_(466101, "life_tool", lambda: life_tool)]
_l_(466102)

# conversational agent memory
memory = _c_(466104, _n_(466103, "ConversationBufferWindowMemory", lambda: ConversationBufferWindowMemory), memory_key='chat_history',
    k=3,
    return_messages=True
)
_l_(466105)


# create our agent
conversational_agent = _c_(466110, _n_(466106, "initialize_agent", lambda: initialize_agent), agent='chat-conversational-react-description',
    tools=_n_(466107, "tools", lambda: tools),
    llm=_n_(466108, "turbo_llm", lambda: turbo_llm),
#     llm=local_llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=_n_(466109, "memory", lambda: memory),
    handle_parsing_errors=True
)
_l_(466111)


_c_(466113, _n_(466112, "conversational_agent", lambda: conversational_agent), 'Can you give me a random number?')
_l_(466114)
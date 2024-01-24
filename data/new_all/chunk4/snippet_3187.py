# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77696025/typeerror-object-of-type-client-is-not-json-serializable-when-using-langchain
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
template = """Tell me a {adjective} joke about {subject}."""
_l_(609240)
prompt = _c_(609243, _n_(609241, "PromptTemplate", lambda: PromptTemplate), template=_n_(609242, "template", lambda: template), input_variables=["adjective", "subject"])
_l_(609244)
llm_chain = _c_(609249, _n_(609245, "LLMChain", lambda: LLMChain), prompt=_n_(609246, "prompt", lambda: prompt), llm=_a_(609248, _n_(609247, "config", lambda: config), "openaiExample"), verbose=True)
_l_(609250)

_c_(609253, _a_(609252, _n_(609251, "llm_chain", lambda: llm_chain), "predict"), adjective="sad", subject="ducks")
_l_(609254)
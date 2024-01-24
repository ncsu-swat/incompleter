# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66924471/typeerror-trace-argument-input-position-1-must-be-tensor-not-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(636079)

except ImportError:
    pass
try:
    import torch
    _l_(636081)

except ImportError:
    pass
try:
    from model import SpeechRecognition
    _l_(636083)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(636085)

except ImportError:
    pass

def trace(model):
    _l_(636109)

    _c_(636088, _a_(636087, _n_(636086, "model", lambda: model), "eval"))
    _l_(636089)
    x = _c_(636092, _a_(636091, _n_(636090, "torch", lambda: torch), "rand"), 1, 81, 300)
    _l_(636093)
    hidden = _c_(636096, _a_(636095, _n_(636094, "model", lambda: model), "_init_hidden"), 1)
    _l_(636097)
    traced = _c_(636105, _c_(636102, _a_(636099, _n_(636098, "torch", lambda: torch), "trace"), _a_(636101, _n_(636100, "model", lambda: model), "forward")), xample_inputs=(_n_(636103, "x", lambda: x), _n_(636104, "hidden", lambda: hidden)))
    _l_(636106)
    aux = _n_(636107, "traced", lambda: traced)
    _l_(636108)
    return aux

def main(args):
    _l_(636174)

    _c_(636113, _n_(636110, "print", lambda: print), "loading model from", _a_(636112, _n_(636111, "args", lambda: args), "model_checkpoint"))
    _l_(636114)
    checkpoint = _c_(636122, _a_(636116, _n_(636115, "torch", lambda: torch), "load"), _a_(636118, _n_(636117, "args", lambda: args), "model_checkpoint"), map_location=_c_(636121, _a_(636120, _n_(636119, "torch", lambda: torch), "device"), 'cpu'))
    _l_(636123)
    h_params = _a_(636125, _n_(636124, "SpeechRecognition", lambda: SpeechRecognition), "hyper_parameters")
    _l_(636126)
    model = _c_(636129, _n_(636127, "SpeechRecognition", lambda: SpeechRecognition), **_n_(636128, "h_params", lambda: h_params))
    _l_(636130)
    model_state_dict = _n_(636131, "checkpoint", lambda: checkpoint)['state_dict']
    _l_(636132)
    new_state_dict = _c_(636134, _n_(636133, "OrderedDict", lambda: OrderedDict))
    _l_(636135)
    for k, v in _c_(636138, _a_(636137, _n_(636136, "model_state_dict", lambda: model_state_dict), "items")):
        _l_(636147)

        name = _c_(636141, _a_(636140, _n_(636139, "k", lambda: k), "replace"), "model.", "") # remove `model.`
        _l_(636142) # remove `model.`
        _n_(636143, "new_state_dict", lambda: new_state_dict)[_n_(636144, "name", lambda: name)] = _n_(636145, "v", lambda: v)
        _l_(636146)

    _c_(636151, _a_(636149, _n_(636148, "model", lambda: model), "load_state_dict"), _n_(636150, "new_state_dict", lambda: new_state_dict))
    _l_(636152)

    _c_(636154, _n_(636153, "print", lambda: print), "tracing model...")
    _l_(636155)
    traced_model = _c_(636158, _n_(636156, "trace", lambda: trace), _n_(636157, "model", lambda: model))
    _l_(636159)
    #print(type(traced_model))
    _c_(636163, _n_(636160, "print", lambda: print), "saving to", _a_(636162, _n_(636161, "args", lambda: args), "save_path"))
    _l_(636164)
    _c_(636169, _a_(636166, _n_(636165, "traced_model", lambda: traced_model), "save"), _a_(636168, _n_(636167, "args", lambda: args), "save_path"))
    _l_(636170)
    _c_(636172, _n_(636171, "print", lambda: print), "Done!")
    _l_(636173)

if _n_(636175, "__name__", lambda: __name__) == "__main__":
    _l_(636198)

    parser = _c_(636178, _a_(636177, _n_(636176, "argparse", lambda: argparse), "ArgumentParser"), description="testing the wakeword engine")
    _l_(636179)
    _c_(636183, _a_(636181, _n_(636180, "parser", lambda: parser), "add_argument"), '--model_checkpoint', type=_n_(636182, "str", lambda: str), default='NameOfYourCheckpoint', required=False,
                        help='Checkpoint of model to optimize')
    _l_(636184)
    _c_(636188, _a_(636186, _n_(636185, "parser", lambda: parser), "add_argument"), '--save_path', type=_n_(636187, "str", lambda: str), default='path/where/you/want/to/save/the/optimized/model', required=False,
                        help='path to save optmized model')
    _l_(636189)

    args = _c_(636192, _a_(636191, _n_(636190, "parser", lambda: parser), "parse_args"))
    _l_(636193)
    _c_(636196, _n_(636194, "main", lambda: main), _n_(636195, "args", lambda: args))
    _l_(636197)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66924773/how-to-solve-typeerror-error-in-jupyter-notebok
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(525780)

    """
    Load train/validation data set and train the model
    """
    parser = _c_(525695, _a_(525694, _n_(525693, "argparse", lambda: argparse), "ArgumentParser"), description='Behavioral Cloning Training Program')
    _l_(525696)
    _c_(525700, _a_(525698, _n_(525697, "parser", lambda: parser), "add_argument"), '-d', help='data directory',        dest='data_dir',          type=_n_(525699, "str", lambda: str),   default='data')
    _l_(525701)
    _c_(525705, _a_(525703, _n_(525702, "parser", lambda: parser), "add_argument"), '-t', help='test size fraction',    dest='test_size',         type=_n_(525704, "float", lambda: float), default=0.2)
    _l_(525706)
    _c_(525710, _a_(525708, _n_(525707, "parser", lambda: parser), "add_argument"), '-k', help='drop out probability',  dest='keep_prob',         type=_n_(525709, "float", lambda: float), default=0.5)
    _l_(525711)
    _c_(525715, _a_(525713, _n_(525712, "parser", lambda: parser), "add_argument"), '-n', help='number of epochs',      dest='nb_epoch',          type=_n_(525714, "int", lambda: int),   default=10)
    _l_(525716)
    _c_(525720, _a_(525718, _n_(525717, "parser", lambda: parser), "add_argument"), '-s', help='samples per epoch',     dest='samples_per_epoch', type=_n_(525719, "int", lambda: int),   default=20000)
    _l_(525721)
    _c_(525725, _a_(525723, _n_(525722, "parser", lambda: parser), "add_argument"), '-b', help='batch size',            dest='batch_size',        type=_n_(525724, "int", lambda: int),   default=40)
    _l_(525726)
    _c_(525730, _a_(525728, _n_(525727, "parser", lambda: parser), "add_argument"), '-o', help='save best models only', dest='save_best_only',    type=_n_(525729, "s2b", lambda: s2b),   default='true')
    _l_(525731)
    _c_(525735, _a_(525733, _n_(525732, "parser", lambda: parser), "add_argument"), '-l', help='learning rate',         dest='learning_rate',     type=_n_(525734, "float", lambda: float), default=1.0e-4)
    _l_(525736)
    args = _c_(525739, _a_(525738, _n_(525737, "parser", lambda: parser), "parse_args"))
    _l_(525740)

    #print parameters
    _c_(525742, _n_(525741, "print", lambda: print), '-' * 30)
    _l_(525743)
    _c_(525745, _n_(525744, "print", lambda: print), 'Parameters')
    _l_(525746)
    _c_(525748, _n_(525747, "print", lambda: print), '-' * 30)
    _l_(525749)
    for key, value in _c_(525754, _a_(525753, _c_(525752, _n_(525750, "vars", lambda: vars), _n_(525751, "args", lambda: args)), "items")):
        _l_(525762)

        _c_(525760, _n_(525755, "print", lambda: print), _c_(525759, _a_(525756, '{:<20} := {}', "format"), _n_(525757, "key", lambda: key), _n_(525758, "value", lambda: value)))
        _l_(525761)
    _c_(525764, _n_(525763, "print", lambda: print), '-' * 30)
    _l_(525765)

    #load data
    data = _c_(525768, _n_(525766, "load_data", lambda: load_data), _n_(525767, "args", lambda: args))
    _l_(525769)
    #build model
    model = _c_(525772, _n_(525770, "build_model", lambda: build_model), _n_(525771, "args", lambda: args))
    _l_(525773)
    #train model on data, it saves as model.h5 
    _c_(525778, _n_(525774, "train_model", lambda: train_model), _n_(525775, "model", lambda: model), _n_(525776, "args", lambda: args), *_n_(525777, "data", lambda: data))
    _l_(525779)


if _n_(525781, "__name__", lambda: __name__) == '__main__':
    _l_(525785)

    _c_(525783, _n_(525782, "main", lambda: main))
    _l_(525784)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58584845/typeerror-float-object-is-not-subscriptable-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(392136)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(392138)

except ImportError:
    pass


class Implementation:
    _l_(392208)

    def __init__(self):
        _l_(392140)

        pass
        _l_(392139)

    def Distancess(self, training_sub_data, query_instance):
        _l_(392158)


        query_params = _n_(392141, "query_instance", lambda: query_instance)[:10]
        _l_(392142)

        eucl = _c_(392150, _a_(392144, _n_(392143, "np", lambda: np), "sqrt"), _c_(392149, _a_(392146, _n_(392145, "np", lambda: np), "sum"), (_n_(392147, "training_sub_data", lambda: training_sub_data) - _n_(392148, "query_params", lambda: query_params)) ** 2, axis=-1))
        _l_(392151)
        aux = _n_(392152, "eucl", lambda: eucl), _c_(392156, _a_(392154, _n_(392153, "np", lambda: np), "argsort"), _n_(392155, "eucl", lambda: eucl))
        _l_(392157)
        return aux

    def weight(self, training_data, distances, sorted_indices, k):
        _l_(392207)

        i = 1
        _l_(392159)
        samples_class = _n_(392160, "training_data", lambda: training_data)[_n_(392161, "sorted_indices", lambda: sorted_indices)[:_n_(392162, "k", lambda: k)]][:, -1]
        _l_(392163)
        nearest_distances = _n_(392164, "distances", lambda: distances)[_n_(392165, "sorted_indices", lambda: sorted_indices)[:_n_(392166, "k", lambda: k)]]
        _l_(392167)
        nearest_weights = _c_(392174, _a_(392169, _n_(392168, "np", lambda: np), "divide"), 1, _c_(392173, _a_(392171, _n_(392170, "np", lambda: np), "square"), _n_(392172, "nearest_distances", lambda: nearest_distances)))
        _l_(392175)
        class_0_weights_sum = _c_(392180, _a_(392177, _n_(392176, "np", lambda: np), "sum"), _n_(392178, "nearest_weights", lambda: nearest_weights)[_n_(392179, "samples_class", lambda: samples_class) == 0])
        _l_(392181)
        class_1_weights_sum = _c_(392186, _a_(392183, _n_(392182, "np", lambda: np), "sum"), _n_(392184, "nearest_weights", lambda: nearest_weights)[_n_(392185, "samples_class", lambda: samples_class) == 1])
        _l_(392187)
        class_2_weights_sum = _c_(392192, _a_(392189, _n_(392188, "np", lambda: np), "sum"), _n_(392190, "nearest_weights", lambda: nearest_weights)[_n_(392191, "samples_class", lambda: samples_class) == 2])
        _l_(392193)

        if _n_(392194, "class_0_weights_sum", lambda: class_0_weights_sum) > _n_(392195, "class_1_weights_sum", lambda: class_1_weights_sum) and _n_(392196, "class_0_weights_sum", lambda: class_0_weights_sum) > _n_(392197, "class_2_weights_sum", lambda: class_2_weights_sum):
            _l_(392206)

            aux = 0
            _l_(392198)
            return aux
        elif _n_(392199, "class_1_weights_sum", lambda: class_1_weights_sum) > _n_(392200, "class_0_weights_sum", lambda: class_0_weights_sum) and _n_(392201, "class_1_weights_sum", lambda: class_1_weights_sum) > _n_(392202, "class_2_weights_sum", lambda: class_2_weights_sum):
            _l_(392205)

            aux = 1
            _l_(392203)
            return aux
        else:
            aux = 2
            _l_(392204)
            return aux

def weight_based_approach(training_data, test_data, kn_k_value):
    _l_(392240)

    training_data_10_columns = _n_(392209, "training_data", lambda: training_data)[:, :10]
    _l_(392210)

    kn = _c_(392212, _n_(392211, "Implementation", lambda: Implementation))
    _l_(392213)

    eucl_weight_prediction_count = 0
    _l_(392214)
    for query_instance in _n_(392215, "test_data", lambda: test_data):
        _l_(392234)

        distances, euclidean_indices = _c_(392220, _a_(392217, _n_(392216, "kn", lambda: kn), "Distancess"), _n_(392218, "training_data_10_columns", lambda: training_data_10_columns), _n_(392219, "query_instance", lambda: query_instance))
        _l_(392221)

        weight_based_average = _c_(392228, _a_(392223, _n_(392222, "kn", lambda: kn), "weight"), _n_(392224, "training_data", lambda: training_data), _n_(392225, "distances", lambda: distances), _n_(392226, "euclidean_indices", lambda: euclidean_indices), _n_(392227, "kn_k_value", lambda: kn_k_value))
        _l_(392229)

        if _n_(392230, "query_instance", lambda: query_instance)[-1] == _n_(392231, "weight_based_average", lambda: weight_based_average):
            _l_(392233)

            eucl_weight_prediction_count += 1
            _l_(392232)
    aux = _n_(392235, "eucl_weight_prediction_count", lambda: eucl_weight_prediction_count) / _c_(392238, _n_(392236, "len", lambda: len), _n_(392237, "test_data", lambda: test_data)) * 100
    _l_(392239)

    return aux


def main():
    _l_(392317)

    global accuracies
    _l_(392241)
    euclidean_accuracies = []
    _l_(392242)
    k_samples = []
    _l_(392243)
    _c_(392250, _a_(392245, _n_(392244, "k_samples", lambda: k_samples), "extend"), _c_(392249, _n_(392246, "list", lambda: list), _c_(392248, _n_(392247, "range", lambda: range), 1, 4, 1)))
    _l_(392251)

    _c_(392256, _n_(392252, "print", lambda: print), "Range" + _c_(392255, _n_(392253, "str", lambda: str), _n_(392254, "k_samples", lambda: k_samples)))
    _l_(392257)

    for k in _n_(392258, "k_samples", lambda: k_samples):
        _l_(392284)

        training_file = "classification/trainingData.csv"
        _l_(392259)
        test_file = "classification/testData.csv"
        _l_(392260)
        kn_k_value = _n_(392261, "k", lambda: k)
        _l_(392262)

        training_data = _c_(392266, _a_(392264, _n_(392263, "np", lambda: np), "genfromtxt"), _n_(392265, "training_file", lambda: training_file), delimiter=",")
        _l_(392267)
        test_data = _c_(392271, _a_(392269, _n_(392268, "np", lambda: np), "genfromtxt"), _n_(392270, "test_file", lambda: test_file), delimiter=",")
        _l_(392272)

        accuracies = _c_(392277, _n_(392273, "weight_based_approach", lambda: weight_based_approach), _n_(392274, "training_data", lambda: training_data), _n_(392275, "test_data", lambda: test_data), _n_(392276, "kn_k_value", lambda: kn_k_value))
        _l_(392278)
        _c_(392282, _a_(392280, _n_(392279, "euclidean_accuracies", lambda: euclidean_accuracies), "append"), _n_(392281, "accuracies", lambda: accuracies)[0])
        _l_(392283)

    _c_(392289, _n_(392285, "print", lambda: print), "distance: " + _c_(392288, _n_(392286, "str", lambda: str), _n_(392287, "euclidean_accuracies", lambda: euclidean_accuracies)))
    _l_(392290)

    _c_(392295, _a_(392292, _n_(392291, "plt", lambda: plt), "plot"), _n_(392293, "k_samples", lambda: k_samples), _n_(392294, "euclidean_accuracies", lambda: euclidean_accuracies), 'r')
    _l_(392296)
    _c_(392299, _a_(392298, _n_(392297, "plt", lambda: plt), "xlabel"), 'K{Number of Nearest Neighbour(s)}')
    _l_(392300)
    _c_(392303, _a_(392302, _n_(392301, "plt", lambda: plt), "ylabel"), 'Accuracy %')
    _l_(392304)
    _c_(392307, _a_(392306, _n_(392305, "plt", lambda: plt), "title"), 'K vs Accuracy graph')
    _l_(392308)
    _c_(392311, _a_(392310, _n_(392309, "plt", lambda: plt), "grid"), True)
    _l_(392312)
    _c_(392315, _a_(392314, _n_(392313, "plt", lambda: plt), "show"))
    _l_(392316)


if _n_(392318, "__name__", lambda: __name__) == '__main__':
    _l_(392322)

    _c_(392320, _n_(392319, "main", lambda: main))
    _l_(392321)
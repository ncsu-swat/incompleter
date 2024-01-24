# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75030446/attributeerror-kmeans-object-has-no-attribute-labels-pytorch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class KMeansInitMostDistantFromMean:
    _l_(614846)

    def __call__(self, *args, **kwargs):
        _l_(614845)

        X, k = _n_(614817, "args", lambda: args)
        _l_(614818)
        mean = _c_(614822, _a_(614820, _n_(614819, "np", lambda: np), "mean"), _n_(614821, "X", lambda: X), axis=0)
        _l_(614823)
        arg_sorted = _c_(614834, _a_(614825, _n_(614824, "np", lambda: np), "argsort"), _c_(614833, _a_(614827, _n_(614826, "np", lambda: np), "apply_along_axis"), lambda y: _c_(614831, _n_(614828, "euclidean", lambda: euclidean), _n_(614829, "mean", lambda: mean), _n_(614830, "y", lambda: y)), 1, _n_(614832, "X", lambda: X)))
        _l_(614835)
        output = _n_(614836, "X", lambda: X)[_c_(614840, _a_(614838, _n_(614837, "np", lambda: np), "flip"), _n_(614839, "arg_sorted", lambda: arg_sorted))[:_n_(614841, "k", lambda: k)]]
        _l_(614842)
        aux = _n_(614843, "output", lambda: output)
        _l_(614844)
        return aux

class KMeansInit:
    _l_(614913)

    def __call__(self, *args, **kwargs):
        _l_(614869)

        X, k = _n_(614847, "args", lambda: args)
        _l_(614848)
        current_centroids = _c_(614855, _a_(614850, _n_(614849, "np", lambda: np), "expand_dims"), _c_(614854, _a_(614852, _n_(614851, "np", lambda: np), "mean"), _n_(614853, "X", lambda: X), axis=0), 0)
        _l_(614856)
        for i in _c_(614859, _n_(614857, "range", lambda: range), _n_(614858, "k", lambda: k) - 1):
            _l_(614866)

            X, current_centroids = _c_(614864, _a_(614861, _n_(614860, "self", lambda: self), "next_centroid"), _n_(614862, "X", lambda: X), _n_(614863, "current_centroids", lambda: current_centroids))
            _l_(614865)
        aux = _n_(614867, "current_centroids", lambda: current_centroids)
        _l_(614868)

        return aux

    def next_centroid(self, X, curr_centroids):
        _l_(614912)

        highest_dist = 0.0
        _l_(614870)
        next_centroid = None
        _l_(614871)
        next_centroid_index = None
        _l_(614872)
        for i, x in _c_(614875, _n_(614873, "enumerate", lambda: enumerate), _n_(614874, "X", lambda: X)):
            _l_(614897)

            max_dist = _c_(614886, _a_(614877, _n_(614876, "np", lambda: np), "amax"), _c_(614885, _a_(614879, _n_(614878, "np", lambda: np), "apply_along_axis"), lambda y: _c_(614883, _n_(614880, "euclidean", lambda: euclidean), _n_(614881, "x", lambda: x), _n_(614882, "y", lambda: y)), 1, _n_(614884, "curr_centroids", lambda: curr_centroids)))
            _l_(614887)
            if _n_(614888, "max_dist", lambda: max_dist) > _n_(614889, "highest_dist", lambda: highest_dist):
                _l_(614896)

                next_centroid = _n_(614890, "x", lambda: x)
                _l_(614891)
                highest_dist = _n_(614892, "max_dist", lambda: max_dist)
                _l_(614893)
                next_centroid_index = _n_(614894, "i", lambda: i)
                _l_(614895)
        aux = _c_(614902, _a_(614899, _n_(614898, "np", lambda: np), "delete"), _n_(614900, "X", lambda: X), _n_(614901, "next_centroid_index", lambda: next_centroid_index), 0), _c_(614910, _a_(614904, _n_(614903, "np", lambda: np), "append"), _n_(614905, "curr_centroids", lambda: curr_centroids), _c_(614909, _a_(614907, _n_(614906, "np", lambda: np), "expand_dims"), _n_(614908, "next_centroid", lambda: next_centroid), 0), 0)
        _l_(614911)

        return aux


class Conv(_a_(614915, _n_(614914, "gnn", lambda: gnn), "MessagePassing")):
    _l_(615040)

   
    def __init__(self, sigma: _a_(614916, nn, "Module"), F: _a_(614917, nn, "Module"), W: _a_(614918, nn, "Module"), M: _a_(614919, nn, "Module"), C: _n_(614920, "int", lambda: int), P: _n_(614921, "int", lambda: int)):
        _l_(614951)

       
        _c_(614924, _a_(614923, _n_(614922, "super", lambda: super)(), "__init__"), aggr="mean")
        _l_(614925)
        _n_(614926, "self", lambda: self).sigma = _n_(614927, "sigma", lambda: sigma)
        _l_(614928)
        _n_(614929, "self", lambda: self).F = _n_(614930, "F", lambda: F)
        _l_(614931)
        _n_(614932, "self", lambda: self).W = _n_(614933, "W", lambda: W)
        _l_(614934)
        _n_(614935, "self", lambda: self).M = _n_(614936, "M", lambda: M)
        _l_(614937)
        _n_(614938, "self", lambda: self).C = _n_(614939, "C", lambda: C)
        _l_(614940)
        _n_(614941, "self", lambda: self).P = _n_(614942, "P", lambda: P)
        _l_(614943)
        _n_(614944, "self", lambda: self).B = _c_(614949, _a_(614946, _n_(614945, "torch", lambda: torch), "randn"), _n_(614947, "C", lambda: C)+_n_(614948, "P", lambda: P), requires_grad=True)
        _l_(614950)

    def forward(self, feature_matrix, edge_index):
        _l_(614958)

        aux = _c_(614956, _a_(614953, _n_(614952, "self", lambda: self), "propagate"), _n_(614954, "edge_index", lambda: edge_index), feature_matrix=_n_(614955, "feature_matrix", lambda: feature_matrix))
        _l_(614957)
        return aux

    def message(self, feature_matrix_i, feature_matrix_j):
        _l_(614989)

        message = _c_(614963, _a_(614960, _n_(614959, "self", lambda: self), "F"), _n_(614961, "feature_matrix_j", lambda: feature_matrix_j) - _n_(614962, "feature_matrix_i", lambda: feature_matrix_i))
        _l_(614964)
        message = _c_(614973, _a_(614966, _n_(614965, "message", lambda: message), "view"), -1, _a_(614968, _n_(614967, "self", lambda: self), "C") + _a_(614970, _n_(614969, "self", lambda: self), "P"), _a_(614972, _n_(614971, "self", lambda: self), "C"))
        _l_(614974)
        feature_matrix_i_ = _c_(614977, _a_(614976, _n_(614975, "feature_matrix_i", lambda: feature_matrix_i), "unsqueeze"), 2)
        _l_(614978)
        output = _c_(614985, _a_(614984, _c_(614983, _a_(614980, _n_(614979, "torch", lambda: torch), "bmm"), _n_(614981, "message", lambda: message), _n_(614982, "feature_matrix_i_", lambda: feature_matrix_i_)), "squeeze"))
        _l_(614986)
        aux = _n_(614987, "output", lambda: output)
        _l_(614988)
        return aux

    def update(self, aggr_out, feature_matrix):
        _l_(615039)

        Weight = _c_(614993, _a_(614991, _n_(614990, "self", lambda: self), "M"), _n_(614992, "aggr_out", lambda: aggr_out))
        _l_(614994)
        aggr_out = _n_(614995, "aggr_out", lambda: aggr_out) * _n_(614996, "Weight", lambda: Weight)
        _l_(614997)
        transform = _c_(615001, _a_(614999, _n_(614998, "self", lambda: self), "W"), _n_(615000, "feature_matrix", lambda: feature_matrix))
        _l_(615002)
        transform = _c_(615011, _a_(615004, _n_(615003, "transform", lambda: transform), "view"), -1, _a_(615006, _n_(615005, "self", lambda: self), "C") + _a_(615008, _n_(615007, "self", lambda: self), "P"), _a_(615010, _n_(615009, "self", lambda: self), "C"))
        _l_(615012)
        feature_matrix = _c_(615015, _a_(615014, _n_(615013, "feature_matrix", lambda: feature_matrix), "unsqueeze"), 2)
        _l_(615016)
        transformation = _c_(615023, _a_(615022, _c_(615021, _a_(615018, _n_(615017, "torch", lambda: torch), "bmm"), _n_(615019, "transform", lambda: transform), _n_(615020, "feature_matrix", lambda: feature_matrix)), "squeeze"))
        _l_(615024)
        aggr_out = _n_(615025, "aggr_out", lambda: aggr_out) + _n_(615026, "transformation", lambda: transformation)
        _l_(615027)
        output = _n_(615028, "aggr_out", lambda: aggr_out) + _a_(615030, _n_(615029, "self", lambda: self), "B")
        _l_(615031)
        output = _c_(615035, _a_(615033, _n_(615032, "self", lambda: self), "sigma"), _n_(615034, "output", lambda: output))
        _l_(615036)
        aux = _n_(615037, "output", lambda: output)
        _l_(615038)
        return aux


class Aggregation(_a_(615042, _n_(615041, "nn", lambda: nn), "Module")):
    _l_(615137)

    
    def __init__(self, mlp1: _a_(615043, nn, "Module"), mlp2: _a_(615044, nn, "Module")):
        _l_(615060)

       
        _c_(615047, _a_(615046, _n_(615045, "super", lambda: super)(), "__init__"))
        _l_(615048)
        _n_(615049, "self", lambda: self).mlp1 = _n_(615050, "mlp1", lambda: mlp1)
        _l_(615051)
        _n_(615052, "self", lambda: self).mlp2 = _n_(615053, "mlp2", lambda: mlp2)
        _l_(615054)
        _n_(615055, "self", lambda: self).softmax = _c_(615058, _a_(615057, _n_(615056, "nn", lambda: nn), "Softmax"), 0)
        _l_(615059)

    def forward(self, feature_matrix_batch: _a_(615061, torch, "Tensor"), conv_feature_matrix_batch: _a_(615062, torch, "Tensor")):
        _l_(615136)

        N, I, D = _c_(615065, _a_(615064, _n_(615063, "feature_matrix_batch", lambda: feature_matrix_batch), "size"))
        _l_(615066)
        N_, I_, D_ = _c_(615069, _a_(615068, _n_(615067, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch), "size"))
        _l_(615070)
        augmentation = _n_(615071, "D_", lambda: D_) - _n_(615072, "D", lambda: D)
        _l_(615073)
        if _n_(615074, "augmentation", lambda: augmentation) > 0:
            _l_(615081)

            feature_matrix_batch = _c_(615079, _a_(615076, _n_(615075, "F", lambda: F), "pad"), _n_(615077, "feature_matrix_batch", lambda: feature_matrix_batch), (0, _n_(615078, "augmentation", lambda: augmentation)))
            _l_(615080)
        S1 = _c_(615085, _a_(615083, _n_(615082, "torch", lambda: torch), "mean"), _n_(615084, "feature_matrix_batch", lambda: feature_matrix_batch), 1)
        _l_(615086)
        S2 = _c_(615090, _a_(615088, _n_(615087, "torch", lambda: torch), "mean"), _n_(615089, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch), 1)
        _l_(615091)
        Z1 = _c_(615095, _a_(615093, _n_(615092, "self", lambda: self), "mlp1"), _n_(615094, "S1", lambda: S1))
        _l_(615096)
        Z2 = _c_(615100, _a_(615098, _n_(615097, "self", lambda: self), "mlp2"), _n_(615099, "S2", lambda: S2))
        _l_(615101)
        M = _c_(615109, _a_(615103, _n_(615102, "self", lambda: self), "softmax"), _c_(615108, _a_(615105, _n_(615104, "torch", lambda: torch), "stack"), (_n_(615106, "Z1", lambda: Z1), _n_(615107, "Z2", lambda: Z2)), 0))
        _l_(615110)
        M1 = _n_(615111, "M", lambda: M)[0]
        _l_(615112)
        M2 = _n_(615113, "M", lambda: M)[1]
        _l_(615114)
        M1 = _c_(615120, _a_(615118, _c_(615117, _a_(615116, _n_(615115, "M1", lambda: M1), "unsqueeze"), 1), "expand"), -1, _n_(615119, "I", lambda: I), -1)
        _l_(615121)
        M2 = _c_(615127, _a_(615125, _c_(615124, _a_(615123, _n_(615122, "M2", lambda: M2), "unsqueeze"), 1), "expand"), -1, _n_(615126, "I", lambda: I), -1)
        _l_(615128)
        output = (_n_(615129, "M1", lambda: M1) * _n_(615130, "feature_matrix_batch", lambda: feature_matrix_batch)) + (_n_(615131, "M2", lambda: M2) * _n_(615132, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch))
        _l_(615133)
        aux = _n_(615134, "output", lambda: output)
        _l_(615135)
        return aux


class MaxPool(_a_(615139, _n_(615138, "nn", lambda: nn), "Module")):
    _l_(615175)

    
    def __init__(self, k: _n_(615140, "int", lambda: int)):
        _l_(615148)

        
        _c_(615143, _a_(615142, _n_(615141, "super", lambda: super)(), "__init__"))
        _l_(615144)
        _n_(615145, "self", lambda: self).k = _n_(615146, "k", lambda: k)
        _l_(615147)

    def forward(self, feature_matrix_batch: _a_(615149, torch, "Tensor"), cluster_index: _a_(615150, torch, "Tensor")):
        _l_(615174)

       
        N, I, D = _c_(615153, _a_(615152, _n_(615151, "feature_matrix_batch", lambda: feature_matrix_batch), "size"))
        _l_(615154)
        feature_matrix_batch = _c_(615158, _a_(615156, _n_(615155, "feature_matrix_batch", lambda: feature_matrix_batch), "view"), -1, _n_(615157, "D", lambda: D))
        _l_(615159)
        output = _c_(615163, _n_(615160, "scatter_max", lambda: scatter_max), _n_(615161, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615162, "cluster_index", lambda: cluster_index), dim=0)[0]
        _l_(615164)
        output = _c_(615170, _a_(615166, _n_(615165, "output", lambda: output), "view"), _n_(615167, "N", lambda: N), _a_(615169, _n_(615168, "self", lambda: self), "k"), -1)
        _l_(615171)
        aux = _n_(615172, "output", lambda: output)
        _l_(615173)
        
        return aux


class GraphConvPool3DPnet(_a_(615177, _n_(615176, "nn", lambda: nn), "Module")):
    _l_(615207)

    
    def __init__(self, shrinkingLayers: [ShrinkingUnit], mlp: _a_(615178, nn, "Module")):
        _l_(615190)

        _c_(615181, _a_(615180, _n_(615179, "super", lambda: super)(), "__init__"))
        _l_(615182)
        _n_(615183, "self", lambda: self).neuralNet = _c_(615188, _a_(615185, _n_(615184, "nn", lambda: nn), "Sequential"), *_n_(615186, "shrinkingLayers", lambda: shrinkingLayers), _n_(615187, "mlp", lambda: mlp))
        _l_(615189)

    def forward(self, x: _a_(615191, torch, "Tensor"), pos: _a_(615192, torch, "Tensor")):
        _l_(615206)

        feature_matrix_batch = _c_(615197, _a_(615194, _n_(615193, "torch", lambda: torch), "cat"), (_n_(615195, "pos", lambda: pos), _n_(615196, "x", lambda: x)), 2) if _n_(615198, "x", lambda: x) is not None else _n_(615199, "pos", lambda: pos)
        _l_(615200)
        aux = _c_(615204, _a_(615202, _n_(615201, "self", lambda: self), "neuralNet"), _n_(615203, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615205)
        return aux

class ShrinkingUnitStack(_a_(615209, _n_(615208, "nn", lambda: nn), "Module")):
    _l_(615298)

   
    def __init__(self, input_stack: _n_(615210, "int", lambda: int), stack_fork: _n_(615211, "int", lambda: int), mlp: _a_(615212, nn, "Module"), learning_rate: _n_(615213, "int", lambda: int), k: _n_(615214, "int", lambda: int), kmeansInit, n_init, sigma: _a_(615215, nn, "Module"), F: _a_(615216, nn, "Module"), W: _a_(615217, nn, "Module"),
                 M: _a_(615218, nn, "Module"), C, P, mlp1: _a_(615219, nn, "Module"), mlp2: _a_(615220, nn, "Module")):
        _l_(615265)

       
        _c_(615223, _a_(615222, _n_(615221, "super", lambda: super)(), "__init__"))
        _l_(615224)
        _n_(615225, "self", lambda: self).stack_fork = _n_(615226, "stack_fork", lambda: stack_fork)
        _l_(615227)
        stack_size = _n_(615228, "input_stack", lambda: input_stack) * _n_(615229, "stack_fork", lambda: stack_fork)
        _l_(615230)
        _n_(615231, "self", lambda: self).selfCorrStack = _c_(615236, _n_(615232, "SelfCorrelationStack", lambda: SelfCorrelationStack), _n_(615233, "stack_size", lambda: stack_size), _n_(615234, "mlp", lambda: mlp), _n_(615235, "learning_rate", lambda: learning_rate))
        _l_(615237)
        _n_(615238, "self", lambda: self).kmeansConvStack = _c_(615250, _n_(615239, "KMeansConvStack", lambda: KMeansConvStack), _n_(615240, "stack_size", lambda: stack_size), _n_(615241, "k", lambda: k), _n_(615242, "kmeansInit", lambda: kmeansInit), _n_(615243, "n_init", lambda: n_init), _n_(615244, "sigma", lambda: sigma), _n_(615245, "F", lambda: F), _n_(615246, "W", lambda: W), _n_(615247, "M", lambda: M), _n_(615248, "C", lambda: C), _n_(615249, "P", lambda: P))
        _l_(615251)
        _n_(615252, "self", lambda: self).localAdaptFeaAggreStack = _c_(615257, _n_(615253, "AggregationStack", lambda: AggregationStack), _n_(615254, "stack_size", lambda: stack_size), _n_(615255, "mlp1", lambda: mlp1), _n_(615256, "mlp2", lambda: mlp2))
        _l_(615258)
        _n_(615259, "self", lambda: self).graphMaxPoolStack = _c_(615263, _n_(615260, "MaxPoolStack", lambda: MaxPoolStack), _n_(615261, "stack_size", lambda: stack_size), _n_(615262, "k", lambda: k))
        _l_(615264)

    def forward(self, feature_matrix_batch):
        _l_(615297)

        
        feature_matrix_batch = _c_(615271, _a_(615267, _n_(615266, "torch", lambda: torch), "repeat_interleave"), _n_(615268, "feature_matrix_batch", lambda: feature_matrix_batch), _a_(615270, _n_(615269, "self", lambda: self), "stack_fork"), dim=0)
        _l_(615272)
        
        feature_matrix_batch = _c_(615276, _a_(615274, _n_(615273, "self", lambda: self), "selfCorrStack"), _n_(615275, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615277)
        
        feature_matrix_batch_, conv_feature_matrix_batch, cluster_index = _c_(615281, _a_(615279, _n_(615278, "self", lambda: self), "kmeansConvStack"), _n_(615280, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615282)
        feature_matrix_batch = _c_(615287, _a_(615284, _n_(615283, "self", lambda: self), "localAdaptFeaAggreStack"), _n_(615285, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615286, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch))
        _l_(615288)
        output = _c_(615293, _a_(615290, _n_(615289, "self", lambda: self), "graphMaxPoolStack"), _n_(615291, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615292, "cluster_index", lambda: cluster_index))
        _l_(615294)
        aux = _n_(615295, "output", lambda: output)
        _l_(615296)
       
        return aux


class SelfCorrelationStack(_a_(615300, _n_(615299, "nn", lambda: nn), "Module")):
    _l_(615339)

   
    def __init__(self, stack_size: _n_(615301, "int", lambda: int), mlp: _a_(615302, nn, "Module"), learning_rate: _n_(615303, "int", lambda: int) = 1.0):
        _l_(615328)

       
        _c_(615306, _a_(615305, _n_(615304, "super", lambda: super)(), "__init__"))
        _l_(615307)
        _n_(615308, "self", lambda: self).selfCorrelationStack = _c_(615321, _a_(615310, _n_(615309, "nn", lambda: nn), "ModuleList"), [_c_(615317, _n_(615311, "SelfCorrelation", lambda: SelfCorrelation), _c_(615315, _a_(615313, _n_(615312, "copy", lambda: copy), "deepcopy"), _n_(615314, "mlp", lambda: mlp)), _n_(615316, "learning_rate", lambda: learning_rate)) for i in _c_(615320, _n_(615318, "range", lambda: range), _n_(615319, "stack_size", lambda: stack_size))])
        _l_(615322)
        _c_(615326, _a_(615324, _n_(615323, "self", lambda: self), "apply"), _n_(615325, "init_weights", lambda: init_weights))
        _l_(615327)

    def forward(self, feature_matrix_batch: _a_(615329, torch, "Tensor")):
        _l_(615338)

        # feature_matrix_batch size = (S,N,I,D) where S=stack_size, N=batch number, I=members, D=member dimensionality
        output = _c_(615334, _n_(615330, "selfCorrThreader", lambda: selfCorrThreader), _a_(615332, _n_(615331, "self", lambda: self), "selfCorrelationStack"), _n_(615333, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615335)
        aux = _n_(615336, "output", lambda: output)
        _l_(615337)
        # output size = (S,N,I,D) where where S=stack_size, N=batch number, I=members, D=member dimensionality
        return aux


class KMeansConvStack(_a_(615341, _n_(615340, "nn", lambda: nn), "Module")):
    _l_(615404)

    
    def __init__(self, stack_size: _n_(615342, "int", lambda: int), k: _n_(615343, "int", lambda: int), kmeansInit, n_init: _n_(615344, "int", lambda: int), sigma: _a_(615345, nn, "Module"), F: _a_(615346, nn, "Module"), W: _a_(615347, nn, "Module"),
                 M: _a_(615348, nn, "Module"), C: _n_(615349, "int", lambda: int), P: _n_(615350, "int", lambda: int)):
        _l_(615391)

        
        _c_(615353, _a_(615352, _n_(615351, "super", lambda: super)(), "__init__"))
        _l_(615354)
        _n_(615355, "self", lambda: self).kmeansConvStack = _c_(615384, _a_(615357, _n_(615356, "nn", lambda: nn), "ModuleList"), [
            _c_(615380, _n_(615358, "KMeansConv", lambda: KMeansConv), _n_(615359, "k", lambda: k), _n_(615360, "kmeansInit", lambda: kmeansInit), _n_(615361, "n_init", lambda: n_init), _c_(615365, _a_(615363, _n_(615362, "copy", lambda: copy), "deepcopy"), _n_(615364, "sigma", lambda: sigma)), _c_(615369, _a_(615367, _n_(615366, "copy", lambda: copy), "deepcopy"), _n_(615368, "F", lambda: F)), _c_(615373, _a_(615371, _n_(615370, "copy", lambda: copy), "deepcopy"), _n_(615372, "W", lambda: W)),
                       _c_(615377, _a_(615375, _n_(615374, "copy", lambda: copy), "deepcopy"), _n_(615376, "M", lambda: M)), _n_(615378, "C", lambda: C), _n_(615379, "P", lambda: P)) for i in _c_(615383, _n_(615381, "range", lambda: range), _n_(615382, "stack_size", lambda: stack_size))])
        _l_(615385)
        _c_(615389, _a_(615387, _n_(615386, "self", lambda: self), "apply"), _n_(615388, "init_weights", lambda: init_weights))
        _l_(615390)

    def forward(self, feature_matrix_batch: _a_(615392, torch, "Tensor")):
        _l_(615403)

        # feature_matrix_batch size = (S,N,I,D) where S=stack size, N=batch number, I=members, D=member dimensionality
        feature_matrix_batch, conv_feature_matrix_batch, cluster_index = _c_(615397, _n_(615393, "kmeansConvThreader", lambda: kmeansConvThreader), _a_(615395, _n_(615394, "self", lambda: self), "kmeansConvStack"),
                                                                                            _n_(615396, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615398)
        aux = _n_(615399, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615400, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch), _n_(615401, "cluster_index", lambda: cluster_index)
        _l_(615402)
  
        return aux


class AggregationStack(_a_(615406, _n_(615405, "nn", lambda: nn), "Module")):
    _l_(615450)

    
    def __init__(self, stack_size: _n_(615407, "int", lambda: int), mlp1: _a_(615408, nn, "Module"), mlp2: _a_(615409, nn, "Module")):
        _l_(615437)

       
        _c_(615412, _a_(615411, _n_(615410, "super", lambda: super)(), "__init__"))
        _l_(615413)
        _n_(615414, "self", lambda: self).localAdaptFeatAggreStack = _c_(615430, _a_(615416, _n_(615415, "nn", lambda: nn), "ModuleList"), [_c_(615426, _n_(615417, "Aggregation", lambda: Aggregation), _c_(615421, _a_(615419, _n_(615418, "copy", lambda: copy), "deepcopy"), _n_(615420, "mlp1", lambda: mlp1)), _c_(615425, _a_(615423, _n_(615422, "copy", lambda: copy), "deepcopy"), _n_(615424, "mlp2", lambda: mlp2))) for i
                                                       in _c_(615429, _n_(615427, "range", lambda: range), _n_(615428, "stack_size", lambda: stack_size))])
        _l_(615431)
        _c_(615435, _a_(615433, _n_(615432, "self", lambda: self), "apply"), _n_(615434, "init_weights", lambda: init_weights))
        _l_(615436)

    def forward(self, feature_matrix_batch: _a_(615438, torch, "Tensor"), conv_feature_matrix_batch: _a_(615439, torch, "Tensor")):
        _l_(615449)

        
        output = _c_(615445, _n_(615440, "threader", lambda: threader), _a_(615442, _n_(615441, "self", lambda: self), "localAdaptFeatAggreStack"), _n_(615443, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615444, "conv_feature_matrix_batch", lambda: conv_feature_matrix_batch))
        _l_(615446)
        aux = _n_(615447, "output", lambda: output)
        _l_(615448)
        
        return aux


class MaxPoolStack(_a_(615452, _n_(615451, "nn", lambda: nn), "Module")):
    _l_(615488)

    
    def __init__(self, stack_size: _n_(615453, "int", lambda: int), k: _n_(615454, "int", lambda: int)):
        _l_(615475)

        
        _c_(615457, _a_(615456, _n_(615455, "super", lambda: super)(), "__init__"))
        _l_(615458)
        _n_(615459, "self", lambda: self).graphMaxPoolStack = _c_(615468, _a_(615461, _n_(615460, "nn", lambda: nn), "ModuleList"), [_c_(615464, _n_(615462, "MaxPool", lambda: MaxPool), _n_(615463, "k", lambda: k)) for i in _c_(615467, _n_(615465, "range", lambda: range), _n_(615466, "stack_size", lambda: stack_size))])
        _l_(615469)
        _c_(615473, _a_(615471, _n_(615470, "self", lambda: self), "apply"), _n_(615472, "init_weights", lambda: init_weights))
        _l_(615474)

    def forward(self, feature_matrix_batch: _a_(615476, torch, "Tensor"), cluster_index: _a_(615477, torch, "Tensor")):
        _l_(615487)

        
        output = _c_(615483, _n_(615478, "threader", lambda: threader), _a_(615480, _n_(615479, "self", lambda: self), "graphMaxPoolStack"), _n_(615481, "feature_matrix_batch", lambda: feature_matrix_batch), _n_(615482, "cluster_index", lambda: cluster_index))
        _l_(615484)
        aux = _n_(615485, "output", lambda: output)
        _l_(615486)
       
        return aux


def selfCorrThreader(modules, input_tensor):
    _l_(615533)

    list_append = []
    _l_(615489)
    threads = []
    _l_(615490)
    for i, t in _c_(615493, _n_(615491, "enumerate", lambda: enumerate), _n_(615492, "input_tensor", lambda: input_tensor)):
        _l_(615506)

        _c_(615504, _a_(615495, _n_(615494, "threads", lambda: threads), "append"), _c_(615503, _n_(615496, "Thread", lambda: Thread), target=_n_(615497, "selfCorrAppender", lambda: selfCorrAppender), args=(_n_(615498, "modules", lambda: modules)[_n_(615499, "i", lambda: i)], _n_(615500, "t", lambda: t), _n_(615501, "list_append", lambda: list_append), _n_(615502, "i", lambda: i))))
        _l_(615505)
    [_c_(615509, _a_(615508, _n_(615507, "t", lambda: t), "start")) for t in _n_(615510, "threads", lambda: threads)]
    _l_(615511)
    [_c_(615514, _a_(615513, _n_(615512, "t", lambda: t), "join")) for t in _n_(615515, "threads", lambda: threads)]
    _l_(615516)
    _c_(615519, _a_(615518, _n_(615517, "list_append", lambda: list_append), "sort"))
    _l_(615520)
    list_append = _c_(615526, _n_(615521, "list", lambda: list), _c_(615525, _n_(615522, "map", lambda: map), lambda x: _n_(615523, "x", lambda: x)[1], _n_(615524, "list_append", lambda: list_append)))
    _l_(615527)
    aux = _c_(615531, _a_(615529, _n_(615528, "torch", lambda: torch), "stack"), _n_(615530, "list_append", lambda: list_append))
    _l_(615532)
    return aux


def selfCorrAppender(module, tensor, list_append, index):
    _l_(615542)

    _c_(615540, _a_(615535, _n_(615534, "list_append", lambda: list_append), "append"), (_n_(615536, "index", lambda: index), _c_(615539, _n_(615537, "module", lambda: module), _n_(615538, "tensor", lambda: tensor))))
    _l_(615541)


def kmeansConvThreader(modules, input_tensor):
    _l_(615621)

    list1_append = []
    _l_(615543)
    list2_append = []
    _l_(615544)
    list3_append = []
    _l_(615545)
    threads = []
    _l_(615546)
    for i, t in _c_(615549, _n_(615547, "enumerate", lambda: enumerate), _n_(615548, "input_tensor", lambda: input_tensor)):
        _l_(615564)

        _c_(615562, _a_(615551, _n_(615550, "threads", lambda: threads), "append"), _c_(615561, _n_(615552, "Thread", lambda: Thread), target=_n_(615553, "kmeansAppender", lambda: kmeansAppender), args=(_n_(615554, "modules", lambda: modules)[_n_(615555, "i", lambda: i)], _n_(615556, "t", lambda: t), _n_(615557, "list1_append", lambda: list1_append), _n_(615558, "list2_append", lambda: list2_append), _n_(615559, "list3_append", lambda: list3_append), _n_(615560, "i", lambda: i))))
        _l_(615563)
    [_c_(615567, _a_(615566, _n_(615565, "t", lambda: t), "start")) for t in _n_(615568, "threads", lambda: threads)]
    _l_(615569)
    [_c_(615572, _a_(615571, _n_(615570, "t", lambda: t), "join")) for t in _n_(615573, "threads", lambda: threads)]
    _l_(615574)
    _c_(615577, _a_(615576, _n_(615575, "list1_append", lambda: list1_append), "sort"))
    _l_(615578)
    _c_(615581, _a_(615580, _n_(615579, "list2_append", lambda: list2_append), "sort"))
    _l_(615582)
    _c_(615585, _a_(615584, _n_(615583, "list3_append", lambda: list3_append), "sort"))
    _l_(615586)
    list1_append = _c_(615592, _n_(615587, "list", lambda: list), _c_(615591, _n_(615588, "map", lambda: map), lambda x: _n_(615589, "x", lambda: x)[1], _n_(615590, "list1_append", lambda: list1_append)))
    _l_(615593)
    list2_append = _c_(615599, _n_(615594, "list", lambda: list), _c_(615598, _n_(615595, "map", lambda: map), lambda x: _n_(615596, "x", lambda: x)[1], _n_(615597, "list2_append", lambda: list2_append)))
    _l_(615600)
    list3_append = _c_(615606, _n_(615601, "list", lambda: list), _c_(615605, _n_(615602, "map", lambda: map), lambda x: _n_(615603, "x", lambda: x)[1], _n_(615604, "list3_append", lambda: list3_append)))
    _l_(615607)
    aux = _c_(615611, _a_(615609, _n_(615608, "torch", lambda: torch), "stack"), _n_(615610, "list1_append", lambda: list1_append)), _c_(615615, _a_(615613, _n_(615612, "torch", lambda: torch), "stack"), _n_(615614, "list2_append", lambda: list2_append)), _c_(615619, _a_(615617, _n_(615616, "torch", lambda: torch), "stack"), _n_(615618, "list3_append", lambda: list3_append))
    _l_(615620)
    return aux


def kmeansAppender(module, input, list1_append, list2_append, list3_append, index):
    _l_(615644)

    x, y, z = _c_(615624, _n_(615622, "module", lambda: module), _n_(615623, "input", lambda: input))
    _l_(615625)
    _c_(615630, _a_(615627, _n_(615626, "list1_append", lambda: list1_append), "append"), (_n_(615628, "index", lambda: index), _n_(615629, "x", lambda: x)))
    _l_(615631)
    _c_(615636, _a_(615633, _n_(615632, "list2_append", lambda: list2_append), "append"), (_n_(615634, "index", lambda: index), _n_(615635, "y", lambda: y)))
    _l_(615637)
    _c_(615642, _a_(615639, _n_(615638, "list3_append", lambda: list3_append), "append"), (_n_(615640, "index", lambda: index), _n_(615641, "z", lambda: z)))
    _l_(615643)


def threader(modules, input_tensor1, input_tensor2):
    _l_(615691)

    list_append = []
    _l_(615645)
    threads = []
    _l_(615646)
    for i, t in _c_(615649, _n_(615647, "enumerate", lambda: enumerate), _n_(615648, "input_tensor1", lambda: input_tensor1)):
        _l_(615664)

        _c_(615662, _a_(615651, _n_(615650, "threads", lambda: threads), "append"), _c_(615661, _n_(615652, "Thread", lambda: Thread), target=_n_(615653, "threaderAppender", lambda: threaderAppender), args=(_n_(615654, "modules", lambda: modules)[_n_(615655, "i", lambda: i)], _n_(615656, "t", lambda: t), _n_(615657, "input_tensor2", lambda: input_tensor2)[_n_(615658, "i", lambda: i)], _n_(615659, "list_append", lambda: list_append), _n_(615660, "i", lambda: i))))
        _l_(615663)
    [_c_(615667, _a_(615666, _n_(615665, "t", lambda: t), "start")) for t in _n_(615668, "threads", lambda: threads)]
    _l_(615669)
    [_c_(615672, _a_(615671, _n_(615670, "t", lambda: t), "join")) for t in _n_(615673, "threads", lambda: threads)]
    _l_(615674)
    _c_(615677, _a_(615676, _n_(615675, "list_append", lambda: list_append), "sort"))
    _l_(615678)
    list_append = _c_(615684, _n_(615679, "list", lambda: list), _c_(615683, _n_(615680, "map", lambda: map), lambda x: _n_(615681, "x", lambda: x)[1], _n_(615682, "list_append", lambda: list_append)))
    _l_(615685)
    aux = _c_(615689, _a_(615687, _n_(615686, "torch", lambda: torch), "stack"), _n_(615688, "list_append", lambda: list_append))
    _l_(615690)
    return aux


def threaderAppender(module, t1, t2, list_append, index):
    _l_(615701)

    _c_(615699, _a_(615693, _n_(615692, "list_append", lambda: list_append), "append"), (_n_(615694, "index", lambda: index), _c_(615698, _n_(615695, "module", lambda: module), _n_(615696, "t1", lambda: t1), _n_(615697, "t2", lambda: t2))))
    _l_(615700)


class Classifier(_a_(615703, _n_(615702, "nn", lambda: nn), "Module")):
    _l_(615742)

    
    def __init__(self, shrinkingLayersStack: [_n_(615704, "ShrinkingUnitStack", lambda: ShrinkingUnitStack)], mlp: _a_(615705, nn, "Module")):
        _l_(615719)

       
        _c_(615708, _a_(615707, _n_(615706, "super", lambda: super)(), "__init__"))
        _l_(615709)
        _n_(615710, "self", lambda: self).neuralNet = _c_(615714, _a_(615712, _n_(615711, "nn", lambda: nn), "Sequential"), *_n_(615713, "shrinkingLayersStack", lambda: shrinkingLayersStack))
        _l_(615715)
        _n_(615716, "self", lambda: self).mlp = _n_(615717, "mlp", lambda: mlp)
        _l_(615718)

    def forward(self, x: _a_(615720, torch, "Tensor"), pos: _a_(615721, torch, "Tensor")):
        _l_(615741)

       
        feature_matrix_batch = _c_(615724, _a_(615723, _n_(615722, "pos", lambda: pos), "unsqueeze"), 0)
        _l_(615725)
        
        output = _c_(615729, _a_(615727, _n_(615726, "self", lambda: self), "neuralNet"), _n_(615728, "feature_matrix_batch", lambda: feature_matrix_batch))
        _l_(615730)
        
        output = _c_(615734, _a_(615732, _n_(615731, "torch", lambda: torch), "mean"), _n_(615733, "output", lambda: output), dim=0)
        _l_(615735)
        aux = _c_(615739, _a_(615737, _n_(615736, "self", lambda: self), "mlp"), _n_(615738, "output", lambda: output))
        _l_(615740)
        
        return aux
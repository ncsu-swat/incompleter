# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70609503/how-to-fix-typeerror-caught-typeerror-in-dataloader-worker-process-1-in-detectr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from detectron2.engine import DefaultTrainer
    _l_(434793)

except ImportError:
    pass

# TOTAL_NUM_IMAGES = 10531

cfg = _c_(434795, _n_(434794, "get_cfg", lambda: get_cfg))
_l_(434796)
_n_(434797, "cfg", lambda: cfg).OUTPUT_DIR = _c_(434801, _a_(434800, _a_(434799, _n_(434798, "os", lambda: os), "path"), "join"), './output')
_l_(434802)
_c_(434808, _a_(434804, _n_(434803, "cfg", lambda: cfg), "merge_from_file"), _c_(434807, _a_(434806, _n_(434805, "model_zoo", lambda: model_zoo), "get_config_file"), "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
_l_(434809)
_a_(434811, _n_(434810, "cfg", lambda: cfg), "DATASETS").TRAIN = ("my_dataset_train",)
_l_(434812)
_a_(434814, _n_(434813, "cfg", lambda: cfg), "DATASETS").TEST = ()
_l_(434815)
_a_(434817, _n_(434816, "cfg", lambda: cfg), "DATALOADER").NUM_WORKERS = 2
_l_(434818)
_a_(434820, _n_(434819, "cfg", lambda: cfg), "MODEL").WEIGHTS = _c_(434823, _a_(434822, _n_(434821, "model_zoo", lambda: model_zoo), "get_checkpoint_url"), "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")  # Let training initialize from model zoo
_l_(434824)  # Let training initialize from model zoo
_a_(434826, _n_(434825, "cfg", lambda: cfg), "SOLVER").IMS_PER_BATCH = 2
_l_(434827)
_a_(434829, _n_(434828, "cfg", lambda: cfg), "SOLVER").BASE_LR = 0.00025  # pick a good LR
_l_(434830)  # pick a good LR

# single_iteration = cfg.SOLVER.IMS_PER_BATCH
# iterations_for_one_epoch = TOTAL_NUM_IMAGES / single_iteration
# cfg.SOLVER.MAX_ITER = int(iterations_for_one_epoch) * 20

_a_(434832, _n_(434831, "cfg", lambda: cfg), "SOLVER").STEPS = []        # do not decay learning rate
_l_(434833)        # do not decay learning rate
_a_(434836, _a_(434835, _n_(434834, "cfg", lambda: cfg), "MODEL"), "ROI_HEADS").NUM_CLASSES = 1  # only has one class (person). (see https://detectron2.readthedocs.io/tutorials/datasets.html#update-the-config-for-new-datasets)
_l_(434837)  # only has one class (person). (see https://detectron2.readthedocs.io/tutorials/datasets.html#update-the-config-for-new-datasets)
# NOTE: this config means the number of classes, but a few popular unofficial tutorials incorrect uses num_classes+1 here.

_c_(434842, _a_(434839, _n_(434838, "os", lambda: os), "makedirs"), _a_(434841, _n_(434840, "cfg", lambda: cfg), "OUTPUT_DIR"), exist_ok=True)
_l_(434843)
trainer = _c_(434846, _n_(434844, "DefaultTrainer", lambda: DefaultTrainer), _n_(434845, "cfg", lambda: cfg)) 
_l_(434847) 
_c_(434850, _a_(434849, _n_(434848, "trainer", lambda: trainer), "resume_or_load"), resume=False)
_l_(434851)
_c_(434854, _a_(434853, _n_(434852, "trainer", lambda: trainer), "train"))
_l_(434855)
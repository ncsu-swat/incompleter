# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75939176/default-collate-typeerror-batch-must-contain-tensors-numbers-dicts-or-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_dataloader(slide_ids: _n_(386511, "List", lambda: List)[_n_(386512, "str", lambda: str)], tile_filenames: _n_(386513, "List", lambda: List)[_n_(386514, "Path", lambda: Path)]) -> _n_(386515, "DataLoader", lambda: DataLoader):
    _l_(386527)

    dataset = _c_(386519, _n_(386516, "ApplicationDataset", lambda: ApplicationDataset), _n_(386517, "slide_ids", lambda: slide_ids), _n_(386518, "tile_filenames", lambda: tile_filenames))
    _l_(386520)
    aux = _c_(386525, _n_(386521, "DataLoader", lambda: DataLoader), _n_(386522, "dataset", lambda: dataset), batch_size=1, shuffle=False, num_workers=1, collate_fn=_a_(386524, _n_(386523, "ApplicationDataset", lambda: ApplicationDataset), "collate"))
    _l_(386526)

    return aux
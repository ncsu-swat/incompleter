# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60191935/typeerror-tuple-object-cannot-be-interpreted-as-an-integer-while-creating-dat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class NumbersDataset(_n_(463154, "Dataset", lambda: Dataset)):
    _l_(463184)

    def __init__(self):
        _l_(463165)

        _n_(463155, "self", lambda: self).X = _c_(463158, _n_(463156, "list", lambda: list), _n_(463157, "df", lambda: df)['input_img'])
        _l_(463159)
        _n_(463160, "self", lambda: self).y = _c_(463163, _n_(463161, "list", lambda: list), _n_(463162, "df", lambda: df)['mask_img'])
        _l_(463164)

    def __len__(self):
        _l_(463175)

        aux = _c_(463169, _n_(463166, "len", lambda: len), _a_(463168, _n_(463167, "self", lambda: self), "X")), _c_(463173, _n_(463170, "len", lambda: len), _a_(463172, _n_(463171, "self", lambda: self), "y"))
        _l_(463174)
        return aux

    def __getitem__(self, idx):
        _l_(463183)

        aux = _a_(463177, _n_(463176, "self", lambda: self), "X")[_n_(463178, "idx", lambda: idx)], _a_(463180, _n_(463179, "self", lambda: self), "y")[_n_(463181, "idx", lambda: idx)]
        _l_(463182)
        return aux


if _n_(463185, "__name__", lambda: __name__) == '__main__':
    _l_(463201)

    dataset = _c_(463187, _n_(463186, "NumbersDataset", lambda: NumbersDataset))
    _l_(463188)
    dataloader = _c_(463191, _n_(463189, "DataLoader", lambda: DataLoader), _n_(463190, "dataset", lambda: dataset), batch_size=50, shuffle=True, num_workers=2)
    _l_(463192)
    # print(len(dataset))
    # plt.imshow(dataset[100])
    # plt.show()
    _c_(463199, _n_(463193, "print", lambda: print), _c_(463198, _n_(463194, "next", lambda: next), _c_(463197, _n_(463195, "iter", lambda: iter), _n_(463196, "dataloader", lambda: dataloader))))
    _l_(463200)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44000486/typeerror-image-data-can-not-convert-to-float-how-to-mitigate-this-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import mean,cov,cumsum,dot,linalg,size,flipud
    _l_(354781)

except ImportError:
    pass
try:
    import numpy as np
    _l_(354783)

except ImportError:
    pass
try:
    from pylab import imread,subplot,imshow,title,gray,figure,show,NullLocator
    _l_(354785)

except ImportError:
    pass

def princomp(A,numpc=0):
    _l_(354836)

    #computing eigenvalues and eigenvectors of covariance matrix
    M = _a_(354791, (_n_(354786, "A", lambda: A)-_c_(354790, _n_(354787, "mean", lambda: mean), _a_(354789, _n_(354788, "A", lambda: A), "T"),axis=1)), "T") # subtract the mean (along columns)
    _l_(354792) # subtract the mean (along columns)
    [latent,coeff] = _c_(354798, _a_(354794, _n_(354793, "linalg", lambda: linalg), "eig"), _c_(354797, _n_(354795, "cov", lambda: cov), _n_(354796, "M", lambda: M)))
    _l_(354799)
    p = _c_(354802, _n_(354800, "size", lambda: size), _n_(354801, "coeff", lambda: coeff),axis=1)
    _l_(354803)
    idx = _c_(354807, _a_(354805, _n_(354804, "np", lambda: np), "argsort"), _n_(354806, "latent", lambda: latent)) # sorting the eigenvalues
    _l_(354808) # sorting the eigenvalues
    idx = _n_(354809, "idx", lambda: idx)[::-1]       # in ascending order
    _l_(354810)       # in ascending order
 #sorting eigenvectors according to the sorted eigenvalues
    coeff = _n_(354811, "coeff", lambda: coeff)[:,_n_(354812, "idx", lambda: idx)]
    _l_(354813)
    latent = _n_(354814, "latent", lambda: latent)[_n_(354815, "idx", lambda: idx)] # sorting eigenvalues
    _l_(354816) # sorting eigenvalues
    if _n_(354817, "numpc", lambda: numpc) < _n_(354818, "p", lambda: p) and _n_(354819, "numpc", lambda: numpc) >= 0:
        _l_(354825)

        coeff = _n_(354820, "coeff", lambda: coeff)[:,_c_(354823, _n_(354821, "range", lambda: range), _n_(354822, "numpc", lambda: numpc))] # cutting some PCs if needed
        _l_(354824) # cutting some PCs if needed
    score = _c_(354830, _n_(354826, "dot", lambda: dot), _a_(354828, _n_(354827, "coeff", lambda: coeff), "T"),_n_(354829, "M", lambda: M)) # projection of the data in the new space
    _l_(354831) # projection of the data in the new space
    aux = _n_(354832, "coeff", lambda: coeff),_n_(354833, "score", lambda: score),_n_(354834, "latent", lambda: latent)
    _l_(354835)
    return aux

A = _c_(354838, _n_(354837, "imread", lambda: imread), 'beatles.jpg') # load an image
_l_(354839) # load an image
A = _c_(354842, _n_(354840, "mean", lambda: mean), _n_(354841, "A", lambda: A),2) # to get a 2-D array
_l_(354843) # to get a 2-D array
full_pc = _c_(354846, _n_(354844, "size", lambda: size), _n_(354845, "A", lambda: A),axis=1) # numbers of all the principal components
_l_(354847) # numbers of all the principal components
i = 1
_l_(354848)
dist = []
_l_(354849)
for numpc in _c_(354852, _n_(354850, "range", lambda: range), 0,_n_(354851, "full_pc", lambda: full_pc)+10,10):
    _l_(354912)

    coeff, score, latent = _c_(354856, _n_(354853, "princomp", lambda: princomp), _n_(354854, "A", lambda: A),_n_(354855, "numpc", lambda: numpc))
    _l_(354857)
    Ar = _a_(354862, _c_(354861, _n_(354858, "dot", lambda: dot), _n_(354859, "coeff", lambda: coeff),_n_(354860, "score", lambda: score)), "T")+_c_(354865, _n_(354863, "mean", lambda: mean), _n_(354864, "A", lambda: A),axis=0) # image reconstruction
    _l_(354866) # image reconstruction
    # difference in Frobenius norm
    _c_(354874, _a_(354868, _n_(354867, "dist", lambda: dist), "append"), _c_(354873, _a_(354870, _n_(354869, "linalg", lambda: linalg), "norm"), _n_(354871, "A", lambda: A)-_n_(354872, "Ar", lambda: Ar),'fro'))
    _l_(354875)
    # showing the pics reconstructed with less than 50 PCs
    if _n_(354876, "numpc", lambda: numpc) <= 50:
        _l_(354911)

        ax = _c_(354879, _n_(354877, "subplot", lambda: subplot), 2,3,_n_(354878, "i", lambda: i),frame_on=False)
        _l_(354880)
        _c_(354886, _a_(354883, _a_(354882, _n_(354881, "ax", lambda: ax), "xaxis"), "set_major_locator"), _c_(354885, _n_(354884, "NullLocator", lambda: NullLocator))) # remove ticks
        _l_(354887) # remove ticks
        _c_(354893, _a_(354890, _a_(354889, _n_(354888, "ax", lambda: ax), "yaxis"), "set_major_locator"), _c_(354892, _n_(354891, "NullLocator", lambda: NullLocator)))
        _l_(354894)
        i += 1 
        _l_(354895) 
        _c_(354900, _n_(354896, "imshow", lambda: imshow), _c_(354899, _n_(354897, "flipud", lambda: flipud), _n_(354898, "Ar", lambda: Ar)))
        _l_(354901)
        _c_(354906, _n_(354902, "title", lambda: title), 'PCs # '+_c_(354905, _n_(354903, "str", lambda: str), _n_(354904, "numpc", lambda: numpc)))
        _l_(354907)
        _c_(354909, _n_(354908, "gray", lambda: gray))
        _l_(354910)

_c_(354914, _n_(354913, "figure", lambda: figure))
_l_(354915)
_c_(354920, _n_(354916, "imshow", lambda: imshow), _c_(354919, _n_(354917, "flipud", lambda: flipud), _n_(354918, "A", lambda: A)))
_l_(354921)
_c_(354923, _n_(354922, "title", lambda: title), 'numpc FULL')
_l_(354924)
_c_(354926, _n_(354925, "gray", lambda: gray))
_l_(354927)
_c_(354929, _n_(354928, "show", lambda: show))
_l_(354930)
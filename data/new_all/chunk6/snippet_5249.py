# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44000486/typeerror-image-data-can-not-convert-to-float-how-to-mitigate-this-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import mean,cov,cumsum,dot,linalg,size,flipud
    _l_(336037)

except ImportError:
    pass
try:
    import numpy as np
    _l_(336039)

except ImportError:
    pass
try:
    from pylab import imread,subplot,imshow,title,gray,figure,show,NullLocator
    _l_(336041)

except ImportError:
    pass

def princomp(A,numpc=0):
    _l_(336092)

    #computing eigenvalues and eigenvectors of covariance matrix
    M = _a_(336047, (_n_(336042, "A", lambda: A)-_c_(336046, _n_(336043, "mean", lambda: mean), _a_(336045, _n_(336044, "A", lambda: A), "T"),axis=1)), "T") # subtract the mean (along columns)
    _l_(336048) # subtract the mean (along columns)
    [latent,coeff] = _c_(336054, _a_(336050, _n_(336049, "linalg", lambda: linalg), "eig"), _c_(336053, _n_(336051, "cov", lambda: cov), _n_(336052, "M", lambda: M)))
    _l_(336055)
    p = _c_(336058, _n_(336056, "size", lambda: size), _n_(336057, "coeff", lambda: coeff),axis=1)
    _l_(336059)
    idx = _c_(336063, _a_(336061, _n_(336060, "np", lambda: np), "argsort"), _n_(336062, "latent", lambda: latent)) # sorting the eigenvalues
    _l_(336064) # sorting the eigenvalues
    idx = _n_(336065, "idx", lambda: idx)[::-1]       # in ascending order
    _l_(336066)       # in ascending order
 #sorting eigenvectors according to the sorted eigenvalues
    coeff = _n_(336067, "coeff", lambda: coeff)[:,_n_(336068, "idx", lambda: idx)]
    _l_(336069)
    latent = _n_(336070, "latent", lambda: latent)[_n_(336071, "idx", lambda: idx)] # sorting eigenvalues
    _l_(336072) # sorting eigenvalues
    if _n_(336073, "numpc", lambda: numpc) < _n_(336074, "p", lambda: p) and _n_(336075, "numpc", lambda: numpc) >= 0:
        _l_(336081)

        coeff = _n_(336076, "coeff", lambda: coeff)[:,_c_(336079, _n_(336077, "range", lambda: range), _n_(336078, "numpc", lambda: numpc))] # cutting some PCs if needed
        _l_(336080) # cutting some PCs if needed
    score = _c_(336086, _n_(336082, "dot", lambda: dot), _a_(336084, _n_(336083, "coeff", lambda: coeff), "T"),_n_(336085, "M", lambda: M)) # projection of the data in the new space
    _l_(336087) # projection of the data in the new space
    aux = _n_(336088, "coeff", lambda: coeff),_n_(336089, "score", lambda: score),_n_(336090, "latent", lambda: latent)
    _l_(336091)
    return aux

A = _c_(336094, _n_(336093, "imread", lambda: imread), 'beatles.jpg') # load an image
_l_(336095) # load an image
A = _c_(336098, _n_(336096, "mean", lambda: mean), _n_(336097, "A", lambda: A),2) # to get a 2-D array
_l_(336099) # to get a 2-D array
full_pc = _c_(336102, _n_(336100, "size", lambda: size), _n_(336101, "A", lambda: A),axis=1) # numbers of all the principal components
_l_(336103) # numbers of all the principal components
i = 1
_l_(336104)
dist = []
_l_(336105)
for numpc in _c_(336108, _n_(336106, "range", lambda: range), 0,_n_(336107, "full_pc", lambda: full_pc)+10,10):
    _l_(336168)

    coeff, score, latent = _c_(336112, _n_(336109, "princomp", lambda: princomp), _n_(336110, "A", lambda: A),_n_(336111, "numpc", lambda: numpc))
    _l_(336113)
    Ar = _a_(336118, _c_(336117, _n_(336114, "dot", lambda: dot), _n_(336115, "coeff", lambda: coeff),_n_(336116, "score", lambda: score)), "T")+_c_(336121, _n_(336119, "mean", lambda: mean), _n_(336120, "A", lambda: A),axis=0) # image reconstruction
    _l_(336122) # image reconstruction
    # difference in Frobenius norm
    _c_(336130, _a_(336124, _n_(336123, "dist", lambda: dist), "append"), _c_(336129, _a_(336126, _n_(336125, "linalg", lambda: linalg), "norm"), _n_(336127, "A", lambda: A)-_n_(336128, "Ar", lambda: Ar),'fro'))
    _l_(336131)
    # showing the pics reconstructed with less than 50 PCs
    if _n_(336132, "numpc", lambda: numpc) <= 50:
        _l_(336167)

        ax = _c_(336135, _n_(336133, "subplot", lambda: subplot), 2,3,_n_(336134, "i", lambda: i),frame_on=False)
        _l_(336136)
        _c_(336142, _a_(336139, _a_(336138, _n_(336137, "ax", lambda: ax), "xaxis"), "set_major_locator"), _c_(336141, _n_(336140, "NullLocator", lambda: NullLocator))) # remove ticks
        _l_(336143) # remove ticks
        _c_(336149, _a_(336146, _a_(336145, _n_(336144, "ax", lambda: ax), "yaxis"), "set_major_locator"), _c_(336148, _n_(336147, "NullLocator", lambda: NullLocator)))
        _l_(336150)
        i += 1 
        _l_(336151) 
        _c_(336156, _n_(336152, "imshow", lambda: imshow), _c_(336155, _n_(336153, "flipud", lambda: flipud), _n_(336154, "Ar", lambda: Ar)))
        _l_(336157)
        _c_(336162, _n_(336158, "title", lambda: title), 'PCs # '+_c_(336161, _n_(336159, "str", lambda: str), _n_(336160, "numpc", lambda: numpc)))
        _l_(336163)
        _c_(336165, _n_(336164, "gray", lambda: gray))
        _l_(336166)

_c_(336170, _n_(336169, "figure", lambda: figure))
_l_(336171)
_c_(336176, _n_(336172, "imshow", lambda: imshow), _c_(336175, _n_(336173, "flipud", lambda: flipud), _n_(336174, "A", lambda: A)))
_l_(336177)
_c_(336179, _n_(336178, "title", lambda: title), 'numpc FULL')
_l_(336180)
_c_(336182, _n_(336181, "gray", lambda: gray))
_l_(336183)
_c_(336185, _n_(336184, "show", lambda: show))
_l_(336186)
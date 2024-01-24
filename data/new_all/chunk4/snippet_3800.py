# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67772067/getting-typeerror-no-loop-matching-the-specified-signature-and-casting-was-foun
# Plotting the KDE Plot 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(645961, _a_(645957, _n_(645956, "sns", lambda: sns), "kdeplot"), _a_(645959, _n_(645958, "x", lambda: x), "loc")[(_n_(645960, "x", lambda: x)['gender']==1),'pixel_per_image'], color='r', shade=True, Label='Male') 
_l_(645962) 
  
_c_(645968, _a_(645964, _n_(645963, "sns", lambda: sns), "kdeplot"), _a_(645966, _n_(645965, "x", lambda: x), "loc")[(_n_(645967, "x", lambda: x)['gender']==0),'pixel_per_image'], color='b', shade=True, Label='Female') 
_l_(645969) 
  
_c_(645972, _a_(645971, _n_(645970, "plt", lambda: plt), "xlabel"), 'Avg pixel value per image') 
_l_(645973) 
_c_(645976, _a_(645975, _n_(645974, "plt", lambda: plt), "ylabel"), 'Probability Density') 
_l_(645977) 
_c_(645980, _a_(645979, _n_(645978, "plt", lambda: plt), "title"), 'Kernel Density Estimate plot to visualize probability density at different values in a continuous variable\n')
_l_(645981)
_c_(645984, _a_(645983, _n_(645982, "plt", lambda: plt), "show"))
_l_(645985)
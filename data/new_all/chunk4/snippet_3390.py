# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74969388/typeerror-unsupported-operand-types-for-list-and-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import numpy as np
 _l_(598215)

except ImportError:
 pass
try:
 from getdist import MCSamples
 _l_(598217)

except ImportError:
 pass
try:
 import os
 _l_(598219)

except ImportError:
 pass
try:
 import imageio
 _l_(598221)

except ImportError:
 pass
try:
 import getdist.plots as gplot
 _l_(598223)

except ImportError:
 pass
try:
 import matplotlib.pyplot as plt
 _l_(598225)

except ImportError:
 pass
try:
 from scipy.misc import derivative
 _l_(598227)

except ImportError:
 pass
try:
 from matplotlib import rc
 _l_(598229)

except ImportError:
 pass
_a_(598231, _n_(598230, "plt", lambda: plt), "rcParams")['text.usetex']=True
_l_(598232)
_c_(598236, _a_(598235, _a_(598234, _n_(598233, "plt", lambda: plt), "rcParams"), "update"), {'font.size': 20})
_l_(598237)
dire=_c_(598240, _a_(598239, _n_(598238, "os", lambda: os), "getcwd")) # This will automatically set your current working directory
_l_(598241) # This will automatically set your current working directory
_c_(598244, _n_(598242, "print", lambda: print), _n_(598243, "dire", lambda: dire))
_l_(598245)
try:
 from scalar_all_eqn import *
 _l_(598247)

except ImportError:
 pass


#Ophi_i,  rd, li, mi, Orad_i, h=0.7, Ob0=0.045, ns=0.96, sigma_8=0.8
#Ophi,  rd, li, mi,  Orad_i, h, sigma8
#Ophi,     rd, li, mi,  Orad_i, h, 0.045, 0.96, sigma8


samps=_c_(598250, _a_(598249, _n_(598248, "np", lambda: np), "loadtxt"), "bao+masers+cmb+hz_c.dat")
_l_(598251)

names = ['Ophi','rd','li','mi','Orad_i','h','sigma8']
_l_(598252)
#names = ['Om0','rd','w0','wa','h','Or0','sigma8']

sample = _c_(598257, _n_(598253, "MCSamples", lambda: MCSamples), samples=_n_(598254, "samps", lambda: samps),names = _n_(598255, "names", lambda: names), labels = _n_(598256, "names", lambda: names))
_l_(598258)
#g = gplot.getSinglePlotter(chain_dir=r'%s'%dire)
#sample = g.sampleAnalyser.samplesForRoot('LCDM')
#sample = g.sampleAnalyser.samplesForRoot('7CPL')
param = _c_(598261, _a_(598260, _n_(598259, "sample", lambda: sample), "getParams"))
_l_(598262)


mean=[]
_l_(598263)
lower=[]
_l_(598264)
upper=[]
_l_(598265)

lower1=[]
_l_(598266)
upper1=[]
_l_(598267)

lower2=[]
_l_(598268)
upper2=[]
_l_(598269)


def hubble_n_s(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 _l_(598285)

 fun = _c_(598281, _a_(598279, _c_(598278, _n_(598270, "scalarpow", lambda: scalarpow), _n_(598271, "Ophi", lambda: Ophi),  _n_(598272, "rd", lambda: rd), _n_(598273, "li", lambda: li), _n_(598274, "mi", lambda: mi),  _n_(598275, "Orad_i", lambda: Orad_i), _n_(598276, "h", lambda: h), _n_(598277, "sigma8", lambda: sigma8)), "hubble_normalized_z"), _n_(598280, "z", lambda: z))
 _l_(598282)
 aux = _n_(598283, "fun", lambda: fun)**2.
 _l_(598284)
# H1 = 1 + q0
 return aux
def hubble_norm_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 _l_(598301)

 fun = _c_(598297, _a_(598295, _c_(598294, _n_(598286, "scalarpow", lambda: scalarpow), _n_(598287, "Ophi", lambda: Ophi),     _n_(598288, "rd", lambda: rd), _n_(598289, "li", lambda: li), _n_(598290, "mi", lambda: mi),  _n_(598291, "Orad_i", lambda: Orad_i)*1e-5, _n_(598292, "h", lambda: h), 0.045, 0.96, _n_(598293, "sigma8", lambda: sigma8)), "hubble_normalized_z"), _n_(598296, "z", lambda: z))
 _l_(598298)
 aux = _n_(598299, "fun", lambda: fun) 
 _l_(598300) 
 return aux 


def hubble_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 _l_(598318)

 fun = _c_(598313, _a_(598311, _c_(598310, _n_(598302, "scalarpow", lambda: scalarpow), _n_(598303, "Ophi", lambda: Ophi),     _n_(598304, "rd", lambda: rd), _n_(598305, "li", lambda: li), _n_(598306, "mi", lambda: mi),  _n_(598307, "Orad_i", lambda: Orad_i)*1e-5, _n_(598308, "h", lambda: h), 0.045, 0.96, _n_(598309, "sigma8", lambda: sigma8)), "hubble_normalized_z"), _n_(598312, "z", lambda: z))
 _l_(598314)
 aux = _n_(598315, "fun", lambda: fun)*100.*_n_(598316, "h", lambda: h)
 _l_(598317)
# return fun*100.*h0
 return aux
_c_(598322, _n_(598319, "print", lambda: print), _c_(598321, _n_(598320, "hubble_z", lambda: hubble_z), 1.99,147.49,0.50,0.0032,0.11,0.7,0.8,0.0))
_l_(598323)


def equation_of_state_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 _l_(598339)

 fun = _c_(598335, _a_(598333, _c_(598332, _n_(598324, "scalarpow", lambda: scalarpow), _n_(598325, "Ophi", lambda: Ophi),     _n_(598326, "rd", lambda: rd), _n_(598327, "li", lambda: li), _n_(598328, "mi", lambda: mi),  _n_(598329, "Orad_i", lambda: Orad_i)*1e-5, _n_(598330, "h", lambda: h), 0.045, 0.96, _n_(598331, "sigma8", lambda: sigma8)), "equation_of_state_z"), _n_(598334, "z", lambda: z))
 _l_(598336)
 aux = _n_(598337, "fun", lambda: fun) 
 _l_(598338) 
 return aux 
_c_(598343, _n_(598340, "print", lambda: print), _c_(598342, _n_(598341, "equation_of_state_z", lambda: equation_of_state_z), 1.99,147.49,0.50,0.0032,0.11,0.7,0.8,0.0))
_l_(598344)
 
 
z=_c_(598347, _a_(598346, _n_(598345, "np", lambda: np), "linspace"), 0,1.5,10)
_l_(598348)
for i in _n_(598349, "z", lambda: z):
 _l_(598449)



#z=np.linspace(0,5,10)
#for i in z:

 
 
 
 EoS = _c_(598353, _a_(598351, _n_(598350, "np", lambda: np), "vectorize"), _n_(598352, "equation_of_state_z", lambda: equation_of_state_z)) 
 _l_(598354) 
 derived = _c_(598371, _n_(598355, "EoS", lambda: EoS), _a_(598357, _n_(598356, "param", lambda: param), "Ophi"), _a_(598359, _n_(598358, "param", lambda: param), "rd"), _a_(598361, _n_(598360, "param", lambda: param), "li"), _a_(598363, _n_(598362, "param", lambda: param), "mi"), _a_(598365, _n_(598364, "param", lambda: param), "Orad_i"), _a_(598367, _n_(598366, "param", lambda: param), "h"), _a_(598369, _n_(598368, "param", lambda: param), "sigma8"),_n_(598370, "i", lambda: i))
 _l_(598372)
  
# cpl OM(z) 
#  hubble_d = np.vectorize(dummy) 
#  hubble = np.vectorize(hubble_n_s)
#  derived = ((2.*(1.+i)*hubble_d(param.Ophi, param.rd, param.li, param.mi, param.Orad_i, param.h, param.sigma8,i))/3. -1.)/(1.- ((1.-param.Ophi-param.Orad_i)*(1.+i)**3./(hubble(param.Ophi, param.rd, param.li, param.mi, param.Orad_i, param.h, param.sigma8,i))))
 
 #m=sample.mean(derived)
 
 m=_c_(598379, _a_(598378, _n_(598373, "sample", lambda: sample)[~_c_(598377, _a_(598375, _n_(598374, "np", lambda: np), "isnan"), _n_(598376, "derived", lambda: derived))], "mean"))
 _l_(598380)
 #print(m)  


 _c_(598386, _n_(598381, "print", lambda: print), _c_(598385, _a_(598383, _n_(598382, "np", lambda: np), "nanmean"), _n_(598384, "m", lambda: m)))
 _l_(598387)
   
 _c_(598391, _a_(598389, _n_(598388, "mean", lambda: mean), "append"), _n_(598390, "m", lambda: m))
 _l_(598392)
 
 #mean=mean+m  
 
 _c_(598395, _n_(598393, "print", lambda: print), _n_(598394, "mean", lambda: mean))
 _l_(598396)

 #lcdm = np.sqrt(hubble_n_s(.27,4.68*1e-5,-1,0,z))
 s=_c_(598400, _a_(598398, _n_(598397, "sample", lambda: sample), "twoTailLimits"), _n_(598399, "derived", lambda: derived),0.683)
 _l_(598401)
 s1=_c_(598405, _a_(598403, _n_(598402, "sample", lambda: sample), "twoTailLimits"), _n_(598404, "derived", lambda: derived),0.954)
 _l_(598406)
 s2=_c_(598410, _a_(598408, _n_(598407, "sample", lambda: sample), "twoTailLimits"), _n_(598409, "derived", lambda: derived),0.997)
 _l_(598411)
 _c_(598415, _a_(598413, _n_(598412, "lower", lambda: lower), "append"), _n_(598414, "s", lambda: s)[0])
 _l_(598416)
 _c_(598420, _a_(598418, _n_(598417, "upper", lambda: upper), "append"), _n_(598419, "s", lambda: s)[1])
 _l_(598421)
 _c_(598425, _a_(598423, _n_(598422, "lower1", lambda: lower1), "append"), _n_(598424, "s1", lambda: s1)[0])
 _l_(598426)
 _c_(598430, _a_(598428, _n_(598427, "upper1", lambda: upper1), "append"), _n_(598429, "s1", lambda: s1)[1])
 _l_(598431)
 _c_(598435, _a_(598433, _n_(598432, "lower2", lambda: lower2), "append"), _n_(598434, "s2", lambda: s2)[0])
 _l_(598436)
 _c_(598440, _a_(598438, _n_(598437, "upper2", lambda: upper2), "append"), _n_(598439, "s2", lambda: s2)[1])
 _l_(598441)
 _c_(598447, _n_(598442, "print", lambda: print), 'z:%f mean:%f  lower:%f  upper:%f'%(_n_(598443, "i", lambda: i),_n_(598444, "m", lambda: m),_n_(598445, "s", lambda: s)[0],_n_(598446, "s", lambda: s)[1]))
 _l_(598448)

#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#rc('text', usetex=True)

#plt.plot((0, 2), (-1, -1) , 'k--',linewidth=0.4)

#plt.plot(z, mean, 'red', linewidth=.6)
_c_(598455, _a_(598451, _n_(598450, "plt", lambda: plt), "plot"), _n_(598452, "z", lambda: z), (_n_(598453, "upper", lambda: upper)-_n_(598454, "lower", lambda: lower))/2.0, 'blue', linewidth=.6)
_l_(598456)

#plt.plot(z,lcdm, 'k-',linewidth=0.3 )



_c_(598461, _a_(598458, _n_(598457, "plt", lambda: plt), "plot"), _n_(598459, "z", lambda: z),_n_(598460, "lower", lambda: lower),  'blueviolet',linewidth=.3)
_l_(598462)
_c_(598467, _a_(598464, _n_(598463, "plt", lambda: plt), "plot"), _n_(598465, "z", lambda: z),_n_(598466, "upper", lambda: upper),  'blueviolet',linewidth=.3)
_l_(598468)
_c_(598473, _a_(598470, _n_(598469, "plt", lambda: plt), "plot"), _n_(598471, "z", lambda: z),_n_(598472, "lower1", lambda: lower1), 'darkviolet',linewidth=.3)
_l_(598474)
_c_(598479, _a_(598476, _n_(598475, "plt", lambda: plt), "plot"), _n_(598477, "z", lambda: z),_n_(598478, "upper1", lambda: upper1), 'darkviolet',linewidth=.3)
_l_(598480)
_c_(598486, _a_(598482, _n_(598481, "plt", lambda: plt), "fill_between"), _n_(598483, "z", lambda: z),_n_(598484, "lower", lambda: lower),_n_(598485, "upper", lambda: upper), color='mediumorchid', alpha=0.5)
_l_(598487)
_c_(598493, _a_(598489, _n_(598488, "plt", lambda: plt), "fill_between"), _n_(598490, "z", lambda: z),_n_(598491, "lower1", lambda: lower1),_n_(598492, "upper1", lambda: upper1), color='violet', alpha=0.5)
_l_(598494)
#plt.plot(z,lower2, 'r-.',linewidth=1.5)
#plt.plot(z,upper2, 'r-.',linewidth=1.5)
#plt.xlim(0.001,1.3)
#plt.plot(z,(upper-lower)/2.0, 'blueviolet',linewidth=.3)


_c_(598497, _a_(598496, _n_(598495, "plt", lambda: plt), "xlim"), 0,1.5)
_l_(598498)
_c_(598501, _a_(598500, _n_(598499, "plt", lambda: plt), "ylim"), -1.5,-0.7)
_l_(598502)

_c_(598505, _a_(598504, _n_(598503, "plt", lambda: plt), "xlabel"), r'$z$')
_l_(598506)
_c_(598509, _a_(598508, _n_(598507, "plt", lambda: plt), "ylabel"), r'$w_{DE}(z)$')
_l_(598510)
_c_(598513, _a_(598512, _n_(598511, "plt", lambda: plt), "savefig"), 'w_mean.pdf',bbox_inches='tight')
_l_(598514)
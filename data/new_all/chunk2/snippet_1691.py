# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63047188/converting-matlab-code-to-python-and-received-typeerror-numpy-ndarray-object
#simulate BE response over a line scan

# define experimental parameters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
IO_rate = 4E6; #[samples/sec]
_l_(461594)#[samples/sec]
N_pixels = 128; # number of pixels along a line scan
_l_(461595)# number of pixels along a line scan
N_points_per_pixel = 8192; # number of data points per pixel
_l_(461596)# number of data points per pixel
w1 = 200E3; # lower edge of band
_l_(461597)# lower edge of band
w2 = 400E3; # upper edge of band
_l_(461598)# upper edge of band
noise_level = .1; #add noise to the signal
_l_(461599)#add noise to the signal

w_vec = _c_(461608, _a_(461601, _n_(461600, "np", lambda: np), "arange"), -_n_(461602, "IO_rate", lambda: IO_rate)/2, _n_(461603, "IO_rate", lambda: IO_rate)/2-_n_(461604, "IO_rate", lambda: IO_rate)/_n_(461605, "N_points_per_pixel", lambda: N_points_per_pixel) + 1, _n_(461606, "IO_rate", lambda: IO_rate)/_n_(461607, "N_points_per_pixel", lambda: N_points_per_pixel))
_l_(461609)
# vary A, wo, Q, and phase over pixels
p_vec = _c_(461613, _a_(461611, _n_(461610, "np", lambda: np), "arange"), 0, _n_(461612, "N_pixels", lambda: N_pixels)-1)/_n_(461614, "N_pixels", lambda: N_pixels)
_l_(461615)
A_vec = _c_(461621, _a_(461617, _n_(461616, "np", lambda: np), "sin"), 2*_a_(461619, _n_(461618, "np", lambda: np), "pi")*3*_n_(461620, "p_vec", lambda: p_vec))+2 #amplitude
_l_(461622) #amplitude
wo_vec = 250E3 + 100E3*_n_(461623, "p_vec", lambda: p_vec) #resonance
_l_(461624) #resonance
Q_vec = 100 - 50*_n_(461625, "p_vec", lambda: p_vec) # Q-factor
_l_(461626) # Q-factor
phi_vec = _c_(461630, _a_(461628, _n_(461627, "np", lambda: np), "sign"), _n_(461629, "p_vec", lambda: p_vec)-.5) # phase
_l_(461631) # phase

D_vec = _c_(461638, _a_(461633, _n_(461632, "np", lambda: np), "zeros"), _c_(461637, _a_(461635, _n_(461634, "np", lambda: np), "size"), _n_(461636, "w_vec", lambda: w_vec)))
_l_(461639)
ind = (_c_(461642, _n_(461640, "abs", lambda: abs), _n_(461641, "w_vec", lambda: w_vec))<_n_(461643, "w2", lambda: w2)) & (_c_(461646, _n_(461644, "abs", lambda: abs), _n_(461645, "w_vec", lambda: w_vec))>_n_(461647, "w1", lambda: w1));
_l_(461648)
_n_(461649, "D_vec", lambda: D_vec)[_n_(461650, "ind", lambda: ind)] = 1; #assign those indices to 1.
_l_(461651)#assign those indices to 1.
band_ind = _c_(461658, _a_(461653, _n_(461652, "np", lambda: np), "nonzero"), (_n_(461654, "w_vec", lambda: (w_vec))<_n_(461655, "w2", lambda: w2)) & (_n_(461656, "w_vec", lambda: (w_vec))>_n_(461657, "w1", lambda: w1)));
_l_(461659)

d_vec = _c_(461672, _a_(461662, _a_(461661, _n_(461660, "np", lambda: np), "fft"), "fftshift"), _c_(461671, _a_(461665, _a_(461664, _n_(461663, "np", lambda: np), "fft"), "ifft"), _c_(461670, _a_(461668, _a_(461667, _n_(461666, "np", lambda: np), "fft"), "ifftshift"), _n_(461669, "D_vec", lambda: D_vec)))) #find drive signal in the time domain
_l_(461673) #find drive signal in the time domain
R_mat = _c_(461678, _a_(461675, _n_(461674, "np", lambda: np), "zeros"), (_n_(461676, "N_pixels", lambda: N_pixels),_n_(461677, "N_points_per_pixel", lambda: N_points_per_pixel)))
_l_(461679)
r_mat = _c_(461684, _a_(461681, _n_(461680, "np", lambda: np), "zeros"), (_n_(461682, "N_pixels", lambda: N_pixels),_n_(461683, "N_points_per_pixel", lambda: N_points_per_pixel)))
_l_(461685)

for k1 in _c_(461688, _n_(461686, "range", lambda: range), _n_(461687, "N_pixels", lambda: N_pixels)):
    _l_(461713)

    H_vec = ((_c_(461691, _n_(461689, "A_vec", lambda: A_vec), _n_(461690, "k1", lambda: k1))*_c_(461694, _n_(461692, "wo_vec", lambda: wo_vec), _n_(461693, "k1", lambda: k1))**2)*_c_(461700, _a_(461696, _n_(461695, "np", lambda: np), "exp"), 1j*_c_(461699, _n_(461697, "phi_vec", lambda: phi_vec), _n_(461698, "k1", lambda: k1)))/(_n_(461701, "w_vec", lambda: w_vec)**2 + 1j*_c_(461704, _n_(461702, "wo_vec", lambda: wo_vec), _n_(461703, "k1", lambda: k1))*_n_(461705, "w_vec", lambda: w_vec)/_c_(461708, _n_(461706, "Q_vec", lambda: Q_vec), _n_(461707, "k1", lambda: k1)) - _c_(461711, _n_(461709, "wo_vec", lambda: wo_vec), _n_(461710, "k1", lambda: k1))**2)); #cantilever transfer function
    _l_(461712)#cantilever transfer function
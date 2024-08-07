#Source: https://stackoverflow.com/questions/42980584/attribute-error-when-using-firls-method-of-scipy
import scipy.signal as signal
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2)
nyq = 5.  # Hz
desired = (0, 0, 1, 1, 0, 0)
for bi, bands in enumerate(((0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 4.5, 5))):
    fir_firls = signal.firls(73, bands, desired, nyq=nyq)
    fir_remez = signal.remez(73, bands, desired[::2], Hz=2 * nyq)
    fir_firwin2 = signal.firwin2(73, bands, desired, nyq=nyq)
    hs = list()
    ax = axs[bi]
    for fir in (fir_firls, fir_remez, fir_firwin2):
        freq, response = signal.freqz(fir)
        hs.append(ax.semilogy(nyq*freq/(np.pi), np.abs(response))[0])
    for band, gains in zip(zip(bands[::2], bands[1::2]), zip(desired[::2],      desired[1::2])):
        ax.semilogy(band, np.maximum(gains, 1e-7), 'k--', linewidth=2)
    if bi == 0:
        ax.legend(hs, ('firls', 'remez', 'firwin2'), loc='lower center',    frameon=False)
    else:
        ax.set_xlabel('Frequency (Hz)')
    ax.grid(True)
    ax.set(title='Band-pass %d-%d Hz' % bands[2:4], ylabel='Magnitude')
fig.tight_layout()
plt.show()
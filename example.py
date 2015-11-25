import matplotlib.pyplot as _plt
import numpy as _np
import rayleigh

def DrogeTest():
    '''
    Data digitized by @jradavenport from original paper:
    http://adsabs.harvard.edu/abs/1990ApJS...73..279D
    Dr{\"o}ge et al. (1990)

    Remake Figure 2 for 64 solar flare events.
    '''

    # Table 1, Occurance Times of ISEE 3 Electron Flares
    # Units of Days since 01-AUG-1978
    data = [53.415, 167.566, 201.688, 212.428, 245.049, 367.896, 382.592,
            403.373, 409.292, 471.847, 498.718, 556.378, 612.627, 676.053,
            676.133, 690.056, 696.676, 698.446, 716.235, 806.215, 814.439,
            816.401, 836.771, 845.779, 965.282, 967.860, 974.065, 976.408,
            977.208, 983.698, 987.986, 997.580, 1001.861, 1003.125, 1084.554,
            1092.840, 1163.958, 1168.269, 1194.163, 1209.139, 1250.257,
            1278.986, 1280.581, 1287.533, 1288.172, 1314.130, 1402.488,
            1426.750, 1438.322, 1446.965, 1448.037, 1451.722, 1468.083,
            1473.958, 1474.213, 1495.083, 1574.513, 1574.740, 1578.107,
            1589.989, 1597.082, 1599.792, 1601.684, 1607.333]

    data = _np.array(data, dtype='float')

    # frequency info given in nHz in the paper
    fmin = 1e-9
    fmax = 500e-9
    df = 1.25e-9

    n = int((fmax - fmin) / df)
    freqs = _np.linspace(fmin, fmax, num=n)

    # convert those limits to Days for this code
    maxper = 1. / (fmin * 24. * 60. * 60.)
    minper = 1. / (fmax * 24. * 60. * 60.)

    # Compute the power spectrum!
    z = rayleigh.RayleighPowerSpectrum(data, minper=minper, maxper=maxper, nper=n)

    # now recreate the actual plot from the paper
    _plt.figure()
    _plt.plot(freqs / 1e-9, z)
    _plt.xlabel('Frequency (nHz)')
    _plt.ylabel('Rayleigh power (z)')
    _plt.show()

    return


if __name__ == "__main__":
    DrogeTest()
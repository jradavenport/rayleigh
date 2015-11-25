'''
Methods related to the Rayleigh test 
 (e.g. Mardia & Jupp 2000,2008)
http://dx.doi.org/10.1002/9780470316979

'''

import numpy as _np

def RayleighTest(t, v):
    '''
    Evaluate the normalized Rayleigh test for a series of event times (t)
    at a single given frequency (v).

    Parameters
    ----------
    t : 1d array
        array of event times
    v : float
        the frequency to evaluate at

    Returns
    -------
    Float, the normalized Rayleigh test at this frequency

    '''

    n = len(t)
    theta = 2. * _np.pi * v * t

    z = 1. / n * (( _np.sum(_np.sin(theta))**2 +
                    _np.sum(_np.cos(theta))**2 ))

    return z


def RayleighPowerSpectrum(times, minper=1.0, maxper=500.0, nper=100):
    '''
    Compute the power spectrum over a range of periods by evaluating the
    Rayleigh test at each frequency.

    Periods are assumed to be in units of Days. Frequencies to calculate the
    Rayleigh Test on are computed as:
    >>> freq = 1 / (per * 24 * 60 * 60)

    Parameters
    ----------
    times : 1d array
        Array of times
    minper : float, optional
        Minimum period in days to evaluate the power spectrum at.
        (Default is 1.0)
    maxper : float, optional
        Maximum period in days to evaluate the power spectrum at.
        (Default is 500.0)
    nper : int, optional
        Number of periods to evaluate the power spectrum at, linearly
        spaced from minper to maxper. (Default is 100)

    Returns
    -------
    1d float array with length of nper
    '''

    maxfreq = 1. / (minper * 24. * 60. * 60.)
    minfreq = 1. / (maxper * 24. * 60. * 60.)

    # Evaluate at linearly spaced frequencies
    freqs = _np.linspace(minfreq, maxfreq, num=nper)

    # periods = 1. / freqs / (24. * 60. * 60.)

    z = map(lambda v: RayleighTest(times * (24. * 60. * 60.), v), freqs)

    return z

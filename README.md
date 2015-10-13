# Rayleigh Test and Power Spectrum

*This code enables you to determine if events are periodically spaced.*

If you have only a list of event times, and not (for example) event amplitudes, you cannot use  something like the Lomb-Scargle method to determine the period.


## Example
Given a list of occurrence times for solar X-ray flare events from [Droge et al. (1990)](http://adsabs.harvard.edu/abs/1990ApJS...73..279D), search for any preferred period for these events to occur.

````python
from rayleigh import DrogeTest
DrogeTest()
````

The output of this example reproduces their Figure 2, and should look like this:

<img src="Fig2.png" width="600">

A periodicity of 153 days (75 nHz) is found.
#!/usr/bin/env python
from __future__ import absolute_import

import os
import numpy as np
from astropy.units import Unit
import sncosmo

lsstbandPassList = ['u', 'g', 'r', 'i', 'z', 'y']
lsstbanddir = os.path.join(os.getenv('THROUGHPUTS_DIR'), 'baseline')
megacamPassList = 'ugriz'
megacambanddir = os.path.join(os.getenv('THROUGHPUTS_DIR'), 'megacam')
# lsstbands = list()
# lsstbp = dict()

for band in lsstbandPassList:

    # setup sncosmo bandpasses
    bandfname = lsstbanddir + "/total_" + band + '.dat'


    # register the LSST bands to the SNCosmo registry
    # Not needed for LSST, but useful to compare independent codes
    # Usually the next two lines can be merged,
    # but there is an astropy bug currently which affects only OSX.
    numpyband = np.loadtxt(bandfname)
    sncosmoband = sncosmo.Bandpass(wave=numpyband[:, 0],
                                   trans=numpyband[:, 1],
                                   wave_unit=Unit('nm'),
                                   name='LSST_' + band)

    sncosmo.registry.register(sncosmoband, force=True)

for band in megacamPassList:
    bandfname = os.path.join(megacambanddir, band + 'Mega.fil.txt')
    numpyband = np.loadtxt(bandfname)
    sncosmoband = sncosmo.Bandpass(wave=numpyband[:, 0],
                                   trans=numpyband[:, 1],
                                   wave_unit=Unit('nm'),
                                   name='megacam_' + band)
    sncosmo.registry.register(sncosmoband, force=True)

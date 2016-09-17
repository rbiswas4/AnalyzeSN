from __future__ import absolute_import, print_function, division
import fitsio
import pandas as pd
import numpy as np
import os
from astropy.table import Table, Column


class SNANASims(object):
    """
    Class to represent SNANA simulations of a particular class of objects, ie.
    Ia or Non_Ia
    """
    def __init__(self, headFile, photFile, coerce_inds2int=True):
	"""
	Parameters
	---------
	headFile : string, mandatory
	    absolute path to head file of simulation
	photFile : string, mandatory
	    absolute path to phot file of simulation
	coerce_inds2int : Bool, optional, defaults to True
	    if true, converts SNID from string to int
	"""
        self.headFile = headFile
        self.photFile = photFile
        self.headData = self.get_headData(self.headFile,
					  coerce_inds2int=coerce_inds2int)
        self.phot = fitsio.FITS(photFile)

    @classmethod
    def fromSNANAfileroot(cls, snanafileroot, location='./',
                          coerce_inds2int=False):
        """
        Class constructor from a root file and a location

        Parameters
        ----------
        snanafileroot : string, mandatory
            root file name for the SNANA which is the prefix to
            '_HEAD.FITS', or '_PHOT.FITS'
        location : string, optional defaults to current working directory './' 
            Relative or absolute path to the directory where the head and phot
            files are located
        snids : integer/string, optional defaults to None
            if not None, only SN observations corresponding to SNID snid
            are loaded
        n : Integer, defaults to None
            if not None, only the first n SN light curves are loaded
        """

        headfile = cls.snanadatafile(snanafileroot, filetype='head',
                                     location=location)
        photfile = cls.snanadatafile(snanafileroot, filetype='phot',
                                     location=location)
        return cls(headFile=headfile, photFile=photfile,
                   coerce_inds2int=coerce_inds2int)
    
    @staticmethod
    def snanadatafile(snanafileroot, filetype='head', location='./'):
        '''
        obtain the name of the head or phot file of an SNANA simulation
        and dataset

        Parameters
        ----------
        snanafileroot : string, mandatory
            root file name for the SNANA which is the prefix to
            '_HEAD.FITS', or '_PHOT.FITS'
        filetype : string, optional defaults to 'head'
            'head' or 'phot' depending on whether a summary file or a photometry
            file is being used.
        location : string, optional defaults to current working directory './' 
            relative or absolute path to the directory in which the file is
            located

        Returns
        -------
            string : absolute path to the SNANA file 

        '''

        desiredfiletype = ['head', 'phot']
        filetype = filetype.lower()
        if not filetype in desiredfiletype:
            raise ValueError(
                'filetype should be one of "head" or "phot"', filetype)
        location = os.path.abspath(location)
        suffix = '_HEAD.FITS'
        if filetype.lower() == 'phot':
            suffix = '_PHOT.FITS'
        fname = snanafileroot + suffix
        return os.path.join(location, fname)
    @staticmethod 
    def get_headData(headFile, coerce_inds2int=False):
	"""
	read the headData of a SNANA simulation and return a dataframe
	representing the simulation
	
	Parameters
	----------
	headFile :
	coerce_inds2int :
	"""
        _head = Table.read(headFile)
        if _head['SNID'].dtype.type is np.string_:
            data = _head['SNID'].data
            name = _head['SNID'].name
            dtype = _head['SNID'].dtype
            if coerce_inds2int:
                arr = list(np.int(x) for x in data)
                dtype=int
            else:
                arr = list(x.strip().lower() for x in data)
            col = Column(data=arr, name=name, dtype=dtype)
            _head.remove_columns('SNID')
            _head.add_column(col, index=0)
        return  _head.to_pandas().set_index('SNID')
        
    def get_photrows(self, row=None, snid=None):
	"""
	return rows of the photometry table corresponding to a SN as listed
	in the head table.

	Parameters
	----------
	row :
	snid :
	"""
        if row is not None:
            ptrs = self.headData.iloc[row][['PTROBS_MIN', 'PTROBS_MAX']]
        elif snid is not None:
            ptrs = self.headData.ix[snid][['PTROBS_MIN', 'PTROBS_MAX']]
        else:
            raise ValueError('Both {0} and {1} cannot be None simulataneously'.format('snid', 'row'))
        ptrs = ptrs.astype('int').values
        ptrs[0] -= 1
        return ptrs

    def get_SNANA_photometry(self, snid=None, ptrs=None):
	"""
	return the photometry table corresponding to a SN with snid (from the
       	head table) or the photometry table within the range of row numbers
	indicated by ptrs
	"""
        if ptrs is not None:
            assert np.shape(ptrs) == (2,)
        elif snid is not None:
            ptrs = self.get_photrows(snid=snid.strip().lower())
        else:
            raise ValueError('Both {0} and {1} cannot be None simulataneously'.format('snid', 'row'))
        lcData = self.phot[1][ptrs[0]: ptrs[1]].byteswap().newbyteorder()
        
        return pd.DataFrame(lcData)

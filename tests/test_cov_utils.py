# IPython log file

import numpy as np
import analyzeSN as ans
import os
#from nose import get_tests_classes


class Test_cov_utils(object):
    @classmethod
    def setup_class(cls):
        cls.cfile = os.path.join(ans.example_data, 'cov_data.dat')
        cls.covStored = np.loadtxt(cls.cfile)
    @classmethod
    def tearDown_class(cls):
        pass

    def test_generateCov(self):
        testmodule = Test_cov_utils()
        cov = ans.generateCov(dims=3, seed=42)
        assert np.allclose(cov, testmodule.covStored)

    def test_covariance(self):
        testmodule = Test_cov_utils()
        paramNames = ['x0', 'x1', 'x2']
        cov =  ans.covariance(testmodule.covStored, paramNames=paramNames)
        assert np.allclose(testmodule.covStored, cov)
        assert np.array_equal(cov.columns, paramNames)
        assert np.array_equal(cov.columns, cov.index.values)




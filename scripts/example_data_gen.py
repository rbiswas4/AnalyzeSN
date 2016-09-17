"""
Script to generate example data sets used in examples and tests
"""
import numpy as np
import analyzeSN as ans


# cov_data.data
cov = ans.generateCov(dims=3, seed=42)
np.savetxt('../example_data/cov_data.dat', cov)


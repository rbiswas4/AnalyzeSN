# AnalyzeSN

[![Build Status](https://travis-ci.org/rbiswas4/AnalyzeSN.svg?branch=master)](https://travis-ci.org/rbiswas4/AnalyzeSN)[![Coverage Status](https://coveralls.io/repos/github/rbiswas4/AnalyzeSN/badge.svg?branch=master)](https://coveralls.io/github/rbiswas4/AnalyzeSN?branch=master)

A repository with codes for supernova data analysis

## Software Requirements
You can find the [requirements here](./Requirements.md)

## Installation
The prerequisite software can be installed using pip and conda. If you have a miniconda/anaconda distribution you should be able to do all of these. 
The following lines should install the code for the user. The first two lines create and activate an environment if you don't want to mess the python distribution.

```
# create and activate an environment
conda create --yes -n AnalyzeSN python
source activate AnalyzeSN
# Actual installation
conda config --add channels pandas
conda config --add channels astropy
conda install -q --yes --file ./continuous_integration/requirements.txt
conda list --explicit > spec-file.txtconda list --explicit > ./continuous_integration/spec-file.txt; 
pip install -r ./continuous_integration/pip_requirements.txt
python setup.py install --user
```
## Contributors

- R. Biswas
- L. McBride

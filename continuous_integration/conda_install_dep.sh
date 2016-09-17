#!/usr/bin/env bash

export PATH="${store_dir}/miniconda/bin:$PATH"
CHANNEL=${CHANNEL:-"http://conda.lsst.codes/sims"} # the URL to the conda channel where LSST conda packages reside
#conda config --add channels "$CHANNEL"
CHANNEL=${CHANNEL:-"pandas"}
#conda config --add channels "$CHANNEL"
CHANNEL=${CHANNEL:-"astropy"}
conda config --add channels "$CHANNEL"
conda create --yes -n AnalyzeSN python
source activate AnalyzeSN
conda install -q --yes --file ./continuous_integration/requirements.txt
conda list --explicit > spec-file.txtconda list --explicit > spec-file.txt;


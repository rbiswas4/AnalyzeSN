#!/usr/bin/env bash

reqfile='../Requirements.md'
echo "# Software Requirements" > $reqfile
echo "It is recommended to a conda python from MiniConda or AnaConda. The code is tested using this version of python. Other versions of python will probably work, but could pose difficulties." >> $reqfile
echo "## installed by conda" >> $reqfile

while read -r line
do
     echo "- $line" >> $reqfile
 done < ../continuous_integration/requirements.txt 

echo "## installed by pip" >> $reqfile
while read -r line
do
     echo "- $line" >> $reqfile
 done < ../continuous_integration/pip_requirements.txt 

echo "## Other requirements" >> $reqfile
 
echo "- Throughputs: Clone this [repository](https://github.com/lsst/throughputs) and set an environment variable 'THROUGHPUTS_DIR' to its location. For example, if you have a bash SHELL, and you clone this to your $HOME directory as throughputs, then use \n ```export THROUGHPUTS_DIR=${HOME}/throughputs```. \n If you are using a different shell or want to keep it in a different location, use the equivalent code in the shell from where you will run the code (or add it to your profile). Note, if you are using the [lsst sims_stack](https://confluence.lsstcorp.org/display/SIM/Catalogs+and+MAF), then you already have this directory, and setting up the sims stack or the throughputs repository will be sufficient." >> $reqfile

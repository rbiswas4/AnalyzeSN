# Software Requirements
It is recommended to a conda python from MiniConda or AnaConda. The code is tested using this version of python. Other versions of python will probably work, but could pose difficulties.
## installed by conda
- sncosmo
- pandas
- matplotlib
- seaborn
- nose
- pip
## installed by pip
- fitsio
- pandas
- bottleneck
- numexpr
- coveralls
- coverage
- python-coveralls
- future
## Other requirements
- Throughputs: Clone this [repository](https://github.com/lsst/throughputs) and set an environment variable 'THROUGHPUTS_DIR' to its location. For example, if you have a bash SHELL, and you clone this to your /Users/rbiswas directory as throughputs, then use \n . \n If you are using a different shell or want to keep it in a different location, use the equivalent code in the shell from where you will run the code (or add it to your profile). Note, if you are using the [lsst sims_stack](https://confluence.lsstcorp.org/display/SIM/Catalogs+and+MAF), then you already have this directory, and setting up the sims stack or the throughputs repository will be sufficient.

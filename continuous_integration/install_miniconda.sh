#!/bin/bash -xe
source ./continuous_integration/setup_env.sh
mkdir -p ${store_dir}

# remove previous installation
rm -rf "${store_dir}/miniconda"
osname=`uname`
# Obtain the miniconda script from continuum for the OS
echo $osname
if [[ "$osname" == 'Linux' ]]
then
    install_file="Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh"
elif [[ "$osname" == 'Darwin' ]]
then
    install_file="Miniconda2-$MINICONDA_VERSION-MacOSX-x86_64.sh"
else
    echo "Error with OS" 1>&2
    exit 64
fi
# Download the miniconda script
curl -L -O "https://repo.continuum.io/miniconda/$install_file"
bash "$install_file" -b -p "${store_dir}/miniconda"
export PATH="${store_dir}/miniconda/bin:$PATH"
#
# Disable MKL. The lsst stack doesn't play nice with it (symbol collisions)
#
rm -f $install_file
conda install --yes nomkl

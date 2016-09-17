#!/usr/bin/env python
export store_dir=${HOME}/store
export MINICONDA_VERSION=${MINICONDA_VERSION:-"latest"}
export CACHE_DIR="${store_dir}/miniconda.tarball"
export CACHE_DIR_TMP="$CACHE_DIR.tmp"
export CACHE_TARBALL_NAME="miniconda.tar.gz"
export CACHE_TARBALL_PATH="$CACHE_DIR/$CACHE_TARBALL_NAME"
export PATH="${store_dir}/miniconda/bin:$PATH"


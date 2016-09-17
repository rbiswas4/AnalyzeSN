#!/usr/bin/env bash
source ./continuous_integration/setup_env.sh
# Minimize our on-disk footprint
conda clean -iltp --yes

#
# Pack for caching. We pack here as Travis tends to time out if it can't pack
# the whole directory in ~180 seconds.
#
rm -rf "$CACHE_DIR" "$CACHE_DIR_TMP"

mkdir "$CACHE_DIR_TMP"
tar czf "$CACHE_DIR_TMP/$CACHE_TARBALL_NAME" -C "${store_dir}" miniconda
mv "${store_dir}/info.txt" "$CACHE_DIR_TMP"

mv "$CACHE_DIR_TMP" "$CACHE_DIR"	# Atomic rename
ls -l "$CACHE_DIR"

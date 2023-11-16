#!/bin/bash

set -euxo pipefail

rm -rf build
mkdir -p build
cd build
cmake ..
make

# Install so it is runnable from anywhere.
find . -type f -executable -exec ln -sf "$(pwd)/{}" /usr/local/bin \;

#!/bin/bash

docker run \
  -it \
  --rm \
  -v $PWD:/root/cmake \
  -w /root/cmake \
  cmake:latest
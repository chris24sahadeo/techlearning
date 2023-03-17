#!/bin/bash

docker run -it --rm \
  --name rust-techlearning \
  -v $PWD:/root/rust-techlearning \
  -w /root/rust-techlearning \
  rust-techlearning

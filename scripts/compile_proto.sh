#!/usr/bin/env bash

sd="./protobuf"
td="./snakebite/protobuf"

for f in `ls "${sd}"`
do
    echo "$f"
    protoc -I="${sd}" --python_out="${td}" "${sd}/${f}"
done

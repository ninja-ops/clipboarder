#!/bin/bash
if [ -p /dev/stdin ]; then
  while IFS= read line; do
    echo ": ${line}"
  done
fi

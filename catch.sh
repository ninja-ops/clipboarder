#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [[ -f "$SCRIPT_DIR"/catch-user.sh ]]
then
  source "$SCRIPT_DIR"/catch-user.sh
fi

python3 "$SCRIPT_DIR"/catch.py

#!/usr/bin/env bash
# Author: Josiah Bull <josiah.bull7@gmail.com>
# This script will retry the command directly following it until it exits with code 0.
# I commonly use this for a case of trying to ssh into something until it succeeds.
# Example:
# retry ssh my_username@192.168.0.54 -p 22

if [[ -z "${RETRY_TIME}" ]]; then
    __RETRY_TIME=5
else
    __RETRY_TIME="${RETRY_TIME}"
fi

if [[ -z "${MAX_ATTEMPTS}" ]]; then
    __MAX_ATTEMPTS=1000
else
    __MAX_ATTEMPTS="${MAX_ATTEMPTS}"
fi

__COUNT=0
until eval "$@"; do
    sleep "${__RETRY_TIME}"
    __COUNT=$((__COUNT+1))
    if [ "$__COUNT" -gt "$__MAX_ATTEMPTS" ]; then
        echo "Max attempts exceeded..."
        exit 1
    fi
done
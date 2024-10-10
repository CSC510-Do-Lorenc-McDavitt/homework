#!/bin/bash
kill $(top -b -n 1 | grep -E "infinite.sh$" | grep -E -o "^\s*[0-9]+")

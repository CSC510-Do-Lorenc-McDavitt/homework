#!/bin/bash
grep -E "S$" titanic.csv | grep -E "^[0-9]*,[0-9],2" |  sed 's/,female,/,F,/' | sed 's/,male,/,M,/' | grep "[MF],[0-9]" | gawk -F, '{ sum += $7 } END {print sum / NR }'

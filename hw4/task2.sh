#!/bin/bash
grep -l "sample" -r dataset1/ | uniq | xargs grep "CSC510" | cut -d: -f1 | uniq -c | grep -E "^\s*([3-9]|[0-9]{2,})" | gawk '{print $2}' | xargs ls -l | gawk '{print $5 " " $9 }' | sort -k1 -r -n | cut -d ' ' -f2 | xargs grep "CSC510" | cut -d: -f1 | uniq -c | sort -k1 -r -n | gawk '{print $2}' | sed 's/file_/filtered_/' | cut -d/ -f2

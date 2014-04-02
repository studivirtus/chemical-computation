#!/bin/bash
varDate=`date +%y-%m-%d_%H:%M:%S:%N`
echo $varDate
file1="euclid-algorithm/02-stage-1/chem.in"
file2="euclid-algorithm/02-stage-1/chem.r"

aleae/aleae $file1 $file2 1 50 12 | tee output/$varDate.outpt
echo $varDate | python aleae-stats-graber.py
#google-chrome $varDate.svg &
#firefox -new-tab $varDate.svg &

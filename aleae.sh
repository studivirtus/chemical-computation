#!/bin/bash
varDate=`date +%y-%m-%d_%H:%M:%S:%N`
echo $varDate
file1="current-react/chem.in"
file2="current-react/chem.r"

aleae/aleae $file1 $file2 1 10 12 | tee output/$varDate.outpt
echo $varDate | python aleae-stats-graber.py
#google-chrome $varDate.svg &
#firefox -new-tab $varDate.svg &

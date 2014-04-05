#!/bin/bash
varDate=`date +%y-%m-%d_%H:%M:%S:%N`
echo $varDate
file1="collatz-procedure/chem.in"
file2="collatz-procedure/chem.r"
repitions="1"
time="100"
detail="12"

aleae/aleae $file1 $file2 $repitions $time $detail | tee output/$varDate.outpt
echo $varDate | python aleae-stats-graber.py
#google-chrome $varDate.svg &
#firefox -new-tab $varDate.svg &

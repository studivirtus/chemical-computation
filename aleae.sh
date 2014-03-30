#!/bin/bash
varDate=`date +%y-%m-%d_%H:%M:%S:%N`
echo $varDate
file1="test.in"
file2="test.r"

/home/adminuser/Dropbox/EE5393/aleae/aleae $file1 $file2 1 1000 12 | tee $varDate.outpt
echo $varDate | python3 aleae_stats_graber.py
#google-chrome $varDate.svg &
#firefox -new-tab $varDate.svg &

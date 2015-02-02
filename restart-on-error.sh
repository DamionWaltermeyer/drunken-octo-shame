#!/bin/sh
#Every 120 seconds this script attempts to restart any docker containers that 
#have failed with a -1 exit code in a time frame greater than one but less than 60 minutes.
#Pair this up with a configuration manager to put on docker hosts and run at boot. 
#If you find you have another frequently occuring exit code, just change this and have it run twice.
#log size estimated to be ~10M per month , change sleep to effect frequency & log size.
#manual usage:   ./restart-on-error.sh &>/dev/null &
while true; do docker start $(docker ps -a |grep '(-1)'| grep minutes|cut -d" " -f 1); sleep 120; done

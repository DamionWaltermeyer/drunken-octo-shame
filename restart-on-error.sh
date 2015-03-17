#Deprecated. Now using services instead. 
#!/bin/sh
#log size estimated to be ~10M per month , change sleep to effect frequency & log size.
while true; do docker start $(docker ps -a |grep '(-1)'| grep minutes|cut -d" " -f 1); sleep 120; done

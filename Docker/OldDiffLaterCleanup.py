import os
dockerversion = []
#versionwanted = str('0.10.0')
Counter = 0

f = os.popen('docker images -a |awk \'{print $3}\'')
now = f.read().splitlines()
print "output is \n", now
for i in now:
    Counter = Counter +1
    #print ('beep %s' % Counter)
    if (i != 'IMAGE'):
        #print ('boop %s %s' % (Counter, i))
        newf = os.popen('docker inspect -f "{{ .DockerVersion }}" %s' % i)
        dockerversion = newf.read()
        if str('0.10.0') in dockerversion:
            print "image: %s  version: %s" %(i,dockerversion)
            containerID = os.popen('docker inspect -f "{{ .Id }}" %s' % i)
            print('docker inspect -f "{{ .Parent }}" %s' % i)
            ID = containerID.read()
            print('rm -rf /var/lib/docker/aufs/diff/%s' % ID)
            print('docker rmi -f %s' %i)
            os.popen('sudo rm -rf /var/lib/docker/aufs/diff/%s' % ID)
            os.popen('docker rmi -f %s'%i)
            os.popen('docker rmi $(docker images -a |awk \'{print $3}\' ')

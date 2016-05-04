#Automatically get list of tor exit nodes from tor website and places them into an ipset table so you can use it for iptables.
#Sorry Tor, it is not you, it is for something one of my providers required.
#Uses fabric framework, needs request library in addition to that. 
#requires at least the following libraries.
from fabric.api import task, warn_only, 
import requests
import paramiko

@task
def getTorList():
    blocklist = []
    counter = 0
    r = requests.get('https://check.torproject.org/exit-addresses')
    rText = r.text.splitlines()
    for i in rText:
	if ('ExitAddress' in i):
	    i = i.split(' ')
	    blocklist.append(i[1])
    run('ipset destroy tor_exit')
    run('ipset create tor_exit iphash')
    for i in blocklist:
	with warn_only():
	    run('ipset add tor_exit '+ i)

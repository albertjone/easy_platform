###precondition:
# ssh is enabled and started
# root user is allowed to login in to the system
###


import socket
from threading import Thread
import threading
import datetime
import time
import yaml
import eventlet
import ipaddress
from paramiko.client import SSHClient


LINUX_OS = 'linux'
LINUX_PORTS = [20, 21, 22, 23, 25, 80, 111, 443, 445, 631, 993, 995]
WIN_OS = 'windows'
WIN_PORTS = [135, 137, 138, 139, 445]
MAC_OS = 'mac'
MAC_PORTS = [22, 445, 548, 631]

_start_time = datetime.datetime.now()

# find all hosts in the network
def _connect(*args):
    host, port = args[0]
    socket.setdefaulttimeout(1)
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket_obj.connect_ex((host, port))
    socket_obj.close()
    return result == 0    

def check_host(*args):
    start_time = datetime.datetime.now()
    ip_addr, os_type = args[0]
    print('start to check host: %s' % ip_addr)
    pool = eventlet.GreenPool()
    if os_type == LINUX_OS:
        args = [(ip_addr, port) for port in LINUX_PORTS]
        for item in pool.imap(_connect, args):
            if item:
                print('host %s is alive and cost %s' % (ip_addr, str(datetime.datetime.now() - start_time)))
                return ip_addr
    print('host %s is dead and cost %s' % (ip_addr, str(datetime.datetime.now() - start_time)))
    return None


# read config file from config.yaml

with open('config.yaml', 'r') as f:
    config = yaml.load(f.read(), Loader=yaml.SafeLoader)

network_segment = config['setup']['network_segment']
os_type = config['setup']['os_type']
nodes = config['setup']['nodes']

network = ipaddress.ip_network(network_segment)
hosts = list(network.hosts())
pool = eventlet.GreenPool()
args = [(str(host), LINUX_OS) for host in hosts]
result = [item for item in pool.imap(check_host, args) if item]
print(result)


# login in with the credentials in config.yaml
# for node in nodes:
#     client = SSHClient()
#     client.connect(hostname=node['id_addr'],                    
#                    username=node['root'],
#                    password=node['password'])
#     client.close()

# change the ip address to what in config.yaml


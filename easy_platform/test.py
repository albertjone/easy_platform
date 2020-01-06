import socket

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

# for i in range(0,255):
#     res = connect("192.168.1."+str(i), 22)
#     if res:
#         print("Device found at: ", "192.168.1."+str(i) + ":"+str(22))
print(connect('192.168.199.156', 22))
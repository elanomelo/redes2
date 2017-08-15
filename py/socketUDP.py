import socket
import datetime
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8053
MESSAGE = ""
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.setblocking(0)
seq = 1
rtt = 0
for i in range(0,10):
    time0 = time.time()
    MESSAGE = "PING {0} {1}".format(seq,time0)
    seq += 1
    print('Enviando ' + MESSAGE)
    try:
        sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
        # time.sleep(1)
        sock.settimeout(1)
        data, addr = sock.recvfrom(1024)
        time1 = time.time()
        data = data.decode('latin-1').split(' ')
        rtt = float(data[1]) - time1
        print(data[0] + ' RTT: ' + str(datetime.datetime.fromtimestamp(rtt / 1e3).time().microsecond / 1000) + 'ms')
    except socket.timeout:
        print('Timeout')
    except Exception as e:
        print('PERDIDO! ' + str(e))

sock.close()

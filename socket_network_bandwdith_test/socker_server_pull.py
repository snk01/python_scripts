import socket
import time
import string
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 20888

sock.bind((host, port))

sock.listen(1)

conn, addr = sock.accept()

while True:
    rdata, addr = conn.recvfrom(2048)
    # Process Accordingly
    # print("Received Message: {}".format(str(rdata, "utf-8")))
    # time.sleep(0.1)

sock.close()

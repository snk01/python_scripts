import socket
import time
import string
import random
import multiprocessing as mp

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''       # Listening Server IP
port = 20888    # Change Accordingly

sock.connect((host, port))

letters = string.ascii_lowercase
sample_message = ''.join(random.choice(letters) for i in range(896))

# Low CPU Load
def sendSampleMessage():
    sock.send(sample_message.encode("UTF-8"))
    return 0

# High CPU Load
def sendRandomMessage(length):
    message = ''.join(random.choice(letters) for i in range(896))
    sock.send(message.encode("UTF-8"))
    return 0

# Single Threaded
# for i in range(1,10000000):
#     sendRandomMessage(i)

# For Multiple Threads to Read/Write
ll = range(1,1000000000) # For Huge Buffere

with mp.Pool(8) as p:
    p.imap_unordered(sendSampleMessage, ll)
    p.imap_unordered(sendRandomMessage, ll)
    p.close()
    p.join()
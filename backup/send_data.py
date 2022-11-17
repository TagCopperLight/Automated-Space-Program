import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4000))
client.sendall("I am CLIENT\n".encode('utf-8'))
client.sendall('salut'.encode('utf-8'))

client.close()
import socket

ip_address = '10.61.59.84'
#10.61.56.10
port = 5000
buffer = 1024
message = 'owo uwu OuO 0w0?'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(message.encode())

s.close()


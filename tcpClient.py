import socket

host = '127.0.0.1'
port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\n\n')
resp = client.recv(1024)
print(resp.decode('utf-8'))

client.close()

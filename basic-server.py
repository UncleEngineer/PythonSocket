# basic-server.py

import socket

serverip = 'localhost'
port = 7000

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	server.bind((serverip,port))
	server.listen(5)
	print('Wating for client...')

	client, addr = server.accept()
	print('Connect from: ', str(addr))
	data = client.recv(1024).decode('utf-8')
	print('Message from client: ', data)
	client.send('We received your Message!'.encode('utf-8'))
	client.close()
	
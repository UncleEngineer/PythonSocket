# chat-server.py

import socket
import datetime
import threading

PORT = 7500
BUFSIZE = 4096
SERVERIP = 'localhost' # YOUR IP

clist = [] # Client List

def client_handler(client,addr):
	while True:
		try:
			data = client.recv(BUFSIZE)
		except:
			clist.remove(client)
			break

		if (not data) or (data.decode('utf-8') == 'q'):
			clist.remove(client)
			print('OUT: ',client)
			break
		msg = str(addr) + '>>> ' + data.decode('utf-8') # ข้อความส่งไปให้ชาวบ้านเขา
		print('USER: ',msg)
		print('----------')
		for c in clist:
			c.sendall(msg.encode('utf-8'))

	client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((SERVERIP,PORT))
server.listen(5)

while True:
	client, addr = server.accept()
	clist.append(client)
	print('ALL CLIENT: ', clist)

	task = threading.Thread(target=client_handler, args=(client, addr))
	task.start()

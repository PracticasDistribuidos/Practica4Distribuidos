import socket
import json
HOST = '127.0.0.1'
PORT = 6969
def sendMsg(msg):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		msg = json.dumps(msg)
		msg = bytes(msg, 'utf-8')
		s.sendall(msg)
		data = s.recv(1024)
	print('Recieved', repr(data))
	
def main():
	nick = input("Nick: ")
	msg = {"username":nick}
	sendMsg(msg)

if(__name__=="__main__"):
    main()

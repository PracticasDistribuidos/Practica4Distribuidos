import socket
import json
HOST = '127.0.0.1'
PORT = 6969
def sendMsg():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		msg = json.dumps({"msg":"hola", "size":"1"})
		msg = bytes(msg, 'utf-8')
		s.sendall(msg)
		data = s.recv(1024)
def main():
	print('Recieved', repr(data))

#	nick = input("Nick: ")
#	print("hola, ", nick)

if(__name__=="__main__"):
    main()

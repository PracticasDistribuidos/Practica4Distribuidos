import socket
import json
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6969        # Port to listen on (non-privileged ports are > 1023)
def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(1024)
				if not data:
					break
				print(data)
				obj = json.loads(data)
				print(obj)
				print(obj["msg"])
				print(obj["size"])
				conn.sendall(data)
if(__name__=="__main__"):
	main()

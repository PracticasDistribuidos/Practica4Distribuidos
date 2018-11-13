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
				if obj["opt"] == 0 :
					if len(obj["username"]) == 0:
						print("no nick found")
						data = {"status":1, "description":"no nick found"}
						conn.sendall(data)
					else :
						print( "welcome, {}".format(obj["username"]))
						data = {"status":0}
						data = json.dumps(data)
						data = bytes(data, 'utf-8')
						conn.sendall(data)

				elif obj["opt"] == 1:
					print(obj)
					data = {"status":0}
					data = json.dumps(data)
					data = bytes(data, 'utf-8')
					conn.sendall(data)
				elif obj["opt"] == 2:
					print(obj)
					data = {"status":0, "users":["nick","joe", "pan"]}
					data = json.dumps(data)
					data = bytes(data, 'utf-8')
					conn.sendall(data)
				elif obj["opt"] == 3:
					print(obj)
					data = {"status":0}
					data = json.dumps(data)
					data = bytes(data, 'utf-8')
					conn.sendall(data)
				elif obj["opt"] == 4:
					print(obj)
					data = {"status":0}
					data = json.dumps(data)
					data = bytes(data, 'utf-8')
					conn.sendall(data)
				else :			
					print(obj)
					data = {"status":0}
					data = json.dumps(data)
					data = bytes(data, 'utf-8')
					conn.sendall(data)	
if(__name__=="__main__"):
	main()

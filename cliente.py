import socket
import json
import threading
HOST = '127.0.0.1'
PORT = 6788

def sendPublicMessage(s, nick):
	message = input("Mensaje: ")
	data = {"type": "SEND_MESSAGE","destinatary": "ALL","message": message}
	sendMsg(data, s)
def checkOnlineUsers(s, nick):
	data = {"type": "LIST_USERS"}
	sendMsg(data, s)
def sendPrivateMessage(s, nick):
	recipient = input("Destinatario: ")
	message = input("Mensaje: ")
	data = {"type": "SEND_MESSAGE","destinatary": recipient,"message": message}
	sendMsg(data, s)
def exitChat(s, nick):
	data = {"type": "EXIT"}
	sendMsg(data, s)
def showMenu():
	print("\n1) Enviar un mensaje público que será enviado a todos los usuarios.")
	print("\n2) Consultar los usuarios conectados.")
	print("\n3) Enviar un mensaje privado a un usuario.")
	print("\n4) Salir del chat.")
def getOption():
	option = input("\nQue quieres hacer? ")
	return option
def sendMsg(msg, s):
	msg = json.dumps(msg)
	msg = bytes(msg, 'utf-8')
	s.sendall(msg)
def reciever(s):
	while True:
		try:
			data,address = s.recvfrom(1024)
		except:
			print("Failed conection")
			continue
		response = json.loads(data.decode('utf-8'))
#		print(response)
		if response["type"] == "ERROR" :
			print("\n{},\n".format(response["description"]))
		else:
#			print("soy el else")
#			print(response)
			#response from conection, doesn't apply
			#if response["opt"]:
			#	print("\n{}".format(response["username"]))
			
			#response from online users
			#{type: "USER_LIST",users: [User A, User B, ...]}
			if response["type"] == "USER_LIST" :
				print("online users:\n")
				for x in response["users"]:
					print(x)
			#response from public message
			#{type: "SEND_MESSAGE",sender: username,message: message}
			elif response["type"] == "MESSAGE" :
				print('\n{}:'.format(response["sender"]))
				print('\t{}'.format(response["message"]))
			#response from private message
			#{type: "SEND_MESSAGE",sender: username,message: message}
			#elif response["type"] == "SEND_MESSAGE" :
			#	print("\n{}(PRIVATE):\n{}\n".format(response["sender"], reponse["message"]))
			#response from exit chat
			#{type: "ACKNOWLEDGE",description: "EXIT_OK"}
			elif response["type"] == "ACKNOWLEDGE" :
				print("\n{} is offline\n".format(response["username"]))
			#wierd response
			else:
				print("Nothing")
def main():
	nick = input("Nick: ")
	msg = {"type":"CONNECT","nick":nick}
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		s.connect((HOST, PORT))
		sendMsg(msg, s)
		data = s.recv(1024)
#		print(data)
		
		response = json.loads(data)
		if response["type"] == "ERROR" :
			print("Oops, {}".format(response["description"]))
			return 
		else :
			print("welcome to the chat, {}".format(nick))
			recieverT = threading.Thread(name='reciever', target=reciever, args=[s], daemon=True)
			recieverT.start()
			while True:
				showMenu()
				opt = getOption()
				if opt == "1" :
					sendPublicMessage(s, nick)
				elif opt=="2" :
					checkOnlineUsers(s, nick)
				elif opt=="3" :
					sendPrivateMessage(s, nick)
				elif opt=="4" :
					exitChat(s, nick)
					break
				else :
					print("nothing")			
		s.close()

if(__name__=="__main__"):
	main()


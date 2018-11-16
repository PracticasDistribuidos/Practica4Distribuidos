import socket
import json
import threading
HOST = '127.0.0.1'
PORT = 6969

def sendPublicMessage(s, nick):
	message = input("Mensaje: ")
	data = {"opt":1,"username":nick, "message":message}
	sendMsg(data, s)
#	response = sendMsg(data, s)
#	if response["status"] == 1 :
#		print("\n{},\n".format(response["description"]))
def checkOnlineUsers(s, nick):
	data = {"opt":2,"username":nick}
	sendMsg(data, s)
#	response = sendMsg(data, s)
#	if response["status"] == 1 :
#		print("\n{},\n".format(response["description"]))
#	else:
#		for x in response["users"]:
#			print(x)	
def sendPrivateMessage(s, nick):
	recipient = input("Destinatario: ")
	message = input("Mensaje: ")
	data = {"opt":3,"username":nick, "recipient":recipient, "message":message}
	sendMsg(data, s)
#	response = sendMsg(data, s)
#	if response["status"] == 1 :
#		print("\n{},\n".format(response["description"]))
def exitChat(s, nick):
	data = {"opt":4,"username":nick}
	sendMsg(data, s)
#	response = sendMsg(data, s)
#	if response["status"] == 1 :
#		print("\n{},\n".format(response["description"]))
#	elif response["status"] == 0 :	
#		print("You're offline.")
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
#	data = s.recv(1024)
	#data = repr(data)
#	response = json.loads(data)
#	return response
def reciever(s):
	while True:
		data = s.recv(1024)
		#data = repr(data)
		response = json.loads(data)
		if response["status"] == 1 :
			print("\n{},\n".format(response["description"]))
		else:
			if response["opt"] == 0 :
				print("\n{}".format(response["username"]))
			elif response["opt"] == 1 :
				print("\n{}:\n{}\n".format(response["username"], reponse["message"]))
			elif response["opt"] == 2 :
				for x in response["users"]:
					print(x)
			elif response["opt"] == 3 :
				print("\n{}:\n{}\n".format(response["username"], reponse["message"]))
			elif response["opt"] == 4 :
				print("\n{} is offline\n".format(response["username"]))
			else:
				print("Nothing")
def main():
	nick = input("Nick: ")
	msg = {"opt":0,"username":nick}
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		sendMsg(msg, s)
		data = s.recv(1024)
		print(data)
		response = json.loads(data)
#		print(response)
		if response["status"] == "1" or  response["status"] == 1 or response["status"] == '1':
			print("Oops")
			return 
		else :
			print("welcome to the chat, {}".format(nick))
#			senderT = threading.Thread(name='sender', target=sender, args=[s], daemon=True)
#			senderT.start()
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


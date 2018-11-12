import socket
import json
HOST = '127.0.0.1'
PORT = 6969

def sendPublicMessage(s, nick):
	message = input("Mensaje: ")
	data = {"opt":1,"username":nick, "message":message}
	response = sendMsg(data, s)
	if response["status"] == 1 :
		print("\n{},\n".format(response["description"]))
def checkOnlineUsers(s, nick):
	message = input("Mensaje: ")
	data = {"opt":2,"username":nick, "message":message}
	response = sendMsg(data, s)
	if response["status"] == 1 :
		print("\n{},\n".format(response["description"]))	
def sendPrivateMessage(s, nick):
	recipient = input("Destinatario: ")
	message = input("Mensaje: ")
	data = {"opt":3,"username":nick, "recipient":recipient, "message":message}
	response = sendMsg(data, s)
	if response["status"] == 1 :
		print("\n{},\n".format(response["description"]))
def exitChat(s, nick):
	data = {"opt":4,"username":nick}
	response = sendMsg(data, s)
	if response["status"] == 1 :
		print("\n{},\n".format(response["description"]))
	elif response["status"] == 0 :	
		print("You're offline.")
def showmenu():
	print("\n1) Enviar un mensaje público que será enviado a todos los usuarios.")
	print("\n2) Consultar los usuarios conectados.")
	print("\n3) Enviar un mensaje privado a un usuario.")
	print("\n4) Salir del chat.")
	option = input("\nQue quieres hacer? ")
	return option

def sendMsg(msg, s):
	s.connect((HOST, PORT))
	msg = json.dumps(msg)
	msg = bytes(msg, 'utf-8')
	s.sendall(msg)
	data = s.recv(1024)
	#data = repr(data)
	response = json.loads(data)
	return response
	
def main():
	nick = input("Nick: ")
	msg = {"opt":0,"username":nick}

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		response = sendMsg(msg, s)
		if response["status"] != 0 :
			print("Oops")
			return 
		else :
			print("welcome to the chat, {}".format(nick))
			opt = showmenu()
			if opt == "1" :
				sendPublicMessage(s, nick)
			elif opt=="2" :
				checkOnlineUsers(s, nick)
			elif opt=="3" :
				sendPrivateMessage(s, nick)
			elif opt=="4" :
				exitChat(s, nick)
			else :
				print("nothing")

if(__name__=="__main__"):
	main()


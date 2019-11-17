
import socket
import random,time
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" 
channel = "#test482" 
botnick = "alpha-bot"
adminname = "Teja0110"
botnickca= "alpha-bot:"
exitcode = "die"
ircsock.connect((server, 6667))
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) 
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8"))
def joinchan(chan):
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8")) 
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1: 
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
def ping():
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
def sendmsg(msg, target=channel):
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))
def main():
	joinchan(channel)
	greet=["Hello","I said Hi","Okay forget it"]
	while 1:
		ch=random.randomint(0,1)
		if ch=0:
			sendmsg("Hi")
		else:
		
			ircmsg = ircsock.recv(2048).decode("UTF-8")
			print(ircmsg)
			i=0
			while ircmsg is None:
				sendmsg(greet[i])
				time.wait(3)
				ircmsg = ircsock.recv(2048).decode("UTF-8")
				if i ==2:
					return

			ircmsg = ircmsg.strip('\n\r')
			if ircmsg.find("PRIVMSG") != -1:
				name = ircmsg.split('!',1)[0][1:]
				message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
				if len(name) < 17:
					message=message.split(':')[1]
					arr=message.split(' ')
					if 'Hi' in arr or 'Hello' in arr != -1:
						sendmsg("Hello back" + name + "!")
						time.sleep(3)
						sendmsg("How are you" + name)
						time.sleep(3)
						print(arr)
					if  'you' in arr and 'how' in arr:
						sendmsg("I'm good" + name + "!")
						time.sleep(3)
						sendmsg("what abt you" + name)
						time.sleep(3)

					
					if message[:5].find('.inbox') != -1:
						target = message.split(' ', 1)[1]
						if target.find(' ') != -1:
							message = target.split(' ', 1)[1]
							target = target.split(' ')[0]
						else:
							target = name
							message = "format is wrong"
						sendmsg(message, target)
					if name.lower() == adminname.lower() and message.rstrip() == exitcode:
						  sendmsg("oh...")
						  ircsock.send(bytes("QUIT \n", "UTF-8"))
						  return
					if message.find('list'):
						 ircsock.send(bytes("NAMES \n", "UTF-8"))


			else:
				if ircmsg.find("PING :") != -1:
					ping()

main()

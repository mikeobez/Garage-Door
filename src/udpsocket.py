import socket
import garagedoor

#TODO: Dynamically get the IP address of the machine
UDP_IP = "192.168.1.140"
UDP_Port = 2523

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#TODO: Try-Catch here in case we are already running. Avoid a crashing
sock.bind((UDP_IP, UDP_Port))

gd = garagedoor.GarageDoor("Open Sesame")

while True: #TODO: There has to be a better way to do this
	data, addr = sock.recvfrom(1024)
	print addr
	print data

	gd.Actuate(data)




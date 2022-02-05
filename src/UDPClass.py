import socket
import garagedoor

#Gets the IP address of the host machine
def get_my_IP_Address():
	BROADCAST_IP = '10.255.255.255'
	try:
		host_ip = socket.gethostbyname(socket.gethostname())
	except:
		host_ip = '-1'

	if host_ip.startswith("127.0"):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((BROADCAST_IP, 1))
		host_ip = s.getsockname()[0]
	return host_ip

UDP_IP = get_my_IP_Address()
#check if the UDP_IP was fetched correctly. If not, exit gracefully.
#if(UDP_IP == '-1'):
#	print("Problem with fetching host IP address, exiting")
#	return

UDP_Port = 2523

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Try-Catch here in case we are already running. Avoid a crashing
try:
	sock.bind((UDP_IP, UDP_Port))
except Exception as e:
	print("Problem opening IP/Port combo")
	print(repr(e))

gd = garagedoor.GarageDoor(b'Open Sesame')

while True: #TODO: There has to be a better way to do this
	data, addr = sock.recvfrom(1024)
	print(addr)
	print(data)

	gd.Actuate(data)





from threading import Thread
import socket
import GarageDoorClass
import UDPClass

global received_data

#Return the IP address of the host machine
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

def main():
    #start the UDP receive thread
    UDP_IP = get_my_IP_Address()
    #TODO check if the UDP_IP was fetched correctly. If not, exit gracefully.
    #if(UDP_IP == '-1'):
    #	print("Problem with fetching host IP address, exiting")
    #	return

    UDP_Port = 2523
    udp = UDPClass.UDP()

    UDP_rx = Thread(target=udp.ReceiveThread, args=(UDP_IP,UDP_Port))
    UDP_rx.start()

    gd = GarageDoorClass.GarageDoor(b'Open Sesame') #create an instance of garage door with passphrase Open Sesame.
    while True:
        if(udp.received_data):
            gd.Actuate(udp.received_data)
            udp.received_data=''

if(__name__=="__main__"):
    main()

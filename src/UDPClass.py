import socket

global received_data

class UDP:
	def __init__(self):
		self.received_data = ''
		print("Init")

	def ReceiveThread(self,IP_Address_In,Port_Num_In):
		print("IP=",IP_Address_In)
		print("Port",Port_Num_In)

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		#Try-Catch here in case port is unailable. Avoid a crashing
		try:
			sock.bind((IP_Address_In, Port_Num_In))
		except Exception as e:
			print("Problem opening IP/Port combo")
			print(repr(e))

		print("successfully opened port")

		while True:
			try:
				data, addr = sock.recvfrom(1024)
				self.received_data = data
				print("Success", data)

			except socket.error:
				pass



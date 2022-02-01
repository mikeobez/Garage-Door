#import libraries
import RPi.GPIO as GPIO
import time

print "garagedoor class loaded successfully"

class GarageDoor:
	def __init__(self,passphrase_init):
		self.passphrase = passphrase_init

		#GPIO init
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		#pin to use for opening the garage door - port #16 -> BCM23
		self.DoorActuateBCM = 23

		#init pin
		GPIO.setup(self.DoorActuateBCM,GPIO.OUT)

	def Actuate(self,passphrase_attempt):
		#check passphrase
		if (passphrase_attempt == self.passphrase):
			#alternate off/on in 1-sec intervals
			print "Simulate Button Press"
			GPIO.output(self.DoorActuateBCM,1)
			time.sleep(1)
			print "Release the Button"
			GPIO.output(self.DoorActuateBCM,0)

	#TODO: Add a function to get the current state of the door


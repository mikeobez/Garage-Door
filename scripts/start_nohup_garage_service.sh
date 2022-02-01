#the nohup service for running the garagedoor service in the background
export ProjectPath=/home/pi/Documents/Projects/Garage-Door

nohup $ProjectPath/scripts/start_udp_service.sh &

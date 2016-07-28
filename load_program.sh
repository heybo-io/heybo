
#network={
#	ssid="The Link"
#	psk="thelinkseoul"
#	key_mgmt=WPA-PSK
#}

sleep 10

#Set up environment

sudo amixer -D default sset PCM 100%

#Execute

cd /home/pi/heybo/ && git pull && python3 heybo-core/cap_and_send.py

exit 0

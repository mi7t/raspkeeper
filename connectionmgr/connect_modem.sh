echo -ne 'AT^NDISDUP=1,0\r\n' > /dev/ttyUSB0
sleep 1
echo "Connecting modem..."
echo -ne 'AT^NDISDUP=1,1,"internet.static"\r\n' > /dev/ttyUSB0
sleep 5
/sbin/dhclient -v wwan0

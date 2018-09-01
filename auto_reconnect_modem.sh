p_hostname=`hostname`;
p_uptime=`uptime | tr " " ,`;
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  echo "IPv4 is up"
	#tmp_ip=`wget http://ipinfo.io/ip -qO -`;
        #python notify_email.py $p_hostname"-Modem_reconnect" "IP :"$tmp_ip"_Uptime"$p_uptime
else
  echo "IPv4 is down disconnecting modem..."
	/sbin/dhclient -r wwan0
	/usr/bin/killall -TERM dhclient
	echo -ne 'AT^NDISDUP=1,0\r\n' > /dev/ttyUSB0
	sleep 1
	echo "Connecting modem..."
	echo -ne 'AT^NDISDUP=1,1,"internet.static"\r\n' > /dev/ttyUSB0
	sleep 5
        /sbin/dhclient -v wwan0
	sleep 2;
	tmp_ip=`wget http://ipinfo.io/ip -qO -`;
        python notify_email.py $p_hostname"-Modem_reconnect" "IP :"$tmp_ip"_Uptime"$p_uptime
fi

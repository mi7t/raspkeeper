#! /bin/bash
### BEGIN INIT INFO
# Provides: noip
# Required-Start: $syslog
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: noip server
# Description:
### END INIT INFO
 
case "$1" in
    start)
	if [ -f /tmp/usb_modem.lock ]
	then
	echo "Another instance is running....";
	exit 0;
fi
        echo "connect modem is starting"
        # Starting Programm
	#/etc/init.d/connect_modem.sh &
        echo -ne 'AT^NDISDUP=1,1,"internet.static"\r\n' > /dev/ttyUSB0
	/sbin/dhclient -v wwan0
	echo $$ > /tmp/usb_modem.lock; 
        ;;
    stop)
        echo "connectmodem is ending"
        # Ending Programm
        echo -ne 'AT^NDISDUP=1,0\r\n' > /dev/ttyUSB0
        ;;
    *)
        echo "Use: /etc/init.d/noip {start|stop}"
        exit 1
        ;;
esac
exit 0

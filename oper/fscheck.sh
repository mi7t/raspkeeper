#!/bin/bash
fs_treshold=90;
zoznam="zoznam.txt";
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env;
send()
{
echo posielam sms $cislo $text;
sendsms $cislo $text
}

f_send_sms()
{
for cislo in `cat $zoznam | grep -v "#"`
do
        send;
        sleep 1;
done
}


df -Pl | grep -v Capacity | grep -v Mobile | awk '{print $5,$6}' | sed 's:\%::g' | while read prvy druhy
do
text=MyRaspberry:${nodename}_${prvy}%_FS:${druhy};
if [ $prvy -gt $fs_treshold ]
then
f_send_sms;
echo "Killing motion daemon";
killall motion
fi
done
exit 0;

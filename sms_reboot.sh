#!/bin/bash

FILE=/tmp/sms_reboot.req     
if [ -f $FILE ]; then
#  echo "File $FILE exists."
sendsms 421949020353 rebooting
/sbin/reboot
fi

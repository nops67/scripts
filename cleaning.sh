#!/bin/bash

#Functions
delay() {
	sleep 2
}

rmlogs() {
	for log in $(ls /var/log/); do
		if [[ $log != apt ]]; then
			rm -rv /var/log/$log
		fi
	done
}

#Check privileges
if [[ $UID != 0 ]]; then
	echo "You don't have permission to run this command. Run as root."
	exit 1
fi

#Menu
while [[ $option != 0 ]]; do

clear

echo "
	Menu:

1 - Clean home cache
2 - Clean all logs
3 - Clean miscellaneous stuff
0 - Quit

"

read -p "Select an option [0-3] > " option

echo ""

case $option in
	1)	echo "Cleaning home directory cache..."
		delay
		rm -r /home/pc/.cache
		;;
	2)	echo "Cleaning all logs..."
		delay
		rmlogs
		delay
		;;
	3)	echo "Cleaning miscellaneous stuff..."
		delay
		rm -rv /home/pc/.local/share/recently-used.*
		rm -rv /home/pc/.mozilla/firefox/Crash\ Reports
		rm -rv /home/pc/.xsession-errors.*
		rm -rv /usr/lib/firefox/browser/features/*
        delay
		;;
	0)	echo "Quiting..."
		delay
	    clear
		exit
		;;
	*)	echo "Insert a valid option [0-3]..."
		sleep 3
esac

done

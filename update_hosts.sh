#!/bin/bash

#Check privileges
if [[ $UID != 0 ]]; then
	echo "You need to run this script as root."
	exit 1
fi

cd /etc/

#Backup hosts file
if [[ -f hosts ]]; then
	mv hosts hosts.old && echo "Backup created successfully!"
else
	echo "Couldn't find hosts file so no backup created!"
fi

sleep 2

#Download hosts file
wget --https-only https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts

#Modify some content in hosts file
sed -i 's/^0.0.0.0/127.0.0.1/; s/#0.0.0.0/127.0.0.1/; s/127.0.0.1 googleads.g.doubleclick.net/#127.0.0.1 googleads.g.doubleclick.net/; s/127.0.0.1 click.discord.com/#127.0.0.1 click.discord.com/' hosts
sed -i -e '14a\127.0.0.1 pc' -e '31a\127.0.0.1 www.reddit.com' hosts

sleep 1

echo "Update Completed."

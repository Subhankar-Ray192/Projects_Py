Adding Cmd_Alias 'BASIC' to sudoers file..."
echo "Cmd_Alias BASIC = /bin/ls, /bin/cd, /bin/pwd, /bin/mkdir, /bin/rm, /bin/cp, /bin/mv, /usr/bin/touch" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'NETWORK' to sudoers file..."
echo "Cmd_Alias NETWORK_CMDS = /sbin/ifconfig, /bin/ping, /usr/bin/ssh, /usr/bin/wget, /usr/bin/curl" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'EDITOR' to sudoers file..."
echo "Cmd_Alias EDITOR = /bin/nano, /bin/vi" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'TOOLS' to sudoers file..."
echo "Cmd_Alias TOOLS = /bin/grep, /usr/bin/awk, /usr/bin/sed, /usr/bin/find, /bin/mount, /sbin/mount.*, /bin/umount" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'MISC' to sudoers file..."
echo "Cmd_Alias MISC = /usr/bin/screen, /usr/bin/tmux, /usr/bin/zip, /usr/bin/unzip, /bin/netstat, /usr/sbin/tcpdump, /usr/sbin/iptraf, /usr/bin/nmap, /usr/bin/rsync, /usr/bin/scp" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'SYSTEM' to sudoers file..."
echo "Cmd_Alias SYSTEM = /usr/bin/sudo, /usr/bin/apt-get, /usr/bin/apt, /bin/systemctl, /usr/bin/top, /usr/bin/htop, /bin/df" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'FIREWALL' to sudoers file..."
echo "Cmd_Alias FIREWALL = /usr/sbin/ufw, /sbin/iptables, /usr/sbin/firewalld" | sudo tee -a /etc/sudoers > /dev/null

Adding Cmd_Alias 'TOOLS' to sudoers file..."
echo "Cmd_Alias TOOLS = /bin/grep, /usr/bin/awk, /usr/bin/sed, /usr/bin/find, /bin/mount, /sbin/mount.*, /bin/umount" | sudo tee -a /etc/sudoers > /dev/null



#### This Session will help you to get familiarized with all the most common Linux commands

#### and their usages. These commands are divided into 15 sections based on their functionalities.

## System Related Commands

#### These commands are used to view and manage Linux system-related information.


**1. uname (https://linoxide.com/linux-command/uname-command/)**
: Displays linux system information. With -a switch you can view all the
information, with -r switch you can view kernel release information and w
ith -o you can view OS information
**2. cat /etc/redhat_release** : Shows which version of redhat installed
**3. uptime (https://linoxide.com/linux-command/linux-uptime-command/)**
: Shows how long the system has been running
**4. hostname (https://linoxide.com/linux-command/display-set-hostname-linu
x/)** : Shows system host name. With -i switch you can view
the ip address of the machine and with -d you can view the domain name
**5. last (https://linoxide.com/linux-command/linux-last-command/) reboot**
: Shows system reboot history
**6. date (https://linoxide.com/linux-command/date-command-linux/)**
: Shows the current date and time. You can specify the format you want to
view the date as well. As an example, by using 'date +%D' you can view the
date in 'MM/DD/YY' format
**7. cal (https://linoxide.com/linux-command/cal-ncal-commands-display-calen
der-linux/)** : Shows the calendar of the current mont
h. With -y switch you can view the calendar of the whole current year
**8. w** : Displays who is logged (https://linoxide.co
m/linux-command/linux-w-command/) on and what they are doing
**9. whoami (https://linoxide.com/linux-command/linux-whoami-command/)**
: Shows current user id
**10. finger (https://linoxide.com/linux-command/finger-command-user-detail
s/) user** : Displays information about user
**11. reboot** : Reboots the system
**12. shutdown (https://linoxide.com/linux-command/examples-linux-shutdown-c
ommands/)** : Shuts down the system

## Hardware Related Commands

#### These commands are used to view and manage hardware-related aspects of the Linux

#### machine.


**13. dmesg (https://linoxide.com/linux-command/linux-dmesg-command/)**
: Displays all the messages from Kernel ring buffer. With -k switch you ca
n view kernel messages and with -u you can view userspace messages
**14. cat /proc/cpuinfo** : Displays information about processes and CPUs
of the system
**15. cat /proc/meminfo** : Displays details on hardware memory
**16. cat /proc/interrupts** : Lists the number of interrupts per CPU per I/O
device
**17. lshw** : Displays information on hardware configuration
of the system. But this command must be run as super user or it will only
report partial information
**18. lsblk** : Displays block device related information of t
he machine. With -a you can view all block devices
**19. free -m** : Shows used and free memory (https://linoxide.c
om/linux-command/linux-free-command/) (-m for MB)
**20. lspci -tv** : Shows information on PCI (https://linoxide.co
m/linux-how-to/few-command-helps-to-get-linux-hardware-details/) buses dev
ices
**21. lsusb -tv** : Shows information on USB (https://linoxide.co
m/linux-command/linux-lsusb-command-print-usb/) devices
**22. dmidecode (https://linoxide.com/linux-command/how-to-display-system-ha
rdware-information-in-bios/)** : Shows hardware info from the BI
OS (vendor details)
**23. hdparm -i /dev/sda** : Shows info about disk sda
**hdparm -tT /dev/sda** : Performs a read speed test on disk sda
**24. badblocks -s /dev/sda** : Tests for unreadable blocks (https://linoxide.
com/linux-how-to/how-to-fix-repair-bad-blocks-in-linux/) on disk sda

## Statistic Related Commands

#### These set of commands are used to view various kinds of stats of the Linux system


**25. mpstat 1** : Displays processors related statistics
(https://linoxide.com/linux-command/linux-mpstat-command/)
**26. vmstat 2** : Displays virtual memory statistics (ht
tps://linoxide.com/linux-command/linux-vmstat-command-tool-report-virtual-
memory-statistics/)
**27. iostat 2** : Displays I/O statistics (https://linox
ide.com/linux-command/linux-iostat-command/)
**28. tail -n 500 /var/log/messages** : Displays the last (https://linoxide.co
m/linux-command/linux-tail-command/) 500 kernel/syslog messages
**29. tcpdump -i eth1** : Captures all packets (https://linoxid
e.com/linux-how-to/14-tcpdump-commands-capture-network-traffic-linux/) flo
w on interface eth1. With -w switch you can specify a file where you can d
irect the output to
**tcpdump -i eth0 'port 80'** : Monitors all traffic on port 80 on int
erface eth
**30. lsof** : Lists all open files (https://linoxid
e.com/how-tos/lsof-command-list-process-id-information/) belonging to all
active processes
**lsof -u testuser** : Lists files opened by a specific user
**31. free -m** : Shows RAM memory details
**32. watch df -h** : Watches changeable (https://linoxide.c
om/linux-command/linux-watch-command/) disk usage continuously

## User-Related Commands

#### These commands are used to manage Linux users


**33. id** : Shows the active user and gr
oup information (https://linoxide.com/linux-command/linux-id-command/). Wi
th -G switch you can view the IDs of groups
**34. last** : Shows a list of last logins
on the system. Using -a switch you can add the hostname to the last colum
n of the output
**35. who** : Shows who is logged (http
s://linoxide.com/linux-command/linux-who-command/) on the system
**36. groupadd admin** : Adds the group (https://lino
xide.com/linux-command/groupadd-command/) "admin"
**37. useradd -c "Sam Tomshi" -g admin -m sam** : Creates user "sam" and adds
to group "admin"
**38. userdel sam** : Deletes user sam
**39. adduser sam** : Adds user (https://linoxide.
com/linux-command/linux-user-add-command/) "sam"
**40. usermod** : Modifies user information
**41. passwd user1** : Changes the password of user
1

## File Related Commands

#### These commands are used to handle files and directories


**42. ls -al** : Displays all information abou
t files/directories (https://linoxide.com/linux-command/20-ls-command-linu
x/). This includes displaying all hidden files as well
**43. pwd** : Shows current directory path
(https://linoxide.com/linux-command/linux-pwd-command/)
**44. mkdir directory-name** : Creates a directory (https://
linoxide.com/linux-command/linux-mkdir-command/)
**45. rm file-name** : Deletes file (https://linoxid
e.com/linux-command/linux-rm-command/)
**rm -r directory-name** : Deletes directory recursively
**rm -f file-name** : Forcefully removes file
**rm -rf directory-name** : Forcefully removes directory
recursively
**46. cp file1 file2** : Copies linux files (https://l
inoxide.com/linux-command/linux-cp-command/), here file1 to file
**cp -r dir1 dir2** : Copies dir1 to dir2, creates
dir2 if it doesn't exist
**47. mv file1 file2** : Moves files (https://linoxid
e.com/linux-command/mv-command-linux/) from one place to another/renames f
ile1 to file
**48. ln -s /path/to/target-directory-name link-dir** : Creates a symbolic
link (https://linoxide.com/linux-how-to/create-soft-link-linux/) to link-d
ir
**49. touch file** : Creates empty file (https://l
inoxide.com/linux-command/linux-touch-command/)
**50. cat file** : Prints the file content (http
s://linoxide.com/linux-command/13-cat-command-examples/) in terminal
**51. more file** : Display the contents of file
(https://linoxide.com/linux-command/linux-more-command/)
**52. head file** : Display the first (https://li
noxide.com/linux-command/linux-head-command/) 10 lines of file
**53. tail file** : Outputs the last 10 lines of
file
**tail -f file** : Outputs the contents of file
as it grows starting with the last 10 lines
**54. gpg -c file** : Encrypts file (https://linoxi
de.com/security/gpg-command-encrypt-decrypt-file/)
**gpg file.gpg** : Decrypts file
**55. cksum file** : View the checksum of the file
**56. diff file1 file2** : View the differences between
contents of file1 and file
**57. ln -s target-file link-file** : Create a soft link named link
-file to target-file


## Process Related Commands

#### These commands are used to handle Linux processes

**64. ps** : Displays your currently active processes
**ps aux | grep 'telnet'** : Displays all process ids related to telnet
process
**65. pmap** : Display Memory map (https://linoxide.com/li
nux-command/pmap-command/) of process
**66. top** : Display all running processes and cpu/memor
y usage (https://linoxide.com/linux-command/linux-top-command-examples-scr
eenshots/)
**67. kill pid** : Kills process (https://linoxide.com/linux-h
ow-to/linux-kill-command-examples/) with mentioned pid
**68. killall proc** : Kills all processes (https://linoxide.com/l
inux-command/linux-killall-my-options/) named proc
**69. pkill processname** : Sends kill signal to a process with its nam
e
**70. bg** : Resumes suspended jobs without bringing the
m to foreground (https://linoxide.com/linux-command/fg-bg/)
**71. fg** : Brings the most recent job to foreground
**fg n** : Brings job n to the foreground

## File Permission Related Commands

```
file to target file
```
**58. sort** : Sorts files in alphabetical o
rder
**59. uniq** : Compares adjacent lines in a

```
file and removes/reports any duplicate lines
```
**60. wc** : Counts number of words/lines
**61. dir** : Lists the content of the dire
ctory
**62. tee** : Command for chaining and redi
rection (https://linoxide.com/linux-how-to/linux-tee-command-examples/)
**63. tr** : Command for translating chara
cters (https://linoxide.com/how-tos/linux-tr-command/)


#### These commands are used to change permissions of the files

**72. chmod octal file-name** : Changes the permissions (ht
tps://linoxide.com/linux-command/chmod-command/) of file to octal
**chmod 777 /data/test.c** : Sets rwx permission for own
er , group and others
**chmod 755 /data/test.c** : Sets rwx permission for own
er and rx for group and others
**73. chown owner-user file** : Changes owner (https://lino
xide.com/linux-command/how-change-file-ownership-with-linux-chown-comman
d/) of the file
**chown owner-user:owner-group file-name** : Changes owner and group own
er of the file
**chown owner-user:owner-group directory** : Changes owner and group own
er of the directory
**74. chgrp group1 file** : Changes the group ownership
of the file to group

## Network Related Commands

#### These commands are used to view and edit network configurations related aspects of the

#### system


**75. ifconfig -a** : Displays all network interface (https://linoxide.
com/how-tos/linux-ifconfig/) and set ip address
**76. ifconfig eth0** : Displays eth0 ethernet port ip address and detail
s
**77. ip addr show** : Display all network interfaces (https://linoxide.
com/linux-command/use-ip-command-linux/) and ip addresses
**78. ip address add 192.168.0.1 dev eth0** : Sets ip address of eth0 device
**79. ethtool eth0** : Linux tool to show ethernet status
**80. mii-tool eth0** : Linux tool to show eth0 status
**81. ping host** : Sends echo requests (https://linoxide.com/linux-h
ow-to/ping-ipv6-address-windows-linux-cli/) to the host to test ipv4 conne
ction
**82. whois domain** : Gets who is information for domain
**83. dig domain** : Gets DNS nameserver information (https://linoxid
e.com/how-tos/useful-options-dig/) for domain
**dig -x host** : Reverse lookup host
**84. host google.com** : Lookup DNS (https://linoxide.com/linux-command/le
arn-host-command/) ip address for the name
**85. hostname -i** : Lookup local ip address
**86. wget file** : Downloads file
**87. netstat -tupl** : Lists all active listening ports (https://linoxid
e.com/linux-how-to/linux-netstat-commands-basic-advanced-examples/)
**88. nslookup** : Resolves domain names to IP addresses

## Compression / Archive Related Commands

#### These commands are used to compress and decompress files

**89. tar cf home.tar home** : Creates a tar (https://linoxide.com/li
nux-how-to/16-tar-commands-compress-extract-files-linux/) named home.tar c
ontaining home/
**tar xf file.tar** : Extracts the files from file.tar
**tar czf file.tar.gz files** : Creates a tar with gzip compression
**90. gzip file** : Compresses file and renames it to fil
e.gz
**91. bzip2 -z file** : Compresses file and renames it to fil
e.bz
**bzip2 -d file.bz2** : Decompress the file


## Package Installation Related Commands

#### These commands are used to manage Linux packages

**92. rpm -i pkgname.rpm** : Installs rpm based package
**rpm -e pkgname** : Removes package
**93. make** : Install from source (https://linoxide.com/how
-tos/linux-make-command-examples/) file

## Search Related Commands

#### These commands are used to search for files and patterns

**94. grep pattern files** : Searches for pattern in files
**grep -r pattern dir** : Searches recursively for pattern in
dir
**95. locate file** : Finds all instances of file
**96. find /home/tom -name 'index*'** : Finds file names that start with "in
dex" inside /home/tom directory
**find /home -size +10000k** : Finds files larger than 10000k in /h
ome

## Login Related Commands

#### These commands are used to log into another host

**97. ssh user@host** : Securely connect (https://linoxide.com/li
nux-command/learn-ssh-connection-options/) to a host as user
**ssh -p port $ user@host** : Connects to host using specific port
**98. telnet host** : Connects to the system using telnet port

## File Transfer Related Commands

#### These commands are used to copy files from one system to another system


**99. scp file.txt server2:/tmp** : Secure copy (https://li
noxide.com/how-tos/scp-command-file-directory-transfer-linux/) file.txt to
remote host /tmp folder
**scp nixsavy@server2:/www/*.html /www/tmp** : Copies *.html files fro
m remote host to current host /www/tmp folder
**scp -r nixsavy@server2:/www /www/tmp** : Copies all files and fo
lders recursively from remote server to the current system /www/tmp folder
**100. rsync -a /home/apps /backup/** : Synchronizes source to
destination (https://linoxide.com/how-tos/rsync-copy/)
**rsync -avz /home/apps $ linoxide@192.168.10.1** :/backup : Synchronize f
iles/directories between the local and remote system with compression enab
led

## Disk Usage Related Commands

#### These commands are used to view disk statistics

**101. df -h** : Shows free space (https://linoxide.
com/linux-command/13-df-command-examples-check-disk-space-linux/) on mount
ed filesystems
**df -i** : Shows free inodes on mounted filesys
tems
**102. fdisk -l** : Shows disks partitions (https://lino
xide.com/linux-command/fdisk-commands-manage-partitions-in-linux/) sizes a
nd types
**103. du -ah** : Displays disk usage (https://linoxid
e.com/linux-command/linux-du-command/) in human readable form
**du -sh** : Displays total disk usage on the cur
rent directory
**104. findmnt** : Displays target mount point (http
s://linoxide.com/linux-command/powerful-findmnt-command/) for all filesyst
ems
**105. mount device-path mount-point** : Mounts a device to the device-path

## Directory Traverse Related Commands

#### These commands are used to change the directory


**106. cd ..** : Goes up one level of the directory tree
**cd** : Goes to $HOME directory
**cd /test** : Changes to /test directory


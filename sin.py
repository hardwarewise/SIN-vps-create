#!/usr/bin/python3
#created by https://t.me/WolfCryptoPub

import fcntl
import os
import socket
import struct
from subprocess import Popen, STDOUT, PIPE
import sys
import termios
import time

DEFAULT_COLOR = "\x1b[0m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
MAX_LEN=struct.unpack('HHHH',fcntl.ioctl(0, termios.TIOCGWINSZ,struct.pack('HHHH', 0, 0, 0, 0)))[1]-5

def run(cmd_list):
	for cmd in cmd_list:
		proc=Popen(cmd,stderr=STDOUT,stdout=PIPE,shell=True)
		output=[]
		while True:
			line=proc.stdout.readline().strip().decode()[:MAX_LEN]
			if sys.argv[-1]!="-v":
				for i in range(len(output)):
					sys.stdout.write('\x1b[1A\r\x1b[2K')
				sys.stdout.flush()
			if not line: break
			output.append("\r  "+line)
			output=output[-5:]
			if sys.argv[-1]!="-v": print(DEFAULT_COLOR+"\n".join(output))
			else: print(DEFAULT_COLOR+output[-1])
			time.sleep(0.05)
		proc.wait()

if os.getuid()!=0:
	sys.exit("This program must be run with root privledges:\n\nsudo python3 {}".format(" ".join(sys.argv)))

os.system('clear')
print("""{1}.------..------..------..------.
|S.--. ||I.--. ||N.--. |
| :/\: || (\/) || (\/) |
| (__) || :\/: || :\/: |
| '--'S|| '--'I|| '--'N|
`------'`------'`------'`------'

{0}SIN Masternode Installer v0.2


Updating & Upgrading Ubuntu...""".format(BLUE,YELLOW))

run(["sudo apt-get update -y",
	'sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o DPkg::options::="--force-confdef" -o DPkg::options::="--force-confold"  install grub-pc',
	"apt-get upgrade -y"])

print(BLUE+"Creating Swap...")

run(["fallocate -l 4G /swap",
	 "chmod 600 /swap",
	 "mkswap /swap",
	 "swapon /swap"])
with open('/etc/fstab','r+') as f:
	line="/swap   none    swap    sw    0   0 \n"
	lines = f.readlines()
	if lines[-1]!=line:
		f.write(line)

print(BLUE+"Securing Server...")
run(["apt-get --assume-yes install ufw",
	 "ufw allow OpenSSH",
	 "ufw allow 18332",
	 "ufw default deny incoming",
	 "ufw default allow outgoing",
	 "ufw --force enable"])

print(BLUE+"Creating SIN User...")
run(["useradd --create-home -G sudo sin"])


print(BLUE+"Installing Build Dependencies...")
run(["apt install -y openssh-server build-essential git automake autoconf pkg-config libssl-dev libboost-all-dev libprotobuf-dev libdb5.3-dev libdb5.3++-dev protobuf-compiler cmake curl g++-multilib libtool binutils-gold bsdmainutils pkg-config python3 libevent-dev screen libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libqrencode-dev libprotobuf-dev protobuf-compiler"])

if os.path.exists('/home/sin/SIN-core'): print(BLUE+"SIN is already installed!")
else:
	print(BLUE+"Downloading & Compiling SIN...")
	run(["git clone https://github.com/SUQAORG/SIN-core.git",
		 "cd SIN-core && ./autogen.sh",
		 "cd SIN-core && ./configure --with-incompatible-bdb CFLAGS=-fPIC CXXFLAGS=-fPIC --enable-shared --disable-tests --disable-bench",
		 "cd SIN-core && make all install",
		 "cp -r /root/SIN-core /home/sin",
		 "chown sin:sin -R /home/sin/SIN-core"])

print(BLUE+"Running SIN...")
run(['su - sin -c "suqad &> /dev/null" '])

print(YELLOW+"Open your desktop wallet console (Help => Debug window => Console) and generate your masternode outputs by entering: masternode outputs")
txid=input(DEFAULT_COLOR+"  Transaction ID: ")
tx_index=input("  Transaction Index: ")

print(YELLOW+"Open your desktop wallet console (Help => Debug window => Console) and create a new masternode private key by entering: masternode genkey")
priv_key=input(DEFAULT_COLOR+"  masternodeprivkey: ")

print(YELLOW+"Open your desktop wallet config file (%appdata%/SIN/mainnet/sin.conf) and copy your rpc username and password! If it is not there create one! E.g.:\n\trpcuser=[SomeUserName]\n\trpcpassword=[DifficultAndLongPassword]")
rpc_user=input(DEFAULT_COLOR+"  rpcuser: ")
rpc_pass=input("  rpcpassword: ")

print(BLUE+"Saving config file...")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
this_ip=s.getsockname()[0]
s.close()
with open('/home/sin/.sin/sin.conf', 'w') as f:
	f.write("""rpcuser={0}
testnet=1
rpcpassword={1}
rpcallowip=127.0.0.1
listen=1
server=1
daemon=1
logtimestamps=1
maxconnections=256
[test]
rpcport=18332
addnode=51.83.43.115
masternode=1
externalip={2}:20980
bind={2}
masternodeaddr={2}
masternodeprivkey={3}""".format(rpc_user, rpc_pass, this_ip, priv_key))

print(BLUE+"Setting Up SIN Service File..."+DEFAULT_COLOR)
with open('/lib/systemd/system/sin.service', 'w') as f:
	f.write("""[Unit]

Description=SIN Masternode Server
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target
Alias=suqad.service

[Service]
User=sin
Group=users
ExecStart=/usr/local/bin/suqad -conf=/home/sin/.sin/sin.conf -datadir=/home/sin/SIN-core/
Type=forking
Restart=always
RestartSec=5
PrivateTmp=true
TimeoutStopSec=60s
TimeoutStartSec=5s
StartLimitInterval=120s
StartLimitBurst=15
PrivateTmp=false""")

os.system('systemctl daemon-reload')
os.system('systemctl enable sin')
os.system('systemctl start sin')
os.system('systemctl --no-pager status sin')
os.system('su - sin -c "suqa-cli masternode status &> /dev/null" ')
print(BLUE+"SIN Masternode Started...")

print(YELLOW+"""
SIN Masternode Setup Finished!
SIN Masternode Data:
IP: {0}:20980
Private key: {1}
Transaction ID: {2}
Transaction index: {3}
--------------------------------------------------
{4} {0}:20980 {1} {2} {3}
""".format(this_ip,priv_key,txid,tx_index,socket.gethostname().split('.')[0])+DEFAULT_COLOR)

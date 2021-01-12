#!/usr/local/bin/python
from pexpect import pxssh

import datetime
import sys, os
import subprocess

# coding: utf-8

now = datetime.datetime.now()


#python druid user1 user2 passwd passwd2

#user1 = str(sys.argv[1])
#user2 = str(sys.argv[2])
#passwd = str(sys.argv[3])
#passwd2 = str(sys.argv[4])
user1 = "gjensen"
user2 = "gil"
passwd = "Nerthus22"
passwd2 = "UllrSon12"
passwd3 = "Freya2018"

print('Chelmsford Squid Start-------------------------------------------------------------')

s=""
s = pxssh.pxssh()
string = ""
dfstring = ""

if s.login ('cmvpd017.chelmsford.visteon.com', user1, passwd):
	print("SSH session login cmvpd017.chelmsford.visteon.com  successful")
	s.sendline ('sudo /etc/init.d/squid status')
	s.prompt()         # match the prompt
	print(s.before)     # print everything before the prompt.
	print("  ")
	s.logout()
else:	
	print("login Failed")
print('Chelmsford Squid End')
print('-------------------------------------------------------------')
print('10.218.230.211 Start-------------------------------------------------------------')

s=""
s = pxssh.pxssh()
string = ""
dfstring = ""

if s.login ('10.218.230.211', user1, passwd):
	print("SSH session login 10.218.230.211  successful")
	s.sendline ('sudo /etc/init.d/squid status')
	s.prompt()         # match the prompt
	print(s.before)     # print everything before the prompt.
	print("  ")
	s.logout()
else:	
	print("login Failed")
	
print('10.218.230.211  End')
print('-------------------------------------------------------------')
print('chipd005.chennai.visteon.com Monit Start-------------------------------------------------------------')

s=""
s = pxssh.pxssh()
string = ""
dfstring = ""

if s.login ('chipd005.chennai.visteon.com ', user1, passwd3):
	print("SSH session login chipd005.chennai.visteon.com successful")
	s.sendline ('sudo /etc/init.d/squid status')
	s.prompt()         # match the prompt
	print(s.before)     # print everything before the prompt.
	print("  ")
	s.logout()
else:	
	print("login Failed")
	
print('chipd005.chennai.visteon.com Monit End')
print('-------------------------------------------------------------')


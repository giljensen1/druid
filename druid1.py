#!/usr/bin/python
# -*- coding: utf-8 -*-
from pexpect import pxssh
import getpass, datetime
import os, sys
import ConfigParser
import io

now = datetime.datetime.now()
process = raw_input('Which Servers do you wish to monitor squid or jenkins?: ')
process.lower()
process.strip()
username = raw_input('username: ')
password = getpass.getpass('password: ')

# Load the configuration file
with open("squid.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

with open("/var/www/html/stats/results.html", "w") as w:
        w.write("<html><head><title>Druid Stats</title></head><body><table>")
        w.write("Processing " + process + " servers \n")
        w.write("start *****************************************************************\n")
        w.write(now.strftime("%Y-%m-%d %H:%M"))
        w.write("\n")
        for section_name in config.sections():           
            for name, value in config.items(section_name):
                        try:                                                            
                            s = pxssh.pxssh()
                            w.write("<tr><td>")
                            hostname = '  %s ' % (value)
                            
                            w.write("</td></tr><tr><td><br><font color=rgb(115, 0, 153)>")
                            w.write("IP Address = ")
                            w.write(hostname + "\n")
                            w.write("</font></td></tr><tr><td><br><font color=blue>")
                            s.login (hostname, username, password)
                            s.sendline('hostname')
                            s.prompt()
                            w.write (s.before)
                            w.write("</font></td></tr><tr><td>")
                            s.sendline ('uptime')   
                            s.prompt()             
                            w.write (s.before)         
                            w.write("</td></tr><tr><td><br><font color=green>")
                            s.sendline ('df -h')
                            s.prompt()
                            w.write (s.before)
                            w.write("</font></td></tr><tr><td><br><font color=rgb(204, 0, 255)>")
                            s.sendline('sudo /etc/init.d/squid status')
                            s.prompt()
                            w.write(s.before)
                            s.logout()
                            w.write("</font></td></tr><tr><td>")
                            w.write("<br>----------------------------------------------------------------------------")
                            w.write("</td></tr>")
                        except pxssh.ExceptionPxssh, e:
                            print("/n")
                            print("error start //////////////////////////////////////////////////////////\n")
                            print("pxssh failed on login.")
                            print(hostname)
                            print(str(e))
                            print("/n")
                            print("error end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
        w.write("</table></body>")
        w.write("end *****************************************************************\n")
                   

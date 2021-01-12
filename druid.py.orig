from pexpect import pxssh
import getpass

import ConfigParser
import io
import datetime
import os


now = datetime.datetime.now()

# Load the configuration file
with open("/home/gjensen/Documents/python/squid.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

for section_name in config.sections():
    print('==================================================')
    print('Squid information for ', now.strftime("%Y-%m-%d %H:%M"))
    print('==================================================')
    #print('Squid:', section_name)
    
    #print '  Options:', config.options(section_name)
    for name, value in config.items(section_name):
       # print 
        try:   
            CPU_Pct=0
            s = pxssh.pxssh()
            #hostname = raw_input('hostname: ')
            #username = raw_input('username: ')
            #password = getpass.getpass('password: ')
            hostname = '  %s ' % (value)
            username = "gjensen"
            password = "Freya2018"    
            print("start *****************************************************************")
            print(hostname)
            s.login (hostname, username, password)
            s.sendline ('uptime')   # run a command
            s.prompt()             # match the prompt
            print (s.before)          # print everything before the prompt.
            s.sendline('hostname')
            s.prompt()
            print (s.before)
            s.sendline('sudo /etc/init.d/squid status')
            s.prompt()
            print(s.before)            
            s.sendline('sudo free -t -m')
            s.sendline ('df -h')
            s.prompt()
            print (s.before)            
            #s.sendline('grep "cpu " /proc/stat | awk "{usage = ($2+$4) * 100 / ($2+$4+$5)} END {print usage}"' )
            #s.prompt()
            #print(s.before)
            s.sendline('sudo ls -l /var/log/squid')
            s.prompt()
            print(s.before)
            s.logout()
            print("end*****************************************************************")
            print('\n\n\n\n\n\n\n')
        except pxssh.ExceptionPxssh, e:
            print("error start //////////////////////////////////////////////////////////")
            print "pxssh failed on login."
            print str(e)
            print
            print("error end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")



from pexpect import pxssh
import getpass
import codecs
import ConfigParser
import io
import datetime
import os
import binascii


now = datetime.datetime.now()
temp = ""
# Load the configuration file

with open("/home/gjensen/Documents/python/squid2.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

# load the output file
f = open("gil.txt","w+")
f.write('==================================================')
f.write('\n')
f.write('Squid information for ')
f.write(now.strftime("%Y-%m-%d %H:%M"))
f.write('\n')
f.write('==================================================')
f.write('\n')
for section_name in config.sections():

    #f.write('Squid:', section_name)
    #f.write '  Options:', config.options(section_name)
    for name, value in config.items(section_name):
       # f.write 
        try:   
            s = pxssh.pxssh()
            #hostname = raw_input('hostname: ')
            #username = raw_input('username: ')
            #password = getpass.getpass('password: ')
            hostname = '  %s ' % (value)
            username = "gjensen"
            password = "Freya2018"    
            f.write("start *****************************************************************")
            f.write('\n')
            f.write('\n')
            f.write("IP Address = ")
            f.write(hostname)
            f.write('\n\n')
            s.login (hostname, username, password)
            s.sendline('hostname')
            s.prompt()
            f.write(s.before)
            f.write('\n')
            s.sendline ('uptime')   # run a command
            s.prompt()             # match the prompt
            f.write (s.before)          # f.write everything before the prompt.
            f.write('\n')
            #temp ='top -bn1 | grep load | awk "{printf "%.2f%%", $(NF-2)}"' 
            #s.sendline(temp)
            #s.prompt()
            temp = (s.before)         
            f.write(temp)
            f.write('\n')
            s.sendline('sudo /etc/init.d/squid status')
            s.prompt()
            f.write(s.before)   
            f.write('\n')
            s.sendline('sudo free -t -m')
            s.sendline ('df -h')
            s.prompt()
            f.write (s.before)
            f.write('\n')
            s.sendline('grep cpu /proc/stat | awk {usage = ($2+$4) * 100 / ($2+$4+$5)} END f.write("usage")' )
            s.prompt()
            f.write(s.before)
            s.sendline('sudo ls -l /var/log/squid')
            s.prompt()
            f.write(s.before)

            f.write('\n')
            s.logout()
            f.write("end*****************************************************************")
            f.write('\n\n\n\n')
        except pxssh.ExceptionPxssh, e:
            f.write("error start //////////////////////////////////////////////////////////")
            f.write("pxssh failed on login.")
            print str(e)
            f.write()
            f.write("error end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
f.close()


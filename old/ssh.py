from pexpect import pxssh
import datetime

now = datetime.datetime.now()

user1 = 'gjensen'
user2 = 'gil'
passwd = "Nerthus22"

print 'Kerpen-------------------------------------------------------------'

s = pxssh.pxssh()
if not s.login ('10.216.84.205', user1, passwd):
    print("SSH session failed on login.")
    print("fatal error")
else:
    print("SSH session login Kerpen Squid successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         
    print(s.before)     
    
    s.logout()

print 'Karlsruhe-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('jazz.karlsruhe.visteon.com', user2, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("login error")
else:
    print("SSH session login Karlsruhe successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()
    string = s.before
    substring = "Active"
    if substring in string:
       print ("Status: squid is running")
    else:
       print(string)
    s.logout()
    

print 'Chelmsford-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('10.216.32.218', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Chelmsford successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    

print 'China-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('136.17.76.73', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login China successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.sendline (passwd)
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Chennai 1-------------------------------------------------------------'

s=""
s = pxssh.pxssh()
if not s.login ('10.218.200.204', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Chennai 1 successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Chennai 2-------------------------------------------------------------'

s=""
s = pxssh.pxssh()
if not s.login ('10.218.200.226', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Chennai 2 successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    #print(s.before)     # print everything before the prompt.
    string = s.before
    substring = "Active"
    if substring in string:
       print ("Status: squid is running")
    else:
       print(string)
    s.logout()
    string = ""
    
print 'GLCC-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('136.17.184.49', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login GLCC successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Pune-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('136.18.228.200', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Pune successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()


#print string
string=""
substring=""
s.logout()

print 'Queretaro-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('10.218.148.201', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Queretaro successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Sofia 1-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('10.185.4.131', user2, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Sofia 1 successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Sofia 2-------------------------------------------------------------'


s=""
s = pxssh.pxssh()

if not s.login ('10.185.4.134', user2, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Sofia 2 successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'Yokohama-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('10.218.230.211', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Yokohama successful")
    
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
    
print 'End-------------------------------------------------------------'

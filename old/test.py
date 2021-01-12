print 'Kerpen Start-------------------------------------------------------------'
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
print 'Kerpen End-------------------------------------------------------------'

print 'Karlsruhe Start-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('jazz.karlsruhe.visteon.com', user2, passwd):
    print("SSH session failed on login.")
    print("login error")
else:
    print("SSH session login Karlsruhe successful")
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()
    string = s.before
    #print(string)

    substring = "active (running)"
    if substring in string:
       print ("Status: squid is running")
    else:
       print(string)
    s.logout()
print 'Karlsruhe Start-------------------------------------------------------------'
print 'Queretaro Start-------------------------------------------------------------'

s=""
s = pxssh.pxssh()

if not s.login ('10.218.148.201', user1, passwd):
    print("SSH session failed on login.")
    
    #print str(s)
    print("fatal error")
else:
    print("SSH session login Queretaro successful")
    print 'Queretaro-------------------------------------------------------------'
    s.sendline ('sudo /etc/init.d/squid status')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    print("  ")
    s.sendline ('df -h')
    s.prompt()

    string = s.before
    #print(string)

#Alert if disk space is low
    substring = "90%"
    if substring in string:
       print("********************************")
       print("********************************")
       print ("Low Disk space found")
       print("********************************")
       print("********************************")
    else:
       print(string)
         # match the prompt
    #print(s.before)
    s.logout()
print 'Queretaro End-------------------------------------------------------------'

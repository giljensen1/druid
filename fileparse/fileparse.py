from pexpect import pxssh
import getpass

import ConfigParser
import io

# Load the configuration file
with open("file.csv") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

for section_name in config.sections():
    print 'Section:', section_name
    print '  Options:', config.options(section_name)
    for name, value in config.items(section_name):
       # print 
        try:                                                            
            s = pxssh.pxssh()
           
            s.sendline ('nslookup '+ value)   # run a command
            s.prompt()             # match the prompt
            print (s.before)          # print everything before the prompt.

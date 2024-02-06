import time
import paramiko
from getpass import getpass
ip=input('enter ip\n')
username=input('enter username\n')
password=input('enter password\n')

SESSION=paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy)
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)
access=SESSION.invoke_shell()
access.send(b'term length 0\n')
access.send(b'enable\n')
time.sleep(3)
access.send(password)
time.sleep(3)
access.send('show running config')
output=access.recv(65000)
print(output.decode('ascii'))
SESSION.close()


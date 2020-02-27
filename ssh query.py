import paramiko
import base64
import time

hostnamelist = ['192.168.100.1','192.168.100.2']
username = 'ubuntu'
pass_encoded=(b'dG9vcg==') #password encoded in base64

commands = ['df -Th','ls -la']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for hostname in hostnamelist:
    try:
        ssh.connect(hostname = hostname,
                    username = username,
                    password = base64.b64decode(pass_encoded))

        for command in commands:
            print('-' * 30 + 'running command: ' + command + ' on server: ' + hostname + '-' * 30)
            print("")

            stdin, stdout, stderr = ssh.exec_command(command)

            for line in stdout:
                if line == " ":
                    print('No output from command!')

                else:
                    print(stdout.read().decode())

        time.sleep(1) #delay for next command

    except:
        print('Can\'t connect to server! '
              '\nCheck your credentials or IP address.')
        ssh.close()
ssh.close()

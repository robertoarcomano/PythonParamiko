#!/usr/bin/python
import paramiko


class Connection:
    def __init__(self, hostname, username, key_path):
        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=hostname,
                                username=username,
                                pkey=paramiko.rsakey.RSAKey.from_private_key_file(key_path))

        except Exception as e:
            print(e)

    def exec(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode('ascii'), stderr.read().decode('ascii')

    def __del__(self):
        self.client.close()


connection = Connection("localhost", "berto", "/home/berto/.ssh/id_rsa")
result, error = connection.exec("uname -a")
print(result)

import paramiko
from scp import SCPClient


class SSHConnection:
    def __init__(self, hostname, username, key_path):
        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=hostname,
                                username=username,
                                pkey=paramiko.rsakey.RSAKey.from_private_key_file(key_path))
            self.scp = SCPClient(self.client.get_transport())

        except Exception as e:
            print(e)

    def exec(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout, stderr

    def get(self, file):
        return self.scp.get(file)

    def put(self, src, dst):
        return self.scp.put(src, dst)

    def __del__(self):
        return self.client.close()

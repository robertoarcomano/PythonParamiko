#!/usr/bin/python
import Utilities

connection = Utilities.SSHConnection("localhost", "berto", "/home/berto/.ssh/id_rsa")
result, error = connection.exec("find /etc")
for line in result:
    print(line.rstrip())

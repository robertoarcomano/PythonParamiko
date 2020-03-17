#!/usr/bin/python
import Utilities
import threading
import time
import random


def exec_command(command):
    connection = Utilities.SSHConnection("localhost", "berto", "/home/berto/.ssh/id_rsa")
    result, error = connection.exec(command)
    for line in result:
        print("Command: " + command + " line: " + line.rstrip())
        time.sleep(random.random())


def get(file):
    connection = Utilities.SSHConnection("localhost", "berto", "/home/berto/.ssh/id_rsa")
    connection.get(file)


def put(src, dst):
    connection = Utilities.SSHConnection("localhost", "berto", "/home/berto/.ssh/id_rsa")
    connection.put(src, dst)


put("test.py", "test.py")
get("start_jenkins.sh")
commands = ["find /usr", "find /var"]
threads = list()
for command in commands:
    threads.append(threading.Thread(target=exec_command, args=(command,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

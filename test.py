#!/usr/bin/python
from Utilities import SSHConnection
import threading
import time
import random
import os


class Mytest(SSHConnection):
    def __init__(self):
        super().__init__("localhost", "berto", "/home/berto/.ssh/id_rsa")

    def exec_delayed(self, command):
        result, error = self.exec(command)
        for line in result:
            print("Command: " + command + " line: " + line.rstrip())
            time.sleep(random.random())

    def test_copy(self):
        SRC = "test.py"
        DSTDIR = "/tmp"
        DSTFILE = "test1.py"
        DSTPATH=DSTDIR+"/"+DSTFILE
        self.put(SRC, DSTPATH)
        self.get(DSTPATH)
        os.remove(DSTFILE)

    def test_multithread(self):
        commands = ["find /usr|head -10", "find /var|head -10"]
        threads = list()
        for command in commands:
            threads.append(threading.Thread(target=self.exec_delayed, args=(command,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def test_connection(self, kind):
        start = time.time()
        N = 0
        while True:
            N += 1
            if kind == "single":
                self.exec("ls")
            elif kind == "new":
                Mytest().exec("ls")
            print(N, end='')
            print('\r', end='')
            stop = time.time()
            if stop - start > 5:
                break
        stop = time.time()
        print("Speed using", kind, "connection:", round(N / (stop - start)), "executions / s")


def main():
    test = Mytest()
    test.test_copy()
    test.test_multithread()
    tests = ["single", "new"]
    for test_case in tests:
        test.test_connection(test_case)


if __name__ == "__main__":
    main()

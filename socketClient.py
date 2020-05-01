import socket

sock = socket.socket()
sock.connect(('178.204.82.250', 9090))
message = str(input()).encode()
sock.send(message)
sock.close()


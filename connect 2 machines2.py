import socket
sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50005
sock.connect(('172.16.2.220', port))
msg = sock.recv(1024)
msg
msg_decoded = msg.decode('utf-8')
msg_decoded
print(' Message From Sercer: ' + msg_decoded)
msg_back = input(' Do You Want to Respond To The Server ?')
msg_back_encoded = msg_back.encoded('utf-8')
sock.send(msg_back_encoded)
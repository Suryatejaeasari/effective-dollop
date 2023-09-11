import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print('File opened')
    while True:
        print('Receiving data...')
        data = s.recv(1024)
        print('Data received:', repr(data))
        if not data:
            break
        # Write data to a file
        f.write(data)

    print('Successfully received the file')
    f.close()

s.close()
print('Connection closed')

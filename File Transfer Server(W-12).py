import socket

port = 60000  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()  # Establish a connection with the client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'mytext.txt'
    with open(filename, 'rb') as f:
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Sent', repr(l))
            l = f.read(1024)
        f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()

import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
timeout = 5  # Set a timeout of 5 seconds

# Create a UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Set a timeout for socket operations
UDPClientSocket.settimeout(timeout)

serverAddressPort = (localIP, localPort)

# Send a message to the server
msgFromClient = "Hello UDP Server"
bytesToSend = msgFromClient.encode()
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

try:
    # Wait for a response from the server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    serverResponse = msgFromServer[0].decode()
    serverAddress = msgFromServer[1]

    print("Server Response: {}".format(serverResponse))
except socket.timeout:
    print("Timeout: No response from the server.")

UDPClientSocket.close()

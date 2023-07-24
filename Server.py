import socket

def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b[1:]))

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[:pick]
    for bit in divident[pick:]:
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + bit
        else:
            tmp = xor('0'*pick, tmp) + bit
    return tmp

def decodeData(data, key):
    l_key = len(key)
    appended_data = data.decode() + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return remainder

s = socket.socket()
print("Socket successfully created")

# Define the port on which you want to listen
port = 8080

s.bind(('', port))
print("Socket binded to %s" % port)

# Put the socket into listening mode
s.listen(5)
print("Socket is listening")

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # Get data from client
    data = c.recv(1024)

    if not data:
        break

    key = "1001"
    ans = decodeData(data, key)

    temp = "0" * (len(key) - 1)
    response = "THANK you Data -> {} Received No error FOUND".format(data.decode()) if ans == temp else "Error in data"
    c.sendto(response.encode(), ('127.0.0.1', 8080))

    c.close()

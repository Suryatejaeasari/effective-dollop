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

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

s = socket.socket()

# Define the port on which you want to connect
port = 8080

try:
    s.connect(('127.0.0.1', port))
except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running.")
    exit(1)

input_string = input("Enter data you want to send -> ")
data = ''.join(format(ord(x), 'b') for x in input_string)
print("Entered data in binary format:", data)
key = "1001"

ans = encodeData(data, key)
print("Encoded data to be sent to the server in binary format:", ans)

s.sendto(ans.encode(), ('127.0.0.1', 8080))

response = s.recv(1024).decode()
print("Received feedback from server:", response)

# Close the connection
s.close()

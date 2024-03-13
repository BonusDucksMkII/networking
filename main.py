import socket
import sys

HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # def waitFor():
    #     recieved = False
        
    #     sock.recv(1024)

    # Begin main body here

    userFile = input('Please select the file you want to transfer: ')
    fileBuf = open(userFile, 'r')
    fileSize = sys.getsizeof(fileBuf)

    print((fileSize.to_bytes(fileSize, 'little').rstrip(b'\x00')))
    fileSize = fileSize.to_bytes(fileSize, 'little').rstrip(b'\x00')
    print(int.from_bytes(fileSize, 'little'))

    print("Attempting connection...")
    try:
        # Make connection
        sock.connect((HOST, PORT))

        # Send file size to make sure whole file is sent
        sock.send(bytes(fileSize))
        # waitFor()

        for line in fileBuf:
            print(line)
            sock.send(bytes(line, "utf-8"))
            # print("Sent:     {}".format(line))

    except ConnectionRefusedError:
        print("Connection failed. Is the host program running on the other machine?")

"""
Do file operations and pass data line by line through connection?
"""
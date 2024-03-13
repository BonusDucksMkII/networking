import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()

        fileSize = int.from_bytes(self.data, 'big')
        print("File size is {}".format(fileSize))

        while (fileSize):
            self.data= self.request.recv(1024).strip()
            print(self.data)
    
        # print("Received from {}: ".format(self.client_address[0]))
        # self.request.sendall(self.data.upper())

if __name__ == "__main__":
    # Declare host addr and port num
    HOST, PORT = "localhost", 9999

    # TCPHandler is callback method for server
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()

# Lee Haynes
# Phone: + 44 (0) 785 374 0636
# Email: LeeHaynes2019@yandex.com
# Website: http: // www.devcoder.me.uk/
# Instagram: junior_web_developer_2020
# Devcoder Youtube: https: // www.youtube.com/channel/UCXqnASrfdoRlyt82YR7n7pQ?view_as
# Lee Haynes Youtube: https: // www.youtube.com/channel/UCjqLeiVDygmpCHXyeDzH04g

import socket

host = "localhost"
port = 8080

# IPV 4 = AF_INET and TCP Connection = SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# Setting up a listener
# 1 is the total number of requests acepted | allowed
s.listen(1)

# Setting up the listening message
print("The server is listening on port:", port)

# To accept a client request
# Accepts connection and address from where connections made
con, address = s.accept()
print(f"A connection has been etablished from {address}")

try:
    # File received
    # Varlibele used for file
    fileName = con.recv(1024)

    # File is opened
    # Reading ib bytes
    receivedFile = open(fileName, "rb")

    # Read file
    readFile = receivedFile.read()

    # This ensure that all the contents in the file is saved
    con.send(readFile)

    # Close file
    receivedFile.close()
    # Closing the connection
    con.close()
except:
    con.send("File not present on server".encode())

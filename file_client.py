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
s = socket.socket()

# The connection "MUST" be in a tuple, "OR" an error will be thrown
s.connect((host, port))

# Accessing the file on the server
fileName = "serverCode.txt"

# Sending the file
s.send(fileName.encode())

# Read the file
# Setting the maximum file size in bytes
readFile = s.recv(1024)

# Print and decode the contents of the file
print(readFile.decode())


s.close()

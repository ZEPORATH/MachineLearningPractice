
import socket                   # Import socket module

port = 60003                # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object

host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename=str(raw_input())
    f = open(filename,'rb')
    #l = f.read(10192000)
    conn.send(filename)
    #conn.send(f)
    while True:
       data = f.readline()
       if data:
           conn.send(data)
       else:break
       #print('Sent ',repr(l))
       
    f.close()

    print('Done sending')
    conn.sendall('')
    print "%s sent successfully!!" %filename 
    conn.send('Thank you for connecting')
    conn.close()
s.shutdown()
s.close()
exit()

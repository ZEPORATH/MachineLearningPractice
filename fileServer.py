#import necessary libraries
import threading
import os
import socket
from Tkinter import Tk
from tkFileDialog import askopenfilename
import easygui
'''
def getipaddr(hostname='default'):
"""Given a hostname, perform a standard (forward) lookup and return
a list of IP addresses for that host."""
    if hostname == 'default':
        hostname = socket.gethostname()
    ips = socket.gethostbyname_ex(hostname)[2]
    return [i for i in ips if i.split('.')[0] != '127'][0]
'''
def getfile():
    Tk().withdraw()
    filename = askopenfilename()
    print (filename)
    return filename
def uploadFile(name,sock):
    filename = sock.recv(1024)
    easygui.msgbox(msg = 'User needs: '+filename,title = 'FILENAME')
    file_on_pc = getfile()
    if os.path.isfile(file_on_pc):
        sock.send('EXISTS' + str(os.path.getsize(file_on_pc)))
        userResponse = sock.recv(1024)
        if userResponse[:2]=='OK':
            with open(file_on_pc,'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != '':
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send('ERR')
    if str(sock.recv(1024))=='CLOSSE THE CONNECTION':
        sock.close()
        exit()
    sock.close()

def Main():
    s = socket.socket()
    host = socket.gethostname()
    port = int(easygui.enterbox(msg = 'Enter the Port No:',\
                                title = 'PORT'))
    s.bind((host,port))
    s.listen(5)
    #hostip = getipaddr('default')

    print 'Server Started'
    #Run the server to its lifetime
    easygui.msgbox(msg = ('Server Started at '+ ' \nPORT: '+str(port)), title = 'SERVER INFO')
    while True:
        c, addr = s.accept()
        print 'Client connected ip: <'+str(addr)+'>'
        t = threading.Thread(target = uploadFile,\
                             args=('retrThread',c))
        t.start()
    s.close()


if __name__ == '__main__':
    Main()
    
    

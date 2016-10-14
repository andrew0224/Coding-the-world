#!/usr/bin/env python

import socket,select


def server_select():
    """
    Use the 'select' function of 'select' module to implement
    the server program for async communication
    """
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,
                      socket.SO_REUSEADDR, 1)
    server.bind(('', 10000))
    server.listen(5)
    inputs = [server]
    while True:
        print "Let's poll another time"
        rlist, wlist, elist = select.select(inputs, [], [], 1)

        for r in rlist:
            if r is server:
                clientsock, clientaddr = r.accept();
                inputs.append(clientsock);
            else:
                data = r.recv(1024);
                if not data:
                    inputs.remove(r);
                else:
                    print data, '\n'


def server_poll():
    """
    Use the 'poll' function of 'select' module to implement
    the server program for async communication
    """
    server = socket.socket()
    host = ""
    port = 10000
    server.bind((host,port))
    # fdmap = {server.fileno():server}
    server.listen(5)
    p = select.poll()
    p.register(server.fileno(),
               select.POLLIN|select.POLLERR|select.POLLHUP)
    while True:
        events = p.poll(5000)
        if len(events) != 0:
            if events[0][1] == select.POLLIN:
                sock, addr = server.accept()
                buf = sock.recv(8196)
                if len(buf) != 0:
                    print buf
                    # sock.close()
        print "no data"


if __name__ == "__main__":
    # server_select()
    server_poll()

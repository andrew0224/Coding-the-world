#!/usr/bin/env python
import socket
from time import sleep

def client_select():
    """
    To work with the server program of 'server_select'
    """
    # host = '127.0.0.1';
    host = socket.gethostname()
    port = 10000;
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    s.connect((host,port))
    try:
        while True:
            sleep(3)
            s.send('hello from client')
    finally:
        print "The client is closed"
        s.close()


def client_poll():
    """
    To work with the server program of 'server_poll'
    """
    host = socket.gethostname()
    port = 10000;
    s = 0
    while True:
        sleep(3)
        print "Connect and send another time"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))
            s.send('hello from client')
        finally:
            s.close()

if __name__ == "__main__":
    # client_select()
    client_poll()

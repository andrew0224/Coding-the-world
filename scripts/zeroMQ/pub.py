#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import gevent
# from gevent_zeromq import zmq
import zmq
# from time import sleep
import time
# Global Context
# context = zmq.Context() #它是GreenContext的一个简写,确保greenlet化socket

def server():
    context = zmq.Context()
    server_socket = context.socket(zmq.PUB) #创建一个socket,使用zmq类型模式PUB/SUB(发布/订阅)
    server_socket.bind("tcp://127.0.0.1:5000") #绑定socket
    tmp = 0
    while True:
        time.sleep(3)
        server_socket.send("Hello world")
        tmp += 1
        print "sending is done, ", tmp


# publisher = gevent.spawn(server)
# client    = gevent.spawn(client)
# gevent.joinall([publisher, client])

if __name__ == '__main__':
    server()

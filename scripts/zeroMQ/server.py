#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import gevent
# from gevent_zeromq import zmq
import zmq
from time import sleep
# Global Context
context = zmq.Context() #它是GreenContext的一个简写,确保greenlet化socket

def server():
    server_socket = context.socket(zmq.REQ) #创建一个socket,使用mq类型模式REQ/REP(请求/回复,服务器是请求),还有PUB/SUB(发布/订阅),push/pull等
    server_socket.bind("tcp://127.0.0.1:5000") #绑定socket
    for request in range(1,10):
        print('Switched to Server for ', request)
        sleep(3)
        server_socket.send("Hello")
        print server_socket.recv()  #这里发生上下文切换


# publisher = gevent.spawn(server)
# client    = gevent.spawn(client)
# gevent.joinall([publisher, client])

if __name__ == '__main__':
    server()

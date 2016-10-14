#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import gevent
# from gevent_zeromq import zmq
import zmq
from time import sleep
# Global Context
# context = zmq.Context() #它是GreenContext的一个简写,确保greenlet化socket


def client():
    context = zmq.Context() 
    client_socket = context.socket(zmq.SUB)  #(客户端是subscribe)
    client_socket.connect("tcp://127.0.0.1:5000")  #连接server的socket端口
    client_socket.setsockopt(zmq.SUBSCRIBE, "Hello")
    while True:
        print client_socket.recv()


# publisher = gevent.spawn(server)
# client    = gevent.spawn(client)
# gevent.joinall([publisher, client])
if __name__ == '__main__':
    client()

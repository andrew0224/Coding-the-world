#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import gevent
# from gevent_zeromq import zmq
import zmq
from time import sleep
# Global Context
context = zmq.Context() #它是GreenContext的一个简写,确保greenlet化socket


def client():
    client_socket = context.socket(zmq.REP)  #(客户端是回复)
    client_socket.connect("tcp://127.0.0.1:5000")  #连接server的socket端口
    for request in range(1,10):
        print('Switched to Client for ', request)
        print client_socket.recv()
        # print('Switched to Client for ', request)
        client_socket.send("World")


# publisher = gevent.spawn(server)
# client    = gevent.spawn(client)
# gevent.joinall([publisher, client])
if __name__ == '__main__':
    client()

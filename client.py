import socket
import pickle
from Request import Request
import time
from Messaging import Messaging
from config import  PORT_TO_ID,CONFIG,CLIENTS
import random

class Client:

    def __init__(self,id):
        self.id = id
        self.port = CLIENTS[id]
        self.request = {}
        self.datastore={}
        self.nodes = ["A","B","C","D","E"]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('localhost', self.port))

    def get(self,key):
        get_request = Request("GET",key)
        dynamo_node = self.nodes[random.randint(0,len(self.nodes))]
        self.socket.settimeout(3)
        Messaging.send_message(self,dynamo_node)
        try:
            while True:
                data,addr = self.socket.recvfrom(40960)
                if data:
                    if data == "FAILURE":
                        print(data)
                    self.datastore[key]=data
                    print(data)
                    break
        except Exception:
            self.get(key)

# clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# clientSock.bind(('localhost',4444))
# msg1 = Request("PUT","x",1)
# msg2 = Request("PUT","y",3)
# msg3 = Request("PUT","x",4)
# msg4 = Request("PUT","y",2)
# msg5 = Request("PUT","z",10)
# msg6 = Request("GET","x")
# msg7 = Request("GET","y")
# msg8 = Request("GET","x")
# msg9 = Request("GET","y")
# msg10 = Request("GET","z")
# msg_die = Request("EXIT",None)
# msg_live = Request("REVIVE",None)
# #clientSock.sendto(pickle.dumps(msg2),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg1),('localhost',CONFIG["A"][1]))
# #time.sleep(4)
# #clientSock.sendto(pickle.dumps(msg_die),('localhost',CONFIG["D"][1]))
# # time.sleep(3)
# #clientSock.sendto(pickle.dumps(msg3),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg2),('localhost',CONFIG["C"][1]))
# clientSock.sendto(pickle.dumps(msg6),('localhost',CONFIG["B"][1]))
# #time.sleep(1)
# #clientSock.sendto(pickle.dumps(msg4),('localhost',CONFIG["A"][1]))
# #time.sleep(3)
# #clientSock.sendto(pickle.dumps(msg_live),('localhost',CONFIG["C"][1]))
# #clientSock.sendto(pickle.dumps(msg5),('localhost',CONFIG["A"][1]))
# #time.sleep(1)
# #clientSock.sendto(pickle.dumps(msg7),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg8),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg10),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg6),('localhost',CONFIG["A"][1]))
# #clientSock.sendto(pickle.dumps(msg9),('localhost',CONFIG["A"][1]))

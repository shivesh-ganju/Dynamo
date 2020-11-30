import unittest
from client import Client
import time

#Simple test with 1 client and 1 get put operation
client1 = Client(1)
client2 = Client(2)
client3 = Client(3)

def test_happyGetSetTest():
    status = client1.put_req('x', 1)
    print(status)
    time.sleep(1)
    num=client1.get_req('x')
    print(num==1)

#Test with multiple gets and puts with delays having one client only
def test_multipleGetSetDelay():
    client1.put_req('x',1)
    client1.put_req('y', 2)
    client1.put_req('z', 3)
    time.sleep(1)
    x=client1.get_req('x')
    y=client1.get_req('y')
    z=client1.get_req('z')
    print(x==1)
    print(y == 2)
    print(z == 3)

#Testing with same keys multiple values. According to semantic reconcilation, answer should be the largest key
def test_multipleGetSetDelaySameKey():
    client1.put_req('x',1)
    client1.put_req('x',2)
    client1.put_req('x',3)
    time.sleep(1)
    x=client1.get_req('x')
    y=client1.get_req('x')
    z=client1.get_req('x')
    print(x==3)
    print(y==3)
    print(z==3)




test_happyGetSetTest()
test_multipleGetSetDelay()
test_multipleGetSetDelaySameKey()
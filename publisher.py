import zmq
import random
import sys
import time, json, uuid
import message as MSG

pub = None
def connect(host="*", port=5555):
    global pub
    if pub is None:
        context = zmq.Context()
        pub = context.socket(zmq.PUB)
        pub.bind("tcp://{}:{}".format(host, port))
    return pub

def publish(topic, msg):
    print ("{} {}".format(topic, msg))

    msg_id = str(uuid.uuid4())
    MSG.write_msg(topic, msg_id, msg)

    pub.send_string("{} {}".format(topic, msg_id))

if __name__ == "__main__":
    port = int(input("Enter port: "))
    connect(port=port)
    while True:
        topic = input("Enter topic name: ")
        msg = input("Enter message: ")
        if msg in ('stop', 'exit'):
            break
        publish(topic, msg)

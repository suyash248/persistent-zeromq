import sys
import zmq
import message as MSG
import settings

sub_id = None

def process_raw_msg(topic, msg):
    print("Received on topic {}: {}".format(topic, msg))

def fetch_and_process_msg(topic, msg_id):
    global sub_id
    if not MSG.is_msg_read(topic, msg_id, sub_id):
        msg = MSG.get_msg(topic, msg_id)
        process_raw_msg(topic, msg)
        MSG.mark_msg_as_read(topic, msg_id, sub_id)
    else:
        print("Message has already been read!")

def process_pending_msgs(*topics):
    for topic in topics:
        for topic_msg_key in MSG.get_msgs_for_topic(topic):
            topic_msg_key = topic_msg_key.decode()
            msg_id = MSG.extract_msg_id_from_topic_msg_key(topic_msg_key)
            print("Pending message found on topic {}".format(topic))
            fetch_and_process_msg(topic, msg_id)

def subscribe(port, topic):
    context = zmq.Context()
    # sub = context.sub(zmq.SUB)

    sub = context.socket(zmq.SUB)
    print("Waiting for messages...")
    sub.connect("tcp://localhost:{}".format(port))
    # for topic in topics:
    topic = topic.strip()

    process_pending_msgs(settings.GLOBAL_TOPIC, topic)

    sub.setsockopt(zmq.SUBSCRIBE, topic.encode())
    sub.setsockopt(zmq.SUBSCRIBE, settings.GLOBAL_TOPIC.encode())

    while True:
        topic_msg = sub.recv().decode()
        print("New message: ", topic_msg)
        for_topic = topic_msg[:topic_msg.find(' ')]
        msg_id = topic_msg[topic_msg.find(' ') + 1:]
        fetch_and_process_msg(for_topic, msg_id)

if __name__ == "__main__":
    sub_id = input("Enter subscriber id(alphanumeric): ")
    port = int(input("Enter port: "))
    topic = input("Enter topic name to subscribe to: ")
    subscribe(port, topic)
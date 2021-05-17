import time
import random

import zmq


if __name__ == "__main__":
    host = "127.0.0.1"
    port = "5001"

    # Creates a socket instance
    context = zmq.Context()
    socket = context.socket(zmq.PUB) # publisher

    # Binds the socket to a predefined port on localhost
    #socket.bind("tcp://*:%s" % port)
    socket.bind("tcp://{}:{}".format(host, port))

    # Data is published along with a topic.
    # The subscribers usually sets a filter on these topics
    # for topic of their interests.
    while True:
        # Sends a string message
        print("傳送訊息")
        topic = "測試"
        message= "訊息群發"
        socket.send_string(f"{topic} {message}")
        time.sleep(1)









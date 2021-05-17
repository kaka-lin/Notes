import sys

import zmq


if __name__ == "__main__":
    host = "127.0.0.1"
    port = "5001"

    # Creates a socket instance
    context = zmq.Context()
    socket = context.socket(zmq.SUB) # subscriber

    # Connects to a bound socket
    print(f"Collecting updates from weather server...")
    socket.connect("tcp://{}:{}".format(host, port))

    # The current version of zmq supports filtering of messages
    # based on topics at subscriber side. This is usually set via socketoption.
    # Subscribes to all topics
    topicfilter = "測試"
    socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

    while True:
        # Receives a string format message
        response = socket.recv_string()
        topic, message = response.split()
        print(f"topic: {topic}, message: {message}")


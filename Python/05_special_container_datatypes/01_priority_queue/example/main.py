import os
import sys
import time
import threading
from collections import deque

from common import get_args
from threads import VideoThread, DisplayThread, ProcessingThread


def main(args):
    # Create 6 threads and deque/lock for data flow
    threads = []
    deque_input = deque()
    deque_output = [] # we use our PriorityQueuen object
    lock_input = threading.Lock()
    lock_output = threading.Lock()

    # Video and Display thread
    video_thread = VideoThread(args.video_file, deque_input, lock_input, 'video_thread')
    display_thread = DisplayThread(deque_output, lock_output, 'display_thread')
    threads.append(display_thread)
    threads.append(video_thread)

    # Yolo Thread
    for i in range(args.thread_num):
        threads.append(ProcessingThread(
            deque_input, lock_input,
            deque_output, lock_output,
            f"processing_thread_{i}"))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    args = get_args().parse_args()
    main(args)

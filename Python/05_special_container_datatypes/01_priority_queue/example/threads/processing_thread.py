import time
import threading
import random

import cv2
import numpy as np

from priority_queue import PriorityQueue


class ProcessingThread(threading.Thread):
    def __init__(self, deque_input, lock_input,
                 deque_output, lock_output, thread_name):
        super(ProcessingThread, self).__init__(name=thread_name)

        self.deque_input = deque_input
        self.lock_input = lock_input
        self.deque_output = deque_output
        self.lock_output = lock_output

    def run(self):
        while True:
            self.lock_input.acquire()

            # empy
            if not self.deque_input:
                self.lock_input.release()
                continue
            else:
                # get input frame from input frames queue
                data_from_deque = self.deque_input[0]
                self.deque_input.popleft()
                self.lock_input.release()

            # Init input image to input buffers
            img = data_from_deque['img']
            idx = data_from_deque['idx']
            img = self.process_img(img, idx)

            self.lock_output.acquire()
            img_info = PriorityQueue(idx, img)
            self.deque_output.append(img_info)
            self.deque_output.sort()
            self.lock_output.release()

    def process_img(self, img, idx):
        time.sleep(random.random())
        return img

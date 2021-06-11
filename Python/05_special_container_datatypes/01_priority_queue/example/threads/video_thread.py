import time
import threading

import cv2
import numpy as np


class VideoThread(threading.Thread):
    def __init__(self, filename, deque_input, lock_input, thread_name):
        super(VideoThread, self).__init__(name=thread_name)

        self.filename = filename
        self.deque_input = deque_input
        self.lock_input = lock_input
        self.running = False

        self.cap = cv2.VideoCapture(self.filename)
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        if not self.cap.isOpened():
            print("Unable to open camera")
        else:
            print(f"Open {self.filename}")

    def run(self):
        self.running = True
        self.input_img_idx = 0

        while self.running:
            time.sleep(0.02)
            if len(self.deque_input) < 30:
                ret, frame = self.cap.read()

                if ret:
                    self.lock_input.acquire()
                    self.input_img_idx += 1
                    self.deque_input.append({'idx': self.input_img_idx, 'img': frame})
                    self.lock_input.release()
            else:
                time.sleep(10/1000000)


        self.cap.release()

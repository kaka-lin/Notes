import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--video_file', default="videos/wids-workshop-2020.mp4", type=str)
    parser.add_argument('--thread_num', default=4, type=int)

    return parser

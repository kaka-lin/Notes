import os, glob
from subprocess import Popen, PIPE

from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string('ipynb_file', None, 'Jupyter Notebook file name.')

def convert_ipynb_to_md(ipynb_file):
    if ipynb_file is None:
        ipynb_files = glob.glob('./**/*.ipynb', recursive=True)
        for ipynb_file in ipynb_files:
            p = Popen('jupyter nbconvert --to markdown {}'.format(ipynb_file),
                shell=True)
            p.communicate()
            p.kill()
    else:
        p = Popen('jupyter nbconvert --to markdown {}'.format(ipynb_file),
                shell=True)
        p.communicate()
        p.kill()

def main(argv):
    convert_ipynb_to_md(FLAGS.ipynb_file)

if __name__ == "__main__":
    app.run(main)

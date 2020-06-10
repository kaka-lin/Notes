import os
import re
import glob
import datetime

from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string('file_path', None, 'The path of the Markdown file.')

def get_file_name(file_path):
    if file_path is None:
        files = glob.glob('./**/*.md', recursive=True)
        for file_path in files:
            file_name = file_path.split('/')[-1].split('.')[0]
            
            if file_name == "README":
                continue

            file_name = underline_to_hump(file_name)
            yield file_name, file_path
    else:
        file_name, file_extention = file_path.split("/")[-1].split('.')
        if file_extention != 'md':
            print("Err: This file is not Markdown file")
            return None, None
        
        file_name = underline_to_hump(file_name)
        yield file_name, file_path

def underline_to_hump(underline_str): 
    underline_str = underline_str.replace('-', '_')
    temp = underline_str.split('_')
    hump = ' '.join(string[0].upper() + string[1:] for string in temp) 
    return hump

def add_front_matter_to_md(file_path, text):
    with open(file_path, 'r+') as f:
        content = f.read()
        if content[:3] == "---":
            return
        f.seek(0, 0)
        f.write(text + '\n' + content)
    
def main(argv):
    ''' text:
    ---
    title: "{The name of Markdown}"
    date: {today}
    ---
    '''

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    for name, path in get_file_name(FLAGS.file_path):
        text = '---\ntitle: "{}"\ndate: {}\n---\n'.format(name, date)
        
        add_front_matter_to_md(path, text)

if __name__ == "__main__":
    app.run(main)

    
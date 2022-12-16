import os
from pprint import pprint

from .step import Step
from settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        # 取得資料夾裡所有檔案
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        # 字幕放Key
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions
        
        pprint(data)
        return data
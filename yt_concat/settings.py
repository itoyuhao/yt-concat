from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY') 

# 後來又發現不用了
# VIDEO_LIST_FILE_NAME = 'video_list.txt'
DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')


####
## https://github.com/pytube/pytube/issues/1085
from .step import Step
import utils

from pytube import YouTube
from settings import VIDEOS_DIR


class DownloadVideos(Step):

    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))
        
        for yt in yt_set:
            url = yt.url
            # 人為檢查跳過了哪些影片
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            try:
                print('downloading ', url)
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id +'.mp4')
            except:
                continue
    
        return data
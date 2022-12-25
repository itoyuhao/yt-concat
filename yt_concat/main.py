from pipeline.steps.preflight import Preflight
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.initalize_yt import InitializeYT
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_caption import ReadCaption
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.postflight import Postflight
from pipeline.steps.step import StepException
from pipeline.pipeline import Pipeline
from utils import Utils

CHANNEL_ID = 'UC8wZnXYK_CGKlBcZp-GxYPA'
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
        

    ]

    utils = Utils() 
    p = Pipeline(steps)
    p.run(inputs, utils)


# 檢查是否為程式進入點
if __name__ == '__main__':
    main()

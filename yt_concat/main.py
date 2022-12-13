from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.step import StepException

from pipeline.pipeline import Pipeline

CHANNEL_ID = 'UC8wZnXYK_CGKlBcZp-GxYPA'



def main():

    inputs = {'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    
    p = Pipeline(steps)
    p.run(inputs)


# 檢查是否為程式進入點
if __name__ == '__main__':
    main()
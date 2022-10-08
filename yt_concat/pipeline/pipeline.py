# from yt_concat.pipeline.steps.step import StepException
from .steps.step import StepException

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                # 這邊要建立一個傳遞的動作
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened: ', e)
                break

        # return data
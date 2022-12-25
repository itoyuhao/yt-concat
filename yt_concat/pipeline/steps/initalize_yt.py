from .step import Step
from model.yt import YT

class InitializeYT(Step):
    def process(self, data, inputs, utils):
        # 用list comprehension來return他
        return [YT(url) for url in data]
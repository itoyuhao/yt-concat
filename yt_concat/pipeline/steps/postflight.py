from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')  # 讓每個 function 的最開始都印某個東西 -> decorator

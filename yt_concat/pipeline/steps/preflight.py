from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')  # 讓每個 function 的最開始都印某個東西 -> decorator
        utils.create_dirs()
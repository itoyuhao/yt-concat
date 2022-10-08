from abc import ABC, abstractclassmethod

class Step(ABC):
    
    # 如果把init function也定義成 abstract method 則所有子孫class都要implement他(要把它寫出來)，在此不需要
    def __init__(self):
        pass


    @abstractclassmethod
    def process(self, data, inputs):
        pass

class StepException(Exception):
    '''
    這邊設定此class的用意是，任何一個步驟有觸發設計的這種StepException，這整個流程就停止
    function裡的Exception是python built-in的，不需要另外import
    '''
    pass

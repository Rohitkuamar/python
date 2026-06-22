# OOPS
class Factory:
    def __init__(self, name):
        self.name = name

    def produce(self):
        print(f"{self.name} is producing something.")
from shlumpy.stage import Stage


class Pipeline:
    def __init__(self, name):
        self.name = name
        self.stages = {}

    def stage(self, func):
        stage = Stage(func)
        self.stages[stage.name] = stage

    def order_stages(self):
        pass

    def run(self):
        for stage in self.stages:
            print("Running stage: {stage_name}".format(stage_name=stage))
            self.stages[stage]()
            print()

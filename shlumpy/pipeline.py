from shlumpy.stage import Stage


class Pipeline:
    def __init__(self, name):
        self.name = name
        self.stages = []
        self.stages_graph = {}

    def stage(self, func):
        stage = Stage(func)
        self.stages.append(stage)

    def order_stages(self):
        pass

    def run(self):
        for stage in self.stages:
            print("Running stage: {stage_name}".format(stage_name=stage.name))
            stage()
            print()

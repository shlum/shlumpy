from shlumpy.pipeline import Pipeline


class PipelineBuilder:
    def __init__(self):
        self.stages = set()
        self.stages_tree = {}
        self.first_stage = None
        self.pipeline = None

    def set_first_stage(self, stage):
        self.stages.add(stage)
        self.first_stage = stage
        self.stages_tree[stage] = []

    def add_stage_after(self, stage_to_run, stage_to_run_after):
        self.stages_tree[stage_to_run_after].append(stage_to_run)
        if stage_to_run not in self.stages_tree:
            self.stages_tree[stage_to_run] = []

    def get_pipeline(self, name):
        return Pipeline(name, self.stages_tree, self.first_stage)


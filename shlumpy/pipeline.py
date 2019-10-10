class Pipeline:
    def __init__(self, name, stages_tree, first_stage):
        self.name = name
        self.stages = set(stages_tree.keys())
        self.stages_tree = stages_tree
        self.first_stage = first_stage

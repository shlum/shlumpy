class Context:
    def __init__(self):
        self.pipeline_params = {}
        self.params = {}

    # def __getattr__(self, item):
    #     return self.pipeline_params[get_current_pipeline()][item]
    #
    # def __setattr__(self, key, value):
    #     self.pipeline_params[get_current_pipeline()][key] = value


CONTEXT = Context()
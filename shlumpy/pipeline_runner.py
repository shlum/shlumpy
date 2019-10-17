from shlumpy.pipeline import Pipeline

class PipelineRunner(Pipeline):
    def __init__(self):
        self.pipelines = {}

    def add_pipeline(self, pipeline):
        self.pipelines[pipeline.name] = pipeline

    def run_server(self):
        pass

    def run_flow_by_name(self, flow_name):
        self.pipelines[flow_name].run()

    def close(self):
        pass

import logging


class PipelineRunner:
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

    def set_up_logger(self):
        root_logger = logging.getLogger()
        root_logger.addHandler(logging.StreamHandler())
        root_logger.setLevel(logging.INFO)

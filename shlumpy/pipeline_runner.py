import logging

from shlumpy.web_app import app

from flask import Flask


class PipelineRunner:
    def __init__(self):
        self.pipelines = {}

    def add_pipeline(self, pipeline):
        self.pipelines[pipeline.name] = pipeline

    def run_server(self):
        self.set_up_logger()
        self.start_flask_server()

    def run_pipeline_by_name(self, flow_name):
        self.pipelines[flow_name].run()

    def close(self):
        pass

    def set_up_logger(self):
        root_logger = logging.getLogger()
        root_logger.addHandler(logging.StreamHandler())
        root_logger.setLevel(logging.INFO)

    def start_flask_server(self):
        app = Flask(__name__)
        app.add_url_rule('/', 'home', 'self.homr')
        app.run()

    def home(self):
        return "hellp"


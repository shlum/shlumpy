from examples.my_pipeline2 import get_pipeline2
from examples.my_pipelne import get_pipeline
from shlumpy.pipeline_runner import PipelineRunner


def main():
    runner = PipelineRunner()
    runner.add_pipeline(get_pipeline())
    runner.add_pipeline(get_pipeline2())
    runner.run_server()


if __name__ == '__main__':
    main()
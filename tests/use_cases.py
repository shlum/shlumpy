from time import sleep

from shlumpy.pipeline_builder import PipelineBuilder
from shlumpy.pipeline_runner import PipelineRunner
from shlumpy.stage import shlumpy_stage


@shlumpy_stage
def my_stage():
    print("Starting")
    sleep(2)
    print("End")


@shlumpy_stage
def my_stage2():
    print("Starting2")
    sleep(2)
    print("End2")




def main():
    builder = PipelineBuilder()
    builder.set_first_stage(my_stage)
    builder.add_stage_after(my_stage2, my_stage)

    pipeline = builder.get_pipeline("Bla")

    runner = PipelineRunner()
    runner.set_up_logger()
    runner.add_pipeline(pipeline)
    runner.run_flow_by_name("Bla")

if __name__ == '__main__':
    main()

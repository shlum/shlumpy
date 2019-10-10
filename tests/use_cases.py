from time import sleep

from shlumpy.pipeline_builder import PipelineBuilder
from shlumpy.shlumpy_runner import ShlumpyRunner
from shlumpy.stage import shlumpy_stage


@shlumpy_stage
def my_stage():
    print("Starting")
    sleep(10)
    print("End")


@shlumpy_stage
def my_stage2():
    print("Starting2")
    sleep(10)
    print("End2")




def main():
    runner = ShlumpyRunner([])

    builder = PipelineBuilder()
    builder.set_first_stage(my_stage)
    builder.add_stage_after(my_stage2, my_stage)



    flow = builder.get_pipeline("Bla")

    runner.add_pipeline(flow)
    runner.run_flow_by_name("Bla")

def main2():
    runner = ShlumpyRunner([])

    with PipelineBuilder() as builder:
        stage1 > stage2 > stage3
        stage2 > stage6
        stage2 + stage6 > stage7
        flow = builder.get_pipeline("DeployToServer")

    runner.add_pipeline(flow)
if __name__ == '__main__':
    main()
from shlumpy.pipeline import Pipeline
from shlumpy.stage import shlumpy_stage


@shlumpy_stage
def my_stage():
    pass



def get_pipeline2():
    pipeline = Pipeline("ss")
    pipeline.stages["ds"] = my_stage
    return pipeline


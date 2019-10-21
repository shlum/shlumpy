from shlumpy.pipeline import Pipeline
from shlumpy.stage import shlumpy_stage
from examples.context import CONTEXT



@shlumpy_stage
def my_stage():
    CONTEXT.y = 1
    CONTEXT.url = 'dsadsadsad'


@shlumpy_stage
def my_stage2():
    url = CONTEXT.url
    return {'b': 1}




def get_pipeline():
    pipeline = Pipeline("ss")
    pipeline.stages["ds"] = my_stage
    #pipeline.order_stages(stage1 > stage2 > stage3)
    return pipeline


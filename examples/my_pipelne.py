from shlumpy.pipeline import Pipeline
from shlumpy.stage import shlumpy_stage
from examples.context import CONTEXT



@shlumpy_stage(context_params=[x])
def my_stage(x):
    CONTEXT.y = 1
    CONTNEXT.url = 'dsadsadsad'


@shlumpy_stage
def my_stage2(a=1):
    url = CONTEXT.url
    return {'b': 1}


@shlumpy_stage
def my_stage2(a=1):
    return Context


@shlumpy_stage
def my_stage2():
    return MyParmas




def get_pipeline():
    pipeline = Pipeline("ss")
    pipeline.stages["ds"] = my_stage
    pipeline.order_stages(stage1 > stage2 > stage3)
    return pipeline


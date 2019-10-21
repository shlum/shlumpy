# shlumpy

Pipeline

Stage


passing parameters between stages

stages inside a pipeline share a context.
this context contains all the parameters of all the stages in the current run.
by using this context stages can communicate parameters to each other

the context can be initialized with values when running the pipeline, by default it will be 
start empty.

example
```python
from shlumpy.context import CONTEXT

def stage():
    CONTEXT.x = 1 
    
    
```
        
        

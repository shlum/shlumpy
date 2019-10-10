class Stage:
    def __init__(self, inner_func):
        self.inner_func = inner_func

    def __call__(self, *args, **kwargs):
        self.inner_func(*args, **kwargs)


def shlumpy_stage(func):
    return Stage(func)

class Stage:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

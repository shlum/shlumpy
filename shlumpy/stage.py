import logging


class Stage:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

    def run(self):
        logging.getLogger(__name__).info("Starting stage {}".format(self.name))
        try:
            return self.function()
        finally:
            logging.getLogger(__name__).info("Finished stage {}".format(self.name))


def shlumpy_stage(func):
    return Stage(func)

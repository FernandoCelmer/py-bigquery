class Table:

    def __init__(self, **kwargs) -> None:
        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self.setup()

    def setup(self):
        pass

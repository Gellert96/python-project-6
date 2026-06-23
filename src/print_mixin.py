class PrintMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__()
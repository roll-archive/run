from ..settings import settings


class Logger:

    # Public

    def __init__(self):
        self.__compact = settings.compact
        self.__plain = settings.plain
        self.__stack = []

    def __call__(self, event):
        pass

    def __repr__(self):
        return '<Logger>'
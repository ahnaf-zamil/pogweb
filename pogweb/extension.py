from pogweb.application import BaseApp

import typing

__all__: typing.Final = ["Extension"]


class Extension(BaseApp):
    def __init__(self) -> None:
        super().__init__()

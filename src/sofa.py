from deta import Deta
from typing import Union

class SofaStorage:
    def __init__(self, drive: Deta.Drive):
        self.drive = drive

    def __repr__(self):
        return f"<SofaStorage>"

    def __log(self, prompt: str) -> None:
        print(prompt)

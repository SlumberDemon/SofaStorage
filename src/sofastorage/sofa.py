from .key import KEY
from deta import Deta
from typing import Union

class SofaStorage:
    def __init__(self, base: Deta.Base, silent: bool = False):
        self.base = base
        self.silent = silent

    def __repr__(self):
        return f"<SofaStorage>"

    def __log__(self, prompt: str) -> None:
        if not self.silent:
            print(prompt)

    

    @classmethod
    def create(cls, username: str, password: str, silent: bool = False):
        base = Deta(KEY).Base(f'{username}-{password}')
        storage = base.put({'item':'.sofa'}, key='.sofa')
        sofa = base.get(key='.sofa')
        if sofa:
            print(f'Account ({username}) created')
        if not silent:
            print(f'Account ({username}) created')
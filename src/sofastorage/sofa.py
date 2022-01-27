from .key import KEY
from deta import Deta
from typing import Union

class SofaStorage:
    def __init__(self, base: Deta.Base, silent: bool = False):
        self.base = base
        self.silent = silent

    def __repr__(self):
        return f"<SofaStorage>"

    def __log(self, prompt: str) -> None:
        if not self.silent:
            print(prompt)

    @classmethod
    def create(cls, username: str, password: str, base: str = None, silent: bool = False):
        key = base if base else KEY
        if len(username) < 5:
            raise ValueError("Use at least 5 characters!")
        if password == KEY:
            raise ValueError("Don't use project key as password!")
        if len(password) < 8:
            raise ValueError("Use at least 8 characters!")
        if username == password:
            raise ValueError("Username and password can't be the same!")
        try:
            base = Deta(key).Base(f'{username}_{password}')
            if not silent:
                print(f"Account ({username}) created!")
                return cls(base=base, silent=silent)
        except AssertionError:
            raise ValueError("Used an invalid login token!")

    @classmethod
    def login(cls, username: str, password: str, base: str = None, silent: bool = False):
        key = base if base else KEY
        try:
            base = Deta(key).Base(f'{username}_{password}')
            if not silent:
                print(f"Logged in as ({username})")
                print('-------')
                return cls(base=base, silent=silent)
            else:
                raise Exception(f"Account ({username}) doesn't exist!")
        except AssertionError:
            raise ValueError("Used an invalid login token!")

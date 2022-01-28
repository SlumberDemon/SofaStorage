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
    def create(cls, username: str, password: str, private: str = None, silent: bool = False):
        key = private if private else KEY
        if len(username) < 5:
            raise ValueError("Use at least 5 characters!")
        if password == KEY:
            raise ValueError("Don't use project key as password!")
        if len(password) < 8:
            raise ValueError("Use at least 8 characters!")
        if username == password:
            raise ValueError("Username and password can't be the same!")
        try:
            base = Deta(key).Base(f'{username}-{password}')
            sofa = base.get(key='.sofa')
            if sofa:
                return cls.login(username, password, private, silent)
            if not silent:
                print(f'Account ({username}) created!')
            storage = base.put({'.sofa':'.sofa'}, key='.sofa')
            return cls(base=base, silent=silent)
        except:
            raise ValueError("Used an invalid login token!")


    @classmethod
    def login(cls, username: str, password: str, private: str = None, silent: bool = False):
        key = private if private else KEY
        try:
            base = Deta(key).Base(f'{username}-{password}')
            sofa = base.get(key='.sofa')
            if sofa:
                if not silent:
                    print(f"Logged in as ({username})")
                    print('-------')
                return cls(base=base, silent=silent)
            else:
                raise Exception(f"Account ({username}) doesn't exist!")
        except AssertionError:
            raise ValueError("Used an invalid login token!")

    def passwords(self, sofa = '.sofa'):
        fetch = self.base.fetch({'.sofa': sofa})
        for item in fetch.items:
            print(f'[↓] ' + item['username'] + ' | ' + item['password'] + ' | ' + item['website'] + ' | ')            
        return print(f'[•] Found {fetch.count} result(s)')         

    def find(self, website: str = None, username: str = None):
        try:
            if username:
                fetch = self.base.fetch({'username', username})
            if website:
                fetch = self.base.fetch({'website': website})
            for item in fetch.items:
                print(f'[↓] ' + item['username'] + ' | ' + item['password'] + ' | ' + item['website'] + ' | ')            
            return print(f'[•] Found {fetch.count} result(s)')
        except:
            raise Exception('Missing website or username search query!')

    def add(self, username: str, password: str, website: str): 
        '''
        Username can also be the email
        '''
        self.__log__(f'[↑] Saving | {website} | ...')
        self.base.insert({'username': username, 'password': password, 'website': website, '.sofa': '.sofa'})
        self.__log__(f'[•] Completed | {website} |')
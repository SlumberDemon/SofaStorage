from .key import KEY
from deta import Deta
from typing import Union

class SofaStorage:
    def __init__(self, base: Deta.Base, silent: bool = False):
        self.base = base
        self.silent = silent

    def __repr__(self):
        return f"<SofaStorage>"

    def sofa_put(username, password, item: Union[list, dict], deta: Deta, key: str):
        print(f'[↑] Uploading | {item} | ...')
        sofa = deta.Base(f'{username}-{password}')
        sofa.put({'item': item}, key)
        print(f'[•] Completed | {item} |')

    def sofa_get(username, password, deta: Deta, key: str):
        print(f'[↓] Fetching | {key} | ...')        
        sofa = deta.Base(f'{username}-{password}')
        sofa.get(key)
        print(f'[•] Completed | {key} |')

    @classmethod
    def test(cls):

        username = 'username'
        password = 'password'
        private = KEY
        silent = ' '

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
            base = SofaStorage.sofa_put(username, password, item=['.sofa'], deta=private, key='.sofa')
            sofa = SofaStorage.sofa_get(username, password, private, key='.sofa')
            if sofa:
                return cls.login(username, password, base)
            if not silent:
                print(f"Account ({username}) created!")
                return cls(base=base, silent=silent)
        except AssertionError:
            raise ValueError("Used an invalid login token!")

        ''''
        key = KEY

        print('[↓] Testing')

        try:
            print(f'[↳] {KEY}')
        except:
            print('[⨯] Key not working')
        try:
            base = Deta(key).Base(f'username_password')
            sofa = base.put({'item': ' '}, key='.sofa')            
            print('[↳] Account created')
        except:
            print('[⨯] Account creation failed')
            
        print('[✔] Test complete')
        '''

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
            storage = base.put({'item': '.sofa'}, key='.sofa')
            sofa = base.get(key='.sofa')
            if sofa:
                return cls.login(username, password, base)
            if not silent:
                print(f"Account ({username}) created!")
                return cls(base=base, silent=silent)
        except AssertionError:
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

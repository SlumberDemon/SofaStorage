from .key import KEY
from deta import Deta

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
    def test(cls):

        username = 'username'
        password = 'password'
        private = ' '
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
            base = Deta(key).Base(f'{username}_{password}')
            sofa = base.put({'item': '.sofa'}, key='.sofa')
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
            base = Deta(key).Base(f'{username}_{password}')
            sofa = base.put({'item': '.sofa'}, key='.sofa')
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
            base = Deta(key).Base(f'{username}_{password}')
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

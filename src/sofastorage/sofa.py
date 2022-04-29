import time
from .key import KEY
from deta import Deta
from tabulate import tabulate

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
            storage = base.put({'sofastorage':'.sofa'}, key='.sofa')
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

    def raw(self):
        """
        Similar to all() but it returns a Dict for every saved website instead
        """
        timer_start = time.perf_counter()
        fetch = self.base.fetch({'sofastorage': '.website'})
        for item in fetch.items:
            print(item)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'   
        return print(f'[•] Found {fetch.count} result(s) | {elapsed}s') 

    def all(self):
        """
        Returns all saved websites
        """
        timer_start = time.perf_counter()
        fetch = self.base.fetch({'sofastorage': '.website'})
        data = []
        for item in fetch.items:
            # data.append(f"['{item['key']}', '{item['username']}', '{item['password']}', '{item['website']}']")
            store = []
            store.append(item['key'])
            store.append(item['username'])
            store.append(item['password'])
            store.append(item['website'])
            data.append(store)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        print(tabulate(data, headers=["Key", "Username", "Password", "Website"], tablefmt="pretty"))   
        return print(f'[•] Found {fetch.count} result(s) | {elapsed}s')         

    def find(self, query: str):
        '''
        Search for passwords
        :param query: This can be the website url/name or the websites username
        :return: SofaStorage object
        '''
        try:
            if query:
                try:
                    fetch = self.base.fetch({'username', query})
                except:
                    fetch = self.base.fetch({'website': query})
            timer_start = time.perf_counter()
            for item in fetch.items:
                print(item)
                print(f'[↓] ' + item['username'] + ' | ' + item['password'] + ' | ' + item['website'] + ' | ')   
            timer_end = time.perf_counter()
            elapsed = f'{timer_end - timer_start:0.4f}'       
            return print(f'[•] Found {fetch.count} result(s) | {elapsed}s')
        except:
            raise Exception('Missing website or username search query!')

    def add(self, username: str, password: str, website: str): 
        '''
        Add a website
        :param username: This can also be an email
        :param password: The password
        :param website: Website url 
        :return: SofaStorage object
        '''
        address = website.replace('https://', '').replace('http://', '')

        self.__log__(f'[↑] Saving | {website} | ...')
        timer_start = time.perf_counter()
        self.base.insert({'username': username, 'password': password, 'website': address, 'sofastorage': '.website'})
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f'[•] Completed | {website} | {elapsed}s')
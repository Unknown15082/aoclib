import requests
from load_config import getSessionID

class AOC:
    def __init__(self, session: str = '') -> None:
        if not session:
            self.sessionID = getSessionID()
        else:
            self.sessionID = session

        self.session = requests.Session()
        self.session.headers.update({'session': self.sessionID})

    def getdata(self, year: int, date: int) -> str:
        

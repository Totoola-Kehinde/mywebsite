from website import app, client



class User():

    def __init__(self):
        self.client = client
        self.database = self.client['users']
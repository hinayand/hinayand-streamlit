import json
from hashlib import sha256


class UserManager(object):
    def __init__(self, path):
        self.path = path
        self.users = {}

    def add_user(self, user, password):
        self.users[user] = sha256(password.encode('utf-8')).hexdigest()

    def del_user(self, user):
        del self.users[user]

    def check_user(self, user, password):
        return user in self.users and self.users[user] == sha256(password.encode('utf-8')).hexdigest()

    def edit_user(self, user, password):
        self.users[user] = sha256(password.encode('utf-8')).hexdigest()

    def show_all_users(self):
        for user in self.users:
            print(user)

    def del_users(self, userList):
        for user in userList:
            del self.users[user]

    def save_users(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.users, f)

    def load_users(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.users = json.load(f)

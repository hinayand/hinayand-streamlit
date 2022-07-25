import json

permissionsList = {
    'op': 'ALL_PERMISSIONS',
    'user': 'USER_PERMISSIONS',
}


class PermissionsTools(object):
    def __init__(self, path):
        self.path = path
        self.groups = {}

    def add_group(self, group, userList):
        self.groups[group] = {
            'users': userList,
            'permissions': []
        }

    def add_group_permission(self, group, permission):
        self.groups[group]['permissions'].append(permissionsList[permission])

    def add_group_user(self, group, user):
        self.groups[group]['users'].append(user)

    def del_group(self, group):
        del self.groups[group]

    def del_groups(self, groupList):
        for group in groupList:
            del self.groups[group]

    def check_group(self, group):
        return group in self.groups

    def check_group_user(self, group, user):
        return user in self.groups[group]['users']

    def check_group_preemission(self, group, permission):
        return permission in self.groups[group][permissionsList[permission]]

    def get_all_groups_info(self):
        return str(self.groups)

    def save_groups(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.groups, f)

    def load_groups(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.groups = json.load(f)

class User:
    def __init__(self, group: str):
        self.group = group


def admin_method(usr):
    print(f'exec {usr.group} method')


def manager_method(usr):
    print(f'exec {usr.group} method')


def client_method(usr):
    print(f'exec {usr.group} method')


def anon_method(usr):
    print(f'exec {usr.group} method')


user = User('admin')

group_methods = {
    'admin': admin_method,
    'manager': manager_method,
    'client': client_method,
    'anon': anon_method,
}

group_methods[user.group](user)

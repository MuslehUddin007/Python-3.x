def decorate_message(fun):
    def addWelcome(site_name):
        return 'Welcome to ' + fun(site_name)

    return addWelcome

@decorate_message
def site(site_name):
    return site_name

print(site("GeeksforGeeks"))

# attach data
def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x,y):
    return x+y

print(add(2,3))
print(add.data)

# example
def message(fun):
    def add(site_name):
        return 'Welcome to ' + fun(site_name)

    return add

@message
def site(site_name):
    return site_name

print(site('GeeksForGeeks'))
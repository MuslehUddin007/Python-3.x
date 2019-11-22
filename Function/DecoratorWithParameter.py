def decorator(*args,**kwargs):
    print('Inside decorator')
    def inner(func):
        print('Inside inner function')
        print('I like',kwargs['like'])
        return func
    return inner

@decorator(like = 'GeeksForGeeks')
def func():
    print('Inside actual function')
func()
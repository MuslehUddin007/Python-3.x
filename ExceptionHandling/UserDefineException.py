class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(repr(self.value))

try:
    raise(MyError(3*2))
except MyError as error:
    print("A new Exception occured: ",error.value)

class Error(Exception):
    pass
class TransitionError(Error):
    def __init__(self,prev,next,msg):
        self.prev = prev
        self.next = next
        self.msg = msg
try:
    raise(TransitionError(2,3*2,"Not Allowed"))
except TransitionError as error:
    print("Exception occured : ",error.msg)
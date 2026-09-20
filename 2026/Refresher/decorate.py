class BaseService:
    def __init__(self):
        self.active = True
        
class CloudService(BaseService):
    def sync(self):
        pass
        
def func():
    print("Hello")

def decorator(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper

def log_call(func):
    def wrapper(*args):
        print(f"Callilng {func.__name__}")
        return func(*args)
    return wrapper

@log_call
def get_data():
    return "Success"

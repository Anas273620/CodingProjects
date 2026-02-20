# def hello(func):
#     func()
    
# def greet():
#     print('still here!')
    
# a = hello(greet)

# print(a)



# Higher Order Function HOC
# def greet(func):
#     func()
    
# def greet2():
#     def func():
#         return 5
#     return func()


#Decorator

# def my_decorator(func):
#     def wrap_func(x):
#         print('*********')
#         func(x)
#         print('*********')
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)

# @my_decorator    
# def bye():
#     print('see ya later')
    
# hello('hiiiii')
# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(100000000):
#         i*5
        
# long_time()




user1 = {
    "name": "Sorna",
    "valid": True,
}


def authenticated(fn):
    def wrapper(*args, **kawrgs):
        if args[0]['valid']:
            return fn(*args, **kawrgs)
        else:
            return print('Invalid user') 
    
    return wrapper
        


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)


def gen_fun(num):
    for i in range(num):
        yield i
        



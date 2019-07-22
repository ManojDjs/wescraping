def smart_fun(fun):
    def wrapper(*args,**kwargs):
        print(*args)
        print(**kwargs)
        result:int=fun(*args,**kwargs)
        print(result)
        print('outside wrap func')
        return result
    return wrapper
@smart_fun
def printsum(a,b):
    return a + b
printsum(2,3)
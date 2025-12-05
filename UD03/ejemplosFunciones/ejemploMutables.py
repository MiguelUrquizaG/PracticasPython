#Se añaden mas valores de manera infinita
def buggy(arg,result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def works (arg):
    result = []
    result.append(arg)
    return result

works('a')
works('b')

def nonbuggy(arg,result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
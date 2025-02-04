


def Decor(func):
    def wrapper(a,b,c):
        count=0
        res=func(a,b,c)
        for i in range(res):
            if res%(i+1)==0:
                count+=1
        if count==2:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper

@Decor
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)
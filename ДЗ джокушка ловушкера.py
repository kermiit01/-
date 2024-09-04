import random
n=random.randint(3,20)
print(n)
result=[]
for i in range(n):
    for a in range(n):
        if i<a:
            if i+a==n:
                result.append(i)
                result.append(a)
result_final=''.join(map(str,result))
print(result_final)

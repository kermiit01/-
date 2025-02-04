def apply_all_func(int_list, *functions):
    results={}
    for i in functions:
        results.update({i.__name__:i(int_list)})
    return results

def min(list):
    min_res=9999999

    for i in list:
        if i < min_res:
            min_res = i
    return min_res

def max(list):
    max_res = 0
    for i in list:
        if i > max_res:
            max_res = i
    return max_res

def lenght(list):
    return len(list)

def sum(list):
    res=0
    for i in list:
        res+=i
    return res

def sorted(list):
    res =[]
    print(list)
    while list != []:
        res.append(min(list))
        list.remove(min(list))
    return res

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], lenght, sum, sorted))
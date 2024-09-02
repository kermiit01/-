def count_calls():
    global count
    count=count+1
def string_info():
    string=input('Введите строку: ')
    string_usage=[]
    string_usage.append(len(string))
    string_usage.append(string.upper())
    string_usage.append(string.lower())
    print(string_usage)
    count_calls()
def is_contains(string,list_to_search):
    check=False
    for i in string:
        if list_to_search.upper()==i.upper():
            check=True
    print(check)
    count_calls()
count=0
string_info()
string_info()
is_contains(('ПитОн','пит','ТОН'),('Питон'))
print(count)
def get_multiplied_digits(numbers):
    global n
    str_numbers=str(numbers)
    if numbers==0:
        print(n)
        return
    else:
        n=n*int(str_numbers[0])
        numbers=numbers-pow(10,len(str_numbers)-1)*int(str_numbers[0])
        get_multiplied_digits(numbers)
n=1
get_multiplied_digits(5112)
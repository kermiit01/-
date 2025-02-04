import itertools
def all_variants(text):
    for i in range(len(text)):
        i+=1
        for j in range(len(text)-i+1):
            value = text[j:j+i]
            yield value




a = all_variants("abc")
for i in a:
    print(i)
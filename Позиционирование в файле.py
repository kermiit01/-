

def custom_write(file_name,strings):
    file = open(file_name,'r',encoding='utf-8')
    text = file.read()
    file.seek(0)
    glos={}
    count=1
    len1=0
    for i in text.split('\n'):
        glos.update({(count,file.tell()):i})
        count+=1
        len1+=len(i)
        file.seek(len1)
    print(glos)

custom_write('sample.txt',4)
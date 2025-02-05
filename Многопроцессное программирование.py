import multiprocessing
import time


def read_info(name):
    all_data=[]
    with open(str(name),'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.strip())

filenames = [f'file {number}.txt' for number in range(1, 5)]

if __name__ ==  '__main__':
    start = time.time()
    for i in filenames:
        read_info(i)
    end = time.time()
    print(f'{end - start}')
    with multiprocessing.Pool(processes=4) as pool:
        start = time.time()
        pool.map(read_info,filenames)
        end = time.time()
        print(f'{end-start}')

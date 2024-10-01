import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open (name,'r',encoding='utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])

filename = [f'./file {number}.txt' for number in range (1,5)]

'''start = datetime.now()
for i in range (4):
   read_info(filename[i])
end = datetime.now()
print(f'{end-start} (линейный)' )'''


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
         pool.map(read_info, filename)
    end = datetime.now()
    print(f'{end - start} (многопроцессный)')
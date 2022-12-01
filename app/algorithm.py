import time
def prime_algo_1(min,max):
    min,max=int(min),int(max)
    start = time.time()
    primeList,flag = [],0
    if min==0:
        min=1
    print(type(max))
    for i in range(min, max + 1):
        # Skip 1 as1 is neither
        if (i == 1):
            continue
        # if i is prime or not
        flag = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break    
        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            primeList.append(i)
    end = time.time()
    total_time = round(((end-start) * 10**3),4)
    return primeList,total_time

def prime_optimised(min,max):
    start = time.time()
    primeList = []
    # handling the cases where min is is lesss than 2
    if min==0:
        min=1
    if (min == 1):
        # primeList.append(min)
        min+=1
        if (max >= 2):
            primeList.append(min)
            min+=1
    if (min == 2):
        primeList.append(min)
     
    if (min % 2 == 0):
        min+=1
    # traversing through only odd number
    for i in range(min,max+1,2):
        # if i is prime or not
        flag = 1
        # largest value of prime number
        j = 2
        while(j * j <= i):
            if (i % j == 0):
                flag = 0
                break
            j+=1
         
        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            primeList.append(i)
    end = time.time()
    total_time = round(((end-start) * 10**3),4)
    return primeList,total_time

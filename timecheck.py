import timeit 
import random 

from task_1 import greedy_change
from task_2 import find_min_coins

if __name__ == "__main__":
    
    data = random.randint(1, 1000_000)


    time1 = timeit.timeit(lambda: greedy_change(data), number = 1)
    time2 = timeit.timeit(lambda: find_min_coins(data), number = 1)

    print(f'Time for greedy_change: {time1}')
    print(f'Time for find_min_coins: {time2}')


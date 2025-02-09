from multiprocessing import Pool, cpu_count
from datetime import datetime
import random

#starmap approach is good as we can pass multiple param.

def decorator(func):
    def inner_func(*args, **kwargs):
        starttime = datetime.now()
        result = func(*args, **kwargs)
        print(
            f"Time taken is {(datetime.now() - starttime).total_seconds()} and length of result is {len(result)}")
    return inner_func


def calculate_exponentail(number):
    return number ** number


@decorator
def calculate_without_multiprocessing(numbers):
    result = [calculate_exponentail(num) for num in numbers]
    return result


@decorator
def calculate_map_multiprocessing(numbers):
    with Pool(int(cpu_count()*0.8)) as pool:
        result = pool.map(calculate_exponentail, numbers)
        return result


@decorator
def calculate_imap_multiprocessing(numbers):
    with Pool(int(cpu_count()*0.8)) as pool:
        result = pool.imap(calculate_exponentail, numbers)
        return list(result)

@decorator
def calculate_starmap_multiprocessing(numbers):
    arguments = [(number,) for number in numbers]
    with Pool(int(cpu_count()*0.8)) as pool:
        result = pool.starmap(calculate_exponentail, arguments)
        return list(result)

if __name__ == '__main__':
    numbers = [number for number in range(10**5, 10**5 + 100)] + [number for number in range(10000)]
    random.shuffle(numbers)

    calculate_starmap_multiprocessing(numbers)
    calculate_imap_multiprocessing(numbers)
    calculate_map_multiprocessing(numbers)
    calculate_without_multiprocessing(numbers)

"""
1. Eventloop
2. coroutine: feature which enables async programing in python. allows multiple tasks to run within same thread.
3. task
4. future
5. synchronization: asyncio.lock
"""
import asyncio
from datetime import datetime


def decorator(func):
    async def inner_func(*args, **kwargs):
        starttime = datetime.now()
        result = await func(*args, **kwargs)
        print(
            f"Time taken is {(datetime.now() - starttime).total_seconds()} and length of result is {len(result)}")
        return result
    return inner_func


async def do_io_task(id, sleep_time):
    await asyncio.sleep(sleep_time)
    return str(id)

@decorator
async def main_with_gather():
    print("With create tasks")
    result = await asyncio.gather(do_io_task(1, 1),do_io_task(2, 3),do_io_task(3, 2))
    return result

@decorator
async def main_with_create_task():
    print("With create tasks")
    task1 = asyncio.create_task(do_io_task(1, 1))
    task2 = asyncio.create_task(do_io_task(2, 3))
    task3 = asyncio.create_task(do_io_task(3, 2))

    r1 = await task1
    r2 = await task2
    r3 = await task3
    return r1 + r2 + r3

@decorator
async def main():
    print("Without create task")
    task1 = do_io_task(1, 2)
    task2 = do_io_task(2, 3)
    task3 = do_io_task(3, 1)

    r1 = await task1
    r2 = await task2
    r3 = await task3
    return r1 + r2 + r3

asyncio.run(main_with_gather())
print("*"*40)
asyncio.run(main_with_create_task())
print("*"*40)
asyncio.run(main())

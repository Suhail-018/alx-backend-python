#!/usr/bin/env python3
'''Task 2's module.
'''
# import asyncio
# import time
# from importlib import import_module as using


# async_comprehension = using('1-async_comprehension').async_comprehension


# async def measure_runtime() -> float:
#     '''Executes async_comprehension 4 times and measures the
#     total execution time.
#     '''
#     start_time = time.time()
#     await asyncio.gather(*(async_comprehension() for _ in range(4)))
#     return time.time() - 
import asyncio
import time
from importlib import import_module as using
# from 1-async_comprehension import async_comprehension
async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and return total runtime."""
    start_time = time.time()  # Start time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))  # Run 4 tasks in parallel
    end_time = time.time()  # End time
    return end_time - start_time  # Return total execution time

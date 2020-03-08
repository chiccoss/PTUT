import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
	
async def hi():
# await asyncio.sleep(delay)
	print("hi")

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task2
    # await task1

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
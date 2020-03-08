import asyncio

async def count():
    print("One")
    await asyncio.sleep(2)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())


import time
s = time.perf_counter()
asyncio.run(main())


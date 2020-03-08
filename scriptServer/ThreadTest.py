from threading import Thread
import asyncio

async def func1():
    print ('Working from 1\n')

async def func2():
    print ('Working from 2\n')

if __name__ == '__main__':
    # Thread(target = func1).start()
    # Thread(target = func2).start()
	
	asyncio.run(func1())
	asyncio.run(func2())
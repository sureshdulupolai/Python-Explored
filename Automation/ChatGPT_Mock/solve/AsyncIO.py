import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("Func 1")
    return True

async def function2():
    await asyncio.sleep(1)
    print("Func 2")
    return False

async def function3():
    await asyncio.sleep(4)
    print("Func 3")
    return True

async def main():
    # task = asyncio.create_task(function1()) # jab isko time milega tab chalega
    # # untill finishing the first it dont go to next like noraml function running
    # await function2()
    # await function3()

    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)

asyncio.run(main())
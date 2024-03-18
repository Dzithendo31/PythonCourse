#by defualy python is sync, so we have to import asycio
import asyncio


#You have to mark tyhe methods that have to be aysnced
#Question
# - Depndecies.

async def helloWorld():
    print('Mujaiva')
    #Sleep wait for 1 second
    await asyncio.sleep(1)
    print('hello Sanlam')



#We should now just see somethong

async def countDown(Range,step):
    for i in range(Range,-1,-1):
        await asyncio.sleep(step)
        print(i)
    print('Happy New Year')

async def Await(sec):
    await asyncio.sleep(sec)


async def Count():
    print(3)
    await Await(1)
    print(2)
    await Await(1)
    print(1)
    await Await(1)
    print('Happy New Year')
asyncio.run(Count())

#Fire Request at the same
async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
 
 
async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
 
 
# Async with event loop 😁🎊
async def main():
    # Request to event loop to schedule
    task1 = asyncio.create_task(cooking_eggs())  # co-currently
    task2 = asyncio.create_task(make_coffee())
    # Waiting for the background_task
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")
 
    #  Wait till the longest one completes
    await asyncio.wait({task1, task2})
 
 
asyncio.run(main())
import asyncio


async def timer(name,delay):
    await asyncio.sleep(delay)
    print(name,' ',delay)
    return f'{name}   {delay}'

async def main():
    output = await asyncio.gather(timer("Slow",3),timer("Slow",5),timer("fast",1))
    print(output)

asyncio.run(main())
import asyncio
#NEw Library
import aiohttp


async def getName():
    URL = 'https://65f8283eb4f842e8088712f6.mockapi.io/users'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            users = await response.json()
            for perosn in users:
                print(perosn['name'])

asyncio.run(getName())

#Multiple aPI at a same time then you can use gather, otherwise Not.
#Delete and Update
#
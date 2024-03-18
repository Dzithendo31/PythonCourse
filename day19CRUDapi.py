import asyncio
#NEw Library
import aiohttp
import pprint


API = 'https://65f8283eb4f842e8088712f6.mockapi.io'
async def delete_user_by_id(id):
    url = f"{API}/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            user = await response.json()
            return user
# async def main(id):
#     user = await delete_user_by_id(id)
#     print(user)
#Get users
async def getIDs():
    URL = 'https://65f8283eb4f842e8088712f6.mockapi.io/users'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            users = await response.json()
            return [user['id'] for user in users]

IdList = asyncio.run(getIDs()) 
first5 = IdList[:5]

async def main3():
    Gather = [asyncio.create_task(delete_user_by_id(userID)) for userID in first5]
    deletedUsers = await asyncio.gather(*Gather)
    print(deletedUsers)

asyncio.run(main3())

#Chnage profile Picture
        #Using Put
async def changeProfiles(userID):
    URL = f'https://65f8283eb4f842e8088712f6.mockapi.io/users/{userID}'
    newProfile = {'avatar':'https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg'}
    async with aiohttp.ClientSession() as session:
        async with session.put(URL) as response:
            users = await response.json()
            return [user['id'] for user in users]
#Delete the first Code

 
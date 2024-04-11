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
        
async def changeProfiles(userID):
    URL = f'https://65f8283eb4f842e8088712f6.mockapi.io/users/{userID}'
    newProfile = {'avatar':'https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg'}
    async with aiohttp.ClientSession() as session:
        async with session.put(URL,data=newProfile) as response:
            users = await response.json()
            return users
#Delete the first Code
async def main4():
    Gather = [asyncio.create_task(changeProfiles(userID)) for userID in IdList]
    NewUsers = await asyncio.gather(*Gather)
    print(NewUsers)


async def create_user(new_user):
    print(new_user)
    url = f"https://65f8283eb4f842e8088712f6.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        #
        async with session.post(url, json=new_user) as response:
            user = await response.json()
            return user
        
async def main():
    #Create the Users
    print('Creating New Users')
    user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
    default_PP = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Hrc_logo.svg/1200px-Hrc_logo.svg.png%22'
    NewUsers = [asyncio.create_task(create_user({'name':user,'avatar':default_PP})) for user in user_list]
    CreatedUser = await asyncio.gather(
        *NewUsers
        )
    print(CreatedUser)

    #Delete the First 5 users
    # print('deleting Forst 5 users')
    # IdList = asyncio.run(getIDs()) 
    # first5 = IdList[:5]
    # Gather = [asyncio.create_task(delete_user_by_id(userID)) for userID in first5]
    # deletedUsers = await asyncio.gather(*Gather)
    # print(deletedUsers)

    #Change profile picture to the human Rghts one


    



#Run the Main
asyncio.run(main())
 
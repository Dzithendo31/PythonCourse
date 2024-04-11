#Now we testing our knowloedge
#Using request witll male it asyncronious
import requests
import asyncio

#NEw Library
import aiohttp

async def getCityWeather(city):
    #Lets create some delay.
    print(f'geting temp for {city}')
    await asyncio.sleep(2)
    URL = f'http://api.weatherapi.com/v1/current.json?key=0858f7e7614a47208cb93022241503&q={city}&aqi=no'
    #There is Some memory Management Thing.
    async with aiohttp.ClientSession() as session:# This context manager ensures that resources associated with the session are 
                                                #properly cleaned up after the block of code within it completes execution.
        async with session.get(URL) as response:
            #This line sends an asynchronous HTTP GET request to the URL constructed earlier
            weather = await response.json()
            print(city,": ",weather['current']['temp_c'])




##Run it
# asyncio.run(getCityWeather('Cape Town'))
# asyncio.run(getCityWeather('New Dehli'))
# asyncio.run(getCityWeather('durban'))

#Now using agther

# async def main():
#     await getCityWeather('Cape Town')
#     await getCityWeather('New Dehli')
#     await getCityWeather('gaza')

async def main():
    # await asyncio.gather(
    #     getCityWeather('Cape Town'),
    #     getCityWeather('New York'),
    #     getCityWeather('Tokyo')
    # )
    #or Use a Train ---- List
    all_get_temp_city = [
        getCityWeather("Cape Town"),
        getCityWeather("Chennai"),
        getCityWeather("Johannesburg")
    ]
    await asyncio.gather(*all_get_temp_city)

#is used to concurrently execute multiple coroutines and wait for all of them to complete.
#Task 02
    #Use Gather and Create_task
async def main():
    print("Task 2")
    all_get_temp_city_co_routines = [
        asyncio.create_task(getCityWeather("Cape Town")),
        asyncio.create_task(getCityWeather("Chennai")),
        asyncio.create_task(getCityWeather("Johannesburg")),
    ]
    await asyncio.gather(*all_get_temp_city_co_routines)
#asyncio.run(main())

#Task
cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]
async def async_with_list_to_dict(cities):
    dictionary = {city:asyncio.run(getCityWeather(city)) for city in cities}
    return dictionary
# asyncio.run(async_with_list_to_dict(cities))
#Using List Comprehensio
async def main2():
    Gather = [asyncio.create_task(getCityWeather(city)) for city in cities]
    await asyncio.gather(*Gather)
#asyncio.run(main2())

#Task 04
async def getCityWeather2(city):
    #Lets create some delay.
    print(f'geting temp for {city}')
    URL = f'http://api.weatherapi.com/v1/current.json?key=0858f7e7614a47208cb93022241503&q={city}&aqi=no'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            weather = await response.json()
            return (city,weather['current']['temp_c'])
async def main3():
    Gather = [asyncio.create_task(getCityWeather2(city)) for city in cities]
    weather = dict(await asyncio.gather(*Gather))
    print(weather)
asyncio.run(main3())      

# def getCityWeather(city):
#     URL = f'http://api.weatherapi.com/v1/current.json?key=0858f7e7614a47208cb93022241503&q={city}&aqi=no'
#     response = requests.get(URL,verify=False)
#     city_weather = response.json()
#     return city_weather
# def getWeather(city):
#     city_weather = getCityWeather(city)
#     temp_in_C = city_weather['current']['temp_c']
#     return f"The Temperature in {city} is {temp_in_C}°C"
# import the module
import python_weather

import asyncio
import os

async def getweather():
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Новосибирск')

    celsius = (weather.temperature - 32) / 1.8

    print(str(round(celsius)) + '°')

if __name__ == '__main__':

  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())



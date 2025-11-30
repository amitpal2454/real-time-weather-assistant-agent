import os
import sysconfig
import json
import requests
import time
from openai import AzureOpenAI

from dotenv import load_dotenv
load_dotenv()
client=AzureOpenAI(azure_endpoint=os.environ.get("AZURE_END_POINT"),
                   api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
                   api_version="2024-05-01-preview")


def get_weather(latitude,longitude):
    if latitude is None:
        return json.dump({"weather_api_response":"Required argument latitude is not provided"})
    if longitude is None:
        return json.dump({"weather_api_response":"Required argument longitude is not provided"})
    if latitude>90 or latitude<-90:
        return json.dump({"weather_api_response":"invalid latitude values"})
    if longitude>180 or longitude<-180:
        return json.dump({"weather_api_response":"invalid longitude values"})
    
    api_key=os.environ.get("WEATHER_API_KEY")
    complete_url=f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response=requests.get(complete_url)
    weather_data=response.json()
    return weather_data

print(get_weather(-45,45))
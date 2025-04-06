import os
import requests


def get_weather(city: str = "Paris") -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY not set in environment variables!")

    url = (f"http: //api.weatherapi.com/v1/"
           f"current.json?key={api_key}&q={city}&aqi=no")

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {location}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()

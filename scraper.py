
import urllib.request
import urllib.parse
import os, json

def get_weather(city,api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  # Use "metric" for Celsius
    }
    url = base_url + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as response:
        if response.status != 200:
            raise Exception(f"API request failed with status {response.status}")
        data = response.read()
        return json.loads(data)

if __name__ == "__main__":
    api_key = os.getenv("OWM_KEY")
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
    else:
        city = "boston"
        weather = get_weather(city,api_key)
        filename = f"weather_{city}.json"
        with open(filename, "w") as f:
            json.dump(weather, f, indent=2)
        print(f"Current weather in Boston:")
        print(f"Temperature: {weather['main']['temp']}°F")
        print(f"Weather: {weather['weather'][0]['description']}")

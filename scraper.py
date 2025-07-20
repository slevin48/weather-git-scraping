
import urllib.request
import urllib.parse
import os, json, datetime, csv

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
        json_data = json.loads(data)
        weather_info = json_data['main']
        # add current date and time
        weather_info['time'] = datetime.datetime.fromtimestamp(json_data['dt']).strftime("%d-%b-%Y_%H-%M-%S")
        return weather_info

if __name__ == "__main__":
    api_key = os.getenv("OWM_KEY")
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
    else:
        city = "boston"
        weather = get_weather(city,api_key)
        # filename = f"weather_{city}.json"
        # with open(filename, "w") as f:
        #     json.dump(weather, f, indent=2)
        print(f"Current weather in Boston:")
        print(f"Temperature: {weather['temp']}°F")
        # Open the existing file in append mode
        with open(f'weather_history_{city}.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write just the values (no header)
            writer.writerow(weather.values())
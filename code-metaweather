import requests

def get_weather():
    # Ask the user for their city
    city = input("Enter your location (e.g., London): ")

    # MetaWeather API endpoint to get location details based on city name
    search_url = f"https://www.metaweather.com/api/location/search/?query={city}"
    
    # Send a GET request to search for the location
    response = requests.get(search_url)
    locations = response.json()

    if len(locations) == 0:
        print("City not found. Please check the city name and try again.")
        return

    # Get the WOEID (Where On Earth ID) of the first result
    woeid = locations[0]['woeid']
    
    # Use the WOEID to get weather details for the city
    weather_url = f"https://www.metaweather.com/api/location/{woeid}/"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Get the current weather
    current_weather = weather_data['consolidated_weather'][0]
    temperature = current_weather['the_temp']
    weather_state = current_weather['weather_state_name']

    # Print the weather details
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature:.1f}°C")
    print(f"Condition: {weather_state}")

if __name__ == "__main__":
    get_weather()

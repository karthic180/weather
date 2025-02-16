import requests
from bs4 import BeautifulSoup

def get_weather():
    city = input("Enter your location (e.g., London): ")

    # The wttr.in service to get weather information
    url = f"https://wttr.in/{city}?format=%C+%t"  # %C for condition, %t for temperature

    # Send a GET request to the wttr.in website
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            weather_info = response.text.strip()
            print(f"Weather in {city}: {weather_info}")
        else:
            print(f"Could not retrieve weather data for {city}. Please check the city name and try again.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while retrieving the weather data: {e}")

if __name__ == "__main__":
    get_weather()

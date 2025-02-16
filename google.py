import requests
from bs4 import BeautifulSoup

def get_weather():
    # Ask the user for their city
    city = input("Enter your location (e.g., London): ")

    # Create the Google Search URL with the city name
    url = f"https://www.google.com/search?q=weather+{city}"
    
    # Send a GET request to fetch the HTML content of the page
    html = requests.get(url).content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find temperature and sky condition
        temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        sky_condition = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        
        # Extract just the weather description
        sky = sky_condition.split('\n')[1]
        
        # Print out the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}")
        print(f"Condition: {sky}")
        
    except AttributeError:
        print("Could not fetch the weather data. Please check the city name and try again.")

if __name__ == "__main__":
    get_weather()

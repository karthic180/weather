
# Weather App

This is a simple Python-based weather app that retrieves current weather information for a given city using web scraping. The app scrapes weather data from the `wttr.in` website and displays the condition and temperature for the specified location.

## Features
- Get current weather information (condition and temperature) for any city.
- No API key required.
- Simple and lightweight solution using web scraping.

## Requirements
- Python 3.x
- `requests` library

## Installation

To run the weather app on your local machine, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine

### 2. Install Required Libraries
You need to install the required Python libraries. You can install them using `pip`:

```bash
pip install requests
```

### 3. Run the App
Once the dependencies are installed, you can run the app with:

```bash
python main.py
```

The app will prompt you to enter a city name, and it will then display the current weather for that city.

## Usage
When you run the app, it will ask you to enter the name of a city (e.g., London). Once you input a city, it will display the current weather condition and temperature.

Example:

```bash
Enter your location (e.g., London): London
Weather in London: Clear 18°C
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributing
Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!

## Acknowledgments
- This app uses the `wttr.in` service for retrieving weather data. Check out [wttr.in](https://wttr.in/) for more information.

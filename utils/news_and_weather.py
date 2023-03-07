from spacewink_terminal.api import fetch_news, fetch_weather

def get_latest_news():
    # Fetch the latest news headlines
    news_headlines = fetch_news()

    # Print the headlines
    for i, headline in enumerate(news_headlines):
        print(f"{i+1}. {headline['title']}")
        print(f"   Source: {headline['source']['name']}")
        print(f"   Published: {headline['publishedAt']}")
        print(f"   URL: {headline['url']}")
        print()

def get_current_weather(city):
    # Fetch the current weather data for the given city
    weather_data = fetch_weather(city)

    # Print the weather information
    print(f"Current weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Feels like: {weather_data['main']['feels_like']}°C")
    print(f"Description: {weather_data['weather'][0]['description']}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind speed: {weather_data['wind']['speed']} m/s")
    print(f"Pressure: {weather_data['main']['pressure']} hPa")

import requests

def get_weather(city, api_key):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    print(f"\nFetching weather for {city}...")
    
    try:
    
        response = requests.get(url)
        
        if response.status_code == 404:
            print("Error: City not found! Enter Correct Spelling.")
            return
            
        
        elif response.status_code == 401:
            print("Error: Invalid API Key! Please check your key.")
            return
            
        response.raise_for_status()
        
        
        data = response.json()
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        
        print("=" * 30)
        print(f"Weather in {city.title()}")
        print("=" * 30)
        print(f"Condition   : {weather_desc.title()}")
        print(f"Temperature : {temp}°C")
        print(f"Feels Like  : {feels_like}°C")
        print(f"Humidity    : {humidity}%")
        print("=" * 30)

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")


def main():
    
    API_KEY = "e5d743a293a549a37711e16cf76ceb84"
    
    print("=== Live Weather Man ===")
    
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        
        if city.lower() == 'exit':
            print("Goodbye!")
            break
            
        if city.strip() == "":
            print("Please enter a valid city name.")
            continue
            
        get_weather(city, API_KEY)


if __name__ == "__main__":
    main()
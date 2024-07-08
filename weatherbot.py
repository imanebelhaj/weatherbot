import discord
import requests
import os

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Initialize the bot with intents
bot = discord.Client(intents=intents)

DISCORD_TOKEN=your_discord_token_here
WEATHER_API_KEY=your_weather_api_key_here

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # If the message starts with '!weather', fetch weather information
    if message.content.startswith('!weather'):
        try:
            # Extract the city from the message
            city = message.content.split(' ', 1)[1]
            # Fetch weather data
            weather_data = get_weather(city)
            # Send the weather information back to the channel
            await message.channel.send(embed=weather_data)
        except IndexError:
            await message.channel.send('Please specify a city name.')

def get_weather(city):
    # API endpoint for weather data
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract weather information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Get weather icon
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        # Determine emoji based on weather description
        emoji = get_weather_emoji(weather)

        # Create an embed message with the weather information
        embed = discord.Embed(title=f"Weather in {city}", description=f"Current weather information for {city}.", color=0x3498db)
        embed.add_field(name="Description", value=f"{emoji} {weather.capitalize()}", inline=False)
        embed.add_field(name="Temperature", value=f"{temperature}°C", inline=False)
        embed.add_field(name="Humidity", value=f"{humidity}%", inline=False)
        embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=False)
        embed.set_thumbnail(url=icon_url)  # Set weather icon as thumbnail

        # Customize field colors based on weather conditions
        if 'rain' in weather.lower() or 'drizzle' in weather.lower():
            embed.color = 0x3498db  # Blue for rainy weather
        elif 'cloud' in weather.lower():
            embed.color = 0x95a5a6  # Gray for cloudy weather
        elif 'clear' in weather.lower():
            embed.color = 0xf1c40f  # Yellow for clear weather
        elif 'snow' in weather.lower():
            embed.color = 0xffffff  # White for snowy weather
        elif 'thunderstorm' in weather.lower():
            embed.color = 0x7f8c8d  # Dark gray for thunderstorms
        else:
            embed.color = 0x3498db  # Default to blue

        # Add footer with attribution and icon
        embed.set_footer(text="Powered by OpenWeatherMap", icon_url="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png")

        return embed
    else:
        # If the city is not found, return an error message
        embed = discord.Embed(title="Error", description=f"Could not find weather data for {city}.", color=0xff0000)
        return embed

def get_weather_emoji(weather):
    if 'clear' in weather.lower():
        return '☀️'
    elif 'rain' in weather.lower() or 'drizzle' in weather.lower():
        return '🌧️'
    elif 'cloud' in weather.lower():
        return '☁️'
    elif 'snow' in weather.lower():
        return '❄️'
    elif 'thunderstorm' in weather.lower():
        return '⛈️'
    else:
        return ''

# Run the bot
bot.run(DISCORD_TOKEN)

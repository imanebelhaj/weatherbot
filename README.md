# Discord Weather Bot

![Weather Bot Logo](https://github.com/imanebelhaj/weatherbot/assets/114827745/509b6b4e-f31d-4983-8dac-4a8a787b27ee)

## Overview

This Discord bot provides current weather information for cities using the OpenWeatherMap API.

## Development

- **Discord Developer Portal:** This bot was created using the [Discord Developer Portal](https://discord.com/developers/applications). You can manage your bot's settings, get its token, and configure permissions there.
- **OpenWeatherMap API:** Weather data is fetched using the OpenWeatherMap API.

## Installation

1. **Clone the repository:**
   git clone https://github.com/imanebelhaj/weatherbot.git
   cd weatherbot

2.**Install dependencies:**
  pip install discord.py requests


3.**Set up environement:**
  Note: Replace your_username, your_discord_token_here, your_weather_api_key_here

DISCORD_TOKEN=your_discord_token_here
WEATHER_API_KEY=your_weather_api_key_here


4.**Run the bot:**
  python weatherbot.py

## Usage
Invite the bot to your Discord server.
Use the command !weather <city> to get current weather information for a specific city.

## Contributing
Contributions are welcome! Please follow these guidelines:

1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bug fix: git checkout -b feature/my-feature
3. Make your changes and test thoroughly.
4. Commit your changes: git commit -am 'Add new feature'
5. Push to the branch: git push origin feature/my-feature
6. Submit a pull request.
   
## License
This project is licensed under the MIT License. See the LICENSE file for details.




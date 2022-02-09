# Univers Account Protector for Discord
This **open-source software** made in Python **protects your account** and **notifies you immediately** after a **suspicious activity is detected**.

## WARNING
This software might be considered as a "self-bot", which is against [Discord Terms of Service](https://discord.com/terms). Use at your own risk!

## Setup

 1. [Download & install **Python 3**](https://www.python.org/downloads/)
 2. Clone or download this project
 3. Create a .env file.
 4. Put this in your *.env* file: 
> TOKEN=[your Discord token*]
> TWILIO_ACCOUNT_SID=[Twilio Account SID. Can be found here: https://console.twilio.com/]
> TWILIO_AUTH_TOKEN=[Twilio Authentification Token. Can be found here: https://console.twilio.com/]
 5. Open *config.json* and edit configuration file
 6. Run this in your command prompt: `pip3 install -r requirements.txt`
 7. Keep your command prompt open and run this `py main.py`
 8. **You're good to go!** If you enabled notifications in *config.json*, a voice should tell you that your account is being monitored.

*\*To get your token, please check on Google for instructions. Make sure the instructions are safe.*

## Special thanks
This project uses:

 - **[discord.py](https://pypi.org/project/discord.py) by [Rapptz](https://github.com/Rapptz)**
 - **Twilio**
 - **[python-dotenv](https://pypi.org/project/python-dotenv/) by [bbc](https://pypi.org/user/bbc/) & [theskumar](https://pypi.org/user/theskumar/)**
 - [**pygame**](https://github.com/pygame/pygame) 

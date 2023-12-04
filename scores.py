import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Constants
RAPID_API_KEY = os.getenv('RAPIDAPI_KEY')
url = "https://odds.p.rapidapi.com/v4/sports/americanfootball_nfl/scores"
querystring = {"daysFrom":"1"}
headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "odds.p.rapidapi.com"
}

def separate_string_space(name):
    name = name.lower()
    name = name.split(" ")
    return name

def separate_string_dash(name):
    name = name.lower()
    name = name.split("-")
    return name

def get_single_game_score(team):
    response = requests.get(url, headers=headers, params=querystring)

    for games in response.json():
        if games['home_team'] is not None or games['away_team'] is not None:
            if team == games['home_team'] or team == games['away_team']:
                print(f"{games['home_team']} VS {games['away_team']}")
                if games['scores'] is not None:
                    scores: {games['scores'][0], games['scores'][1]}
                    game_info = [games['home_team'], games['away_team'], scores]
                    print(game_info)
                    return game_info
                else:
                    scores: {None}
                    game_info = [games['home_team'], games['away_team'], scores]
                    print(f"No scores yet! Game starts at {games['commence_time']}")

async def get_scores():
    response = requests.get(url, headers=headers, params=querystring)

    #print(response.json()[0])
        # # JSON OBJECT
        # id
        # sport_key
        # sport_title
        # commence_time
        # completed
        # home_team
        # away_team
        # scores
        # last_update

    return response.json()

    for games in response.json():
        
        print(f"{games['home_team']} VS {games['away_team']}")
        if games['scores'] is not None:
            print(f"{games['scores'][0]}")
            print(f"{games['scores'][1]}")
        else:
            print(f"No scores yet! Game starts at {games['commence_time']}")

async def get_avatar(team):

    ####### URL format #######
    ### https://github.com/mhussain790/nfl-discord-bot/blob/main/img/detroit.png?raw=true

    # https://raw.githubusercontent.com/mhussain790/nfl-discord-bot/main/img/detroit.png
    ##########################

    # Get the list of files
    img_url_prefix = 'https://github.com/mhussain790/nfl-discord-bot/blob/main/img/'
    path = "./img"
    files = os.listdir(path)

    # Check if the team is a special case (los angeles chargers, los angeles rams, new orleans saints, new york giants, new york jets, tampa bay buccaneers)
    if team == 'san francisco 49ers':
        print(f"{path}/san-francisco.png")
        return path + 'san-francisco.png'
    elif team == 'green bay packers':
        return path + 'green-bay.png'
    elif team == 'kansas city chiefs':
        return path + 'kansas-city.png'
    elif team == 'new england patriots':
        return path + 'new-england.png'
    elif team == 'new orleans saints':
        return path + 'new-orleans.png'
    elif team == 'new york giants':
        return path + 'new-york-giants.png'
    elif team == 'new york jets':
        return path + 'new-york-jets.png'
    elif team == 'los angeles chargers':
        return path + 'los-angeles-chargers.png'
    elif team == 'los angeles rams':
        return path + 'los-angeles-rams.png'
    elif team == 'tampa bay buccaneers':
        return path + 'tampa-bay.png'

    #  Separate the name
    name_array = separate_string_space(team)
    print(name_array)

    for file in files:
        temp = file
        file = file.removesuffix(".png")
        if file in name_array:
            print(f"Found {temp} in {name_array}")
            print(f"{path}/{temp}")
            return img_url_prefix + '/' + img_url_suffix

get_avatar('san francisco 49ers')
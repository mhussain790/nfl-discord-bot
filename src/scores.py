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

async def get_single_game_score(team):
    response = requests.get(url, headers=headers, params=querystring)

    for games in response.json():
        if games['home_team'] is not None or games['away_team'] is not None:
            home_team = games['home_team']
            away_team = games['away_team']
            
            if team == home_team.lower() or team == away_team.lower():
                print(f"{games['home_team']} VS {games['away_team']}")
                if games['scores'] is not None:

                    scores = [games['scores'][0], games['scores'][1]]
                    score_1_name = games['scores'][0].get('name')
                    score_1_value = games['scores'][0].get('score')

                    score_2_name = games['scores'][1].get('name')
                    score_2_value = games['scores'][1].get('score')

                    if home_team == score_1_name:
                        home_score = score_1_value
                        away_score = score_2_value
                    else:
                        home_score = score_2_value
                        away_score = score_1_value

                    # Debugging purposes
                    # game_info = [games['home_team'], games['away_team'], scores]

                    # Create game_info dict
                    game_info = {"home_team": games['home_team'], "away_team": games['away_team'], "scores": True, "home_score": home_score, "away_score": away_score, "commence_time": games['commence_time']}


                    print(game_info)
                    return game_info
                
                else:
                    game_info = {"home_team": games['home_team'], "away_team": games['away_team'], "scores": None, "commence_time": games['commence_time']}
                    print(game_info)
                    print(f"No scores yet! Game starts at {games['commence_time']}")
                    return game_info

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

async def get_avatar(team):
    print(f"Getting avatar for {team}")
    ####### URL format #######
    ### https://github.com/mhussain790/nfl-discord-bot/blob/main/img/detroit.png?raw=true

    # https://raw.githubusercontent.com/mhussain790/nfl-discord-bot/main/img/detroit.png
    ##########################

    # Get the list of files
    img_url = 'https://raw.githubusercontent.com/mhussain790/nfl-discord-bot/main/img/'
    path = "./img"
    files = os.listdir(path)

    # Check if the team is a special case (los angeles chargers, los angeles rams, new orleans saints, new york giants, new york jets, tampa bay buccaneers)
    if team == 'san francisco 49ers' or team == 'san francisco':
        print(f"{path}/san-francisco.png")
        return img_url + 'san-francisco.png'
    elif team == 'green bay packers':
        return img_url + 'green-bay.png'
    elif team == 'kansas city chiefs' or team == 'kansas city':
        return img_url + 'kansas-city.png'
    elif team == 'new england patriots':
        return img_url + 'new-england.png'
    elif team == 'new orleans saints':
        return img_url + 'new-orleans.png'
    elif team == 'new york giants':
        return img_url + 'new-york-giants.png'
    elif team == 'new york jets':
        return img_url + 'new-york-jets.png'
    elif team == 'los angeles chargers':
        return img_url + 'los-angeles-chargers.png'
    elif team == 'los angeles rams':
        return img_url + 'los-angeles-rams.png'
    elif team == 'tampa bay buccaneers':
        return img_url + 'tampa-bay.png'

    #  Separate the name
    name_array = separate_string_space(team)
    print(name_array)

    for file in files:
        temp = file
        file = file.removesuffix(".png")
        if file in name_array:
            print(f"Found {temp} in {name_array}")
            output = img_url + temp

            print(output)
            return output

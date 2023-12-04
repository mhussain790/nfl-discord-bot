import requests
api_url = 'https://api.breakingbadquotes.xyz/v1/quotes'

def get_a_quote():
    response = requests.get(api_url)

    if response.status_code == 200:
        output = response.json()[0]['quote'] + " - " + response.json()[0]['author']
        print(output)
        return output
    else:
        return "No quote for you!"
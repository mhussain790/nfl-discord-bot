import requests

async def get_meme_url():
    url = 'https://meme-api.com/gimme'

    response = requests.get(url)

    data = response.json()
    print(f"URL Found!\n URL is: {data['url']}")

    return data['url']
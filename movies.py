import requests

url = "https://moviesdatabase.p.rapidapi.com/titles/x/upcoming"

headers = {
	"X-RapidAPI-Key": "5a606e8d9cmshe8d8346ac3f1decp185020jsn4225398e4311",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
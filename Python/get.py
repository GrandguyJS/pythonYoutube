import requests, json

data = json.load(open('./Secrets/Secret.json', 'r'))

API_KEY = data["API_KEY"]
CHANNEL_ID = data["CHANNEL_ID"]

num = input("How many videos do you want to download? Type x for all! ")

url = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=100")

text = url.text
data = json.loads(text)
fullData = data
data = data["items"]

if num == "x":
    end = len(data)
else:
    end = int(num)

jsonFile = {
    "id": [],
    "title": [],
    "picture": [],
    "description": [],
    "publishedAt": [],
    "infos": {"name": []}
}
jsonFile["infos"]["name"].append(data[0]["snippet"]["channelTitle"])
for i in range(0, end):
    jsonFile["id"].append(data[i]["id"]["videoId"])
    jsonFile["title"].append(data[i]["snippet"]["title"])
    jsonFile["picture"].append(data[i]["snippet"]["thumbnails"]["high"]["url"])
    jsonFile["description"].append(data[i]["snippet"]["description"])
    jsonFile["publishedAt"].append(data[i]["snippet"]["publishedAt"])
    
    




with open('videos.json', 'w') as d:
    json.dump(jsonFile, d, indent=2)
    print("New json file is created from jsonFile")
    d.close()
with open('fullJSON.json', 'w') as a:
    json.dump(fullData, a, indent=2)
    print("New jsonFULL file is created from jsonFile")
    a.close()








    


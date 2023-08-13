
import os
import json
from pytube import YouTube

f = open('videos.json')

path = #path

data = json.load(f)
f.close()

a = open("fullJSON.json")
fullData = json.load(a)
a.close()



name = data["infos"]["name"][0]

if os.path.exists(path+name):
    print("Path already exists!")



else:




    os.mkdir(path+name)

    from pytube import YouTube




    number = 1

    for i in range(0, len(data["id"])):

        
        

        link = "https://www.youtube.com/watch?v="+data["id"][i]

        yt = YouTube(link)  

        
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=path+name)
       



    

        print(f'Video {number} downloaded successfully...? Video number {number}! With name {data["title"][i]}')
        number += 1

   




    with open(path + name + f"/{name}.json", 'w') as f:
        json.dump(data, f, indent=2)

    f.close()
with open(path + name + f"/{name}FULL.json", 'w') as b:
    json.dump(fullData, b, indent=2)
    print("Done")
b.close()

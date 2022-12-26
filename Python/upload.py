
import os
import json


f = open('videos.json')

data = json.load(f)
f.close()

a = open("fullJSON.json")
fullData = json.load(a)
a.close()



name = data["infos"]["name"][0]

if os.path.exists("//Jedi/SharedFolder/Sergei/Python/YT/vids/"+name):
    print("Path already exists!")



else:




    os.mkdir("//Jedi/SharedFolder/Sergei/Python/YT/vids/"+name)

    from pytube import YouTube




    number = 1

    for i in range(0, len(data["id"])):

        
        from pytube import YouTube

        link = "https://www.youtube.com/watch?v="+data["id"][i]

        yt = YouTube(link)  

        
        yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = "//Jedi/SharedFolder/Sergei/Python/YT/vids/"+name)

       



    

        print(f'Video {number} downloaded successfully...? Video number {number}! With name {data["title"][i]}')
        number += 1

    print("Done!!")




    with open("//Jedi/SharedFolder/Sergei/Python/YT/vids/" + name + f"/{name}.json", 'w') as f:
        json.dump(data, f, indent=2)

    f.close()
with open("//Jedi/SharedFolder/Sergei/Python/YT/vids/" + name + f"/{name}FULL.json", 'w') as b:
    json.dump(fullData, b, indent=2)
    print("really DONE!!!")
b.close()
import json
import pprint

arq = open("saida_completa/ed_dataset_complete.json").read()
videos = json.loads(arq)

for video in videos:
    if video['id']['videoId'] == "2Vv-BfVoq4g":
        id_channel = video['snippet']['channelId']
        break

print(id_channel)

oficial_channel = "UC0C-w0YjGpqDXGB8IHb662A"

c = 0
for video in videos:
    if video['snippet']['channelId'] == oficial_channel:
        c += 1
        video['isOfficialChannel'] = 1
    else:
        video['isOfficialChannel'] = 0

print(c)

pprint.pprint(videos[15876])

arqout = open("saida_completa/ed_dataset_complete.json", 'w')

arqout.write(json.dumps(videos))
import json
import pprint
import youtube_tools as yt

txt = open("items.json").read()
videos = json.loads(txt)
aux = open("temporario.json").read()
prov = open("temporario.json", 'w')
prov.write(aux)
ed = 0
missing = {}
missing['stats'] = 0
missing['tags'] = 0
missing['contentDetails'] = 0
missing['categoryId'] = 0
missing['publishedAt'] = 0
bugs = 0

'''teste = yt.youtube_stats(videos[17])
pprint.pprint(teste)
try:
    print(teste['items'][0]['snippet']['tags'])
except KeyError as err:
    print("Deu ruim")
    pass

print("passou")'''

count = str(aux).count("videoId")

for video in videos:
    if ed < count:
        ed += 1 
        continue

    info = yt.youtube_stats(video)
    try:
        video['stats'] = info['items'][0]['statistics']
    except KeyError as err:
        video['stats'] = None
        missing['stats'] += 1
        print("Missing stats - {}".format(missing['stats']))
    except IndexError as err:
        print("Dado bugado")
        video = []
        bugs += 1
    
    try:
        video['tags'] = info['items'][0]['snippet']['tags']
    except KeyError as err:
        video['tags'] = None
        missing['tags'] += 1
        print("Missing tags - {}".format(missing['tags']))
    except IndexError as err:
        print("Dado bugado")
        video = []
        bugs += 1
    
    try:
        video['contentDetails'] = info['items'][0]['contentDetails']
    except KeyError as err:
        video['contentDetails'] = None
        missing['contentDetails'] += 1
        print("Missing contentDetails - {}".format(missing['contentDetails']))
    except IndexError as err:
        print("Dado bugado")
        video = []
        bugs += 1

    try:
        video['categoryId'] = info['items'][0]['snippet']['categoryId']
    except KeyError as err:
        video['categoryId'] = None
        missing['categoryId'] += 1
        print("Missing categoryId - {}".format(missing['categoryId']))
    except IndexError as err:
        print("Dado bugado")
        video = []
        bugs += 1

    try:
        video['publishedAt'] = info['items'][0]['snippet']['publishedAt']
    except KeyError as err:
        video['publishedAt'] = None
        missing['publishedAt'] += 1
        print("Missing publishedAt - {}".format(missing['publishedAt']))
    except IndexError as err:
        print("Dado bugado")
        video = []
        bugs += 1
    #print(videos[ed]['categoryId'])

    if ed % 5 == 0:
        print("{} - Give me Love".format(ed))
    else:
        print("{} - My".format(ed))

    ed += 1
    prov.write(json.dumps(video) + "\n")


print("\nStats Missing")
print("Missing stats - {}".format(missing['stats']))
print("Missing tags - {}".format(missing['tags']))
print("Missing contentDetails - {}".format(missing['contentDetails']))
print("Missing categoryId - {}".format(missing['categoryId']))
print("Missing publishedAt - {}".format(missing['publishedAt']))

out = open("items_extended.json", 'w')
out.write(json.dumps(videos))

import json
import pprint
import youtube_tools as yt

def check_title(item, word):
    
    title = item['snippet']['title']
    if(word in title):
        return 1
    else:
        return 0

def check_description(item, word):
    
    description = item['snippet']['description']
    if word in description:
        return 1
    else:
        return 0

def search_list_generate(q, n, t):
    num = n // 50
    res = n % 50
    nextPageToken = None
    result_search = []
    qtdd = 0

    print("####Search Parameters####\n")
    print("Search: {}\nMaximum: {}\nType of videos: {}".format(q, n, t))
    print("\n#########################")

    for i in range(num):
        aux = yt.youtube_search(q, max_results=50, token=nextPageToken, video_duration=t)
        result_search.append(aux)
        item = aux['items']
        qtdd += len(item)
        nextPageToken = aux['nextPageToken']

        print("work {} -> {}".format(qtdd, nextPageToken))

        if len(item) == 0:
            print("\nTOTAL DE VIDEOS COLETADOS: {}".format(qtdd))
            break
    #result_search.append(yt.youtube_search(q, max_results=res,token=nextPageToken))

    arqout = open("results/{}_{}.json".format(q.replace(" ", "_"), t), 'w')
    arqout.write(json.dumps(result_search))

    return result_search



def add_to_list(dic):
    items = []
    all_items = []
    ids = []
    arq = open("items.json")
    txt = arq.read()
    arq.close()
    
    for i in dic:
        items.append(i['items'])

    if txt == "":
        all_lists = []

    else:
        all_lists = json.loads(txt)
        
        for i in all_lists:
            ids.append(i['id']['videoId'])
    
    print("Tamanho da Base de Dados Atual: {}\n".format(len(all_lists)))

    for item in items:
        all_items.extend(item)

    for item in all_items:
        if item['id']['videoId'] not in ids:
            all_lists.append(item)
            print("Video {} was added to the dataset".format(item['id']['videoId']))
        
        else:
            print("Video {} already is in dataset".format(item['id']['videoId']))

    arqout = open("items.json", 'w')
    arqout.write(json.dumps(all_lists))
    print("\nNovo Tamanho da Base de Dados: {}".format(len(all_lists)))

    return len(all_lists)



items = search_list_generate("ed sheeran what do i know", 300, "medium")

num = add_to_list(items)


for i in items:
    print(len(i['items']))

print(num)
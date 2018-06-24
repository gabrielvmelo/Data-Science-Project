import json
import pprint

def check_title(item, word):
    
    title = item['snippet']['title']
    if(word.lower() in title.lower()):
        return 1
    else:
        return 0

def check_description(item, word):
    
    description = item['snippet']['description']
    if word.lower() in description.lower():
        return 1
    else:
        return 0


def check_tag(item, word):

    tags = item['tags']

    if tags == None:
        return 0

    else:
        for tag in tags:
            if word.lower() in tag.lower():
                return 1

    return 0

def maior(a, b):
    if a > b:
        return a
    else :
        return b

def convert_duration(time):
    t = time.find("T")
    w = time.find("W")
    d = time.find("D")
    h = time.find("H")
    m = time.find("M")
    s = time.find("S")

    
    if h > 0:
        hours = int(time[maior(t, d)+1:h])
    else:
        hours = 0

    if m > 0:
        minutes = int(time[maior(t, h)+1:m])
    else:
        minutes = 0

    if s > 0:
        segundos = int(time[maior(t, m)+1:s])
    else:
        segundos = 0

    return (hours, minutes, segundos)
    

def dur_category(time):
    time_adjuste = convert_duration(time)

    time_total = time_adjuste[0]*60*60 + time_adjuste[1]*60 + time_adjuste[2]
    
    if time_total <= 60:
        category = 0
    elif time_total <= 120:
        category = 1
    elif time_total <= 240:
        category = 2
    elif time_total <= 360:
        category = 3
    elif time_total <= 600:
        category = 4
    elif time_total <= 1200:
        category = 5
    else:
        category = 6

    return category 

    return time_total

arq = open("saida/ed_dataset.json").read()
videos = json.loads(arq)
a = 18765
pprint.pprint(videos[a])

lens = []
tipos = []



for video in videos:
    cover_title = check_title(video, "cover")
    cover_description = check_description(video, "cover")
    cover_tag = check_tag(video, "cover")
    ed_title = check_title(video, "ed sheeran")
    ed_description = check_description(video, "ed sheeran")
    ed_tag = check_tag(video, "ed sheeran")
    ofi_title = check_title(video, "official")
    ofi_description = check_description(video, "official")
    ofi_tag = check_tag(video, "official")
    live_title = check_title(video, "live")
    live_description = check_description(video, "live")
    live_tag = check_tag(video, "live")

    video['coverTitle'] = cover_title
    video['coverDescription'] = cover_description
    video['coverTag'] = cover_tag
    video['edTitle'] = ed_title
    video['edDescription'] = ed_description
    video['edTag'] = ed_tag
    video['ofiTitle'] = ofi_title
    video['ofiDescription'] = ofi_description
    video['ofiTag'] = ofi_tag
    video['liveTitle'] = live_title
    video['liveDescription'] = live_description
    video['liveTag'] = live_tag
    video['durationCategory'] = dur_category(video['contentDetails']['duration'])
    aux = len(video['contentDetails']['duration'])
    idChannel = []

    if aux > 14:
        pprint.pprint(video)

    if aux not in lens:
        lens.append(aux)
        tipos.append(video['contentDetails']['duration'])

    if video['snippet']['channelTitle'] == "Ed Sheeran":
        idChannel.append( video['snippet']['channelId'] )
        print(video['snippet']['channelId'])
    #if video['snippet']['channelId'] == "UC0C-w0YjGpqDXGB8IHb662A":
     #   print(video['snippet']['title'])

#pprint.pprint(videos[a])
print(lens)
print(tipos)
print(idChannel)

for i in tipos:
    print("{} - {} - {}".format(i, convert_duration(i), dur_category(i)))

arqout = open("saida_completa/ed_dataset_complete.json", 'w')

arqout.write(json.dumps(videos))
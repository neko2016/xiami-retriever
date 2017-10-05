import requests
import lxml
import json
from bs4 import BeautifulSoup

lib = "http://www.xiami.com/space/lib-song/u/322716/page/"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"}
baseURI = "http://www.xiami.com/song/playlist/id/"
mySongs = []

for n in range(1,101):
    page = lib + str(n)
    r = requests.get(page, headers = header)
    contents = r.content
    soup = BeautifulSoup(contents,"html.parser")
    tracks = soup.find_all("td", class_="song_name")
    
    for i in range(len(tracks)):
        record = dict();
        song = tracks[i].a.get_text()
        songId = tracks[i].parent["id"][9:]

        singers = ""
        ppl = tracks[i].find_all("a", class_="artist_name")
        for a in range(len(ppl)):
            if (a != len(ppl)-1):
                singers += ppl[a].get_text() + "; "
            else:
                singers += ppl[a].get_text()

        record["song_name"] = song
        record["song_id"] = songId
        record["singer_name"] = singers

        songURI = baseURI + songId
        xmlRq = requests.get(songURI, headers = header)
        metaContents = xmlRq.content
        xmlSoup = BeautifulSoup(metaContents, "xml")

        if not (xmlSoup.playlist == None):
            print("parsing data for", songId)
            #  data = xmlSoup.find_all(["songName","albumId","album_name","artistId","artist_name","albumLanguage"])
            data = xmlSoup.find_all(["album_id","album_name", "artist_id","artist_name"])

            for j in range(len(data)):
                key = data[j].name
                value = data[j].get_text()
                record[key] = value
            mySongs.append(record)
        else:
            print("No data for song_id", songId)
            mySongs.append(record)

print(len(mySongs))

jmySongs = json.dumps(mySongs)
print(jmySongs)

# todo: export jmySongs into csv 
from bs4 import BeautifulSoup
#import urllib.request
import urllib2

def get_links(num=0):
    url = "http://www.hotnewhiphop.com/songs/latest/{}".format(num)

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    allGridItems = soup.find_all('a', {'class': 'cover-title grid-item-title'})

    items = [str(item) for item in allGridItems]

    list = []

    for item in items:
        start = item.index("href=") + 6
        end = item.index(".html") + 5
        list.append("http://www.hotnewhiphop.com" + item[start:end])

    #print(list)
    return list


def stripInfo(soup):
    soup = str(soup)
    start = soup.index(">") + 1
    end = soup.index("<", start)
    return soup[start:end]

def getInfo(url='https://www.hotnewhiphop.com/e-40-straight-out-the-dirt-feat-youngboy-never-broke-again-and-yo-gotti-new-song.1975539.html'):
    page = urllib2.urlopen(url)

    soup = BeautifulSoup(page, "html.parser")

    allGridItems = soup.find_all('iframe', {'id': 'soundcloud_player'})
    items = [str(item) for item in allGridItems]

    for item in items:
        start = item.index("src=")+5
        end = item.index("&amp",start)
        if "secret_token" in item[start:end]:
            return None
        else:
            sclink = item[start:end]
            songTitle = soup.find_all('span', {'class': 'song-info-title'})
            songTitle = stripInfo(songTitle)
            songArtist = soup.find_all('a', {'class': 'song-artist-main'})
            songArtist = stripInfo(songArtist)
            songFeatures = soup.find_all('a', {'class': 'song-feature-link'})
            feat=[]
            for f in songFeatures:
                feat.append(stripInfo(f))

            return (sclink, songTitle,songArtist," & ".join(feat))


def get_songs(page=0):
    songs = []
    links = get_links(page)

    for link in links:
        s = getInfo(link)
        if s:
            songs.append(s)

    return songs

#tokenURL = 'https://www.hotnewhiphop.com/choo-jackson-and-rob-stone-connect-on-talk-new-song.1975554.html'
#url='https://www.hotnewhiphop.com/e-40-straight-out-the-dirt-feat-youngboy-never-broke-again-and-yo-gotti-new-song.1975539.html'

#print(get_songs())






    #page = urllib.open(url)
    #page = urllib2.urlopen(url)



    # links = list()
    #
    # for item in items:
    #     now = str(item)
    #     start = now.index("href=") + 6
    #     end = now.index('"', start)
    #     links.append("http://www.hotnewhiphop.com" + now[start:end])
    #
    # soundLinks = list()
    # notFound = list()
    # meta = list()
    #
    # for link in links:
    #     web = link
    #     site = urllib2.urlopen(web)
    #     soup = BeautifulSoup(site.read(), "html.parser")
    #     sound = str(soup.find("iframe"))
    #     lstart = sound.find("https://soundcloud.com/")
    #     if (lstart == -1):
    #         # soundLinks.append("CANNOT FIND: " + link)
    #         notFound.append("CANNOT FIND: " + link)
    #     else:
    #         lend = sound.find("&amp;", lstart)
    #         sclink = "https://w.soundcloud.com/player/?url=" + sound[lstart:lend]
    #         soundLinks.append(sclink)
    #         heading = str(soup.find_all('h1', {'class': 'audioContent-title'}))
    #         start = heading.find('>') + 3
    #         end = heading.find('</h1>', start)
    #         info = heading[start:end].strip().replace('&amp;', '&').replace('</h1>', '').split(" - ")
    #         meta.append({'artist': info[0], 'title': info[1], 'link': sclink})
    #
    # upToDate = False
    # already = Latest.query()
    # for each in already:
    #     mod = each.date_modified
    #     if (mod == datetime.datetime.now().date()):
    #         upToDate = True
    #         break
    #
    # if (not upToDate):
    #     linkStore = Latest(songs=meta, date_modified=datetime.datetime.now().date())
    #     linkStore.put()
    # else:
    #     ret = Latest.query().order(-Latest.date_modified).get()
    #     ret.songs = meta
    #     ret.put()
import argparse
import logging

import requests
from bs4 import BeautifulSoup 

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    return parser.parse_args()

def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

def artist(source):
    artist = dict()
    response = requests.get(source)
    soup = BeautifulSoup(response.content, "lxml")
    track=soup.find('table', {'class':'tracklist'})
    headings =track.find_all('h3')
    for heading in headings[:6]:
        artist[heading.text] = heading.a['href']
        
    return artist

def get_song_list(url):
    song = dict()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    track=soup.find('table', {'class':'tracklist'})
    links =track.find_all('a')
    for link in links[0:6]:
        song[link.text] = link['href']

    return song


def song_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    paragraph=soup.find('p', {'id':'songLyricsDiv'})
    return paragraph.text



def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    
    source= 'http://www.songlyrics.com/top-artists-lyrics.html'
    artists = artist(source)
#    print('meh', list(artists.values())[0])
    song_list = get_song_list(list(artists.values())[0])
    song = song_lyrics(list(song_list.values())[0])
    print(song)
#    song_lyric=artists
    # print('meh', artist_play_list)
  

if __name__ == "__main__":
    main()
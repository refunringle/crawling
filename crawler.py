import argparse
import logging

import requests
from bs4 import BeautifulSoup

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    return parser.parse_args()

def configure_logging(level= logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler =logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

def get_artists_name(base):
    resp =requests.get(base)
    soup = BeautifulSoup(resp.content,"lxml")
    trackl_ists = soup.find("table", attrs= {"class": "tracklist"})
    track_link = trackl_ists.find_all('a')
    for link in track_link:
        if link.find('img') not in link:
            print("artists name:",link.text) 

def get_songs(artists_name):
    resp = requests.get(artists_name)
    soup = BeautifulSoup(resp.content,'lxml')
    songs = soup.find("table", attrs= {"class": "tracklist"})
    song_link = songs.find_all('a')
    for songs in song_link:
        if songs.find('img') not in songs:
            print(songs.text)

def get_song_lyrics(song):
    resp = requests.get(song)
    soup = BeautifulSoup(resp.content,'lxml')
    lyrics = soup.find("p",attrs = {"id": "songLyricsDiv"})
    print(lyrics.text)


def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)

    get_artists_name("http://www.songlyrics.com/top-artists-lyrics.html")
    get_songs("http://www.songlyrics.com/hillsong-lyrics/")
    get_song_lyrics("http://www.songlyrics.com/hillsong/oceans-where-feet-may-fail-lyrics/")


if __name__ == "__main__":
    main()
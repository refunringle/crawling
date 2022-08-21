import argparse
import logging

import requests
from bs4 import BeautifulSoup 

import db

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    parser.add_argument("--db", help="Name of database to use", action="store", default="lyrics")
    subcommands = parser.add_subparsers(help="Commands", dest="command", required=True)
    subcommands.add_parser("initdb", help="Initialise the database")
    subcommands.add_parser("crawl", help="Perform a crawl")
    subcommands.add_parser("web", help="Start web server")
    
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

def artist(url_address):
    artist = dict()
    response = requests.get(url_address)
    soup = BeautifulSoup(response.content, "lxml")
    track=soup.find('table', {'class':'tracklist'})
    headings =track.find_all('h3')
    for heading in headings[:5]:
        artist[heading.text] = heading.a['href']
        
    return artist

def get_songs_list(url):
    songs = dict()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    track=soup.find('table', {'class':'tracklist'})
    links =track.find_all('a')
    for link in links[:5]:
        songs[link.text] = link['href']

    return songs


def song_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    paragraph=soup.find('p', {'id':'songLyricsDiv'})
    return paragraph.text

def create_tables(db_name):
    conn = db.get_connection(db_name)
    with conn.cursor() as cursor:
        with open("init.sql") as f:
            sql = f.read()
            cursor.execute(sql)
    conn.commit()
    conn.close()

def insert_data_to_database(url):
    for artist_name, artist_url in artist(url).items():
        artist_id = db.add_artist(artist_name)
        for songs, song_url in get_songs_list(artist_url).items():
            lyrics = song_lyrics(song_url)
            db.add_song(songs, artist_id, lyrics)


def main():
    args = parse_args()
    url_address= 'http://www.songlyrics.com/top-artists-lyrics.html'

    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)

    if args.command == "crawl":
        logger.info("Crawling")
        artists = artist(url_address)
        song_list = get_songs_list(list(artists.values())[0])
        songs = song_lyrics(list(song_list.values())[0])
        print(songs)
    
    elif args.command == "initdb":
        logger.info("Initialising database")
        create_tables(args.db)
        insert_data_to_database(url_address)
    else:
        logger.warning("%s not implemented", args.command)

if __name__ == "__main__":
    main()
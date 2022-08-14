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

def crawl(source):
    response = requests.get(source)
    soup = BeautifulSoup(response.content)
    track=soup.find('table', {'class':'tracklist'})
    headings =track.find_all('h3')
    for heading in headings:
        print(heading.text)
        print(heading.a)

    logger.debug("Crawling starting")
    for i in range(4):
        logger.debug("Fetching URL %s", i)
        print ("https://....")
    logger.debug("Completed crawling")

def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    logger.debug("Here's a debug message")
    logger.info("Here's an info message!")
    logger.warning("Here's an warning message!")
    logger.critical("Here's an critical message!")
    crawl('http://www.songlyrics.com/top-artists-lyrics.html')

if __name__ == "__main__":
    main()
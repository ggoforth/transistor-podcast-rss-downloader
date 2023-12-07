# Transistor.fm Podcast Downloader

This Python script is designed to download podcasts from a Transistor.fm RSS 
feed URL. It fetches podcast data, downloads MP3 files, and saves pertinent 
details about each podcast in text and JSON formats.  I used it to download all 
my podcast episodes for archival.  

## Features

- Fetches podcast data from an RSS feed.
- Downloads podcast episodes in MP3 format.
- Creates a dedicated folder for each podcast episode.
- Saves podcast details such as title, publication date, link, and description in a text file.
- Stores complete podcast entry data in a JSON file.

## Requirements

- Python 3.x
- External Libraries:
  - `requests` for handling HTTP requests.
  - `feedparser` for parsing the RSS feed.
  
You can install these libraries using the following command:

```bash
pip install requests feedparser

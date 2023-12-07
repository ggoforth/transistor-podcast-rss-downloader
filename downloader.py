import requests
import os
import feedparser
import sys

if len(sys.argv) > 1:
    rss_feed_url = sys.argv[1]
else:
    rss_feed_url = input("Enter the podcast RSS feed URL: ")

feed = feedparser.parse(rss_feed_url)

podcast_directory = "podcasts"
os.makedirs(podcast_directory, exist_ok=True)

print(f"Downloading {feed.feed.title}!")
print(f"Fetching {len(feed.entries)} podcast episodes...")

for idx, entry in enumerate(feed.entries):
    # calculate the percentage complete
    percentage = (idx / len(feed.entries)) * 100
    print(f"\r{percentage:.0f}% complete", end="", flush=True)

    podcast_folder = f"{podcast_directory}/{entry.title}"
    os.makedirs(podcast_folder, exist_ok=True)
    mp3 = entry.enclosures[0].href

    # download the mp3, and save it into podcast_folder
    response = requests.get(mp3)
    filename = mp3.split("/")[-1]
    with open(f"{podcast_folder}/{filename}", "wb") as f:
        f.write(response.content)

    # now save a text file with all the other pertinent details like
    # title, published, link, description, id and save it in the same folder
    with open(f"{podcast_folder}/info.txt", "w") as f:
        f.write(f"Title: {entry.title}\n")
        f.write(f"Published: {entry.published}\n")
        f.write(f"Link: {entry.link}\n")
        f.write(f"Description: {entry.description}\n")
        f.write(f"ID: {entry.id}\n")

    # finally save the entry into a file with the same name as the mp3 file but with a .json extension
    with open(f"{podcast_folder}/{filename}.json", "w") as f:
        # replace all single quotes with double quotes
        entry = str(entry).replace("'", '"')

        # replace all None with ""
        entry = entry.replace("None", '""')

        # replace all True with true and False with false
        entry = entry.replace("True", "true")
        entry = entry.replace("False", "false")

        f.write(entry)

    # if the percentage is 100, then we are done
    print(f"\r100% complete", end="", flush=True)

print()
print("Done!")
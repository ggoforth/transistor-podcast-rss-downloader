import requests
import os
import feedparser


rss_feed_url = "https://feeds.transistor.fm/just-the-facts-and-that-is-that"
feed = feedparser.parse(rss_feed_url)

podcast_directory = "podcasts"
os.makedirs(podcast_directory, exist_ok=True)

print("Fetching podcast feed...")

for idx, entry in enumerate(feed.entries):
    print(f"Downloading episode {idx + 1} of {len(feed.entries)}...", end="", flush=True)

    # calculate the percentage complete
    percentage = (idx / len(feed.entries)) * 100

    # print the percentage complete
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

    print(".", end="", flush=True)

print()
print("Done!")
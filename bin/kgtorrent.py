import requests
import os

if os.getenv("ACCESS_TOKEN"):

    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
else:
    print("kgtorrent:ERROR:ACCESS_TOKEN not found.")
    quit()

RECORD_ID = "4468523"
RECORD_FILE = "files/KT_dataset.tar.bz2/content"

r = requests.get(
    f"https://zenodo.org/api/records/{RECORD_ID}/{RECORD_FILE}",
    params={'access_token': ACCESS_TOKEN}
)
download_urls = [f['links']['self'] for f in r.json()['files']]
filenames = [f['key'] for f in r.json()['files']]

for filename, url in zip(filenames, download_urls):
    print("Downloading:", filename)
    r = requests.get(url, params={'access_token': ACCESS_TOKEN})
    with open(filename, 'wb') as f:
        f.write(r.content)

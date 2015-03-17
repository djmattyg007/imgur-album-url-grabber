#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    raise Exception("No URL supplied")

gallery_url = sys.argv[1]

response = requests.get(gallery_url)
soup = BeautifulSoup(response.text)
image_container = soup.find(id="image-container")
images = image_container.select(".album-view-image-link > a")

for image in images:
    print("http:" + image["href"])

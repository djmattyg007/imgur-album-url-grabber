Imgur album URL grabber

Gets all URLs for all images in an imgur album.
It uses requests and Beautiful Soup to do the heavy lifting.

Usage:

python3 get_album_urls.py http://imgur.com/a/Y5MHe

This outputs URLs to stdout. It's then very simple to download all of these
URLs one by one with a shell script:

for url in `cat urls.txt`; do
    echo $url
    wget $url
done

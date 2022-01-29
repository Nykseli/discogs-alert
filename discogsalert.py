#!/usr/bin/env python3

import os
import json
import time
import urllib.request

# No need to spam so many quotes :)
url = "url"
name = "name"

# Add your list of albums here
# The example is currenlty found so remove to avoid notificaion spam
ALBUMS = [
    {
        name: "Eppu vinyl",
        url: "https://www.discogs.com/release/3356020-Eppu-Normaali-Kahdeksas-Ihme"
    }
]

# By default this will check the albums once every hour.
# Please be nice to the discogs servers
TIMEOUT_SECONDS = 3600

class AlbumInfo:
    name = ""
    url = ""
    html = ""
    orderable = False

    def __init__(self, data: object):
        """
        data: {
            # descriptive name. can be anything
            name: string,
            # discogs url to the album
            url: string
        }
        """
        self.url = data[url]
        self.name = data[name]
        self.html = ""
        self.orderable = False

    def fetch_data(self):
        req = urllib.request.Request(
            self.url,
            data=None,
            # We have to fake the User-Agent or we get 403 responce
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        try:
            with urllib.request.urlopen(req) as html:
                self.html = html.read().decode('utf-8')
        except err:
            print(err)


    def can_order(self) -> bool:
        self.orderable = False

        # When album is not found, discogs recommends searching if from the market place
        if "Search for" not in self.html:
            self.orderable = True

        return self.orderable

    def to_json(self) -> object:
        return {
            "url": self.url,
            "name": self.name,
            "orderable": self.orderable,
        }

    def to_json_str(self) -> str:
        return json.dumps(self.to_json())

    def notify_user(self):
        title = "'Discogs album has been found'"
        message = f"'{self.name} is now available'"
        os.system(f"termux-notification -t {title} -c {message} --priority high")

while True:
    for album in ALBUMS:
        info = AlbumInfo(album)
        info.fetch_data()
        if info.can_order():
            info.notify_user()

    time.sleep(TIMEOUT_SECONDS)

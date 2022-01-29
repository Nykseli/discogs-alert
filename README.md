# Discogs Alert

Simple python script to check if albums are available on discogs

## How to use

Install [termux](https://play.google.com/store/apps/details?id=com.termux) and [termux api](https://play.google.com/store/apps/details?id=com.termux.api) on your android phone

In termux install the api package

```
pkg install termux-api
```

Then you can download the script

```
curl "https://raw.githubusercontent.com/Nykseli/discogs-alert/main/discogsalert.py" > discogsalert.py
```

Set the albums you want to watch inside the python script

```python
ALBUMS = [
    {
        name: "foo album",
        url: "https://www.discogs.com/ etc"
    }
]

```

And then run the script and wait for the notifications!

```
python3 discogsalert.py &
```

Note that the script will stop working if you close the termux app

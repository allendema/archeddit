# archeddit
Save posts from Reddit locally. Forever.

This Python code uses the APIs from [Teddit](https://codeberg.org/teddit/teddit/) instances to get the media URLs and Titles.

It then uses the URL it found to download the media, which are hosted by Reddit Inc. 

## Saving this locally
```bash
$ git clone https://github.com/allendema/archeddit.git
$ pip3 install -r requirements.txt
```

## Run it
```bash
$ cd archeddit # Changing to this directory.
$ chmod +x archeddit.py # Make the script executable.
$ ./archeddit.py # Running the script.
```
## Use it
Just enter one public Subreddit.
It saves the media in a Folder with the name of given sub.

Use cases include downloading top [/r/wallpapers](https://teddit.net/r/wallpapers/) or [/r/pizza](https://teddit.net/r/pizza) weekly posts.

## Heads Up
Made by exploring Python. Inspired by similiar programms. Use at own risk.
Teddit instances are choosen randomly to better load-balance.
Keep in mind that they are community run.

## Use it to archive important things, be polite and cause no harm.

## Bonus Information
Depending on changes Reddit Inc. makes, they might or might not block your IP.

Has not happend 'till now.

Soon on [Codeberg.org](https://codeberg.org/explore/) too.

Allen 2021


[![License: GNU - GPL 3.0](https://img.shields.io/github/license/allendema/archeddit)](https://github.com/allendema/archeddit/blob/main/LICENSE)
[![github commits](https://img.shields.io/github/last-commit/allendema/archeddit)](https://github.com/allendema/archeddit/commits/main)
[![Lines of Code](https://img.shields.io/tokei/lines/github/allendema/archeddit?style=flat-square)](https://github.com/allendema/archeddit/blob/main/SnapScrap.py)


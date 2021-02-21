#!/usr/bin/python3

from bs4 import BeautifulSoup
from random import choice
import requests
import json
import os

url = ["https://teddit.net/r/", "https://teddit.zaggy.nl/r/", "https://teddit.namazso.eu/r/"]

query = input("Type the Subreddit you want: ")

path = query

try:
	os.mkdir(path)
except FileExistsError:
	print("Great, this Subreddit already has a folder in your System.")

os.chdir(path)


mix = (choice(url)) + str(query) + "?sort=top&t=week" + "&api&target=reddit" # hour, day, month, year, all 
print(mix, "\n")

headers = {
    'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
}

print(headers)


html = requests.get(mix, headers=headers)

if html.status_code == 200:
	print("Sucsess")
	
else:
	print("Nicht erfolgreich")


data = json.loads(html.text)



for i in data["data"]["children"]:
	
	url = i["data"]["url"]
	 
	x = url.endswith((".jpg" or ".png"))
	if x is True:
		file_url = url
		file_description = i["data"]["title"]
		file_name = url.split('/')[-1]
		print(file_description, url)

		r = requests.get(file_url, stream=True)
			
		if r.status_code == 200:
			with open(file_name, 'wb') as f:
				for chunk in r:
					f.write(chunk)
				print(f"\033[33mGetting posts from:\033[33m r/{query}")
		else:
			print("Cannot make connection to download media!")
	else:
		print("Galleries cannot be downloaded ATM.")

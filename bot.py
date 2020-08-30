# twitter bot coded in python to post images  
# you need a developer account for this to work

import os
import time
import tweepy as tp

# important data from your account
account_key = "Put your account key here"
account_secret = "Put your account secret here"

access_token = "Put your access token here"
access_secret = "Put your account secret here"

# authenticate informations to use the api
authentication = tp.OAuthHandler(account_key, account_secret)
authentication.set_access_token(access_token, access_secret)
api = tp.API(authentication)

# iterate images from the directory created in scraping.py
os.chdir('directory_name')
for image in os.listdir('.'):
  api.update_with_media(image)
  time.sleep(100)



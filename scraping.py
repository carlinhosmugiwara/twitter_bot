# scraping for the twitter bot

import os
import requests as rqts
from bs4 import BeautifulSoup as btsp # library to do the actual scraping

# site that has the images that will be used
url = 'examplesite.com/images'

# parsing of the page
page = rqts.get('url')
soup = btsp(page.text, 'html.parser')

# find all image tag elements
img_tag = soup.findAll('img')

# create directory with these images
if not os.path.exists('name_dir'):
  os.makedirs('name_dir')

# navegate through the directory
os.chdir('name_dir')

# variable to name the images in a generic way
va = 0

# putting images in the directory
for img in img_tag:
  try:
    url = img[src']
    response = rqts.get(url)
    if response.status_code == 200:
      with(open('image_' + str(va) + '.png', 'wb') as f:
        f.write(rqts.get(url).content)
        va+=1
  except:
    pass

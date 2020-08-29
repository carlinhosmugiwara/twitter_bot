# scraping do bot de twitter/scraping for the twitter bot

import os
import requests as rqts
from bs4 import BeautifulSoup as btsp

# site com as imagens ques serão usadas/site that has the images that will be used
url = 'siteexemplo.com.br/imagens'

#fazer o parsing da página/parsing of the page
pagina = rqts.get('url')
soup = btsp(pagina.text, 'html.parser')

# agora localizar todos os elementos com a tag de imagem/find all image tag elements
img_tag = soup.findAll('img')

# criar diretório com imagens do site/create directory with these images
if not os.path.exists('nome_dir'):
  os.makedirs('nome_dir')

# entrar no diretório criado/navegate through the directory
os.chdir('nome_dir')

# variável para nomear de forma genérica as imagens/variable to name the images in a generic way
va = 0

# colocando imagens no diretório/putting images in the directory
for img in img_tag:
  try:
    url = img[src']
    resposta = rqts.get(url)
    if resposta.status_code == 200:
      with(open('imagem_' + str(va) + '.jpg', 'wb') as f:
        f.write(rqts.get(url).content)
        f.close()
        va+=1
   except:
    pass

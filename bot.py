# bot de twitter feito em python para postar imagens/twitter bot coded in python to post images  
# para que seu código rode, você deve primeiro criar uma conta developer no twitter/you need a developer account for this to work

import os
import time
import tweepy as tp

# dados importantes de sua conta developer/important data from your account
key_conta = "Coloque a chave de sua conta aqui"
secret_conta = "Coloque o secret de sua conta aqui"

token_acesso = "Insira o token de acesso aqui"
secret_acesso = "Insira o secret de acesso aqui"

#autenticar informações e usar api/authenticate informations to use the api
autenticacao = tp.OAuthHandler(key_conta, secret_conta)
autenticacao.set_access_token(token_acesso, secret_acesso)
api = tp.API(autenticacao)

#iterar imagens do diretório criada no scraping.py/iterate images from the directory created in scraping.py
os.chdir('nome_dir')
for imagem in os.listdir('.'):
  api.update_with_media(imagem)
  time.sleep(100)



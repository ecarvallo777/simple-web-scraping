import requests #Import library to request a url
from bs4 import BeautifulSoup
url = 'http://condor2.utalca.cl/pls/sgc/matico2_log.parciales?mRutE=0D71C41B4FE4348E&ip=B19C22CA11029E8945E2F348B79D029B&sesion=DE6DA2E18A639B70774C29CF476FAE1A&sistema=MATICO&mPra_codigo=3419'

response = requests.get(url) #Use method of requests to request url
soup = BeautifulSoup(response.text, 'lxml') #Convert response to an lxml text
print(soup)
import requests #Import library to request a url
from bs4 import BeautifulSoup
url = 'http://condor2.utalca.cl/pls/sgc/matico_log.ficha_alumno?mRutE=0D71C41B4FE4348E&ip=B19C22CA11029E8945E2F348B79D029B&sesion=DE6DA2E18A639B70828FA5834F797ED4&sistema=MATICO'

response = requests.get(url) #Use method of requests to request url
soup = BeautifulSoup(response.text, 'lxml') #Convert response to an lxml text
tables = soup.find_all('td', class_='tabladatosper', align='center')
print(soup) #This print all html document requested.
#print(tables) #This print find_all results with tag 'td' and class 'tabladatosper'

#for table in tables:
    #print(table.text) #Print only text of the tables, one for one with for loop.
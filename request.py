import requests #Import library to request a url
from bs4 import BeautifulSoup
url = 'http://condor2.utalca.cl/pls/sgc/matico2_log.parciales?mRutE=0D71C41B4FE4348E&ip=B19C22CA11029E8945E2F348B79D029B&sesion=DE6DA2E18A639B7082A20FE1850BD45F&sistema=MATICO&mPra_codigo=3419'

response = requests.get(url) #Use method of requests to request url
soup = BeautifulSoup(response.text, 'lxml') #Convert response to an lxml text
items = soup.find('table', width="100%", border="0", cellpadding="1", cellspacing="1")
tbody= items.find_all('tr')
count=0
for i in tbody:

    
    if count>0:
        if count==2 :
            ramo=i.find('td', class_="tabladatosper", height="19", valign="top").text
            teacher= i.find('td', align="left", class_="tabladatosper", valign="top").text
            nota= i.find('td', align="center", class_="tabladatosper", valign="top").text
            print(ramo+" "+teacher+" "+nota)
        else:
            ramo=i.find('a').text
            teacher= i.find('td', align="left", class_="tabladatosper", valign="top").text
            nota= i.find('td', align="center", class_="tabladatosper", valign="top").text
            print(ramo+" "+teacher+" "+nota)
    count+=1
#print(items)
#print(tbody)
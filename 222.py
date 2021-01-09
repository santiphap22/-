from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

url = "https://ddc.moph.go.th/viralpneumonia/"

webopen = req(url)
pange_html = webopen.read()
webopen.close()

#print(pange_html)
data = soup(pange_html,'html.parser')
#print(data)

temp = data.findAll('h4',{'class':'txt'})
temp2 = data.findAll('h4',{'class':'txt'})
result= temp[0].text
#only= temp2[0].text
print(result)

#print('ผู้ติดเชื้อสะสม: {} ผู้ติดเชื้อวันนี้: {}'.format(result,only))

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

url = "https://ddc.moph.go.th/viralpneumonia/"

webopen = req(url)
pange_html = webopen.read()
webopen.close()


data = soup(pange_html,'html.parser')

temp = data.findAll('h4',{'class':'txt'})
result= temp[0].text
result1= temp[1].text
result2= temp[2].text
result3= temp[3].text

print('ผู้ติดเชื้อสะสม: {} ผู้ติดเชื้อวันนี้: {} รุนแรง: {}: เสียชีวิต {}'.format(result,result1,result2,result3))

from songline import Sendline

token = 'clO63p0RQzYzYit1teVQvt6WNIRCvJnWZtWZ2x36xa0'
messenger = Sendline(token)
messenger.sendtext('ผู้ติดเชื้อสะสม: {}ผู้ติดเชื้อวันนี้: {} รุนแรง: {}: เสียชีวิต {}'.format(result,result1,result2,result3))

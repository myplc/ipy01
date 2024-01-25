import requests as req
from bs4 import BeautifulSoup as bs
web = req.get('https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do')
soup = bs(web.content,'html5lib')
date = soup.select('.menu-tbl .date')
day = soup.select('.menu-tbl .day')
won = soup.select('h3.menu-tit01')
menu = soup.select('h3.menu-tit01+p')
def bab(days='모두'):
    list=''
    for y,d,w,m in zip(date,day,won,menu):
        if days in ['모두',d.text]:
            list+='-'*15 +'\n'
            list+=f'{y.text} ({d.text})\n'
            list+='-'*15 +'\n'  
            list+=w.text +'\n'
            list+=m.text
        else:pass
    return list
if __name__=='__main__':
    inp = input('원하는 요일을 입력하세요. 전체 요일을 원할 때는 \'모두\'를 입력하세요')
    print(bab(inp))
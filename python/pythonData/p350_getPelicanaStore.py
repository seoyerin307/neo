from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'pelicana'
base_url = 'http://www.pelicana.co.kr/store_search.html'

def getData():
    saveData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        print(url)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('div', attrs={'class': 'info_box'})
        # mytable = mytable.find

print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 완료')


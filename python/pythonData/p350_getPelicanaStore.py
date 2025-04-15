from itertools import count
from p340_ChichkenUtil import ChickenStore

brandName = 'pelicana'
base_url = 'http://www.pelicana.co.kr/store_search.html'

def getData():
    saveData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        print(url)

print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 완료')


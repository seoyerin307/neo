from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'cheogajip'
base_url = 'http://www.cheogajip.co.kr/bbs/board.php'

def getData():
    saveData = []

    for page_idx in count():
        if page_idx >= 127:
            ChickenStore.save2Csv(saveData)
            break
        else:
            url = base_url
            url += '?bo_table=store'
            url += '&page=' + str(page_idx + 1)
            print(url)

    print(brandName + ' 매장 크롤링 시작')
    getData()
    print(brandName + ' 매장 크롤링 완료')
        



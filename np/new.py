import urllib.request
import urllib.parse
import json
import html

client_id = "bCovPC7wNjEApG0cQfSl"
client_secret = "4rVLgMBI4Z"

query = "미국증시"
enc_query = urllib.parse.quote(query)
display = 100

url = f"https://openapi.naver.com/v1/search/news.json?query={enc_query}&display={display}"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

try:
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')
    result = json.loads(response_body)

    for item in result['items']:
        title = html.unescape(item['title'])  # HTML 태그 제거
        link = item['link']
        originallink = item.get('originallink', '원본 링크 없음')
        description = html.unescape(item['description'])  # HTML 태그 제거
        pubDate = item['pubDate']

        print(f"📌 제목: {title}")
        print(f"🔗 링크: {link}")
        print(f"📰 출처 원본 링크: {originallink}")
        print(f"📝 요약: {description}")
        print(f"📅 게시일: {pubDate}")
        print("-" * 100)

except urllib.error.HTTPError as e:
    print(f"❌ HTTPError: {e.code} - {e.reason}")
    print(e.read().decode())
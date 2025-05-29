import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

contents_url = "https://www.khan.co.kr/culture/culture-general/article/202212310830021"
api_url = "https://kagi.com/api/v0/summarize"
headers = {"Authorization": "Bot " + KAGI_API_KEY}
parameters = {"url": contents_url, "target_language": "KO"}

response = requests.get(api_url, headers=headers, params=parameters)

summary = response.json()['data']['output']
shorted_summary = textwrap.shorten(summary, width=100, placeholder="[이하 생략]")
print("- 요약 내용(축약) : ", shorted_summary)
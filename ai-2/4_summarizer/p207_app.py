import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

engines = ['cecil','agnes','daphne','muriel']

api_url = "https://kagi.com/api/v0/summarize"
contents_url = "https://www.hankookilbo.com/News/Read/A2025053009510003758"
headers = {"Authorization": "Bot " + KAGI_API_KEY}

for engine in engines:
  parameters = {"url": contents_url, "engine":engine, "target_language": "KO"}

  response = requests.get(api_url, headers=headers, params=parameters)

  data = response.json().get('data')
  summary = data['output']
  shorted_summary = textwrap.shorten(summary, width=150, placeholder="[…이하 생략…]")
  print("- 요약 엔진 : " , engine)
  print("- 요약 내용(축약) : ", shorted_summary)
  print("-"*50)

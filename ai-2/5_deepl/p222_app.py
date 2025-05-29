import deepl
import os

auth_key = os.environ.get('DEEPL_API_KEY')
translator = deepl.Translator(auth_key)

text = "Improve your writeing in just one clinck"
result = translator.translate_text(
    text,
    target_lang="KO"
)

print("- 감지된 언어 코드 : ", result.detected_source_lang)
print("- 변환된 텍스트 : ", result.text)
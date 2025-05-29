import deepl
import os

auth_key = os.environ.get('DEEPL_API_KEY')
translator = deepl.Translator(auth_key)

input_path = './data/어린왕자_영어_원본.docx'
output_path = './data/어린왕자_영어_변환.docx'

result = translator.translate_document_from_filepath(
    input_path,
    output_path,
    target_lang="KO"
)

print(result.done)
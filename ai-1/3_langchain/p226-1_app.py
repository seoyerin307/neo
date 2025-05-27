from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.chat_models import ChatOpenAI  # ✅ 필수 import
from langchain.schema import HumanMessage

# 예시 데이터
examples = [
    {"input": "明るい", "output": "暗い"},
    {"input": "おもしろい", "output": "つまらない"},
]

# 예시 포맷 정의
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="入力: {input}\n出力: {output}",
)

# 프롬프트 템플릿 구성
prompt_from_string_examples = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="모든 입력에 대한 반의어를 입력하세요.",
    suffix="입력 : {adjective}\n출력 : ",
    input_variables=["adjective"],
    example_separator="\n\n",
)

# '큰'이라는 단어에 대한 프롬프트 생성
prompt = prompt_from_string_examples.format(adjective="큰")
print("생성된 프롬프트:\n")
print(prompt)

# LLM 호출
chat_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
response = chat_llm([HumanMessage(content=prompt)])

# 결과 출력
print("\n출력:")
print(response.content)
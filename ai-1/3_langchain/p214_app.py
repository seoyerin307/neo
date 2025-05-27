from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)

Chat_llm=ChatOpenAI(
    model = 'gpt-3.5-turbo-instruct',
    temperature = 0,
)

message = [
    HumanMessage(content="고양이의 울음 소리는?"),
]
print('-' * 50)
print(result)

message_list = [
    [HumanMessage(content="고양이의 울음 소리는?")]
    [HumanMessage(content="까마귀 울음 소리는?")]
]
print('-' * 50)
result = chat_llm.generate(messages_list)
print("result 0 : ", result.generations[0][0].text)
print("result 1 : ", result.generations[1][0].text)
print("llm output : ", result.llm_output)
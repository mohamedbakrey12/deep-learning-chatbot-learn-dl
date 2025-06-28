from langchain.chat_models import ChatOpenAI
import os

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    model="nous-hermes-2-mixtral",
    temperature=0.1
)

response = llm.invoke("من هو النبي محمد؟")
print(response.content)

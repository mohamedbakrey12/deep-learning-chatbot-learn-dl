# llm/llm_config.py

from langchain_community.llms import OpenRouter
import os

def load_llm():
    """
    تحميل نموذج توليدي من OpenRouter (يدعم اللغة العربية)
    تأكد من وضع مفتاح API في المتغير البيئي: OPENROUTER_API_KEY
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("❌ لم يتم العثور على مفتاح OpenRouter. الرجاء إضافته إلى المتغيرات البيئية.")

    llm = OpenRouter(
        model="nous-hermes-2-mixtral",  # يمكنك تغييره لنموذج آخر يدعم العربية
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    return llm

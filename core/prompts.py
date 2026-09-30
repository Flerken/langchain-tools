from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableLambda


currency_prompt_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file('./prompts/convert_current.txt', []),
    HumanMessagePromptTemplate.from_template("{text}")
])

def currency_prompt_func(input_dict: dict):
    return currency_prompt_template.format_messages(**input_dict)

currency_prompt = RunnableLambda(currency_prompt_func)


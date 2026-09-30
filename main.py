from locale import currency

from core.chains import currency_chain
from tools.tools import convert_currency
from core.prompts import currency_prompt_template
from langchain_core.messages import ToolMessage
from core.models import currency_model
from core.callback import BaseCallback, ErrorHandler
from random import choice

text = input("Что конвертируем: ")

result = currency_chain.invoke({"text": text})

tool_message = []

#print(result)

tool_calls = result.tool_calls

if tool_calls:
    for tool_call in tool_calls:
        if tool_call["name"] == "convert_currency":
            output = convert_currency.invoke(tool_call["args"])
            tool_message.append(ToolMessage(tool_call_id=tool_call["id"], content=output))
    messages = currency_prompt_template.format_messages(text=text)
    messages += [result]
    messages += tool_message

    final_result = currency_model.invoke(messages)
else:
    print(result.text)

print(messages)
print(final_result.text)
#recipes = recipe_chain.invoke({ "dish" : dishes[0], "price" : 300 }, config={"callbacks": [BaseCallback()]})
#
##recipes = recipe_chain.batch([{ "dish" : d, "price" : 300 } for d in dishes])
##
##
#print(f"{recipes}")
#
#recipes = zip(dishes, recipes)
#
#for name, recipe in recipes:
#    with open(f"./recipes/{name}.txt", "w") as f:
#        f.write(recipe)

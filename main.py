from locale import currency

from core.chains import currency_chain
from tools.tools import convert_currency
from core.callback import BaseCallback, ErrorHandler
from random import choice

text = input("Что конвертируем: ")
result = currency_chain.invoke({"text": text})

print(result)

tool_calls = result.tool_calls

if tool_calls:
    for tool_call in tool_calls:
        if tool_call["name"] == "convert_currency":
            output = convert_currency.invoke(tool_call["args"])
            print(output)
    pass
else:
    print(result.text)
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

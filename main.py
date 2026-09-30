from core.chains import dishes_chain, recipe_chain
from core.callback import BaseCallback, ErrorHandler
from random import choice

text = input("Для чего предложить блюдо: ")
dishes = dishes_chain.invoke({"text": text}, config={"callbacks": [ErrorHandler()]})

print(dishes)
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

from random import choice
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage
from shemas.choice import GeneratedMenu, GeneratedRecipe

def sort_dishes_func(menu: GeneratedMenu | AIMessage):
    #if isinstance(menu, GeneratedMenu):
    #    dishes = menu.dishes
    #else:
    #    dishes = [menu.content]
    #raise ValueError("Ошибка сортировки")
    return sorted(menu.dishes)

sort_dishes = RunnableLambda(sort_dishes_func)

def make_markdown_func(recipe: GeneratedRecipe):

    md = f"\n# Готовим {recipe.name}#"
    md += f"\n\n##Ингредиенты\n"

    for i, ingredient in enumerate(recipe.ingredients, start=1):
        md += f"\n{i}. {ingredient}"

    md += f"\n\n##Рецепт\n"

    for i, step in enumerate(recipe.steps, start=1):
        md += f"\n{i}. {step}"

    return md

make_markdown = RunnableLambda(make_markdown_func)

def random_dish_func(dishes: list):
    return choice(dishes)

random_dish = RunnableLambda(random_dish_func)

dish_to_dict = RunnableLambda(lambda dish_srt: {"dish": dish_srt})
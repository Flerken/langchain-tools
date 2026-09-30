from langchain_core.runnables import Runnable, RunnableLambda

from core.models import gigachat_model, yandex_model, choice_model, recipe_model, choice_model_fallback
from core.prompts import choice_template, choice_prompt, chef_template, chef_prompt
from core.parsers import sort_dishes, make_markdown, random_dish, dish_to_dict
from gigachat.exceptions import BadRequestError


def get_dishes_chain(llm):
    return choice_prompt | llm | sort_dishes

dishes_chain = get_dishes_chain(choice_model)
dishes_chain_fallback = get_dishes_chain(choice_model_fallback)
emergency_dishes_chain = RunnableLambda(lambda i: ["Хлеб с маслом"])

dishes_chain = dishes_chain.with_fallbacks(
    fallbacks=[emergency_dishes_chain],
    exceptions_to_handle=[Exception]
)

recipe_chain = (chef_prompt | recipe_model | make_markdown)


super_chain = dishes_chain | random_dish | dish_to_dict | recipe_chain
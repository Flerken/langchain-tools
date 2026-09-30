from langchain_core.runnables import Runnable, RunnableLambda
from langchain_core.output_parsers import JsonOutputToolsParser, JsonOutputKeyToolsParser

from core.models import gigachat_model, yandex_model, currency_model
from core.prompts import currency_prompt

from core.parsers import sort_dishes, make_markdown, random_dish, dish_to_dict
from gigachat.exceptions import BadRequestError

tools_parser = JsonOutputKeyToolsParser(first_tool_only=True, return_id=True, strict=True, key_name="convert_currency")

currency_chain = currency_prompt | currency_model | tools_parser

#dishes_chain = dishes_chain.with_fallbacks(
#    fallbacks=[emergency_dishes_chain],
#    exceptions_to_handle=[Exception]
#)
#
#recipe_chain = (chef_prompt | recipe_model | make_markdown)
#
#
#super_chain = dishes_chain | random_dish | dish_to_dict | recipe_chain
import httpx
from  langchain_core.tools import tool, BaseTool
from pydantic import BaseModel, Field
from typing import Type
from tools.shemas import ConvertCurrencyArgs


class ConvertCurrencyTool(BaseTool):
    name: str = "convert_currency"
    description: str = "Конвертирует заданную сумму из одной валюты в другую по актуальному курсу."
    args_schema: Type[BaseModel] = ConvertCurrencyArgs


    client: httpx.Client = Field(exclude=True) #Спрятанное поле только для метода

    def _run(self, amount: float, from_currency: str, to_currency: str) -> float| str:
        """
        Конвертирует заданную сумму из одной валюты в другую по актуальному курсу.
        """
        print("convert_currency")
        try:
            response = self.client.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        except (httpx.ConnectError, httpx.ConnectTimeout) as e:
            return "Ошибка соединения c сервисом"

        rate = response.json()["rates"][to_currency]
        result = amount * rate
        return round(result, 2)

client = httpx.Client()
convert_currency_tool = ConvertCurrencyTool(client=client)

@tool()
def iphone_price() -> float:
    """
    Возращает стоймость одного iPhone в рублях
    """
    print("iphone_price")
    return 85_000.00

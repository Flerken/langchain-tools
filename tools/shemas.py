from pydantic import BaseModel, ConfigDict, field_validator, Field


class ConvertCurrencyArgs(BaseModel):
    amount: float = Field(description="Сумма для конвертации.")
    from_currency : str = Field(min_length=3, max_length=3, description="Трехбуквенный код исходной валюты в стандарте ISO 4217 (например, 'USD', 'EUR', 'RUB')")
    to_currency: str = Field(min_length=3, max_length=3,
                               description="Трехбуквенный код целевой валюты в стандарте ISO 4217 (например, 'USD', 'EUR', 'RUB')")

    model_config = ConfigDict(str_strip_whitespace=True) #str_strip_whitespace Удаляет пробелы


    @field_validator('from_currency', 'to_currency')
    @classmethod
    def upper_code(cls, value) -> str:
        return value.upper()
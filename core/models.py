# Импортируем модель GigaChat из библиотеки LangChain для отправки и получения сообщений через API GigaChat
from random import choices
from typing import Tuple

from langchain_core.language_models import fake_chat_models
# Базовый класс для тестов и аварийных ситуаций
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.runnables import RunnableLambda
from langchain_gigachat.chat_models import GigaChat
# Импортируем модель GigaChat из библиотеки LangChain для отправки и получения сообщений через API GigaChat
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.chat_models.base import OpenAIAuthenticationError
from openai import AuthenticationError, APIError  # общий класс
from gigachat.exceptions import BadRequestError

from core.config import settings
#from shemas.choice import GeneratedMenu, GeneratedRecipe
from tools.tools import convert_currency

# Инициализация объекта GigaChat
gigachat_model = GigaChat(
    model=settings.GIGACHAT_CHAT_MODEL, # Можно явно задать модель GigaChat (по умолчанию запросы передаются в модель GigaChat Lite, поэтому для теста строка закоментирована).
    credentials=settings.GIGACHAT_CREDENTIALS, # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    scope=settings.GIGACHAT_SCOPE, # Область использования API (по умолчанию GIGACHAT_API_PERS для физ. лиц)
    verify_ssl_certs=settings.GIGACHAT_VERIFY_SSL, # Проверка сертификата, для учебных задач можно отключить, но для производственных средств его необходимо включить и установить сертификаты
    ca_bundle_file=settings.GIGACHAT_CA_BUNDLE_FILE,
    temperature=settings.GIGACHAT_TEMPERATURE,  # Креативность ответов
    max_tokens=settings.GIGACHAT_MAX_TOKENS,
)

yandex_model = ChatOpenAI(
    model=settings.OPEN_AI_CHAT_MODEL, # Можно явно задать модель GigaChat (по умолчанию запросы передаются в модель GigaChat Lite, поэтому для теста строка закоментирована).
    api_key = settings.OPEN_AI_API_KEY,
    base_url = settings.OPEN_AI_BASE_URL,
    temperature=settings.OPEN_AI_TEMPERATURE,  # Креативность ответов
    max_tokens=settings.GIGACHAT_MAX_TOKENS,
)

currency_model = yandex_model.bind_tools([convert_currency])
# Структурированные модели



#choice_model = gigachat_model.with_structured_output(GeneratedMenu)
#recipe_model = gigachat_model.with_structured_output(GeneratedRecipe)
#fake_models = GenericFakeChatModel(messages=iter(["Творог"]))
#
#choice_model_fallback = yandex_model.with_structured_output(GeneratedMenu)
#recipe_model_fallback = yandex_model.with_structured_output(GeneratedRecipe)



#def fallback_response_func(_):
#    return GeneratedMenu(dishes=["Варенные яйца"])
#
#fallback_response = RunnableLambda(fallback_response_func)
#
#
#choice_model_fallback = choice_model_fallback.with_retry(
#    stop_after_attempt=2,
#    retry_if_exception_type=(AuthenticationError, OpenAIAuthenticationError, ))
#
#choice_model = choice_model.with_retry(stop_after_attempt=2, retry_if_exception_type=(BadRequestError, )).with_fallbacks(
#    fallbacks=[choice_model_fallback],
#    exceptions_to_handle=(BadRequestError, )
#)

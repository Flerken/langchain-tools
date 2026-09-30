from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Настройки приложения"""

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'  # или 'allow', в зависимости от нужд
    )
    # GigaChat
    GIGACHAT_CREDENTIALS: str
    GIGACHAT_CHAT_MODEL: str = "GigaChat-2"
    GIGACHAT_VERIFY_SSL: bool = False
    GIGACHAT_SCOPE: str = "GIGACHAT_API_PERS"
    GIGACHAT_CA_BUNDLE_FILE: str = "russian_trusted_root_ca_pem.crt"
    GIGACHAT_TEMPERATURE: float = 0.9
    GIGACHAT_MAX_TOKENS: int = 512
    GIGACHAT_MAX_RETRIES: int = 0
    FILE_SYSTEM_PROMPTS: str = "./prompts/game.txt"

    # YANDEX_GPT
    OPEN_AI_CHAT_MODEL: str
    OPEN_AI_API_KEY: str
    OPEN_AI_BASE_URL: str
    OPEN_AI_TEMPERATURE: float= 0.7
    OPEN_AI_MAX_TOKENS: int = 100

# Создаем глобальный экземпляр настроек
settings = Settings()
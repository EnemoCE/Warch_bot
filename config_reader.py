from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr 
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr
    heroku_app_name: str
    database_url: str
    webapp_host: str = '0.0.0.0'  # default value
    webapp_port: int = 8000      # default value
    model_config = SettingsConfigDict(env_file=' .env', env_file_encoding='utf-8')



config = Settings()
#print(config.model_dump())
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    backend_host: str = "learn-k8s-apiserver-clusterip"
    backend_protocol: str = "http"
    backend_port: int = 27525
    secret_key: str = "ajoke"

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()
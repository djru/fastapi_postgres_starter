from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    pg_url: str = Field(alias="PG_URL", default="")


settings = Config()

from pydantic_settings import BaseSettings

class Setings(BaseSettings):
    DATABASE_USENAME:str
    DATABASE_NAME:str
    DATABASE_PASSWORD:str
    DATABASE_HOST:str
    DATABASE_PORT:str
    MONGO_DB:str
    MONGO_SRV:str

    SERVICE_PORT:str

    
    class Config:
        env_file = ".env"

setings = Setings()
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # database related
    
    db_host: str
    db_port: int
    db_name: str
    db_pwd: str
    db_usr: str
    port: str
    
    # JWT Token Related
    SECRET_KEY: str
    REFRESH_SECRET_KEY : str
    ALGORITHM: str
    TIMEOUT: int

    # internal env
    ADMINAPIKEY: str
    DIGIFARMKEY: str

    SERVER: str
    REDIS_HOST: str
    REDIS_PORT:  str
    SENDINBLUE_KEY: str

    class Config:
        env_file = Path(Path(__file__).resolve().parent) / ".env"
        print(f'farm.MMC envvvv - {Path(Path(__file__).resolve().name)}')


setting = Settings()

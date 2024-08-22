from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql+mysqlclient://user:password@localhost/dbname"

settings = Settings()

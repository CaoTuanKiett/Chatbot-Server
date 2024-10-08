from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

class Settings(BaseSettings):
    database_url: str = "mysql+mysqlclient://user:password@localhost/dbname"

settings = Settings()

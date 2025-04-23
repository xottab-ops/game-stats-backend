import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

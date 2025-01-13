import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','picturas-key')
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ES_HOST = os.getenv('ES_HOST', "http://58.216.10.35:9200")
    ES_USER = os.getenv('ES_USER', "elastic")
    ES_PWD = os.getenv('ES_PWD', "byfen123456")
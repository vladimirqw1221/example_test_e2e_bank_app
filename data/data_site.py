import os
from dotenv import load_dotenv

load_dotenv()


class DataSite:
    BASE_URL = os.getenv('BASE_URL')

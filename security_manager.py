from dotenv import dotenv_values

config = dotenv_values(".env")

MONGO_HOST = config.get("MONGO_HOST")
MONGO_DATABASE = config.get("MONGO_DATABASE") 
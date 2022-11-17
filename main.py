import config
import os
from dotenv import load_dotenv

"""This is one method to use the .env file"""
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
print("DB_NAME", DB_NAME)


"""This is Another way to use .env file ,This use the config.py  """
"""we need to create  manually a config file in our prj"""


print(config.settings.DB_NAME, config.settings.HOST, config.settings.PORT)


""" This is another way to create to use env file, using decouple package"""
""" here we no need to create a manual config file """
"""pip install python-decouple"""

from decouple import config

print(config("DB_NAME"))

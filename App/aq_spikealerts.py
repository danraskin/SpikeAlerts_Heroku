## import

import os # For working with Operating System
import sys
from dotenv import load_dotenv # Loading .env info
from App.modules.db_init import db_init, db_need_init
from App.modules.MAIN import main_loop

load_dotenv() # load .env file

if db_need_init() == True:
  print("Minneapolis Boundaries table empty. running db init.")
  db_init()
main_loop()

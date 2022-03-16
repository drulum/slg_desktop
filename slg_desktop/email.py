import os
from dotenv import load_dotenv

load_dotenv()

message = os.getenv('SLG_EMAIL_MESSAGE')

print(message.format(date='2022-03-15'))


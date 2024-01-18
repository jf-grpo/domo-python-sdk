from pydomo import Domo
from pydomo.users import CreateUserRequest
import os

from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("CLIENT_ID")
secret = os.getenv("SECRET")
api_host = os.getenv("API_HOST")


domo = Domo(client_id, secret, api_host)

all_users = domo.users.list(10, 0)
print(all_users)
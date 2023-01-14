import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
# reading .env file ~/projects/broker/config/.env
env.read_env(BASE_DIR + '/config/.env' )

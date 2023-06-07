import os
from dotenv import load_dotenv

def create_config_dict():
    load_dotenv()
    return {
        'host': os.getenv('email_host'),
        'port': os.getenv('email_port'),
        'username': os.getenv('email_username'),
        'password': os.getenv('email_password'),
        'receiver': os.getenv('receiver_email'),
    }
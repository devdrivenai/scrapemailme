from config import create_config_dict
from scraper import web_scrape_manager
from email_sender import send_email

websites_info = [
    {'url': 'https://mywebsite.com',
    'id': 'my-id',
    'name': 'Name I want for this info'},
    {'url': 'https://anotherwebsite.com',
    'class': 'my-class',
    'name': 'Name I want for this info'},
]
subject = 'Info scraped today'
config = create_config_dict()
info = web_scrape_manager(websites_info)
send_email(info, subject, config)

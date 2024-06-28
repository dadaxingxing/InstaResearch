from instagrapi import Client
from dotenv import dotenv_values
from login import login_user
from process import process_info

config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']

cl = login_user(True, USERNAME, PASSWORD)
data = cl.user_medias_gql('10642672448', 4, 2)

print(process_info(data))
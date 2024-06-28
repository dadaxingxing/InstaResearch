from instagrapi import Client
from dotenv import dotenv_values
from login import login_user


config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']

cl = login_user(True, USERNAME, PASSWORD)
print(cl.user_medias_gql('10642672448', 4, 2))
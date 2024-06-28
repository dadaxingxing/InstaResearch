from instagrapi import Client
from dotenv import dotenv_values
from login import login_user
from process import process_info

config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
cl = login_user(True, USERNAME, PASSWORD)

USER_USERNAME = input('Enter the instagram username: ')
USER_ID = cl.user_info_by_username_v1(USER_USERNAME)

data = cl.user_medias_gql(USER_ID.pk, 20, 2)
print(process_info(data))
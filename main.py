from instagrapi import Client
from dotenv import dotenv_values
from login import login_user
from process import process_info

config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
cl = login_user(True, USERNAME, PASSWORD)

# https://subzeroid.github.io/instagrapi/usage-guide/user.html

USER_USERNAME = input('Enter the instagram username: ')
USER_INFO = cl.user_info_by_username_v1(USER_USERNAME).dict()
USER_TOTAL = USER_INFO['media_count']

USER_POSTNUM = min(int(input('Enter number of recent posts to sort (type \"-1\" to sort all posts): ')), USER_TOTAL)

data = cl.user_medias_gql(USER_INFO['pk'], USER_POSTNUM if USER_POSTNUM != -1 else USER_TOTAL, 2)

processed = process_info(data)
for i in range(len(processed)):
    print(f'{i + 1}. Link: {processed[i]['link']}, Likes: {processed[i]['likes']}')
from instagrapi import Client
from dotenv import dotenv_values
from login import login_user
from process import process_info
import time
from db import update

start_time = time.time()

config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
cl = login_user(True, USERNAME, PASSWORD)
cl.delay_range = [1, 3]


USER_INFO = cl.user_info_by_username_v1(input('Enter the instagram username: ')).dict()
USER_TOTAL = USER_INFO['media_count']
USER_POSTNUM = min(int(input('Enter number of recent posts to sort (type \"-1\" to sort all posts): ')), USER_TOTAL)

start_time = time.time()
if USER_POSTNUM == -1: USER_POSTNUM = USER_TOTAL

data = cl.user_medias_gql(USER_INFO['pk'], USER_POSTNUM, 2)

processed = process_info(data)
for i in range(len(processed)):
    print(f"{i + 1}. Link: {processed[i]['link']}, Likes: {processed[i]['likes']}")

print(f'\nShowing {USER_POSTNUM} of {USER_TOTAL} posts')
print("Scrapping finished --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print('Storing the data into mongo DB...')
update(USER_INFO['username'], processed)
print("Storing finished --- %s seconds ---" % (time.time() - start_time))
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
from pprint import pprint
from bson import ObjectId
import re
import bson

#todo: need to add trouble shooting/try & except

def config():
    url = f'mongodb+srv://joey:{dotenv_values('login.env')['DATA_PASSWORD']}@cluster0.lqsceha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    cl = MongoClient(url, server_api=ServerApi('1'))
    db = cl['instagram_post_info']
    cur_user = db['testing_user']
    valid_pages = (cur_user.find_one({"pages": {"$exists": True}}))['pages']
    return (cl, db, cur_user, valid_pages)

def retrive():
    _, _, cur_user, valid_pages = config()

    i = 1
    page = str(input(f'please pick a valid page >> {valid_pages}: '))
    for link, likes in (cur_user.find_one({page : {"$exists": True}}))[page]:
        print(f'rank: {i}, link: {link}, like: {likes}')
        i += 1

def update(add_page_name, page_info):
    add_page_name = re.sub(r'[.]', '_', add_page_name)
    cl, db, cur_user, valid_pages = config()
    page_info = [(post['link'], post['likes']) for post in page_info]

    if add_page_name not in valid_pages:
        valid_pages.append(add_page_name)
        cur_user.update_one({'pages': {"$exists": True}}, {"$set": {'pages': valid_pages}})
    else:
        cur_user.delete_one({add_page_name: {"$exists": True}})
    
    cur_user.insert_one({add_page_name: page_info})


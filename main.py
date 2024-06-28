from instagrapi import Client
from dotenv import dotenv_values


def login_user(check, USERNAME, PASSWORD):
    cl = Client()
    try:
        if check:
            cl.load_settings('session.json')
            cl.login(USERNAME, PASSWORD)
            cl.get_timeline_feed()
            # except Exception as e:
            #     cl.login(USERNAME, PASSWORD)
            #     cl.dump_settings('session.json')
        else:
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings('session.json')

        return cl
    
    except Exception as e:
        print('Could not login, error occured.')  
        return None

config = dotenv_values('login.env')
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']

print(USERNAME, PASSWORD)
# cl = login_user(True, )
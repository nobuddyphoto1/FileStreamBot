# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(os.getenv('API_ID'))
    API_HASH = os.getenv('API_HASH')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    SESSION_NAME = os.getenv('SESSION_NAME')
    SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(os.getenv('WORKERS", '4'))
    BIN_CHANNEL = int(os.getenv('BIN_CHANNEL'))
    PORT = int(os.getenv('PORT', 3000))
    BIND_ADRESS = str(os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(os.getenv('OWNER_ID'))
    NO_PORT = bool(os.getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = os.getenv('APP_NAME')
    else:
        ON_HEROKU = False
    FQDN = os.getenv('FQDN', BIND_ADRESS) if not ON_HEROKU or os.getenv('FQDN') else APP_NAME+'.adaptable.app'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = os.getenv('DATABASE_URL')
    PING_INTERVAL = int(os.getenv('PING_INTERVAL', '200'))
    UPDATES_CHANNEL = os.getenv('UPDATES_CHANNEL', None)
    BANNED_CHANNELS = list(set(int(x) for x in str(os.getenv('BANNED_CHANNELS', '-1001236895100')).split()))

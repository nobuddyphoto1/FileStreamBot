# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = str(os.environ.get('API_HASH'))
    BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
    SESSION_NAME = str(os.environ.get('SESSION_NAME'))
    SLEEP_THRESHOLD = int(os.environ.get('SLEEP_THRESHOLD', '60'))
    WORKERS = int(os.environ.get('WORKERS', '4'))
    BIN_CHANNEL = int(os.environ.get('BIN_CHANNEL'))
    PORT = int(os.environ.get('PORT', 8080))
    BIND_ADRESS = str(os.environ.get('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(os.environ.get('OWNER_ID'))
    NO_PORT = bool(os.environ.get('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(os.environ.get('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(os.environ.get('FQDN', BIND_ADRESS)) if not ON_HEROKU or os.environ.get('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(os.environ.get('DATABASE_URL'))
    PING_INTERVAL = int(os.environ.get('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(os.environ.get("BANNED_CHANNELS", "-1001236895100")).split()))

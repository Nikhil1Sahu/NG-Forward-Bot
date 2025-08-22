# bot developer @OwnerOfNG
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "18466881")
    API_HASH = environ.get("API_HASH", "8c8ca14ad8e416ce4e6ea717db7ec6af")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8375007513:AAF_ayuts-Qj3s0GOeHnyaGUeXaqIZXqZXI") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", "5565120414").split()]
    BOT_SESSION = environ.get("BOT_SESSION", "NG_share_bot") 

    PICS = (environ.get('PICS', 'https://envs.sh/uxo.jpeg https://envs.sh/uxr.jpeg https://envs.sh/uxs.jpeg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://nikhilsahu7j:dTQKfvo0jABOYKOu@cluster0.n2csgvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002731391701'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/network_of_kingdom") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF

    START_MESSAGE = environ.get(
        "START_MESSAGE",
        "Hello [NG]Sharing bot\n\nI can store private files in Specified Channel and other users can access it from special link."
    )


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

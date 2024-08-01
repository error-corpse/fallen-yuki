class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "6435225"
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

    CASH_API_KEY = "V48U2FLLKRHSVD4X"  
    DATABASE_URL = "postgres://biglxqlm:K_CuQM58BPWlHCWjQa1hDd4xRSiDs_tm@dumbo.db.elephantsql.com/biglxqlm"  

    EVENT_LOGS = ("-1002092954715")  

    MONGO_DB_URI = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/56c9da084a528eac54142.jpg"

    SUPPORT_CHAT = "paradoxdump"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5527818445:AAE7TLprBfyUuQvYZsaOesQ0F-9C2sl2I80"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "1CUBX1HXGNHW" 

    OWNER_ID = "6259443940" 

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

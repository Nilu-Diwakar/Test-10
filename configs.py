import os

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
  
ADMINS.append(7409044848)

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28377464"))
  API_HASH = os.environ.get("API_HASH", "4d7869d1807d42fa3683f1eee8248697")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7461694036:AAF6q1OpYSMu5DjO3d7NuoUu524DEtZPbWk")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Paapiyon_ka_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002229719242"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gplinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "5cfebe36ddc1800f0ac5ba1c35bfdecc524a4ceb")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7409044848"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://docibe6636:8qwvOSBAW8NjqWxm@cluster0.eotuglt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002206949341")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002206949341"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
𝓣𝓱𝓲𝓼 𝓲𝓼 𝓪 𝓟𝓮𝓻𝓶𝓪𝓷𝓮𝓷𝓽 𝓕𝓲𝓵𝓮𝓢𝓽𝓸𝓻𝓮 𝓑𝓸𝓽. 𝓢𝓮𝓷𝓭 𝓪𝓷𝔂 𝓜𝓮𝓭𝓲𝓪 𝓸𝓻 𝓕𝓲𝓵𝓮 𝓽𝓸 𝓘𝓽 𝓪𝓷𝓭 𝓘𝓽 𝔀𝓲𝓵𝓵 𝓪𝓭𝓭 𝓼𝓪𝓿𝓮 𝓕𝓲𝓵𝓮 𝓲𝓷 𝓒𝓱𝓪𝓷𝓷𝓮𝓵 𝓪𝓷𝓭 𝓟𝓻𝓸𝓿𝓲𝓭𝓮 𝔂𝓸𝓾 𝓪 𝓢𝓱𝓪𝓻𝓮𝓪𝓫𝓵𝓮 𝓛𝓲𝓷𝓴. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 𝐌𝐲 𝐍𝐚𝐦𝐞: [𝓕𝓲𝓵𝓮𝓢𝓽𝓸𝓻𝓮 𝓑𝓸𝓽](https://t.me/{BOT_USERNAME})
│
├🔹 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: [Python 3](https://www.python.org)
│
├🔸 𝐋𝐢𝐛𝐫𝐚𝐫𝐲: [𝓟𝔂𝓽𝓱𝓸𝓷 3](https://docs.pyrogram.org)
│
├🔹 𝐂𝐫𝐞𝐚𝐭𝐞𝐫: [@𝓝𝓲𝓵𝓮𝓼𝓱𝓓𝔀𝓴𝓻](https://t.me/Paapi_Aadmi)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@𝙉𝙞𝙡𝙚𝙨𝙝𝘿𝙬𝙠𝙧](https://t.me/Paapi_Aadmi)
 
 𝘐 𝘢𝘮 𝘚𝘶𝘱𝘦𝘳 𝘯𝘰𝘰𝘣 𝘗𝘭𝘦𝘢𝘴𝘦 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘔𝘺 𝘏𝘢𝘳𝘥 𝘞𝘰𝘳𝘬.

[𝓓𝓸𝓷𝓪𝓽𝓮 𝓜𝓮](https://t.me/Paapi_Aadmi)
"""
  HOME_TEXT = """
𝓗𝓮𝓵𝓵𝓸, [{}](tg://user?id={})\n\n𝓣𝓱𝓲𝓼 𝓲𝓼 𝓪 𝓟𝓮𝓻𝓶𝓪𝓷𝓮𝓷𝓽 **𝓕𝓲𝓵𝓮𝓢𝓽𝓸𝓻𝓮 𝓑𝓸𝓽**.

𝓗𝓸𝔀 𝓽𝓸 𝓤𝓼𝓮 𝓑𝓸𝓽 & 𝓲𝓽'𝓼 𝓑𝓮𝓷𝓮𝓯𝓲𝓽𝓼??

╰┈➤ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘍𝘪𝘭𝘦 & 𝘐𝘵 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘶𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘪𝘯 𝘔𝘺 𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦 & 𝘠𝘰𝘶 𝘸𝘪𝘭𝘭 𝘎𝘦𝘵 𝘵𝘩𝘦 𝘍𝘪𝘭𝘦 𝘓𝘪𝘯𝘬.

✅ 𝓑𝓮𝓷𝓮𝓯𝓲𝓽𝓼: 𝘐𝘧 𝘺𝘰𝘶 𝘩𝘢𝘷𝘦 𝘢 𝘛𝘦𝘭𝘦𝘎𝘳𝘢𝘮 𝘊𝘩𝘢𝘯𝘯𝘦𝘭, 𝘛𝘩𝘦𝘯 𝘐𝘵𝘴 𝘜𝘴𝘦𝘧𝘶𝘭 𝘧𝘰𝘳 𝘋𝘢𝘪𝘭𝘺 𝘜𝘴𝘢𝘨𝘦, 𝘠𝘰𝘶 𝘤𝘢𝘯 𝘚𝘦𝘯𝘥 𝘔𝘦 𝘠𝘰𝘶𝘳 𝘍𝘪𝘭𝘦 & 𝘐 𝘸𝘪𝘭𝘭 𝘚𝘦𝘯𝘥 𝘗𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘓𝘪𝘯𝘬 𝘵𝘰 𝘠𝘰𝘶 & 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘚𝘢𝘧𝘦 𝘧𝘳𝘰𝘮 **𝘊𝘰𝘱𝘺𝘙𝘪𝘨𝘩𝘵 𝘐𝘯𝘧𝘳𝘪𝘯𝘨𝘦𝘮𝘦𝘯𝘵** 𝘐𝘴𝘴𝘶𝘦. 𝘐 𝘴𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘊𝘩𝘦𝘤𝘬 **𝘈𝘣𝘰𝘶𝘵 𝘉𝘰𝘵**.
"""

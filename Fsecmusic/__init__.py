from Fsecmusic.core.bot import FALCON 
from Fsecmusic.core.dir import dirr
from Fsecmusic.core.git import git
from Fsecmusic.core.userbot import Userbot
from Fsecmusic.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = FALCON()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


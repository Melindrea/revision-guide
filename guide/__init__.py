from flask import Flask
from posts import Posts
# from config import Config

app = Flask(__name__)

app.config.from_envvar('SETTINGS_FILE')
posts = Posts(app)

import guide.routes

from flask import Flask
from posts import Posts

app = Flask(__name__)
posts = Posts(app, root_dir='posts')

import blog.routes

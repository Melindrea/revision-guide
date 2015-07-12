from flask import Flask, render_template
from werkzeug import cached_property
import markdown

POSTS_FILE_EXTENSION = '.md'

app = Flask(__name__)

class Post(object):
    def __init__(self, path):
        self.path = path

    @cached_property
    def html(self):
        with open(self.path, 'r') as fin:
            content = fin.read().strip()

        return markdown.markdown(content)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/blog/<path:path>')
def post():
    path = os.path.join('posts', path + POSTS_FILE_EXTENSION)

    post = Post(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(port=8000)

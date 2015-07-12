import os

from flask import Flask, render_template
from werkzeug import cached_property
import markdown
import yaml

POSTS_FILE_EXTENSION = '.md'

app = Flask(__name__)

class Post(object):
    def __init__(self, path):
        self.path = path
        self._initialise_metadata()

    def _initialise_metadata(self):
        content = ''
        first_separator = False

        with open(self.path, 'r') as fin:
            for line in fin:
                if line.strip() == '---':
                    if first_separator:
                        break
                    else:
                        first_separator = True
                        continue

                content += line

        self.__dict__.update(yaml.load(content))

    @cached_property
    def html(self):
        with open(self.path, 'r') as fin:
            content = fin.read().split('---', 2)[2].strip()

        return markdown.markdown(content)

@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)

# One way of registering filters for jinja
# app.jinja_env.filters['date'] = format_date

# Injecting the function into the context, use as format_date(value)
# @app.context_processor
# def inject_format_date():
#     return { 'format_date': format_date }

@app.route('/')
def index():
    return 'Hello World'

@app.route('/blog/<path:path>')
def post(path):
    # raise # Breakpoint for werkzeug, browser-based
    # import ipdb; ipdb.stack_trace() # Breakpoint for ipdb (needs to be installed), console-based
    path = os.path.join('posts', path + POSTS_FILE_EXTENSION)

    post = Post(path)
    return render_template('post.html', post=post)
    # Inject the function straight into the template, use as format_date(value)
    # return render_template('post.html', post=post, format_date=format_date)

if __name__ == '__main__':
    app.run(port=8000, debug=True)

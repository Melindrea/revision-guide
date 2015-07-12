import os

from flask import Flask, render_template, url_for, abort
from werkzeug import cached_property
import markdown
import yaml

POSTS_FILE_EXTENSION = '.md'

class Post(object):
    def __init__(self, path, root_dir=''):
        self.url_path = os.path.splitext(path.strip('/'))[0]
        self.file_path = os.path.join(root_dir, path.strip('/'))
        self._initialise_metadata()

    def _initialise_metadata(self):
        content = ''
        first_separator = False

        with open(self.file_path, 'r') as fin:
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
        with open(self.file_path, 'r') as fin:
            content = fin.read().split('---', 2)[2].strip()

        return markdown.markdown(content)

    @property
    def url(self):
        return url_for('post', path=self.url_path)

class Blog(object):
    def __init__(self, app, root_dir, file_ext=POSTS_FILE_EXTENSION):
        self.root_dir = root_dir
        self.file_ext = file_ext
        self._app = app
        self._cache = {}
        self._initialise_cache()

    @property
    def posts(self):
        return self._cache.values()

    def get_post_or_404(self, path):
        """ Returns the post object for given path, or raises a NotFound exception
        """

        try:
            return self._cache[path]
        except KeyError:
            abort(404)

    def _initialise_cache(self):
        """ Walks the root directory and adds all posts to the cache
        """

        for (root, dirpaths, filepaths) in os.walk(self.root_dir):
            for filepath in filepaths:
                filename, ext = os.path.splitext(filepath)

                if ext == self.file_ext:
                    path = os.path.join(root, filepath).replace(self.root_dir, '')
                    post = Post(path, root_dir=self.root_dir)
                    self._cache[post.url_path] = post

app = Flask(__name__)
blog = Blog(app, root_dir='posts')

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
    return render_template('index.html', posts=blog.posts)

@app.route('/blog/<path:path>')
def post(path):
    # raise # Breakpoint for werkzeug, browser-based
    # import ipdb; ipdb.stack_trace() # Breakpoint for ipdb (needs to be installed), console-based

    post = blog.get_post_or_404(path)
    return render_template('post.html', post=post)
    # Inject the function straight into the template, use as format_date(value)
    # return render_template('post.html', post=post, format_date=format_date)

if __name__ == '__main__':
    app.run(port=8000, debug=True)

import os

from flask import abort
from sorteddict import SortedDict
from post import Post

POSTS_FILE_EXTENSION = '.md'

class Posts(object):
    def __init__(self, app, root_dir, file_ext=POSTS_FILE_EXTENSION):
        self.root_dir = root_dir
        self.file_ext = file_ext
        self._app = app
        self._cache = SortedDict(key=lambda p: p.date, reverse=True)
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

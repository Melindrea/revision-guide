import os

from flask import abort
from sorteddict import SortedDict
from post import Post


class Posts(object):
    def __init__(self, app, root_dir=None, file_ext=None):
        self.root_dir = root_dir if root_dir is not None else app.config['POSTS_DIRECTORY']
        self.file_ext = file_ext if file_ext is not None else app.config['POSTS_FILE_EXTENSION']
        self._app = app
        self._cache = SortedDict(key=lambda p: p.step)
        self._initialise_cache()

    @property
    def posts(self):
        if self._app.debug:
            return self._cache.values()
        else:
            return [post for post in self._cache.values() if post.published]

    def get_post_or_404(self, path):
        """ Returns the post object for given path, or raises a NotFound exception
        """

        try:
            return self._cache[path]
        except KeyError:
            abort(404)

    def next_post(self, path):
        return self._cache.next(path)

    def previous_post(self, path):
        return self._cache.previous(path)

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

    def get_posts_by_category(self, category):
        return [post for post in self._cache.values() if post.category == category]

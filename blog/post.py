import os

from werkzeug import cached_property
from flask import url_for
import markdown
import yaml

class Post(object):
    def __init__(self, path, root_dir=''):
        self.url_path = os.path.splitext(path.strip('/'))[0]
        self.file_path = os.path.join(root_dir, path.strip('/'))
        self.published = False
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

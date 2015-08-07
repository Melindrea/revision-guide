#!/usr/bin/env python

import sys
from flask.ext.frozen import Freezer
from blog import app

freezer = Freezer(app)

if len(sys.argv) > 1 and sys.argv[1] == 'build':
    freezer.freeze()
else:
    app.run(port=8000, debug=True)

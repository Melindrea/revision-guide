import os

from blog import app, posts
from flask import render_template
import markdown

@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)

@app.template_filter('md')
def md(content):
    return markdown.markdown(content, extensions=['codehilite'])

# One way of registering filters for jinja
# app.jinja_env.filters['date'] = format_date

# Injecting the function into the context, use as format_date(value)
# @app.context_processor
# def inject_format_date():
#     return { 'format_date': format_date }

def safe_content(filename):
    file_path = app.config['PAGES_DIRECTORY'] + '/' + filename + app.config['PAGES_FILE_EXTENSION']
    with open(file_path, 'r') as fin:
            content = fin.read().split('---', 2)[2].strip()
    return markdown.markdown(content, extensions=['codehilite'])

@app.route('/')
def index():
    return render_template('index.tpl', content=safe_content('index'))

@app.route('/posts/<path:path>/')
def post(path):
    # raise # Breakpoint for werkzeug, browser-based
    # import ipdb; ipdb.stack_trace() # Breakpoint for ipdb (needs to be installed), console-based

    post = posts.get_post_or_404(path)
    return render_template('post.tpl', post=post)
    # Inject the function straight into the template, use as format_date(value)
    # return render_template('post.tpl', post=post, format_date=format_date)

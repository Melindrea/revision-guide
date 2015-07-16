import os

from blog import app, posts
from flask import render_template

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
    return render_template('index.tpl', posts=posts.posts)

@app.route('/blog/<path:path>/')
def post(path):
    # raise # Breakpoint for werkzeug, browser-based
    # import ipdb; ipdb.stack_trace() # Breakpoint for ipdb (needs to be installed), console-based

    post = posts.get_post_or_404(path)
    return render_template('post.tpl', post=post)
    # Inject the function straight into the template, use as format_date(value)
    # return render_template('post.tpl', post=post, format_date=format_date)

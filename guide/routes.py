import os

from datetime import datetime
from guide import app, posts
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
    return render_template(
        'index.tpl',
        content=safe_content('index'),
        title='Revision &amp; Writing Guide',
        summary='A guide to <em>my</em> process, with tips, tricks and resources.',
        active_menu_item = 'index',
        updated = datetime.now()
    )

@app.route('/<category>/')
def category_index(category):
    return render_template(
        'category.tpl',
        category=category,
        posts=posts.get_posts_by_category(category),
        title=category.title(),
        active_menu_item = category,
        updated = datetime.now()
    )

@app.route('/posts/<path:path>/')
def post(path):
    # raise # Breakpoint for werkzeug, browser-based
    # import ipdb; ipdb.stack_trace() # Breakpoint for ipdb (needs to be installed), console-based

    post = posts.get_post_or_404(path)
    title = '<small>' + str(post.step) + '</small> ' + post.title
    return render_template(
        'post.tpl',
        post=post,
        next=posts.next_post(path),
        previous=posts.previous_post(path),
        title=title,
        summary=post.summary,
        active_menu_item = post.category,
        updated = post.updated
    )
    # Inject the function straight into the template, use as format_date(value)
    # return render_template('post.tpl', post=post, format_date=format_date)

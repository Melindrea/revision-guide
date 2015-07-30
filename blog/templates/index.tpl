{% extends "base.tpl" %}

{% block content %}
<header>
    <h1>My awesome blog</h1>
</header>

<ul id="posts">
    {% for post in posts %}
    <li class="post">
        <span class="post-date">{{ post.date|date }}</span>
        <a href="{{ post.url }}" class="post-title">{{ post.title }}{% if post.subtitle%} <small>{{ post.subtitle }}</small>{% endif %}</a>
    </li>
    {% endfor %}
</ul>
{% endblock content %}
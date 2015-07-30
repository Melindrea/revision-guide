{% extends "base.tpl" %}

{% block content %}
<header>
    <h1>{{ post.title }}{% if post.subtitle %} <small>{{ post.subtitle }}</small>{% endif %}</h1>
    <div class="date">{{ post.date|date }}</div>
    <div class="date">{{ post.date|date('%Y') }}</div>
</header>

<div id="post-content">
    {{ post.html|safe }}
</div>
{% endblock content %}

{% block head %}
    <title>{{ post.title }}</title>
{% endblock head %}
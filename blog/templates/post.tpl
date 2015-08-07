{% extends "base.tpl" %}

{% block content %}
<header>
    <h1>{{ post.title }}{% if post.subtitle %} <small>{{ post.subtitle }}</small>{% endif %}</h1>
    <div class="date">Last updated: {{ post.date|date }}</div>
</header>

<div>
    {{ post.html|safe }}
</div>
{% endblock content %}

{% block head %}
    <title>{{ post.title }}</title>
{% endblock head %}

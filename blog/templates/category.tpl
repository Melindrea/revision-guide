{% extends "base.tpl" %}

{% block content %}
{% if posts %}
<ul id="posts">
    {% for post in posts %}
    <li class="post">
        {{ post.step }}
        <a href="{{ post.url }}" class="post-title">{{ post.title }}{% if post.subtitle%} <small>{{ post.subtitle }}</small>{% endif %}</a>
    </li>
    {% endfor %}
</ul>
{% else %}
<p>No posts in that category</p>
{% endif %}
{% endblock content %}

{% extends "base.tpl" %}

{% block content %}
<div>
    {{ post.html|safe }}

    {% if next %}
    <p>Next: <a href="{{ next.url }}">{% if post.category != next.category %}{{ next.category|capitalize }}: {% endif %}{{ next.title }}</a></p>
    {% endif %}
    {% if previous %}
    <p>Previous: <a href="{{ previous.url }}">{% if post.category != previous.category %}{{ previous.category|capitalize }}: {% endif %}{{ previous.title }}</a></p>
    {% endif %}
</div>
{% endblock content %}

{% block title %}
    {{ post.step }} {{ post.title }} / {{ super() }}
{% endblock title %}

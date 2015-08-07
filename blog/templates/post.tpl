{% extends "base.tpl" %}

{% block content %}
<div>
    {{ post.html|safe }}

    {% if next %}
    <p>Next: {{ next.title }} - {{ next.url }}</p>
    {% endif %}
    {% if previous %}
    <p>Previous: {{ previous.title }} - {{ previous.url }}</p>
    {% endif %}
</div>
{% endblock content %}

{% block head %}
    <title>{{ post.step }} {{ post.title }}</title>
{% endblock head %}

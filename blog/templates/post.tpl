{% extends "base.tpl" %}

{% block content %}
<div>
    {{ post.html|safe }}

</div>
<hr>
<nav>
  <ul class="pager">
    {% if previous %}
    <li class="previous">
      <a href="{{ previous.url }}" aria-label="Previous" rel="prev">
        <span aria-hidden="true">&laquo;</span> {% if post.category != previous.category %}<strong>{{ previous.category|capitalize }}</strong> {% endif %}<small>{{ previous.step }}</small> {{ previous.title }}
      </a>
    </li>
    {% endif %}
    {% if next %}
    <li class="next">
      <a href="{{ next.url }}" aria-label="Next" rel="next">
        {% if post.category != next.category %}<strong>{{ next.category|capitalize }}</strong> {% endif %}<small>{{ next.step }}</small> {{ next.title }} <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
    {% endif %}
  </ul>
</nav>
{% endblock content %}

{% block title %}
    {{ post.step }} {{ post.title }} / {{ super() }}
{% endblock title %}

{% extends "base.tpl" %}

{% block content %}
<header class="jumbotron">
      <div class="container">
        <h1>Revision &amp; Writing Guide</h1>
        <p>A guide to <em>my</em> process, with tips, tricks and resources.</p>
      </div>
    </header>

<div class="container">
    <div class="row">
            <div class="col-md-8 col-md-offset-2">
                {{ content|safe }}
            </div>
    </div>
</div>

{% endblock content %}

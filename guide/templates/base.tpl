
<!DOCTYPE html>
<!--[if lt IE 9]>         <html class="no-js ie"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/lib/bootstrap-readable.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/lib/font-awesome.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    {% block head %}
        <title>{% block title %}Småty in the land{% endblock title %}</title>
    {% endblock head %}
</head>
<body>

    <!--[if lt IE 10]>
    <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->
<nav class="navbar navbar-inverse navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Revision Guide</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li{% if active_menu_item == 'index' %} class="active"{% endif %}><a href="/revision-guide/">Home</a></li>
            <li{% if active_menu_item == 'writing' %} class="active"{% endif %}><a href="/revision-guide/writing">Writing</a></li>
            <li{% if active_menu_item == 'narrative' %} class="active"{% endif %}><a href="/revision-guide/narrative">Narrative</a></li>
            <li{% if active_menu_item == 'language' %} class="active"{% endif %}><a href="/revision-guide/language">Language</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <main id="content">
        <header class="page-header">
          <div class="container">
            <h1>{{ title|safe }}</h1>
            {% if summary %}
                <p>{{ summary|safe }}</p>
            {% endif %}
          </div>
        </header>

    <div class="container">
    {% block content %}

    {% endblock content %}
    </div>
    </main>
    <footer role="contentinfo">
      <div class="container">
        <p class="text-muted">Marie Hogebrandt &copy; 2015 under <i class="fa fa-creative-commons"></i>BY <br>
        Last Updated {{ updated }} <br>
        <a href="https://github.com/Melindrea/revision-guide.git">Fork on <i class="fa fa-github"></i></a></p>
      </div>
    </footer>
    <script src="{{ url_for('static', filename='js/lib/vendor.min.js') }}"></script>
</body>
</html>

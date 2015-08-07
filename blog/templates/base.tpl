
<!DOCTYPE html>
<!--[if lt IE 9]>         <html class="no-js ie"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-readable.css') }}">
    {% block head %}
    <title>Småty in the land</title>
    {% endblock head %}
</head>
<body>

    <!--[if lt IE 10]>
    <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->
<nav class="navbar navbar-inverse navbar-fixed-top">
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
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/writing">Writing</a></li>
            <li><a href="/narrative">Narrative</a></li>
            <li><a href="/language">Language</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <main id="content">
    {% block content %}

    {% endblock content %}
    </main>
    <footer role="contentinfo">
    </footer>
    <script src="{{ url_for('static', filename='js/vendor.min.js') }}"></script>
</body>
</html>

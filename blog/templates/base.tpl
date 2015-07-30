
<!DOCTYPE html>
<!--[if lt IE 9]>         <html class="no-js ie"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block head %}
    <title>Småty in the land</title>
    {% endblock head %}
</head>
<body>

    <!--[if lt IE 10]>
    <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->

    <main id="content">
    {% block content %}

    {% endblock content %}
    </main>
    <footer role="contentinfo">
    </footer>
</body>
</html>
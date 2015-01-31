<!doctype html>
<html>
    <head>
            <meta charset="utf-8">
            {{ HTML::style('css/forum.css'); }}
    </head>
    
    <body>
    <div id="nav">
    <u>Winston's Healthy Food Domain</u>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/Recipes">Recipes Index</a></li>
      <li><a href="/login">Sign In</a></li>
    </ul>
    </div>
    <br>
        @yield('content')
    </body>
</html>

<!doctype html>
<html>
    <head>
            <meta charset="utf-8">
            {{ HTML::style('css/food.css'); }}
    </head>
    
    <body>
    <div id="nav">
    <u>Winston's Public Food Recipes</u>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/Recipes">Recipes Index</a></li>
      <li><a href="/login">Sign In</a></li>
      <li><a href="/useradmin">User Admin</a></li>
    </ul>
    </div>
        @yield('content')
        @yield('footer')
         <div class="footer">
            <div id="links">
            <ul>
            <li>Made by Winston Kouch 2015</li>
            <li><a href="/about">About this website</a></li>
            <li><a href="/faqs">F.A.Q.S</a></li>
            </ul>
            </div>
        </div>
    </body>
</html>

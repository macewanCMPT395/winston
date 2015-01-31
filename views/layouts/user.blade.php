<!doctype html>
<html>
    <head>
            <meta charset="utf-8">
            {{ HTML::style('css/userpanel.css'); }}
    </head>
    
    <body>
    <div id="items">
    <h1>User Control Panel</h1>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/login">Login</a></li>
      <li><a href="/users/create">Create New User</a></li>
      <li><a href="/userpanel">Edit Account Details</a></li>
      <li><a href="/logout">Logout</a></li>
    </ul>
    </div>
        @yield('content')
        @yield('footer')
    </body>
</html>

@extends('layouts.forum')

@section('content')

    <div class = "main">
    <h1>Edit User Information</h1>
    <?php
    $user_data = Auth::user();
    $username = $user_data->username;
    $pass = $user_data->password;
    echo "Hello $username! Here you can change your user details!";
    ?>
    
<!--    {{ Form::open(['route' => 'users.update']) }} -->
        
        
        <div class = "box">
            {{ Form::label('username', 'Username:&nbsp;&nbsp;&nbsp; ') }}
            {{ Form::text('username') }}           
            {{ $errors->first('username', '<span class=error>:message</span>') }}
        </div>
        
        <div class = "box">
            {{ Form::label('password', 'Password:&nbsp;&nbsp;&nbsp; ') }}
            {{ Form::text('password') }}           
            {{ $errors->first('username', '<span class=error>:message</span>') }}
        </div>
        
        <div class = "box">
            {{ Form::label('email', 'Email:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ') }}
            {{ Form::email('email') }}           
            {{ $errors->first('email', '<span class=error>:message</span>') }}
        </div>
        
        <div class = "box">
            {{ Form::label('fname', 'First Name: ') }}
            {{ Form::text('fname') }}           
            {{ $errors->first('fname', '<span class=error>:message</span>') }}
        </div>
          
        <div class = "box">
            {{ Form::label('lname', 'Last Name: ') }}
            {{ Form::text('lname') }}           
            {{ $errors->first('lname', '<span class=error>:message</span>') }}
        </div>
        
        <div><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        {{ Form::submit('Update User Details') }}</div>
        {{ Form::close() }}
        
     </div>
        
@stop

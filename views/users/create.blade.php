@extends('layouts.forum')

@section('content')

    <div class = "main">
    <h1>Create New User Account</h1>
    
    {{ Form::open(['route' => 'users.store']) }}
        <div class = "box">
            {{ Form::label('username', 'Username: &nbsp;') }}
            {{ Form::text('username') }}
            {{ $errors->first('username', '<span class=error>:message</span>') }}
        </div>
        
        
        <div class = "box">
            {{ Form::label('password', 'Password: &nbsp;&nbsp;') }}
            {{ Form::password('password') }}           
            {{ $errors->first('password', '<span class=error>:message</span>') }}
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
        {{ Form::submit('Create User') }}</div>
        {{ Form::close() }}
        
     </div>
        
@stop

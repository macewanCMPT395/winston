@extends('layouts.user')

@section('content')
    <div>
        <h1> Please sign-in! </h1>
    <div>
    {{ Form::open(['route' => 'sessions.store']) }}
        {{ Form::label('username', 'Username:') }}
        {{ Form::text('username') }}
    </div>
    
    <div>
        {{ Form::label('password', 'Password:') }}
        {{ Form::password('password') }}
    </div>
    
    <div>
        {{ Form::submit('Login') }}
        {{ Form::close() }}
    </div>
@stop

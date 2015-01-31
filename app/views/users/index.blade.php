@extends('layouts.user')

@section('content')
    <div>
    <h1>All Users</h1>
       
    @if ($users->count())
        @foreach ($users as $user)
            <li>{{ link_to("/users/{$user->username}", $user->username) }}</li>
        @endforeach
    @else
        <p>Unfortunately, there are no users.</p>
    @endif
    </div>
@stop

@section('footer')
@stop

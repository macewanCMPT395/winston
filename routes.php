<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|
*/

Route::resource('users', 'UsersController');

Route::get('/', function() {
    //Show the home page when someone opens up the root address of website
    return View::make('homepage');
});

Route::get('/Recipes', function() {
    //Show recipes library
    return View::make('recipes');
});

Route::get('/faqs', function() {
    //Show frequently asked questions page
    return View::make('faqs');
});

Route::get('/about', function() {
    //Show about page
    return View::make('about');
});

//Page is not working correctly, it is breaking from a function within the page
Route::get('/useradmin', function() {
    return View::make('useradmin');
});



Route::get('/logout', 'SessionsController@destroy');

//This deals with the edit user details function
//It returns to the homepage if you are not an authenticated user
Route::get('/userpanel', function() {
    if (Auth::check()) return View::make('users.edit');
    return View::make('homepage');
});

Route::resource('sessions', 'SessionsController');
Route::get('login', 'SessionsController@create');
Route::get('logout', 'SessionsController@destroy');

// User Administration page (not working)
Route::get('/admin', function()
{
    return View::make('admin');
});
